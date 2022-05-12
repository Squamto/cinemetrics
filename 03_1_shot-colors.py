# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import scipy.cluster
import os
import sys
import xml.etree.ElementTree as et
import time
import math

from lib import hls_sort, hls_sort2


def unique(seq, idfun=None): 
	if idfun is None:
		def idfun(x): return x
	seen = {}
	result = []
	for item in seq:
		marker = idfun(item)
		if marker in seen: continue
		seen[marker] = 1
		result.append(item)
	return result


def unique2(seq):
	checked = []
	for e in seq:
		if e not in checked:
			checked.append(e)
	return checked


DEBUG = False

NUM_CLUSTERS = 5
PIXELS_PER_COLOR = 20
EVERY_NTH_FRAME = 5
OUTPUT_DIR_NAME = "shot_colors"


def main():
	os.chdir(sys.argv[1])
	try:
		os.mkdir(OUTPUT_DIR_NAME)
	except:
		pass
	
	tree = et.parse("project.xml")
	movie = tree.getroot()
	file_path = movie.attrib["path"]
	cap = cv.VideoCapture(file_path)
	cap.read()
	
	# skip frames in the beginning, if neccessary
	start_frame = int( movie.attrib["start_frame"] )
	for i in range(start_frame):
		cap.read()
	
	if DEBUG:
		cv.namedWindow("win", cv.WINDOW_AUTOSIZE)
		cv.moveWindow("win", 200, 200)

	t = time.time()
	
	f = open("shots.txt", "r")
	scene_durations = [int(values[2]) for values in [line.split("\t") for line in f if line]]
	f.close()
	
	for scene_nr, duration in enumerate(scene_durations):
		print("shot #%d" % scene_nr, "/", len(scene_durations)-1)
		
		h = int( math.ceil( float(duration) / EVERY_NTH_FRAME ) )
		output_img = np.zeros((h, PIXELS_PER_COLOR*NUM_CLUSTERS, 3), np.uint8)
		frame_counter = 0
		
		for i in range(duration):
			ret, img_orig = cap.read()
			if not ret: # eof
				break
			
			if i % EVERY_NTH_FRAME != 0:
				continue
			
			new_width = int(img_orig.shape[1]/4.0)
			new_height = int(img_orig.shape[0]/4.0)
			
			img_small = cv.resize(img_orig, (new_width, new_height), cv.INTER_AREA)
			
			if DEBUG:
				cv.imshow("win", img_small)
			
			img = cv.cvtColor(img_small, cv.COLOR_BGR2HLS)
			
			# convert to numpy array
			a = img.astype(np.float32)
			a = a.reshape(a.shape[0] * a.shape[1], a.shape[2]) # make it 1-dimensional

			# set initial centroids
			init_cluster = []
			for y in [int(new_height/4.0), int(new_height*3/4.0)]:
				for x in [int(new_width*f) for f in [0.25, 0.75]]:
					init_cluster.append(a[y * new_width + x])
			init_cluster.insert(2, a[int(new_height/2.0) * new_width + int(new_width/2.0)])
			
			centroids, labels = scipy.cluster.vq.kmeans2(a, np.array(init_cluster))
			
			vecs, dist = scipy.cluster.vq.vq(a, centroids) # assign codes
			counts, bins = scipy.histogram(vecs, len(centroids)) # count occurrences
			centroid_count = []

			for i, count in enumerate(counts):
				#print(centroids[i], count)
				if count > 0:
					centroid_count.append((centroids[i].tolist(), count))
			
			#centroids = centroids.tolist()
			#centroids.sort(hls_sort)


			from functools import cmp_to_key

			centroid_count.sort(key=cmp_to_key(hls_sort2))
			
			px_count = new_width * new_height
			x = 0
			for item in centroid_count:
				count = item[1] * (PIXELS_PER_COLOR*NUM_CLUSTERS)
				count = int(math.ceil(count / float(px_count)))
				centroid = item[0]
				for l in range(count):
					if x+l >= PIXELS_PER_COLOR*NUM_CLUSTERS:
						break
					output_img[frame_counter, x+l] = (centroid[0], centroid[1], centroid[2])
				x += count
			
			if DEBUG:
				if cv.waitKey(1) == 27:
					cv.destroyWindow("win");
					return
			
			frame_counter += 1
		
		output_img_rgb = cv.cvtColor(output_img, cv.COLOR_HLS2BGR)
		cv.imwrite(OUTPUT_DIR_NAME + "\\shot_colors_%04d.png" % (scene_nr), output_img_rgb)
	
	if DEBUG:
		cv.destroyWindow("win");
	print("%.2f min" % ((time.time()-t) / 60))
	#print("- done -")
	return



# #########################
if __name__ == "__main__":
	main()
# #########################

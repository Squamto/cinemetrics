# -*- coding: utf-8 -*-
import sys
import os
import os.path
import glob
import cv2 as cv
import math
import numpy as np
import scipy.cluster
import xml.etree.ElementTree as et

from lib import hls_sort2, append_images


OUTPUT_DIR_NAME = "chapters"

NUM_CLUSTERS = 10
PIXELS_PER_COLOR = 40


def main():
	os.chdir(sys.argv[1])
	
	#print("DELETE ALL FILES FIRST!")
	
	#tree = et.parse("project.xml")
	#movie = tree.getroot()
	#start_frame = int( movie.attrib["start_frame"] )
	#end_frame = int( movie.attrib["end_frame"] )
	
	f_shots = open("shots.txt")
	shots = [(int(start), int(end)) for start, end in [line.split("\t")[0:2] for line in f_shots if line]]
	f_shots.close()
	
	f_chapters = open("chapters.txt")
	chapters = [int(line) for line in f_chapters if line]
	f_chapters.close()
	'''# fix first and add last frame
	chapters[0] = start_frame
	chapters.append(end_frame)'''
	
	os.chdir("shot_colors")
	try:
		os.mkdir(OUTPUT_DIR_NAME)
	except:
		pass
	
	filenames = glob.glob("shot_colors_*.png")
	
	last_shot_nr = 0
	ch = 1
	for i, shot in enumerate(shots):
		start_frame, end_frame = shot
		if ch == len(chapters): # will this ever happen, freder?
			print("den rest noch")
			#print(" ".join(filenames[last_shot_nr:]))
			append_images(filenames[last_shot_nr:], "chapters/chapter_%02d.png" % (ch))
			# os.system("wsl convert %s -append chapters/chapter_%02d.png" % (" ".join(filenames[last_shot_nr:]), ch))
			break
		elif end_frame >= chapters[ch]:
		#if end_frame >= chapters[ch]:
			print(ch, ":", last_shot_nr, "->", i-1)
			print(" ".join(filenames[last_shot_nr:i]))
			append_images(filenames[last_shot_nr:i], "chapters/chapter_%02d.png" % (ch))
			# os.system("wsl convert %s -append chapters/chapter_%02d.png" % (" ".join(filenames[last_shot_nr:i]), ch))
			last_shot_nr = i
			ch += 1
			
	
	os.chdir(OUTPUT_DIR_NAME)
	
	for file_nr, file in enumerate( os.listdir(os.getcwd()) ):
		if os.path.isdir(file):
			continue
		
		img_orig = cv.imread(file)
		w, h = img_orig.shape[1], img_orig.shape[0]
		
		img_hls = cv.cvtColor(img_orig, cv.COLOR_BGR2HLS)
		
		output_img = np.zeros((h, PIXELS_PER_COLOR*NUM_CLUSTERS, 3), np.uint8)
		
		# convert to numpy array
		a = img_hls.astype(np.float32)
		a = a.reshape(a.shape[0] * a.shape[1], a.shape[2]) # make it 1-dimensional
		
		# set initial centroids
		init_cluster = []
		step = w / NUM_CLUSTERS
		#for x, y in [(0*step, h*0.1), (1*step, h*0.3), (2*step, h*0.5), (3*step, h*0.7), (4*step, h*0.9)]:
		for x, y in [(0*step, h*0.1), (1*step, h*0.1), (2*step, h*0.3), (3*step, h*0.3), (4*step, h*0.5), (5*step, h*0.5), (6*step, h*0.7), (7*step, h*0.7), (8*step, h*0.9), (9*step, h*0.9)]:
			x = int(x)
			y = int(y)
			init_cluster.append(a[y*w + x])
		
		centroids, labels = scipy.cluster.vq.kmeans2(a, np.array(init_cluster))
		
		vecs, dist = scipy.cluster.vq.vq(a, centroids) # assign codes
		counts, bins = scipy.histogram(vecs, len(centroids)) # count occurrences
		centroid_count = []
		for i, count in enumerate(counts):
			if count > 0:
				centroid_count.append((centroids[i].tolist(), count))
		
		from functools import cmp_to_key

		centroid_count.sort(key=cmp_to_key(hls_sort2))
		
		px_count = w * h
		x = 0
		for item in centroid_count:
			count = item[1] * (PIXELS_PER_COLOR*NUM_CLUSTERS)
			count = int(math.ceil(count / float(px_count)))
			centroid = item[0]
			for l in range(count):
				if x+l >= PIXELS_PER_COLOR*NUM_CLUSTERS:
					break
				for y in range(h):
					output_img[y, x+l] = (centroid[0], centroid[1], centroid[2])
			x += count
		
		output_img_rgb = cv.cvtColor(output_img, cv.COLOR_HLS2BGR)
		cv.imwrite(file, output_img_rgb)
		
		# save to text-file
		if file_nr == 0:
			f_out = open("..\\..\\chapter_colors.txt", "w")
			f_out.write("") # reset
			f_out.close()
		
		f_out = open("..\\..\\chapter_colors.txt", "a")
		row = output_img_rgb[0]
		WIDTH = row.shape[0]
		#print(WIDTH)
		
		data_items = []
		counter = 0
		last_px = row[0]
		for i in range(WIDTH):
			px = row[i]
			if np.all(np.equal(px, last_px)):
				counter += 1
				if i == WIDTH-1:
					#f_out.write("%d, %d, %d, %d _ " % (int(last_px[2]), int(last_px[1]), int(last_px[0]), counter))
					data_items.append( "%d, %d, %d, %d" % (int(last_px[2]), int(last_px[1]), int(last_px[0]), counter) )
				continue
			else:
				#f_out.write("%d, %d, %d, %d _ " % (int(last_px[2]), int(last_px[1]), int(last_px[0]), counter))
				data_items.append( "%d, %d, %d, %d" % (int(last_px[2]), int(last_px[1]), int(last_px[0]), counter) )
				counter = 1
				last_px = px
		
		# print(NUM_CLUSTERS - len(data_items), "colors missing")
		for j in range( NUM_CLUSTERS - len(data_items) ): # sometimes there are fewer colors
			data_items.append("0, 0, 0, 0")
		f_out.write( " _ ".join(data_items) )
		f_out.write("\n")
		f_out.close()
	
	# os.system("wsl convert chapter_*.png -append _CHAPTERS.png")
	
	append_images(glob.glob("chapter_*.png"), "_CHAPTERS.png")

	return


# #########################
if __name__ == "__main__":
	main()
# #########################
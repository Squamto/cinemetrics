# -*- coding: utf-8 -*-
import cv2 as cv
import math
import os
import sys
import xml.etree.ElementTree as et
import time
import numpy as np


OUTPUT_DIR_NAME = "shot_slitscans"


def main():
	os.chdir(sys.argv[1])
	try:
		os.mkdir(OUTPUT_DIR_NAME)
	except OSError:
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
	
	f = open("shots.txt", "r")
	lines = [line for line in f if line]
	f.close()
	
	t = time.time()
	
	w = None
	h = None
	
	#for line in f:
	for nr, line in enumerate(lines):
		print((nr+1), "/", len(lines))
		
		#frame_from, frame_to, width, scene_nr = [int(i) for i in line.split("\t")]
		#width, scene_nr = [int(i) for i in line.split("\t")][2:]
		start_frame, end_frame, width = [int(splt) for splt in line.split("\t")]
		#width *= STRETCH_FAKTOR
		
		faktor = None
		output_img = None
		
		for frame_counter in range(width):
			#if frame_counter % STRETCH_FAKTOR == 0:
			#	img = cv.QueryFrame(cap)
			#	if not img:
			#		break
			
			ret, img = cap.read()
			if not ret:
				break
			
			if nr == 0:
				w = img.shape[1]
				h = img.shape[0]
				
			if frame_counter == 0:
				faktor = float(w) / float(width)
				output_img = np.zeros((h, width, 3), np.uint8)
			
			col_nr = faktor * (frame_counter+0.5)
			col_nr = int( math.floor(col_nr) )
			#print(frame_counter, width, col_nr, w)
			col = img[::, col_nr]
			
			output_img[::, frame_counter] = col

		#return
			
		cv.imwrite(OUTPUT_DIR_NAME + "\\shot_slitscan_%03d_%d.png" % (nr+1, start_frame), output_img)
	
	print("%.2f min" % ((time.time()-t) / 60))
	#print("- done -")
	return
	

# #########################
if __name__ == "__main__":
	#STRETCH_FAKTOR = 1
	main()
# #########################

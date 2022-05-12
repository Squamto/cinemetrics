# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import math
import os
import sys
import xml.etree.ElementTree as et


OUTPUT_DIR = "100_stills"
WIDTH = 240


def main():
	os.chdir(sys.argv[1])
	try:
		os.mkdir(OUTPUT_DIR)
	except OSError:
		pass
	
	tree = et.parse("project.xml")
	
	movie = tree.getroot()
	file_path = movie.attrib["path"]
	#fps = float( movie.attrib["fps"] )
	
	cap = cv.VideoCapture(file_path)
	cap.read()
	
	# skip frames in the beginning, if neccessary
	start_frame = int( movie.attrib["start_frame"] )
	for i in range(start_frame):
		cap.read()
	
	end_frame = int( movie.attrib["end_frame"] )
	every_nth_frame = int( (end_frame - start_frame) / 100 )
	print("every", every_nth_frame, "frames")
	#print("=", every_nth_frame / fps, "sec")
	frame = start_frame
	counter = 1
	
	while 1:
		print(counter)
		ret, img = cap.read()
		if not ret or frame > end_frame:
			break
		
		img_small = cv.resize(img, (int( img.shape[1] * float(WIDTH)/img.shape[0] ), WIDTH), cv.INTER_CUBIC)
		
		cv.imwrite(OUTPUT_DIR + "\\still_%07d.jpg" % (frame), img_small)
		
		for i in range(every_nth_frame-1):
			cap.read()
		
		frame += every_nth_frame
		counter += 1
	
	#print("- done -")
	return


# #########################
if __name__ == "__main__":
	main()
# #########################

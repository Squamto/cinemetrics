# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import math
import os
import sys
import xml.etree.ElementTree as et
import time

from lib import skip_frames


# TODO
# - last 499


DEBUG = False
MAX_FRAMES = 1000
WIDTH = 500

OUTPUT_DIR_NAME = "motion"


def main():
	os.chdir(sys.argv[1])
	try:
		os.mkdir(OUTPUT_DIR_NAME)
	except OSError:
		pass
	
	tree = et.parse("project.xml")
	
	movie = tree.getroot()
	file_path = movie.attrib["path"]
	
	if DEBUG:
		cv.namedWindow("win", cv.CV_WINDOW_AUTOSIZE)
		cv.moveWindow("win", 200, 200)
	
	cap = cv.VideoCapture(file_path)
	skip_frames(cap, movie)
	
	pixel_count = None
	prev_img = None
	
	global_frame_counter = 0
	file_counter = 0
	
	w = None
	h = None
	
	output_img = np.zeros((MAX_FRAMES, WIDTH, 3), np.uint8)
	
	f = open("shots.txt", "r")
	lines = [line for line in f if line] # (start_frame, end_frame, duration)
	f.close()
	
	f_frm = open("motion.txt", "w")
	f_avg = open("motion_shot-avg.txt", "w")
	motion = []
	
	t = time.time()
	
	for nr, line in enumerate(lines):
		print((nr+1), "/", len(lines))
		
		duration = int( line.split("\t")[2] )
		
		for frame_counter in range(duration):
			ret, img = cap.read()
			if not ret:
				print("error?")
				print(nr, frame_counter)
				#break
				return
			
			if DEBUG:
				cv.imshow("win", img)
			
			global_frame_counter += 1
			
			if nr == 0 and frame_counter == 0: # first shot, first frame
				w = img.shape[1]
				h = img.shape[0]
				pixel_count = float( w*h )
				prev_img = np.zeros(img.shape, np.uint8)
			
			diff = cv.absdiff(img, prev_img)
			_, diff = cv.threshold(diff, 10, 255, cv.THRESH_BINARY)
			d_color = 0
			for i in range(1, 3):
				d_color += float(cv.countNonZero(diff[:: ,:: , i])) / float(pixel_count)
			d_color = d_color / 3 # 0..1
			#print("%.1f" % (d_color*100), "%")
			
			motion.append(d_color)
			prev_img = img.copy()
			
			# WRITE TEXT FILE
			f_frm.write("%f\n" % (d_color))
			if frame_counter == duration-1: # last frame of current shot
				motion_value = sum(motion) / len(motion)
				print("average motion:", motion_value)
				f_avg.write("%f\t%d\n" % (motion_value, duration))
				motion = []
			
			# WRITE IMAGE
			if frame_counter == 0: # ignore each first frame -- the diff after a hard cut is meaningless
				global_frame_counter -= 1
				continue
			else:
				for i in range(WIDTH):
					value = d_color * 255
					output_img[(global_frame_counter-1) % MAX_FRAMES, i] = (value, value, value)
			
			if global_frame_counter % MAX_FRAMES == 0:
				cv.imwrite(OUTPUT_DIR_NAME + "\\motion_%03d.png" % (file_counter), output_img)
				file_counter += 1
			
			if DEBUG:
				if cv.waitKey(1) == 27:
					break
	
	if global_frame_counter % MAX_FRAMES != 0:
		#cv.SetImageROI(output_img, (0, 0, WIDTH-1, (global_frame_counter % MAX_FRAMES)-1))
		tmp = output_img[0:WIDTH-1, 0:(global_frame_counter-1) % MAX_FRAMES]
		cv.imwrite(OUTPUT_DIR_NAME + "\\motion_%03d.png" % (file_counter), tmp)
	
	f_frm.close()
	f_avg.close()
	
	if DEBUG:
		cv.destroyWindow("win");
	
	print("%.2f min" % ((time.time()-t) / 60))
	#print("- done -")
	return



# #########################
if __name__ == "__main__":
	main()
# #########################

# -*- coding: utf-8 -*-
import sys
import cv2 as cv
import time
import winsound
import os
import os.path
import xml.etree.ElementTree as et
import numpy as np


DEBUG = False
# DEBUG = True
DEBUG_INTERACTIVE = False

OUTPUT_DIR_NAME = "shot_snapshots"
soundfile = "ton.wav"


def main():
	BLACK_AND_WHITE = False
	THRESHOLD = 0.48
	BW_THRESHOLD = 0.4
	
	os.chdir(sys.argv[1])
	try:
		os.mkdir(OUTPUT_DIR_NAME)
	except:
		pass
	
	if len(sys.argv) > 2:
		if sys.argv[2] == "bw":
			BLACK_AND_WHITE = True
			THRESHOLD = BW_THRESHOLD
			print("##########")
			print(" B/W MODE")
			print("##########")
	
	tree = et.parse("project.xml")
	movie = tree.getroot()
	file_path = movie.attrib["path"]
	cap = cv.VideoCapture(file_path)

	if DEBUG:
		cv.namedWindow("win", cv.WINDOW_AUTOSIZE)
		cv.moveWindow("win", 200, 200)

	hist = None
	prev_hist = None
	prev_img = None

	pixel_count = None
	frame_counter = 0

	last_frame_black = False
	black_frame_start = -1

	t = time.time()

	while 1:
		retval, img_orig = cap.read()
		
		if not retval: # eof
			cv.imwrite(OUTPUT_DIR_NAME + "\\%06d.png" % (frame_counter-1), prev_img)
			"""movie.set("frames", str(frame_counter))
			tree.write("project.xml")"""
			break
		
		img = cv.resize(img_orig, img_orig.shape[:2][::-1], 0.25, 0.25, interpolation=cv.INTER_AREA)
		
		if frame_counter == 0: # erster frame
			cv.imwrite(OUTPUT_DIR_NAME + "\\%06d.png" % (0), img)
			pixel_count = img.shape[0] * img.shape[1]
			prev_img = np.zeros(img.shape, np.uint8)
		
		if DEBUG and frame_counter % 2 == 1:
			cv.imshow("win", img)
		
		# img_hsv = np.zeros(img.shape, np.uint8)
		img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		
		# #####################
		# METHOD #1: find the number of pixels that have (significantly) changed since the last frame
		diff = cv.absdiff(img_hsv, prev_img)
		_, diff = cv.threshold(diff, 10, 255, cv.THRESH_BINARY)
		# cv.Threshold(diff, diff, 10, 255, cv.CV_THRESH_BINARY)
		d_color = 0
		for i in range(1, 3):
			d_color += float(cv.countNonZero(diff[:: ,:: , i])) / float(pixel_count)
		
		if not BLACK_AND_WHITE:
			d_color = float(d_color/3.0) # 0..1

		# #####################
		# METHOD #2: calculate the amount of change in the histograms
		h_plane = cv.Mat(np.zeros(img.shape[:2], np.uint8))
		s_plane = cv.Mat(np.zeros(img.shape[:2], np.uint8))
		v_plane = cv.Mat(np.zeros(img.shape[:2], np.uint8))
		cv.split(img_hsv, [h_plane, s_plane, v_plane])
		
		hist_size = [50, 50, 50]
		hist_range = [0, 360, 0, 255, 0, 255]
		# if not hist:
		# 	hist = cvCreateHist(hist_size, cv.CV_HIST_ARRAY, hist_range, 1)

		hist = cv.calcHist([img_hsv], [0, 1, 2], None, hist_size, hist_range)
		# cv.NormalizeHist(hist, 1.0)
		cv.normalize(hist, hist)

		if prev_hist is None:
			# prev_hist = cv.CreateHist(hist_size, cv.CV_HIST_ARRAY, hist_range, 1)
			# wieso gibt es kein cv.CopyHist()?!
			prev_hist = cv.calcHist([img_hsv], [0,1,2], None, hist_size, hist_range)
			# cv.NormalizeHist(prev_hist, 1.0)
			cv.normalize(prev_hist, prev_hist)
			continue
		
		d_hist = cv.compareHist(prev_hist, hist, cv.HISTCMP_CHISQR)

		# combine both methods to make a decision
		if ((0.4*d_color + 0.6*(d_hist/150))) >= THRESHOLD:
			if DEBUG:
				if frame_counter % 2 == 0:
					cv.imshow("win", img)
				winsound.PlaySound(soundfile, winsound.SND_FILENAME|winsound.SND_ASYNC)
				print("%.3f" % ((0.4*d_color + 0.6*(1-d_hist))), "%.3f" % (d_color), "%.3f" % (1-d_hist), frame_counter)
				cv.imwrite(OUTPUT_DIR_NAME + "\\%06d.png" % (frame_counter), img)
			else:
				cv.imwrite(OUTPUT_DIR_NAME + "\\%06d.png" % (frame_counter), img)
		
		prev_hist = cv.calcHist([img_hsv], [0,1,2], None, hist_size, hist_range)
			
		# cv.NormalizeHist(prev_hist, 1.0)
		cv.normalize(prev_hist, prev_hist)
		
		# #####################
		# METHOD #3: detect series of (almost) black frames as an indicator for "fade to black"
		average = np.average(v_plane)
		if average <= 0.6:
			if not last_frame_black: # possible the start
				print("start", frame_counter)
				black_frame_start = frame_counter
			last_frame_black = True
		else:
			if last_frame_black: # end of a series of black frames
				cut_at = black_frame_start + int( (frame_counter - black_frame_start) / 2 )
				print("end", frame_counter, "cut at", cut_at)
				img_black = np.zeros((int(img_orig.shape[1]/4), int(img_orig.shape[0]/4), 3), np.uint8)
				img_black[::] = (0, 255, 0)
				cv.imwrite(OUTPUT_DIR_NAME + "\\%06d.png" % (cut_at), img_black)
			last_frame_black = False
		
		prev_img = img_hsv.copy()
		frame_counter += 1
		
		if DEBUG:
			if cv.waitKey(1) == 27:
				break
		

	if DEBUG:
		cv.destroyWindow("win")
	
	print("%.2f min" % ((time.time()-t) / 60))
	#print("- done -")
	return


# #########################
if __name__ == "__main__":
	main()
# #########################

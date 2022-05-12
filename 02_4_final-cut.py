# -*- coding: utf-8 -*-
import sys
import os
import glob
import cv2 as cv
import numpy as np


startframe = 0


def main():
	global startframe
	os.chdir(sys.argv[1])
	os.chdir("shot_slitscans")
	
	'''cv.NamedWindow("win", cv.CV_WINDOW_AUTOSIZE)
	cv.MoveWindow("win", 500, 200)
	cv.SetMouseCallback("win", mouse_callback)'''
	
	bg_img = np.zeros((576, 576, 3), np.uint8)
	#cv.Set(bg_img, (180))
	
	files = sorted( glob.glob("*.png") )
	i = 0
	while i < len(files):
		file = files[i]
		startframe = int( file.split("_")[3].split(".")[0] )
		print(startframe)
		
		img = cv.imread(file)
		
		win_name = "%d" % (int(float(i+1)*100.0/len(files))) + "% - " + file
		cv.namedWindow(win_name, cv.WINDOW_AUTOSIZE)
		cv.moveWindow(win_name, 500, 200)
		cv.setMouseCallback(win_name, mouse_callback)
		
		cv.imshow(win_name, bg_img)
		cv.imshow(win_name, img)
		
		key = cv.waitKey(0)
		if key == 2555904: # right arrow
			i += 1
		elif key == 2424832: # left arrow
			i -= 1
			if i < 0:
				i = 0
		elif key == 27: # ESC
			break
		
		cv.destroyWindow(win_name)
	
	os.chdir("../../..")
	os.system("python 02_2_save-shots.py \"" + sys.argv[1] + "\"")


def mouse_callback(event, x, y, flags, param):	
	if event == 1: # left mouse down
		# draw line?
		pass
	elif event == 4: # left mouse up
		f = open("../shot_snapshots/%06d.png" % (startframe + x), "w")
		print("cut added at %06d" % (startframe + x))
		f.close()


# #########################
if __name__ == "__main__":
	main()
# #########################

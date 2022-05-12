# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
import os
import os.path
import sys


OUTPUT_DIR_NAME = "downsampled"


def main():
	os.chdir(os.path.join(sys.argv[1], "motion"))
	try:
		os.mkdir(OUTPUT_DIR_NAME)
	except OSError:
		pass
	
	#os.system("del klein\\*.png")
	os.system("wsl convert motion_*.png -adaptive-resize 500x500! " + OUTPUT_DIR_NAME + "/motion_%02d.png")
	
	os.chdir(OUTPUT_DIR_NAME)

	from lib import append_images
	import glob
	append_images(glob.glob("./motion_*.png"), "result.png")


	# os.system("wsl convert ../motion_*.png -append result.png")
	
	img = cv.imread("result.png")
	values = []
	
	for y in range(img.shape[0]):
		value = img[y, 0, 0]
		values.append(value)
	
	values.sort(reverse=True)
	
	output_img = np.zeros(img.shape, np.uint8)
	for y in range(img.shape[0]):
			output_img[y] = (values[y], values[y], values[y])
	
	cv.imwrite("result_sorted.png", output_img)
	
	print("- done -")
	return


# #########################
if __name__ == "__main__":
	main()
# #########################
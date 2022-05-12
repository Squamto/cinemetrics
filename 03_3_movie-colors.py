# -*- coding: utf-8 -*-
import cv2 as cv
import os
import os.path
import sys
import numpy as np
import scipy
import scipy.cluster
import math

#from lib import hls_sort


from colormath.color_objects import HSLColor, sRGBColor, LabColor
from colormath.color_diff import delta_e_cie1976 as delta_e
from colormath.color_conversions import convert_color

def difference(a, b): # HLS
	# print(a, b)
	#c1 = HSLColor(hsl_h = a[0], hsl_s = a[2]/100.0, hsl_l = a[1]/100.0)
	#c2 = HSLColor(hsl_h = b[0], hsl_s = a[2]/100.0, hsl_l = a[1]/100.0)
	c1 = sRGBColor(a[0], a[1], a[2])
	c2 = sRGBColor(b[0], b[1], b[2])
	#c1.convert_to('lab')
	c1 = convert_color(c1, LabColor)
	#c2.convert_to('lab')
	c2 = convert_color(c2, LabColor)
	# print(delta_e(c1, c2))
	return delta_e(c1, c2)


#import grapefruit
#def difference(a, b):
#	c1 = grapefruit.Color.NewFromHsl(a[0], a[2], a[1])
#	c2 = grapefruit.Color.NewFromHsl(b[0], b[2], b[1])
#	return 1


def sort_by_distance(colors):
	# Find the darkest color in the list.
	root = colors[0]
	for color in colors[1:]:
		if color[1] < root[1]: # l
			root = color
	
	# Remove the darkest color from the stack,
	# put it in the sorted list as starting element.
	stack = [color for color in colors]
	stack.remove(root)
	sorted = [root]
	
	# Now find the color in the stack closest to that color.
	# Take this color from the stack and add it to the sorted list.
	# Now find the color closest to that color, etc.
	while len(stack) > 1:
		closest, distance = stack[0], difference(stack[0], sorted[-1])
		for clr in stack[1:]:
			d = difference(clr, sorted[-1])
			if d < distance:
				closest, distance = clr, d
		stack.remove(closest)
		sorted.append(closest)
	sorted.append(stack[0])
	
	return sorted


WIDTH = 1000
OUTPUT_DIR_NAME = "shot_colors"


def main():
	project_root_dir = sys.argv[1]
	os.chdir(project_root_dir)
	os.chdir(os.path.join(OUTPUT_DIR_NAME, OUTPUT_DIR_NAME))
	
	print(os.system("wsl identify -format \"%k\" result.png"))
	print("reducing colors to 10")
	# os.system("wsl convert result.png +dither -colors 10 result_quant.png")
	
	orig = cv.imread("result.png")

	div = 128
	quantized = orig // div * div + div // 2

	cv.imwrite("result_quant.png", quantized)

	del orig
	del quantized


	img_orig = cv.imread("result_quant.png")
	output_img = np.zeros((WIDTH, WIDTH, 3), np.uint8)
	
	img_hls = cv.cvtColor(img_orig, cv.COLOR_BGR2HLS)
	
	pixels = img_hls.astype(np.float32)
	d = {}
	
	print("counting...")
	for line in pixels:
		for px in line:
			if tuple(px) in d:
				d[tuple(px)] += 1
			else:
				d[tuple(px)] = 1
	
	colors = list(d.keys())
	#print("%d pixels, %d colors" % (img_orig.width*img_orig.height, len(colors)))
	
	print("sorting...")
	#colors.sort(hls_sort)
	colors = sort_by_distance(colors)
	
	px_count = img_orig.shape[1] * img_orig.shape[0]
	x_pos = 0
	
	print("building image...")
	for color in colors:
		l = d[color] / float(px_count)
		l = int(math.ceil( l*WIDTH ))
		
		for x in range(l):
			if x_pos+x >= WIDTH:
					break
			for y in range(WIDTH):
				output_img[y, x_pos+x] = (int(color[0]), int(color[1]), int(color[2]))
		x_pos += l
	
	print("saving...")
	output_img_rgb = cv.cvtColor(output_img, cv.COLOR_HLS2BGR)
	cv.imwrite("_RESULT.png", output_img_rgb)
	
	os.chdir( r"..\.." )
	f = open("colors.txt", "w")
	row = output_img_rgb[0]
	
	counter = 0
	last_px = row[0]
	for i in range(WIDTH):
		px = row[i]
		if np.all(np.equal(px, last_px)):
			counter += 1
			if i == WIDTH-1:
				f.write("%d, %d, %d, %d\n" % (int(last_px[2]), int(last_px[1]), int(last_px[0]), counter))
			continue
		else:
			f.write("%d, %d, %d, %d\n" % (int(last_px[2]), int(last_px[1]), int(last_px[0]), counter))
			counter = 1
			last_px = px
	f.close()
	
	return


# #########################
if __name__ == "__main__":
	main()
# #########################

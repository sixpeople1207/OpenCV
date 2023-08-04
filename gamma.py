from __future__ import print_function
import numpy as np
import argparse
import cv2
import glob
import os 

path = './raw_image/*.jpg'
file_list = glob.glob(path)

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

if __name__ == '__main__': 
	index = 0
	for li in file_list:
		image = cv2.imread(li)
		img_gamma = adjust_gamma(image, 2.5) # 감마값 적용
		dst = img_gamma + (img_gamma-255)*0.6 ## 콘트라스트 적용
		newPath = f'./new_image/{index}.jpg'
		index+=1
		cv2.imwrite(newPath, dst)

import os

import cv2
import numpy as np

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))
PARENT_PATH = os.path.dirname(LOCAL_PATH)

MID_PATH = os.path.join(PARENT_PATH, 'MiddEval3')
TRAIN_PATH = os.path.join(MID_PATH, 'trainingQ')

BASELINE = "baseline"
CALIBTXT = "calib.txt"

IMG0 = "im0.png"
IMG1 = "im1.png"

NDISP = "ndisp"

def covert_to_grey(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def read_calib_txt(filename):
	res = {}
	lines = open(filename, 'r').read().splitlines()
	for line in lines:
		k, v = line.split('=', 1)
		res[k] = v
	return res
	
def ssd(imgL, imgR, prop):
	height, width = imgL.shape
	max_int = np.iinfo(np.int32).max
	min_ssd = np.full(imgL.shape, max_int, dtype=int)

	depth = np.zeros_like(imgL)
	max_offset = int(prop[NDISP])

	for offset in range(max_offset):
		offset = 2
		sub_width = width-offset
		tmpR = np.concatenate((imgR[:, :offset], imgR[:, :sub_width]), axis=1)
		print(tmpR.shape)

		# caculate ssd value
		for h in range(height):
			for w in range(width):
				pass


def main():
	train_dir_list = [os.path.join(TRAIN_PATH, x[0]) for x in os.walk(TRAIN_PATH)]
	for train in train_dir_list[1:2]:
		print("handle "+train)
		img0_grep = covert_to_grey(cv2.imread(os.path.join(train, IMG0)))
		img1_grep = covert_to_grey(cv2.imread(os.path.join(train, IMG1)))
		'''
		cv2.imshow("img0_grep", img0_grep)
		cv2.imshow("img1_grep", img1_grep)
		cv2.waitKey()
		'''
		img_prop = read_calib_txt(os.path.join(train, CALIBTXT))
		ssd(img0_grep, img1_grep, img_prop)

if __name__ == '__main__':
	main()
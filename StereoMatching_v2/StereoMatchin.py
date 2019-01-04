import os

import cv2
import numpy as np

LOCAL_PATH = os.path.dirname(os.path.realpath(__file__))
PARENT_PATH = os.path.dirname(LOCAL_PATH)

MID_PATH = os.path.join(PARENT_PATH, 'MiddEval3')
TRAIN_PATH = os.path.join(MID_PATH, 'trainingQ')

BASELINE = "baseline"
DOFFS 	 = "doffs"
CAM0	 = "cam0"
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

def get_focal(cam):
	return float(cam.split()[0][1:])

def trans_offset(offset):
	return (offset-offset%10)*3
	
def ssd(imgL, imgR, prop, name):
	kernel_size = 5
	baseline = float(prop[BASELINE])
	doffs = float(prop[DOFFS])
	if doffs>85:
		doffs = 85
	focal = get_focal(prop[CAM0])

	height, width = imgL.shape
	max_int = np.iinfo(np.int32).max
	min_ssd = np.full(imgL.shape, max_int, dtype=int)

	depth = np.zeros_like(imgL, dtype='d')
	max_offset = int(prop[NDISP])

	#imgR += 20

	for offset in range(max_offset+1):
		sub_width = width-offset
		print(sub_width)
		tmpR = np.concatenate((imgR[:, :offset], imgR[:, :sub_width]), axis=1)
		print(offset)

		# caculate ssd value
		for h in range(height):
			for w in range(width):
				start_x, start_y = max(0, w-kernel_size), max(0, h-kernel_size)
				end_x, end_y = min(width-1, w+kernel_size), min(height-1, h+kernel_size)
				sum_ssd = np.sum((imgL[start_y:end_y, start_x:(end_x+1)] - tmpR[start_y:end_y, start_x:(end_x+1)])**2)
				if sum_ssd < min_ssd[h, w]:
					# print(sum_ssd, end=" ")
					min_ssd[h, w] = sum_ssd
					#depth[h, w] = baseline*focal / (offset+doffs)
					#print(depth[h, w], end=". ")
					depth[h, w] = trans_offset(offset)
		print(".........................................................")
	
	'''
	md = depth.max()
	mi = depth.min()
	print(md)
	print(mi)
	dl = (md-mi)/255.0
	depth = (depth-mi)/dl
	'''
	
	#print(depth)
	dst = np.array(depth, dtype = np.uint8)
	#dst = cv2.normalize(np.array(depth, dtype = np.uint8), None, 255,0, cv2.NORM_MINMAX, cv2.CV_8UC1)
	#cv2.imshow("depth", dst)
	#cv2.waitKey()
	cv2.imwrite(name+"1.png", dst)

def main():
	train_dir_list = [os.path.join(TRAIN_PATH, x[0]) for x in os.walk(TRAIN_PATH)]
	for train in train_dir_list[1:]:
		print("handle "+train)
		img0_grep = covert_to_grey(cv2.imread(os.path.join(train, IMG0)))
		img1_grep = covert_to_grey(cv2.imread(os.path.join(train, IMG1)))
		#print(img0_grep)
		'''
		cv2.imshow("img0_grep", img0_grep)
		cv2.imshow("img1_grep", img1_grep)
		cv2.waitKey()
		'''
		name = train.split("/")[-1]
		img_prop = read_calib_txt(os.path.join(train, CALIBTXT))
		ssd(img0_grep, img1_grep, img_prop, name)

if __name__ == '__main__':
	main()
import numpy as np
import cv2
import glob
import os

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

def check_lowImage():
	folder_name = "raw_image"
	current= os.getcwd() +f"\\{folder_name}"
	if not os.path.exists(current):	
		print("raw_image폴더가 없습니다.")
		return False
	else:
		print("raw_image확인!.")
		return True
	
if __name__ == '__main__': 

	index=0
	print("--------------------<< DINNO Image Editor >>--------------------")

	while True:
		openPath = input("\n  원본 이미지 폴더 경로(전체경로) : ")
		savePath = input("\n  수정한 이미지 저장 폴더 경로(전체경로) : ")
		print("\n----------------------------------------------------------------")
		print("\n  수정할 폴더 : ",openPath)
		print("\n  저장할 폴더 : ",savePath)
		print("\n----------------------------------------------------------------")
		isOk = input("\n  경로가 맞습니까?(y/n):")
		
		if(isOk=='y' or isOk == 'Y'):
			print("\n  Image Editing...작업시작")
			break
	
	try:
		path = openPath + '/*.jpg'
		file_list = glob.glob(path)
		print(f"\n  {len(file_list)}개의 이미지가 검색되었습니다.")

		if not os.path.exists(savePath):
			os.makedirs(savePath)

		for li in file_list:
			img_array = np.fromfile(li, np.uint8)
			curImg = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
			filename = li.split('\\')

			img_gamma = adjust_gamma(curImg, 2.0) # 감마값 적용
			final_img = img_gamma + (img_gamma-255)*0.6 ## 콘트라스트 적용
			
			newPath = f'{savePath}\{filename[len(filename)-1]}_.jpg'
			result, encoded_img = cv2.imencode('.jpg', final_img)
			
			if result:
				with open(newPath, mode='w+b') as f:
					encoded_img.tofile(f)

			msg = f'\r진행 수량 : {index+1}/{len(file_list)}(완료/총계)'
			index+=1
			print(msg, end='')

		if index == len(file_list):
			print("작업이 완료 되었습니다.")

		os.system("pause")
	except SystemError as e:
		print(e)
		os.system("pause")



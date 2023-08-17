import numpy as np
import argparse
import cv2
import glob
import os
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtGui import *
import sys
from PyQt5.QtCore import Qt, QPoint

form_class = uic.loadUiType('./main.ui')[0]

class MainWindows(QMainWindow, form_class):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
		self.btn_close.clicked.connect(self.window_closed)
		self.btn_minimize.clicked.connect(self.window_minimized)
		self.btn_maximize_restore.clicked.connect(self.window_maximized)
		self.isMaximized = 0

	def window_maximized(self):
		if(self.isMaximized == 0):
			self.setFixedSize(2400, 2400)
			self.isMaximized = 1
		elif(self.isMaximized == 1):
			self.setFixedSize(500, 500)
			self.isMaximized = 0

	def window_minimized(self):
		print(int(self.isMinimized()))
		self.showMinimized()
		print(int(self.isMinimized()))

	def window_closed(self):
		self.window_closed()
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.__press_pos = event.pos()  
			print(event.pos())

	def mouseReleaseEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.__press_pos = QPoint()

	def mouseMoveEvent(self, event):
		if not self.__press_pos.isNull():  
			self.move(self.pos() + (event.pos() - self.__press_pos))
			
def ui_auto_complete(ui_dir, ui_to_py_dir):
    encoding = 'utf-8'

    # UI 파일이 존재하지 않으면 아무 작업도 수행하지 않는다.
    if not os.path.isfile(ui_dir):
        print("The required file does not exist.")
        return
 
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
	app = QApplication(sys.argv)
	myWindow = MainWindows()
	myWindow.show()
	sys.exit(app.exec_())


	# if(isRaw):
	# 	folder_name = "new_images"
	# 	current= os.getcwd() +f"\\{folder_name}"
	# 	if not os.path.exists(current):
	# 		os.makedirs(current)
		
	# 	for li in file_list:
	# 		image = cv2.imread(li)
	# 		filename = li.split('\\')
	# 		img_gamma = adjust_gamma(image, 2.0) # 감마값 적용
	# 		dst = img_gamma + (img_gamma-255)*0.6 ## 콘트라스트 적용
	# 		newPath = f'./{folder_name}/{filename[len(filename)-1]}_.jpg'
	# 		msg = f'\r진행 수량 : {index+1}/{len(file_list)}(완료/총계)'
	# 		index+=1
	# 		print(msg, end='')
	# 		cv2.imwrite(newPath, dst)

	# 	if index == len(file_list):
	# 		print("작업이 완료 되었습니다.")
	# else:
	# 	print("폴더 확인 필요합니다.")
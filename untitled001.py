# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 13:16:44 2021

@author: Administrator
"""
import PySide2.QtCore
from PySide2 import QtCore

print(QtCore.QString('foo'))
# import time_log
import cv2
# import tensorflow

count = cv2.cuda.getCudaEnabledDeviceCount()
print(count)
# print(tensorflow.test.is_gpu_available())

# import sys

# sys.path.append('D:\\Anaconda\\envs\\python36\\lib\\site-packages\\IPython\\extensions')
# sys.path.append('C:\\Users\\Administrator\\.ipython')
# print(sys.path)
import os
print(os.environ.get("CUDA_VISIBLE_DEVICES"))
# path = os.environ['PATH']
# new_path = r'D:\Anaconda\envs\python36\lib\site-packages\PyQt5\Qt5\bin;' + path
# os.environ['PATH'] = new_path
# print(os.environ['PATH'])
#os.environ["LANG"] = 'en'
#os.environ["QT_SCALE_FACTOR"] = ''
#os.environ["QT_SCREEN_SCALE_FACTORS"] = ''
#for key in os.environ.keys():
#    print(key + ":::::")
#    print(os.environ[key])

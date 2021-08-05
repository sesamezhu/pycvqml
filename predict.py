# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:30:57 2020

@author: Lenovo
"""
#import tensorflow as tf
from tensorflow.keras.layers import Input
from mask_rcnn import MASK_RCNN 
from PIL import Image

import os
import skimage



def SinglePredict(filename):
    #img = input(filename)
    try:
        image = skimage.io.imread(filename)
        if image.ndim != 3:
            image = skimage.color.gray2rgb(image)
        if image.shape[-1] == 4:
            image = image[..., :3]
        #image = Image.open(filename)
    except:
        mask_rcnn.close_session()
        print('Open Error! Try again!')
    else:
        mask_rcnn.detect_image(image)
        #angle = mask_rcnn.detect_image(image)
        #print("predict ", filename ,"ok")
    
    #return angle

def BatchPredict(DirPath, SafeSignal):
    fileList=os.listdir(DirPath)
    for fileName in fileList:
        name=DirPath+'\\'+fileName
        SinglePredict(name)
        '''
        angle = SinglePredict(name)
        print(str(angle))
        signal='no distance'
        if abs(angle) > 65:
            signal = 'safe'
        elif abs(angle) >0 :
            signal = 'not safe'
        else:
            signal = 'no distance'
        print(str(angle))
        '''

        
        # src='TestResult/tmp1.png'
        # dst='TestResult/'+fileName.replace('.png', '_mask.png')
        # os.rename(src,dst)
        
        src='TestResult/tmp2.png'
        dst='TestResult/'+fileName.replace('.png', '_predict.png')
        os.rename(src,dst)
        
        '''
        src='TestResult/tmp2.png'
        dst='TestResult/'+fileName.replace('.png', '_predict.png')
        os.rename(src,dst)
        '''
if __name__ == "__main__":
    

    mask_rcnn = MASK_RCNN()
    BatchPredict('./VID3', SafeSignal=True)  # 要进行预测的文件夹
    #SinglePredict('E:/maskrcnn20200419/mask-rcnn-keras-master/2.png')
    mask_rcnn.close_session()
    
    #clientSocket.close()  
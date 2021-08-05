'''
针对detect_image函数，增加了返回值angle
用于计算挂钩和耳轴角度
是predict_angle.py专用的库
'''
import os
import sys
import random
import math
import numpy as np
import skimage.io
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
from nets.mrcnn import get_predict_model
from utils.config import Config
from utils.anchors import get_anchors
from utils.utils import mold_inputs,unmold_detections
from utils import visualize
import keras.backend as K
import tensorflow as tf


class MASK_RCNN(object):
    _defaults = {
        "model_path": 'logs_test/epoch049_loss0.051_val_loss0.051.h5',
        "classes_path": './model_data/hook_classes.txt',
        "confidence": 0.7,

        # 使用coco数据集检测的时候，IMAGE_MIN_DIM=1024，IMAGE_MAX_DIM=1024, RPN_ANCHOR_SCALES=(32, 64, 128, 256, 512)
        "RPN_ANCHOR_SCALES": (16,32, 64, 128, 256),
        "IMAGE_MIN_DIM": 512,
        "IMAGE_MAX_DIM": 512,
        
        # 在使用自己的数据集进行训练的时候，如果显存不足要调小图片大小
        # 同时要调小anchors
        #"IMAGE_MIN_DIM": 512,
        #"IMAGE_MAX_DIM": 512,
        #"RPN_ANCHOR_SCALES": (16, 32, 64, 128, 256)
    }

    @classmethod
    def get_defaults(cls, n):
        if n in cls._defaults:
            return cls._defaults[n]
        else:
            return "Unrecognized attribute name '" + n + "'"

    #---------------------------------------------------#
    #   初始化Mask-Rcnn
    #---------------------------------------------------#
    def __init__(self, **kwargs):
        self.__dict__.update(self._defaults)
        # fix graph error
        self.graph = tf.get_default_graph()
        
        self.class_names = self._get_class()
        self.sess = K.get_session()
        #self.sess = tf.compat.v1.keras.backend.get_session()
        self.config = self._get_config()
        self.generate()
    #---------------------------------------------------#
    #   获得所有的分类
    #---------------------------------------------------#
    def _get_class(self):
        classes_path = os.path.expanduser(self.classes_path)
        with open(classes_path) as f:
            class_names = f.readlines()
        class_names = [c.strip() for c in class_names]
        class_names.insert(0,"BG")
        return class_names

    def _get_config(self):
        class InferenceConfig(Config):
            NUM_CLASSES = len(self.class_names)
            GPU_COUNT = 1
            IMAGES_PER_GPU = 1
            DETECTION_MIN_CONFIDENCE = self.confidence
            
            NAME = "hook"
            RPN_ANCHOR_SCALES = self.RPN_ANCHOR_SCALES
            IMAGE_MIN_DIM = self.IMAGE_MIN_DIM
            IMAGE_MAX_DIM = self.IMAGE_MAX_DIM

        config = InferenceConfig()
        config.display()
        return config

    #---------------------------------------------------#
    #   生成模型
    #---------------------------------------------------#
    def generate(self):
        model_path = os.path.expanduser(self.model_path)
        assert model_path.endswith('.h5'), 'Keras model or weights must be a .h5 file.'
        
        # 计算总的种类
        self.num_classes = len(self.class_names)

        # 载入模型，如果原来的模型里已经包括了模型结构则直接载入。
        # 否则先构建模型再载入
        self.model = get_predict_model(self.config)
        self.model.load_weights(self.model_path,by_name=True)
    
    #---------------------------------------------------#
    #   检测图片
    #---------------------------------------------------#
    def detect_image(self, image):
        # 以np数组读取图片，和后边的image[0]完全一致，没有区别
        # print(image.shape, type(image))
        image = [np.array(image)]
        # 根据config对图片进行resize等一系列预处理操作
        # 注：moold_input可以处理一个batch的图像的
        molded_images, image_metas, windows = mold_inputs(self.config,image)
        # 获取图片shape
        image_shape = molded_images[0].shape
        # 生成anchors
        anchors = get_anchors(self.config,image_shape)
        anchors = np.broadcast_to(anchors, (1,) + anchors.shape)
        # 调用模型进行检测
        # detections.shape=(N,100,6)
        # N代表预测的图片数量，单张预测时候都是1
        # 100代表每张图片最多预测100个目标（实际上并没有那么多，后边的都是000000）
        # 6的前4个元素是box信息（y1,x1,y2,x2），第5个元素是class_id即预测的类别号，第6个元素是置信度
        # mrcnn_mask.shape=(N,100,28,28,k),即N张图，每个100个目标，每个目标的mask是一个(28,28)的矩阵
        # 由于对每种目标都进行了预测，所以k个目标对应k个mask即（28,28，k）
        with self.graph.as_default():
            detections, _, _, mrcnn_mask, _, _, _ =\
                self.model.predict([molded_images, image_metas, anchors], verbose=0)
        #print('detections',detections.shape,detections)
        #print('mrcnn_mask',mrcnn_mask.shape,mrcnn_mask)
        # 将预测结果根据之前的预处理信息，反变换到原图上
        # 反变换结果：
        # final_rois是对应于原图的box信息(y1,x1,y2,x2)
        # final_class_ids是类别信息 
        # final_scores是置信度
        # final_masks是mask信息
        final_rois, final_class_ids, final_scores, final_masks =\
            unmold_detections(detections[0], mrcnn_mask[0],
                                    image[0].shape, molded_images[0].shape,
                                    windows[0])
        
        #print('rois',final_rois.shape,final_rois)
        #print('class_ids',final_class_ids.shape,final_class_ids)
        #print('scores',final_scores.shape,final_scores)
        #print('masks',final_masks.shape,final_masks)

        r = {
            "rois": final_rois,
            "class_ids": final_class_ids,
            "scores": final_scores,
            "masks": final_masks,
        }
        # print(image[0].shape, type(image[0]))  # 就是np格式的原图
        img_predict = visualize.display_instances(image[0], r['rois'], r['masks'], r['class_ids'], self.class_names, r['scores'])
        
        #angle = visualize.get_angle(image[0], r['rois'], r['masks'], r['class_ids'], self.class_names, r['scores'])
        
        #return angle
        return np.array(img_predict)
        
        
    def close_session(self):
        self.sess.close()
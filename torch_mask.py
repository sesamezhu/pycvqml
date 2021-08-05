import numpy as np
import argparse
import glob
import multiprocessing as mp
import os
import time
import cv2
import tqdm

from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets import load_coco_json
from detectron2.data.detection_utils import read_image
from detectron2.engine import default_setup
from detectron2 import model_zoo
from detectron2.utils.logger import setup_logger
from detectron2.utils.visualizer import ColorMode
from predictor import VisualizationDemo

class mask_rcnn(object):
    def __init__(self, *args):
        self.args = self.get_parser().parse_args(args=[])
        self.cfg = self.setup(self.args)
        self.vis = VisualizationDemo(self.cfg, instance_mode=ColorMode.SEGMENTATION, parallel=True)



    def get_parser(self):
        parser = argparse.ArgumentParser(description="Detectron2 Inference")
        parser.add_argument("--config-file", default="", metavar="FILE", help="path to config file")
        parser.add_argument("--input", nargs="+", help="A list of space separated input images")
        parser.add_argument(
            "--output",
            help="A file or directory to save output visualizations. "
                "If not given, will show output in an OpenCV window.",
        )
        parser.add_argument(
            "--confidence-threshold",
            type=float,
            default=0.5,
            help="Minimum score for instance predictions to be shown",
        )
        parser.add_argument(
            "--opts",
            help="Modify config options using the command-line 'KEY VALUE' pairs",
            default=[],
            nargs=argparse.REMAINDER,
        )
        return parser

    def setup(self,args):
        """
        Create configs and perform basic setups.
        """
        cfg = get_cfg()
        args.config_file = model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
        cfg.merge_from_file(args.config_file)
        cfg.merge_from_list(args.opts)
        cfg.DATASETS.TRAIN = ("self_train",) # 训练数据集名称
        cfg.DATASETS.TEST = ("self_val",)
        cfg.DATALOADER.NUM_WORKERS = 4  # 单线程
        # cfg.INPUT.CROP.ENABLED = True
        # cfg.INPUT.MAX_SIZE_TRAIN = 640 # 训练图片输入的最大尺寸
        # cfg.INPUT.MAX_SIZE_TEST = 640 # 测试数据输入的最大尺寸
        # cfg.INPUT.MIN_SIZE_TRAIN = (512, 768) # 训练图片输入的最小尺寸，可以设定为多尺度训练
        # cfg.INPUT.MIN_SIZE_TEST = 640
        #cfg.INPUT.MIN_SIZE_TRAIN_SAMPLING，其存在两种配置，分别为 choice 与 range ：
        # range 让图像的短边从 512-768随机选择
        #choice ： 把输入图像转化为指定的，有限的几种图片大小进行训练，即短边只能为 512或者768
        # cfg.INPUT.MIN_SIZE_TRAIN_SAMPLING = 'range'
        #  本句一定要看下注释！！！！！！！！
        cfg.MODEL.RETINANET.NUM_CLASSES = 3  # 类别数+1（因为有background，也就是你的 cate id 从 1 开始，如果您的数据集Json下标从 0 开始，这个改为您对应的类别就行，不用再加背景类！！！！！）
        #cfg.MODEL.WEIGHTS="/home/yourstorePath/.pth"
        cfg.MODEL.WEIGHTS = 'model_0008995.pth'    # 预训练模型权重
        cfg.SOLVER.IMS_PER_BATCH = 4  # batch_size=2; iters_in_one_epoch = dataset_imgs/batch_size
        # 根据训练数据总数目以及batch_size，计算出每个epoch需要的迭代次数
        #9000为你的训练数据的总数目，可自定义
        ITERS_IN_ONE_EPOCH = int(9000 / cfg.SOLVER.IMS_PER_BATCH)
        # 指定最大迭代次数
        cfg.SOLVER.MAX_ITER = (ITERS_IN_ONE_EPOCH * 12) - 1 # 12 epochs，
        # 初始学习率
        cfg.SOLVER.BASE_LR = 0.002
        # 优化器动能
        cfg.SOLVER.MOMENTUM = 0.9
        #权重衰减
        cfg.SOLVER.WEIGHT_DECAY = 0.0001
        cfg.SOLVER.WEIGHT_DECAY_NORM = 0.0
        # 学习率衰减倍数
        cfg.SOLVER.GAMMA = 0.1
        # 迭代到指定次数，学习率进行衰减
        cfg.SOLVER.STEPS = (7000,)
        # 在训练之前，会做一个热身运动，学习率慢慢增加初始学习率
        cfg.SOLVER.WARMUP_FACTOR = 1.0 / 1000
        # 热身迭代次数
        cfg.SOLVER.WARMUP_ITERS = 1000
        cfg.SOLVER.WARMUP_METHOD = "linear"
        # 保存模型文件的命名数据减1
        cfg.SOLVER.CHECKPOINT_PERIOD = ITERS_IN_ONE_EPOCH - 1
        # 迭代到指定次数，进行一次评估
        cfg.TEST.EVAL_PERIOD = ITERS_IN_ONE_EPOCH
        #cfg.TEST.EVAL_PERIOD = 100
        #cfg.merge_from_file(args.config_file)
        #cfg.merge_from_list(args.opts)
        cfg.freeze()
        default_setup(cfg, args)

        return cfg


    def inference(self, image):
        #image应为BGR格式
        _, visualized_output = self.vis.run_on_image(image)
        img_predict = visualized_output.get_image()[:, :, ::-1]
        return np.array(img_predict)


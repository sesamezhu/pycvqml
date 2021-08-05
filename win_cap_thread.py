# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:16:48 2021

@author: zhugh
"""
from concurrent.futures import ThreadPoolExecutor
import traceback
# import mask_rcnn
# from qtpy import QtCore
from torch_mask import mask_rcnn
import cv2
import win_app_model
import win_capture
import time
import time_log
import win_cap_utils

global server_running
server_running = True
cap_threads = []


class WinCapThread:
    def __init__(self):
        self.rcnn = mask_rcnn()

    def detect(self, cap):
        frame = cap.m_raw_data
        if win_app_model.win_app_data_model.m_rcnn:
            time_log.time_log("detecting.no-{}-{}".format(
                cap._read_total, cap._mask_total))
            if win_cap_utils.get_color_len(frame.shape) == 4:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
                frame = cv2.flip(frame, 1)
            try:
                # frame = self.rcnn.detect_image(frame)
                frame = self.rcnn.inference(frame)
            except:
                traceback.print_exc()
            cap._mask_count += 1
            cap._mask_total += 1
        else:
            frame = win_app_model.win_app_data_model.cv2_filter(frame)
        
        cap.process_image(frame)

    def detect_main(self):
        global server_running
        try:
            while server_running:
                cap = win_capture.get_indexed_capture()
                if cap._detecting:
                    time_log.time_log("detecting already")
                    time.sleep(0.1)
                    continue
                if cap._sec_last > 0:
                    cap._detecting = False
                    try:
                        self.detect(cap)
                    except:
                        traceback.print_exc
                    cap._detecting = False
                else:
                    time.sleep(0.1)
        except:
            traceback.print_exc()
        self.rcnn.close_session()


def detect_stop():
    global server_running
    server_running = False 

# def detect_sync(cap):
#     detect_cap(m_mask_rcnn, cap)

def detect_run():
    executor = ThreadPoolExecutor(max_workers=4)
    for i in range(3):
        run = WinCapThread()
        cap_threads.append(run)
        executor.submit(run.detect_main)

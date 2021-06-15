import cv2 as cv
import numpy as np


class PinnedMem(object):
    def __init__(self, size, dtype=np.uint8):
        self.array = np.empty(size, dtype)
        cv.cuda.registerPageLocked(self.array)
        self.pinned = True

    def __del__(self):
        cv.cuda.unregisterPageLocked(self.array)
        self.pinned = False

    def __repr__(self):
        return f'pinned = {self.pinned}'


class VidCap:
    def __init__(self, vid_path, max_frames=-1):
        self.vid_path = vid_path
        self.frame_num = 0
        self.open = False
        cap = cv.VideoCapture(vid_path)
        assert cap.isOpened(), f"{vid_path}: cannot be opened!"
        self.num_frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
        self.max_frames = self.num_frames if max_frames == -1 else max_frames
        ret, frame = cap.read()
        cap.release()
        self.rows, self.cols, self.channels = frame.shape

    def UpdateState(self, ret):
        if (not ret or self.frame_num + 1 == self.max_frames):
            self.open = False
        if (ret or self.frame_num + 1 == self.max_frames):
            self.frame_num += 1

    def isOpened(self):
        return self.open

    def __del__(self):
        pass


class CudaCap(VidCap):
    def __init__(self, vid_path, max_frames=-1):
        VidCap.__init__(self, vid_path, max_frames)
        # cudacodec always returns 4 channels - check grey video
        self.channels = 4
        # cudacodec seems to need rows/16
        self.rows = (np.ceil(self.rows / 16) * 16).astype(int)
        self.cap = cv.cudacodec.createVideoReader(self.vid_path)
        self.open = True
        self.frame_device = cv.cuda_GpuMat(self.rows, self.cols, cv.CV_8UC4)
        self.frame_host = PinnedMem((self.rows, self.cols, self.channels))
        self.stream = cv.cuda_Stream()

    def GetFrame(self):
        return self.GetDeviceFrame()

    def GetDeviceFrame(self):
        ret, _ = self.cap.nextFrame(self.frame_device, self.stream)
        self.UpdateState(ret)
        return ret, self.frame_device

    def read(self):
        ret, self.frame_device = self.GetDeviceFrame()
        if ret:
            colored = cv.cuda.cvtColor(self.frame_device, cv.COLOR_BGRA2RGBA)
            flipped = cv.cuda.flip(colored, 1)
            flipped.download(self.frame_host.array)
        return ret, self.frame_host.array

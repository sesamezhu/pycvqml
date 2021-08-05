# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:22:01 2021

@author: zhugh
"""

class win_cap_counter:
    def __init__(self):
        #图像读取总计数
        self._read_total = 0
        # read amount in current second
        self._sec_count = 0
        # read amount in previous whole second
        self._sec_last = 0
        # 模型检测总次数
        self._mask_total = 0
        # check amount in current second
        self._mask_count = 0
        # check amount in previous whole second
        self._mask_last = 0
        # read failure amount
        self._failure_total = 0
        # exception amount on read
        self._error_total = 0
        # bad amount in previous hour
        self._bad_last = 0
        # bad amount in current hour
        self._bad_count = 0
        
    def inc_read(self):
        self._read_total += 1
        self._sec_count += 1
    
    def inc_mask(self):
        self._mask_total += 1
        self._mask_count += 1
        
    def inc_error(self):
        self._error_total += 1
        self._bad_count += 1
    
    def inc_failure(self):
        self._failure_total += 1
        self._bad_count += 1

    def last_read(self):
        self._sec_last = self._sec_count
        self._sec_count = 0
    
    def last_mask(self):
        self._mask_last = self._mask_count
        self._mask_count = 0
    
    def last_bad(self):
        self._bad_last = self._bad_count
        self.bad_count = 0
    
    def last_info(self):
        return "read-{},mask-{},bad-{}".format(
            self._sec_last, self._mask_last, self._bad_last)
    
    def add_last_other(self, other):
        self._sec_last += other._sec_last
        self._mask_last += other._mask_last
        self._bad_last += other._bad_last

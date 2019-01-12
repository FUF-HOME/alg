#!/usr/bin/env python
# -*-coding:utf-8-*-

class Sort():
    """常见的排序算法"""



    def quick_sort(self,nums,):
        """快速排序"""
        if len(nums)<2:
            return nums
        else:
            middle = nums[0]
            less=[i for i in nums[1:] if i <= middle]
            greater=[j for j in nums[1:] if j >= middle]
            return self.quick_sort(less)+middle+self.quick_sort(greater)



    def bubble_sort(self):
        pass
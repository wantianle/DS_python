# coding=utf-8

# 53、最大子序列
# 题目：给定⼀个整数数组 nums ，找到⼀个具有最⼤和的连续⼦数组（⼦数组最少包含⼀个元素），返回其最⼤和。
# ⽰例:
# 输⼊: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续⼦数组 [4,-1,2,1] 的和最⼤，为 6

# 主要思路：1.暴力解法 2.贪心算法：代码随想录里面的方法好，只要总和出现负数就归零，即找到起始位置，然后遍历求最值就行了。没考虑负数数组啊。。。

import numpy as np

nums = np.random.randint(-5, -1, size=5)
print(nums)
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


class Solution:

    def maxSubArray(self, nums):
        count = 0
        max_sum = nums[0]
        max = nums[0]
        for num in nums:
            count += num
            # 定起始位置
            if count < 0:
                count = 0
            # 定结束位置
            if count >= max_sum:
                max_sum = count
            if num > max:
                max = num
        if max != 0 and max_sum == 0:
            return max
        else:
            return max_sum


s = Solution()
print(s.maxSubArray(nums))

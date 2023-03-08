# coding=utf-8

# 53、最大子序列
# 给定⼀个整数数组 nums ，找到⼀个具有最⼤和的连续⼦数组（⼦数组最少包含⼀个元素），返回其最⼤和。
# ⽰例:
# 输⼊: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续⼦数组 [4,-1,2,1] 的和最⼤，为 6

# 主要思路：1.暴力解法 2.贪心算法：代码随想录里面的方法好，只要总和出现负数就归零，我这里思想是定多次最值，最后判定保存

import numpy as np
import random

nums = [i-random.randint(0, 20) for i in np.random.choice(21, 10)]
print(nums)
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum = 0
max = nums[0]
min = nums[0]
res = 0
for i, num in enumerate(nums):
    sum += num
    # 定起始位置
    if sum <= min:
        min = sum
        ind = i
    # 定结束位置
    if sum >= max:
        max = sum
        index = i
    # 判断最值合理性并保存
    if ind < index and (max - min) > res:
        res = max - min
print(res)

# coding=utf-8

# 53、最大子序列
# 题目：给定⼀个整数数组 nums ，找到⼀个具有最⼤和的连续⼦数组（⼦数组最少包含⼀个元素），返回其最⼤和。
# ⽰例:
# 输⼊: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续⼦数组 [4,-1,2,1] 的和最⼤，为 6

# 主要思路：1.暴力解法 2.贪心算法：代码随想录里面的方法好，只要总和出现负数就归零，我这里思想是定多次最值，最后判定保存，有点动态规划感觉在里面

import numpy as np

nums = np.random.randint(-10, 10, size=6)
print(nums)
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
count = 0
max = nums[0]
min = nums[0]
res = 0
for i, num in enumerate(nums):
    count += num
    # 定起始位置
    if count <= min:
        min = count
        ind = i
    # 定结束位置
    if count >= max:
        max = count
        index = i
    # 判断最值合理性并保存
    if ind < index and (max - min) > res:
        res = max - min
print(res)

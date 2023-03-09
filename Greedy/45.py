# coding=utf-8

# 45、跳跃游戏II
# 题目：给定⼀个⾮负整数数组，你最初位于数组的第⼀个位置。数组中的每个元素代表你在该位置可以跳跃的最⼤长度。你的⽬标是使⽤最少的跳跃次数到达数组的最后⼀个位置。
# ⽰例:
# 输⼊: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后⼀个位置的最⼩跳跃数是 2。从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后⼀个位置。
# 说明:假设你总是可以到达数组的最后⼀个位置。

# 主要思路：求最小跳数，就求每跳一步能覆盖的范围就行了

# import numpy as np
# nums = np.random.randint(0, 6, size=10)
# nums = [2, 3, 1, 1, 4]
nums = [3, 4, 3, 2, 5, 4, 3]
# nums = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
print(nums)


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_distance = 0
        res = 0
        next_distance = 0
        lenth = len(nums) - 1
        for i in range(lenth):
            next_distance = max(nums[i] + i, next_distance)
            if next_distance == lenth:
                res += 1
                break
            if i == cur_distance:
                cur_distance = next_distance
                res += 1
        return res

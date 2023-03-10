# coding=utf-8

# 55、跳跃游戏
# 题目：给定⼀个⾮负整数数组，你最初位于数组的第⼀个位置。数组中的每个元素代表你在该位置可以跳跃的最⼤长度。判断你是否能够到达最后⼀个位置。
# ⽰例 1:
# 输⼊: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后⼀个位置。
# ⽰例 2:
# 输⼊: [3,2,1,0,4]
# 输出: false
# 解释: ⽆论怎样，你总会到达索引为 3 的位置。但该位置的最⼤跳跃长度是 0 ， 所以你永远不可能到达最后⼀个位置

# 主要思路：只要求最大覆盖范围即可得到答案，把整体覆盖范围拆成每一步的覆盖范围看，每走一步对比新增步数和剩余步数直到剩余步数归0，如果都不能获得更多步数使得总步数大于总距离，即不能跳到最后位置。

import numpy as np

nums = np.random.randint(0, 5, size=8)
print(nums)
# 这里关键是python不能设置循环下标从1开始，所以开始空跳一步，cur=1，接着获取当前格子步数，再逐格对比，多则替换，少则不变，并且每一格减一步，最终输出在最终格的剩余步数，小于0则不能


class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur = 1
        for i, num in enumerate(nums):
            cur -= 1
            if cur <= num and cur >= 0:
                cur = num
            # print(cur)
        return cur >= 0

# coding=utf-8

# 1005、K次取反后最大化数组和
# 题目：给定⼀个整数数组A，我们只能⽤以下⽅法修改该数组：我们选择某个索引i并将A[i]替换为-nums[i]，然后总共重复这个过程K次。（我们可以多次选择同⼀个索引i）以这种⽅式修改数组后，返回数组可能的最⼤和。
# ⽰例 1：
# 输⼊：A = [4,2,3], k = 1
# 输出：5
# 解释：选择索引 (1,) ，然后 nums 变为 [4,-2,3]。
# ⽰例 2：
# 输⼊：A = [3,-1,0,2], k = 3
# 输出：6
# 解释：选择索引 (1, 2, 2) ，然后 nums 变为 [3,1,0,2]。
# ⽰例 3：
# 输⼊：A = [2,-3,-1,5,-4], k = 2
# 输出：13
# 解释：选择索引 (1, 4) ，然后 nums 变为 [2,3,-1,5,4]。
# 提⽰：
# 1 <= nums.length <= 10000
# 1 <= k <= 10000
# -100 <= nums[i] <= 100

# 主要思路：排序取反，关键是排序算法能用api吗？

import numpy as np
from random import randint

nums = np.random.randint(-10, 10, size=5)
k = randint(3, 10)
# nums = [-8, -1, -4, -1, -9]
# k = 8
print(nums, k)


class Solution(object):

    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        # print(nums)
        flag = 1
        res = 0
        lenth = len(nums)
        for a in range(k):
            if a < lenth:
                if nums[a] <= 0:
                    nums[a] = -nums[a]
                elif nums[a] > 0 and flag:
                    flag = 0
                    nums.sort()
                    nums[0] = -nums[0]
                    # print("just once")
                else:
                    nums[0] = -nums[0]
            elif a == lenth:
                # print("a == len")
                nums.sort()
                nums[0] = -nums[0]
            else:
                nums[0] = -nums[0]
            # print(nums)
        for a in nums:
            res += a
        return res

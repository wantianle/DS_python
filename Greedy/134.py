# coding=utf-8

# 134、加油站
# 题目：在⼀条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。你有⼀辆油箱容量⽆限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的⼀个加油站出发，开始时油箱为空。如果你可以绕环路⾏驶⼀周，则返回出发时加油站的编号，否则返回 -1。
# 说明:
# 如果题⽬有解，该答案即为唯⼀答案。
# 输⼊数组均为⾮空数组，且长度相同。
# 输⼊数组中的元素均为⾮负数。
# ⽰例 1:
# 输⼊:
# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好⾜够你返回到 3 号加油站。
# 因此，3 可为起始索引。
# ⽰例 2:
# 输⼊:
# gas = [2,3,4]
# cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有⾜够的汽油可以让你⾏驶到下⼀个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你⽆法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，⽆论怎样，你都不可能绕环路⾏驶⼀周。

# 主要思路：1.暴力解法，就循环遍历 2.贪心算法：明显汽车第一站只能从油量大于消耗的加油站开始，由说明可知，gas<=cost，这样才会有唯一解或无解，在这条件下，通过求gas-cost的差分，让连续子序列差分和最大（局部最优，汽油盈余最多，整体最优），则序列起点即是起点加油站。

# import numpy as np

# 数据输入区域
# list = [1, 2, 3, 4, 5, 6]
# gas = np.random.choice(list, 6, replace=False)
# cost = np.random.choice(list, 6, replace=False)
# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
gas = [4, 2, 5, 1, 3, 6]
cost = [1, 5, 2, 3, 6, 4]
# gas = [2, 3, 4]
# cost = [3, 4, 3]
print("gas =", gas)
print("cost =", cost)

# # 贪心算法：转换为求差分环最大子序和
# diff = [0] * len(gas)
# sum = 0
# # # 求差分列表
# for i in range(len(gas)):
#     diff[i] = gas[i] - cost[i]
#     sum += diff[i]
# print("diff =", diff)
# if sum < 0:
#     print(-1)
# else:
#     # 求差分环路最大子序列和，即看成两个差分列表的拼接，求单向最大子序和
#     diff2 = diff + diff
#     max = diff2[0]
#     count = 0
#     for i in range(len(diff2)):
#         count += diff2[i]
#         if count < 0:
#             count = 0
#             start = i + 1
#         if count >= max:
#             max = count
#     print(start % len(gas))

# 贪心算法2：差分的实际意义。⾸先如果总油量减去总消耗⼤于等于零那么⼀定可以跑完⼀圈，说明 各个站点的加油站 剩油量rest[i]相加⼀定是⼤于等于零的。每个加油站的剩余量rest[i]为gas[i] - cost[i]。i从0开始累加rest[i]，和记为curSum，⼀旦curSum⼩于零，说明[0, i]区间都不能作为起始位置，起始位置从i+1算起，再从0计算curSum。


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curSum = 0
        totalSum = 0
        start = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if (curSum < 0):
                start = i + 1
                curSum = 0
        if (totalSum < 0):
            return -1
        return start

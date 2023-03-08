# coding=utf-8

# 1005、K次取反后最大化数组和
# 题目：给定⼀个整数数组A，我们只能⽤以下⽅法修改该数组：我们选择某个索引i并将A[i]替换为-A[i]，然后总共重复这个过程K次。（我们可以多次选择同⼀个索引i）以这种⽅式修改数组后，返回数组可能的最⼤和。
# ⽰例 1：
# 输⼊：A = [4,2,3], K = 1
# 输出：5
# 解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
# ⽰例 2：
# 输⼊：A = [3,-1,0,2], K = 3
# 输出：6
# 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
# ⽰例 3：
# 输⼊：A = [2,-3,-1,5,-4], K = 2
# 输出：13
# 解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
# 提⽰：
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100

# 主要思路：排序取反，关键是排序算法能用api吗？

# import numpy as np
# from random import randint

# A = np.random.randint(-100, 100, size=10)
# K = randint(1, 10)
# print(A, K)
A = [2, -3, -1, 5, -4]
K = 2
A.sort()
# print(A)
flag = 1
res = 0
for a in range(K):
    if A[a] <= 0:
        A[a] = -A[a]
    elif A[a] > 0 and flag:
        flag = 0
        A.sort()
        A[0] = -A[0]
        # print("just once")
    else:
        A[0] = -A[0]
    # print(A)
for a in A:
    res += a
print(res)

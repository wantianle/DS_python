# coding=utf-8

# 376、摆动序列
# 题目：如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第⼀个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。例如， [1,7,4,9,2,5] 是⼀个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第⼀个序列是因为它的前两个差值都是正数，第⼆个序列是因为它的最后⼀个差值为零。给定⼀个整数序列，返回作为摆动序列的最长⼦序列的长度。通过从原始序列中删除⼀些（也可以不删除）元素来获得⼦序列，剩下的元素保持其原始顺序。
# ⽰例 1:
# 输⼊: [1,7,4,9,2,5]
# 输出: 6
# 解释: 整个序列均为摆动序列
# ⽰例 2:
# 输⼊: [1,17,5,10,13,15,10,5,16,8]
# 输出: 7
# 解释: 这个序列包含⼏个长度为 7 摆动序列，其中⼀个可为[1,17,10,13,10,16,8]
# ⽰例 3:
# 输⼊: [1,2,3,4,5,6,7,8,9]
# 输出: 2

# 主要思路：贪⼼算法，让峰值尽可能的保持峰值，然后删除单⼀坡度上的节点，计算两数差值然后比较，关键在于如何处理开头和末尾，以及中间值的保存与计算。(不考虑空列表)

import numpy as np

list = np.random.choice(30, 8, replace=False)
pre_diff, cur_diff = 0, 0
res = 1
for index, num in enumerate(list):
    print(num, end=" ")
    if index == 0:
        pre_num = num
    else:
        cur_diff = num - pre_num
        pre_num = num
        # print("pre_diff = %d" % pre_diff, end=" ")
        # print("cur_diff = %d," % cur_diff, end=" ")
        if (pre_diff > 0 and cur_diff > 0) or (pre_diff < 0 and cur_diff < 0):
            # print("no", end=" ")
            pre_diff = cur_diff + pre_diff
        else:
            # print("yes", end=" ")
            res += 1
            pre_diff = cur_diff
print(res)

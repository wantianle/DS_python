# coding=utf-8

# 45、跳跃游戏II
# 题目：给定⼀个⾮负整数数组，你最初位于数组的第⼀个位置。数组中的每个元素代表你在该位置可以跳跃的最⼤长度。你的⽬标是使⽤最少的跳跃次数到达数组的最后⼀个位置。
# ⽰例:
# 输⼊: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后⼀个位置的最⼩跳跃数是 2。从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后⼀个位置。
# 说明:假设你总是可以到达数组的最后⼀个位置。

# 主要思路：求最小跳数，就求每跳一步能覆盖的范围就行了，只要最大范围能到队尾就是最小跳数，因为每跳一步判断需不需要更新可跳步数，只有大于剩余可跳步数才更新，flag+1，同时判断此刻的覆盖范围能否到队尾，不能则继续跳，能到就结束。那么不考虑队长为1则开局必跳一次，以题目为例，跳一步之后覆盖范围是2-1+3=4刚好是队长，能到队尾，且最小跳数。简而言之，就是贪心算法，求每一跳的最大覆盖范围，使得总覆盖能最先到整个队长。

import numpy as np

nums = np.random.randint(0, 6, size=10)
print(nums)
# nums = [2, 3, 1, 1, 4]
# 判断是否能到队尾
cur = 1
for i, num in enumerate(nums):
    cur -= 1
    if cur <= num and cur >= 0:
        cur = num
print(cur >= 0)
# 判断最小步数，感觉就像接力问题，或者搭桥搭船问题
if cur >= 0:
    step = 1
    flag = 0
    count = 0
    for i, num in enumerate(nums):
        step -= 1
        if step < num:
            step = num
            flag += 1
            count += num
            # print(count)
            if count >= len(nums) - 1:
                break
    print(flag)

# coding=utf-8

# 714、买卖股票的最佳时机含⼿续费
# 题⽬：给定⼀个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；⾮负整数 fee 代表了交易股票的⼿续费⽤。你可以⽆限次地完成交易，但是你每笔交易都需要付⼿续费。如果你已经购买了⼀个股票，在卖出它之前你就不能再继续购买股票了。返回获得利润的最⼤值。
# 注意：这⾥的⼀笔交易指买⼊持有并卖出股票的整个过程，每笔交易你只需要为⽀付⼀次⼿续费。
# ⽰例 1:
# 输⼊: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最⼤利润:
# 在此处买⼊ prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买⼊ prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 注意:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
# coding=utf-8

# 968、监控⼆叉树
# 题⽬：给定⼀个⼆叉树，我们在树的节点上安装摄像头。节点上的每个摄影头都可以监视其⽗对象、⾃⾝及其直接⼦对象。计算监控树的所有节点所需的最⼩摄像头数量。
# ⽰例 1：
# 输⼊：[0,0,null,0,0]
# 输出：1
# 解释：如图所⽰，⼀台摄像头⾜以监控所有节点。
# ⽰例 2：输⼊：[0,0,null,0,null,0,null,null,0]
# 输出：2
# 解释：需要⾄少两个摄像头来监视树的所有节点。 上图显⽰了摄像头放置的有效位置之⼀。
# 提⽰：
# 给定树的节点数的范围是 [1, 1000]。
# 每个节点的值都是 0。

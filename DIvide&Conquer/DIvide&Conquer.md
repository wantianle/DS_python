## 一、算法概述

   递归算法是一种直接或者间接调用自身函数或者方法的算法。说简单了就是程序自身的调用。

## 二、算法实质

递归算法就是将原问题不断分解为规模缩小的子问题，然后递归调用方法来表示问题的解。（用同一个方法去解决规模不同的问题）

## 三、算法思想

递归算法，顾名思义就是有两个大的阶段：递和归，即就是有去（递去）有回（归来）。
递去：将递归问题分解为若干个规模较小，与原问题形式相同的子问题，这些子问题可以用相同的解题思路来解决
归来：当你将问题不断缩小规模递去的时候，必须有一个明确的结束递去的临界点（递归出口），一旦达到这个临界点即就从该点原路返回到原点，最终问题得到解决。



![递归的图解分析](https://img-blog.csdnimg.cn/20200607172648138.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xsdHF5bA==,size_16,color_FFFFFF,t_70#pic_center)

## 四、递归算法的设计要素

递归思维是一种从下向上的思维方式，使用递归算法往往可以简化我们的代码，而且还帮我们解决了很复杂的问题。递归算法的难点就在于它的逻辑性，一般设计递归算法需要考虑以下几点:

1. 明确递归的终止条件
2. 提取重复的逻辑，缩小问题的规模不断递去
3. 给出递归终止时的处理办法

## 五、递归算法的经典实例

**问题定义即为递归定义**

- 阶乘
- 斐波纳契数列
- 杨辉三角的取值

**问题应用递归算法来解决**

- hanoi塔问题

**部分数据结构也是用递归来定义的**

- 树


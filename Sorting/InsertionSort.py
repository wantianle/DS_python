"""

简单插入排序
遍历索引作为分割线，划分已排序与未排序的序列，每遇到一个新的数据就对比已排序序列，并且做交换插入到合适位置
空间：平均 n^2 最坏 n^2 最好 n
时间：1

"""

import numpy as np
import time


def InsertionSort(list):
    length = len(list)
    if length <= 1:
        return list
    else:
        print(list)
        for i in range(1, length):
            print(f"-----No.{i}-----")
            j = i
            while j > 0:
                if list[j] < list[j - 1]:
                    list[j], list[j - 1] = list[j - 1], list[j]
                    j -= 1
                    print(list)
                else:
                    break
        return list


if __name__ == '__main__':
    print('<<<<<<<<<<')
    list = np.random.randint(0, 100, size=9)
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t1 = time.time()
    InsertionSort(list)
    t2 = time.time()
    print("%.2fms" % ((t2 - t1)*1000))
    print('>>>>>>>>>>')

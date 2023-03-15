"""

冒泡排序
空间：1
时间：平均 n^2 最好 n^2 最坏 n^2
优化：平均 n^2 最好 n 最坏 n^2
当最好的情况，数据本身有序，就不用再排序了，加个flag，1表示有序，0表示无序
"""

import numpy as np
import time


def BubbleSort(list):
    length = len(list)
    if length <= 1:
        return list
    else:
        print(list)
        for i in range(length):
            flag = 1
            print(f"-----No.{i + 1}-----")
            for j in range(length - i - 1):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    flag = 0
                print(list)
            if flag:
                return list
        return list


if __name__ == '__main__':
    print('<<<<<<<<<<')
    list = np.random.randint(0, 100, size=9)
    # list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t1 = time.time()
    BubbleSort(list)
    t2 = time.time()
    print("%.2fms" % ((t2 - t1)*1000))
    print('>>>>>>>>>>')

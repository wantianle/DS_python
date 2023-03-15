"""

简单选择排序
本质上虽然选择排序是冒泡的一个优化，但是从时间复杂度上而言，二者差距并不大
空间：1
时间：n^2
优化：

"""

import numpy as np
import time


def SelectionSort(list):
    length = len(list)
    if length <= 1:
        return list
    else:
        print(list)
        for i in range(length):
            print(f"-----No.{i + 1}-----")
            for j in range(i+1, length):
                if list[j] < list[i]:
                    list[i], list[j] = list[j], list[i]
                print(list)
        return list


if __name__ == '__main__':
    print('<<<<<<<<<<')
    list = np.random.randint(0, 100, size=9)
    # list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    t1 = time.time()
    SelectionSort(list)
    t2 = time.time()
    print("%.2fms" % ((t2 - t1)*1000))
    print('>>>>>>>>>>')

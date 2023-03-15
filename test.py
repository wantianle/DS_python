# def list_null():
#     if True:
#         return True
#     return False

# if []:
#     print(list_null())
# else:
#     print("None")

# list = [1, 2, 3, 4]
# for i in range(2, 10):
#     print(i)

# for i in range(2, 2):
#     print(i)

# 变量之间的赋值语句都是更改指针指向地址
# 切片索引赋值语句是更改该列表的值
# 切片是一种浅拷贝如果改变列表里的列表数据
# 浅拷贝的切片还是会被更改数据
# 因为浅拷贝只拷贝了二维列表的地址指针，没有创建新的二位列表
# s = "Hello World"
# temp = s
# s = s[:6] + "wantianle"
# print(s, temp)

# list1 = [1, 2, 3, 4, [1, 2]]
# temp = list1[:]
# # temp[0] = 2
# list1[4][0] = 4
# print(temp)

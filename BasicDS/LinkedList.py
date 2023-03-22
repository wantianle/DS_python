"""

单链表定义:
带不带头结点之分
基本操作：
建立销毁、增删改查

"""


# 链表结点
class ListNode:
    def __init__(self, val):  # 结点只能初始化值，还需手动设置next指针
        self.val = val
        self.next = None


# 带头结点的链表实现，与不带头结点的相比，就是在遍历时处理空链表与非空链表的首结点操作保持一致。
class LinkedList_HEAD:
    # 1.初始化：带头结点和头指针的链表创建，头指针指向头结点，头结点不存储数据
    def __init__(self):
        self.head = ListNode(None)
        self.head.next = None  # 其实结点那已经初始化，这里可以不写

    # 2.遍历输出：展示出链式结构，返回格式化字符串，这个类里面没有专门写遍历的方法，是因为遍历不能写死，每一个使用遍历的方法在遍历中都有不同的操作
    def __repr__(self) -> str:
        output = "*head=HNode"  # 头指针指向头结点
        temp = self.head.next  # 遍历指针，因为头结点无数据不输出，所有要让temp初始指向第一个结点，即头结点后的首结点
        while temp:  # 遍历指针从首结点循环到尾结点，直到None停止
            output += f"->{temp.val}"
            temp = temp.next
        output += "->None"
        return output  # __repr__方法重写显示类属性或其他信息

    # 3.头插法：在链表头部插入元素
    def head_insert(self, val):
        node = ListNode(val)
        node.next = self.head.next  # 头插法只要让新结点node.next指向头结点所指处，即首结点或None
        self.head.next = node  # 接着将头结点指向新结点，即新结点成为首结点

    # 4.尾插法：在链表尾部插入元素
    def tail_insert(self, val):
        node = ListNode(val)
        temp = self.head  # 尾插法需要找到尾结点，将新结点接到尾结点之后，所以需要遍历指针从头结点开始遍历，temp.next初始指向None或首结点
        while temp.next:  # 当temp.next指向None时，temp遍历指针即指向尾结点，令temp.next = node，完成尾插
            temp = temp.next
        temp.next = node
        # node.next = None

    # 5.查询长度：返回链表长度count
    def query_length(self):
        temp = self.head.next
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # 6.查询位置：返回指向给定位置结点的指针temp和元素值，失败返回None
    def query_site(self, site):
        temp = self.head.next
        index = 1
        length = self.query_length()
        if 0 < site <= length:
            while index < site:  # 注意从首结点到该结点，需要的循环次数应该是site - index(e.g. 3 - 1 = 2 从位置1到位置3，循环两次，所以<不取=号)
                temp = temp.next
                index += 1
            return temp, temp.val
        else:
            return None, None  # 为了方便接口判空使用，返回None元组

    # 7.查询元素：返回给定元素结点的位置列表temp_list
    def query_elem(self, val):
        temp = self.head.next
        temp_list = []
        index = 1
        while temp:
            if temp.val == val:
                temp_list.append(index)
            index += 1
            temp = temp.next
        return temp_list  # 不考虑val的不合理值，这个放到调用程序解决，如果是单独调用则只能通过返回空列表判定

    # 8.位置插入：在给定位置处插入元素，返回bool，这里又分为找前位元素还是该位元素来移位，单链表只能向后遍历，因为要移位只能找前位元素
    def insert(self, site, val):
        length = self.query_length()
        if 0 < site < length:
            temp = self.query_site(site - 1)[0]  # 找前位元素
            node = ListNode(val)
            node.next = temp.next
            temp.next = node
        elif site == length:
            self.tail_insert(val)
        elif site == 1:
            self.head_insert(val)
        else:
            print("Insert failed.")
            return False
        return True

    # 9.位置删除：删除给定位置处元素，返回bool，同插入，这里移位需考虑查询元素的选取
    def delete_site(self, site):
        length = self.query_length()
        if length == 0:  # 长度为0不能删除，但是可以插入
            return False
        if 0 < site < length:
            temp = self.query_site(site - 1)[0]
            temp.next = temp.next.next
        elif site == length:
            temp = self.query_site(site - 1)[0]
            temp.next = None
        elif site == 1:
            self.head = self.head.next
        else:
            print("Delete failed.")
            return False
        return True

    # 10.元素删除：删除链表中所有给定元素，返回bool
    def delete_elem(self, val):
        temp_list = self.query_elem(val)
        if not temp_list:
            print("Delete failed.")
            return False
        for item in temp_list:
            self.delete_site(item)
        return True

    # 11.元素更改：更改指定位置元素的值，返回bool
    def update_elem(self, site, val):
        length = self.query_length()
        if 0 < site <= length:
            temp = self.query_site(site)[0]
            temp.val = val
            return True
        else:
            print("Update failed.")
            return False

    # 12.链表删除：删除链表所有元素，返回bool
    def delete(self):
        self.head.next = None
        return True


# 不带头结点的链表实现
class LinkedList:
    # 1.初始化：不带头结点，只有头指针的链表创建，头指针head直接指向首结点，即head = node
    def __init__(self):
        self.head = None

    # 2.遍历输出：展示出链式结构，返回格式化字符串，这个类里面没有专门写遍历的方法，是因为遍历不能写死，每一个使用遍历的方法在遍历中都有不同的操作
    def __repr__(self) -> str:
        output = "*head="  # 头指针
        temp = self.head  # 遍历指针
        while temp:  # 遍历指针从首结点循环到尾结点，直到None停止
            output += f"{temp.val}->"  # 输出链式连接和结点数据，数据格式化映射
            temp = temp.next
        output += "None"
        return output  # __repr__方法重写显示类属性或其他信息

    # 3.头插法：在链表头部插入元素
    def head_insert(self, val):
        node = ListNode(val)
        node.next = self.head  # 头插法只要让新结点node.next指向头指针所指处，即首结点或None
        self.head = node  # 接着将头指针指向新结点，即新结点成为首节点

    # 4.尾插法：在链表尾部插入元素
    def tail_insert(self, val):
        node = ListNode(val)
        temp = self.head  # 尾插法需要找到尾结点，将新结点接到尾结点之后，所以需要个遍历指针
        if not temp:
            self.head = node  # 没有头结点，因此头指针指向None，没有temp.next，需要判空单独使头指针指向node，令head = node
        else:
            while temp.next:  # 当temp.next指向None时，temp遍历指针即指向尾结点，令temp.next = node，完成尾插
                temp = temp.next
            temp.next = node
            # node.next = None

    # 5.查询长度：返回链表长度count
    def query_length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # 6.查询位置：返回指向给定位置结点的指针temp和元素值，失败返回None
    def query_site(self, site):
        temp = self.head
        index = 1
        length = self.query_length()
        if 0 < site <= length:
            while index < site:  # 注意从首结点到该结点，需要的循环次数应该是site - index(e.g. 3 - 1 = 2 从位置1到位置3，循环两次，所以<不取=号)
                temp = temp.next
                index += 1
            return temp, temp.val
        else:
            return None, None  # 为了方便接口使用，设置双None返回值

    # 7.查询元素：返回给定元素结点的位置列表temp_list
    def query_elem(self, val):
        temp = self.head
        temp_list = []
        index = 1
        while temp:
            if temp.val == val:
                temp_list.append(index)
            index += 1
            temp = temp.next
        return temp_list  # 不考虑val的不合理值，这个放到调用程序解决，如果是单独调用则只能通过返回空列表判定

    # 8.位置插入：在给定位置处插入元素，返回bool，这里又分为找前位元素还是该位元素来移位，单链表只能向后遍历，因为要移位只能找前位元素
    def insert(self, site, val):
        length = self.query_length()
        if 0 < site < length:
            temp = self.query_site(site - 1)[0]  # 找前位元素
            node = ListNode(val)
            node.next = temp.next
            temp.next = node
        elif site == length:
            self.tail_insert(val)
        elif site == 1:
            self.head_insert(val)
        else:
            print("Insert failed.")
            return False
        return True

    # 9.位置删除：删除给定位置处元素，返回bool，同插入，这里移位需考虑查询元素的选取
    def delete_site(self, site):
        length = self.query_length()
        if length == 0:  # 长度为0不能删除，但是可以插入
            return False
        if 0 < site < length:
            temp = self.query_site(site - 1)[0]
            temp.next = temp.next.next
        elif site == length:
            temp = self.query_site(site - 1)[0]
            temp.next = None
        elif site == 1:
            self.head = self.head.next
        else:
            print("Delete failed.")
            return False
        return True

    # 10.元素删除：删除链表中所有给定元素，返回bool
    def delete_elem(self, val):
        temp_list = self.query_elem(val)
        if not temp_list:
            print("Delete failed.")
            return False
        for item in temp_list:
            self.delete_site(item)
        return True

    # 11.元素更改：更改指定位置元素的值，返回bool
    def update_elem(self, site, val):
        length = self.query_length()
        if 0 < site <= length:
            temp = self.query_site(site)[0]
            temp.val = val
            return True
        else:
            print("Update failed.")
            return False

    # 12.链表删除：删除链表所有元素，返回bool
    def delete(self):
        self.head = None
        return True


"""

经典算法与应用
# 12.链表翻转：将链表顺序逆转
# def reverse(self):
# 13.逆序输出：不改变链表顺序的同时逆序输出
# def reverse_print(self):

"""


if __name__ == '__main__':
    # list = LinkedList_HEAD()
    list = LinkedList()
    # list.head_insert(1)
    # list.head_insert("2+6")
    # list.head_insert([1, 2, 3, 3, 4])
    # list.head_insert(4)
    # list.head_insert(5)
    list.tail_insert(1)
    list.tail_insert(2)
    list.tail_insert(2)
    list.tail_insert(4)
    list.tail_insert(5)
    # list.delete()
    # length = list.query_length()
    # elem = list.query_site(4)
    # site = list.query_elem(2)
    # list.insert(2, 9)
    # list.delete_site(2)
    # list.delete_elem(5)
    # list.update_elem(3, 3)
    print(list)
    # print(length)
    # print(elem[0].val, elem[1])
    # print(site)

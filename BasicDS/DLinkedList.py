"""

双向链表：
以及结合的，双向循环链表
基本操作：
建立销毁、增删改查

"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


# 带头结点
class DLinkedList_HEAD:

    def __init__(self):
        self.head = ListNode(None)

    def __repr__(self) -> str:
        output = "None<-*head=HNode"
        temp = self.head.next
        while temp:
            output += f"<=>{temp.val}"
            temp = temp.next
        output += "->None"
        return output

    def head_insert(self, val):
        node = ListNode(val)
        node.next = self.head.next
        if self.head.next:
            self.head.next.pre = node
        self.head.next = node
        node.pre = self.head

    def tail_insert(self, val):
        node = ListNode(val)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.pre = temp
        # node.next = None

    def query_length(self):
        temp = self.head.next
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def query_site(self, site):
        temp = self.head.next
        index = 1
        length = self.query_length()
        if 0 < site <= length:
            while index < site:
                temp = temp.next
                index += 1
            return temp, temp.val
        else:
            return None, None

    def query_elem(self, val):
        temp = self.head.next
        temp_list = []
        index = 1
        while temp:
            if temp.val == val:
                temp_list.append(index)
            index += 1
            temp = temp.next
        return temp_list

    def insert(self, site, val):
        length = self.query_length()
        if 0 < site < length:
            # 前插转后插操作
            temp = self.query_site(site)[0]
            node = ListNode(val)
            temp.pre.next = node
            node.pre = temp.pre
            node.next = temp
            temp.pre = node
        elif site == length:
            self.tail_insert(val)
        elif site == 1:
            self.head_insert(val)
        else:
            print("Insert failed.")
            return False
        return True

    def delete_site(self, site):
        length = self.query_length()
        if length == 0:  # 长度为0不能删除，但是可以插入
            print("Delete failed.")
            return False
        if 0 < site < length:
            temp = self.query_site(site)[0]
            temp.pre.next = temp.next
            temp.next.pre = temp.pre
            temp.pre = None
            temp.next = None
        elif site == length:
            temp = self.query_site(site)[0]
            temp.pre.next = None
            temp.pre = None
        elif site == 1:
            self.head = self.head.next
            self.head.pre = None
        else:
            print("Delete failed.")
            return False
        return True

    def delete_elem(self, val):
        temp_list = self.query_elem(val)
        if not temp_list:
            print("Delete failed.")
            return False
        for item in temp_list:
            self.delete_site(item)
        return True

    def update_elem(self, site, val):
        length = self.query_length()
        if 0 < site <= length:
            temp = self.query_site(site)[0]
            temp.val = val
            return True
        else:
            print("Update failed.")
            return False

    def delete(self):
        self.head.next = None
        return True


# 不带头结点
class DLinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        output = "None<-*head="
        temp = self.head
        while temp:
            if not temp.next:
                output += f"{temp.val}"
            else:
                output += f"{temp.val}<=>"
            temp = temp.next
        output += "->None"
        return output

    def head_insert(self, val):
        node = ListNode(val)
        node.next = self.head
        if self.head:
            self.head.pre = node
        self.head = node
        node.pre = None

    def tail_insert(self, val):
        node = ListNode(val)
        temp = self.head
        if not temp:
            self.head = node
        else:
            while temp.next:
                temp = temp.next
            temp.next = node
            node.pre = temp
        # node.next = None

    def query_length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def query_site(self, site):
        temp = self.head
        index = 1
        length = self.query_length()
        if 0 < site <= length:
            while index < site:
                temp = temp.next
                index += 1
            return temp, temp.val
        else:
            return None, None

    def query_elem(self, val):
        temp = self.head
        temp_list = []
        index = 1
        while temp:
            if temp.val == val:
                temp_list.append(index)
            index += 1
            temp = temp.next
        return temp_list

    def insert(self, site, val):
        length = self.query_length()
        if 0 < site < length:
            # 前插转后插操作
            temp = self.query_site(site)[0]
            node = ListNode(val)
            temp.pre.next = node
            node.pre = temp.pre
            node.next = temp
            temp.pre = node
        elif site == length:
            self.tail_insert(val)
        elif site == 1:
            self.head_insert(val)
        else:
            print("Insert failed.")
            return False
        return True

    def delete_site(self, site):
        length = self.query_length()
        if length == 0:  # 长度为0不能删除，但是可以插入
            print("Delete failed.")
            return False
        if 0 < site < length:
            temp = self.query_site(site)[0]
            temp.pre.next = temp.next
            temp.next.pre = temp.pre
            temp.pre = None
            temp.next = None
        elif site == length:
            temp = self.query_site(site)[0]
            temp.pre.next = None
            temp.pre = None
        elif site == 1:
            self.head = self.head.next
            self.head.pre = None
        else:
            print("Delete failed.")
            return False
        return True

    def delete_elem(self, val):
        temp_list = self.query_elem(val)
        if not temp_list:
            print("Delete failed.")
            return False
        for item in temp_list:
            self.delete_site(item)
        return True

    def update_elem(self, site, val):
        length = self.query_length()
        if 0 < site <= length:
            temp = self.query_site(site)[0]
            temp.val = val
            return True
        else:
            print("Update failed.")
            return False

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
    # list = DLinkedList_HEAD()
    list = DLinkedList()
    list.head_insert(1)
    list.head_insert("2+6")
    list.head_insert([1, 2, 3, 3, 4])
    list.head_insert(4)
    list.head_insert(5)
    # list.tail_insert(1)
    # list.tail_insert(2)
    # list.tail_insert(3)
    # list.tail_insert(4)
    # list.tail_insert(5)
    # list.delete()
    # length = list.query_length()
    # elem = list.query_site(4)
    # site = list.query_elem(2)
    # list.insert(10, 9)
    # list.delete_site(2)
    # list.delete_elem(5)
    # list.update_elem(3, 9)
    print(list)
    # print(length)
    # print(elem[0], elem[1])
    # print(site)

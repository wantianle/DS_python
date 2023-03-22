"""

带头结点的双向循环链表：
基本操作：
建立销毁、增删改查

"""


class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.pre = None


class DCLinkedList:
    def __init__(self) -> None:
        self.head = ListNode(None)

# 先定义一个 Node 类
class Node:
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, new_value):
        self._value = new_value

    def setNext(self, new_next):
        self._next = new_next


# 实现 Linked List 及其各类操作方法
class LinkedList(object):
    def __init__(self):
        self._head = Node()
        self._tail = None
        self._length = 0

    # 检测是否为空
    def isEmpty(self):
        return self._head.getNext() is None

    # add 在链表前端添加元素：o(1)
    def add(self, value):
        newnode = Node(value, None)
        newnode.setNext(self._head)
        self._head = newnode

    # append 在链表尾部添加元素 o(n)
    def append(self, value):
        newnode = Node(value, None)
        if self.isEmpty():
            self._head = newnode  # 若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() is not None:
                current = current.getNext()  # 遍历列表
            current.setNext(newnode)

    # search 检索元素是否在链表中
    def search(self, value):
        current = self._head
        foundvalue = False
        while current is not None and not foundvalue:
            if current.getValue() == value:
                foundvalue = True
            else:
                current = current.getNext()
        return foundvalue

    # index 索引元素在链表中的位置
    def index(self, value):
        current = self._head
        count = 0
        found = False
        while current is not None and not found:
            count += 1
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            return ValueError("%s is not in linkedlist" % value)

    # 删除链表中的某项元素
    def remove(self, value):
        current = self._head
        pre = None
        while current is not None:
            if current.getValue() == value:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    # insert 链表中插入元素
    def insert(self, pos, value):
        if pos <= 1:
            self.add(value)
        elif pos > self.size():
            self.append(value)
        else:
            temp = Node(value)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)
            




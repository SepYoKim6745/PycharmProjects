import copy
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None

    def size(self):
        node = self.head
        count = 0
        while node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedStack: "):
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end='->')
            node = node.link
        print('None')

    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None: node.data = elem

    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.link
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos - 1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos):
        before = self.getNode(pos - 1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link


class Polynomial():
    def __init__(self):
        self.node = LinkedList()
        self.high = int(input('다항식의 최고 차수를 입력하시오: '))
        for i in range(self.high, -1, -1):
            self.node.insert(0, int(input('x^{}의 계수 : '.format(i))))

    def add(self, newNode):
        if self.high > newNode.high:
            node = copy.deepcopy(self.node)
            while newNode is not None:
                node.data += newNode.data
                node = node.link
                newNode = newNode.link
        else:
            node = copy.deepcopy(newNode)
            while newNode is not None:
                node.data += newNode.data
                node = node.link
                newNode = newNode.link

        return node

a = Polynomial()
b = Polynomial()
c = a.add(b)
# s = LinkedList()
# s.display('단순연결리스트로 구현한 리스트(초기상태): ')
# s.insert(0, 10); s.insert(0, 20); s.insert(1,30); s.insert(s.size(), 40); s.insert(2, 50)
# s.display('단순연결리스트로 구현한 리스트(삽입x5): ')
# s.replace(2, 90)
# s.display(('단순연결리스트로 구현한 리스트 (교체x1): '))
# s.delete(2); s.delete(s.size()-1); s.delete(0)
# s.display('단순연결리스트로 구현한 리스트(삭제x3): ')
# s.clear()
# s.display('단순연결리스트로 구현한 리스트 (정리후): ')
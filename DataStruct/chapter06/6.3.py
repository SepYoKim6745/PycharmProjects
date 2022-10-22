#실패
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        return str(self.head)

    def clear(self):
        self.head = None

    def size(self):
        node = self.head
        count = 0
        while node != None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedStack: "):
        x = self.size()-1
        print(msg, end='')
        node = self.head
        while not node == None:
            print('{}x^{}'.format(float(node.data), x), end='')
            if node.link != None:
                print(' + ', end='')
            x -= 1
            node = node.link
        print()

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


class Polynomial:
    def __init__(self):
        self.node = LinkedList()
        self.high = int(input('다항식의 최고 차수를 입력하시오: '))
        for i in range(self.high, -1, -1):
            self.node.insert(0, int(input('x^{}의 계수 : '.format(i))))

    def add(self, newNode):
        addNode = LinkedList()
        temp1 = self.node.head
        temp2 = newNode.node.head

        while (temp1 != None) or (temp2 != None):
            if self.high > newNode.high:
                if temp2 == None:
                    addNode.insert(0, temp1.data)
                    temp1 = temp1.link
                    print(addNode.size())
                else:
                    addNode.insert(0, temp1.data + temp2.data)
                    temp1 = temp1.link
                    temp2 = temp2.link
            elif self.high < newNode.high:
                if temp1 == None:
                    addNode.insert(0, temp2.data)
                    temp2 = temp2.link
                else:
                    addNode.insert(0, temp1.data + temp2.data)
                    temp1 = temp1.link
                    temp2 = temp2.link
            else:
                addNode.insert(0, temp1.data + temp2.data)
                temp1 = temp1.link
                temp2 = temp2.link
        return addNode

    def sub(self, newNode):
        subNode = LinkedList()
        temp1 = self.node.head
        temp2 = newNode.node.head
        while (temp1 != None) or (temp2 != None):
            if self.high > newNode.high:
                if temp2 == None:
                    subNode.insert(0, temp1.data)
                    temp1 = temp1.link
                else:
                    subNode.insert(0, temp1.data - temp2.data)
                    temp1 = temp1.link
                    temp2 = temp2.link
            elif self.high < newNode.high:
                if temp1 == None:
                    subNode.insert(0, temp2.data)
                    temp2 = temp2.link
                else:
                    subNode.insert(0, temp1.data - temp2.data)
                    temp1 = temp1.link
                    temp2 = temp2.link
            else:
                subNode.insert(0, temp1.data - temp2.data)
                temp1 = temp1.link
                temp2 = temp2.link
        return subNode

    def multiply(self, newNode):
        multiplyNode = LinkedList()
        temp1 = self.node.head
        temp2 = newNode.node.head

    def display(self, msg='LinkedList'):
        x = 0
        print(msg, end='')
        node = self.node.head
        while not node == None:
            print('{}x^{}'.format(float(node.data), x), end='')
            if node.link != None:
                print(' + ', end='')
            x += 1
            node = node.link
        print()

    def size(self):
        node = self.node.head
        count = 0
        while node != None:
            print('-')
            node = node.link
            count += 1
        return count


a = Polynomial()
b = Polynomial()
c = a.add(b)
a.display('a: ')  # display 할 차례
b.display('b: ')
c.display('add: ')


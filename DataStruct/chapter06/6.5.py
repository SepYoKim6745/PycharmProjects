class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next


class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def clear(self):
        self.front = self.front = None

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.front.next
            while not node == self.front:
                node = node.next
                count += 1
            return count

    def display(self, msg="DoublyLinkedDeque: "):
        print(msg, end='')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.next
        print()

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if (self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if (self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data


def isValidPos(x, y):
    if x < 0 or y < 0 or x >= X_MAX_SIZE or y >= Y_MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


def DFS():
    stack = DoublyLinkedDeque()
    stack.addRear((0, 1))
    print('DFS: ')

    while not stack.isEmpty():
        here = stack.deleteRear()
        print(here, end='->')
        (x, y) = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): stack.addRear((x, y - 1))
            if isValidPos(x, y + 1): stack.addRear((x, y + 1))
            if isValidPos(x - 1, y): stack.addRear((x - 1, y))
            if isValidPos(x + 1, y): stack.addRear((x + 1, y))
    return False


map = [['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '0', '0', '0', '1', '1'],
       ['1', '1', '1', '0', '1', '1', '1', '0', '1', '1'],
       ['1', '1', '0', '0', '0', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '0', '0', '0', 'x', '1'],
       ['1', '1', '1', '1', '1', '1', '1', '0', '1', '1'],
       ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

Y_MAZE_SIZE = 11
X_MAX_SIZE = 10

if DFS():
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')

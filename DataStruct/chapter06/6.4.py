class Node:
    def __init__(self, elem, link):
        self.data = elem
        self.link = link


class CircularLinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail == None

    def clear(self):
        self.tail = None

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node = node.next
            count += 1
        return count

    def display(self, msg='CircularLinkedQueue: '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end=' ')
        print()

def isValidPos(x, y):
    if x < 0 or y < 0 or x >= X_MAX_SIZE or y >= Y_MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


def BFS():
    que = CircularLinkedQueue()
    que.enqueue((0, 1))
    print('BFS: ')
    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x, y = here
        if (map[y][x] == 'x'):
            print(' 도착')
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): que.enqueue((x, y - 1))
            if isValidPos(x, y + 1): que.enqueue((x, y + 1))
            if isValidPos(x - 1, y): que.enqueue((x - 1, y))
            if isValidPos(x + 1, y): que.enqueue((x + 1, y))
    print(' 실패')
    return False

map = [['1','1','1','1','1','1','1','1','1','1'],
       ['e','0','0','0','0','0','0','0','1','1'],
       ['1','1','1','0','1','1','1','0','1','1'],
       ['1','1','0','0','0','1','1','0','1','1'],
       ['1','1','1','0','1','1','1','0','1','1'],
       ['1','1','1','0','0','0','1','0','1','1'],
       ['1','1','1','1','1','1','1','0','1','1'],
       ['1','1','1','1','1','0','1','0','1','1'],
       ['1','1','1','1','1','0','0','0','x','1'],
       ['1','1','1','1','1','1','1','0','1','1'],
       ['1','1','1','1','1','1','1','1','1','1']]

Y_MAZE_SIZE = 11
X_MAX_SIZE = 10
result = BFS()
if result:
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')
# q = CircularLinkedQueue()
# for i in range(10):
#     q.enqueue(i)
# q.display()
# for _ in range(7):
#     q.dequeue()
# q.display()
# for i in range(7):
#     q.enqueue(i)
# q.display()

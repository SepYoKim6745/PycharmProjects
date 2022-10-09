from CircularQueue import CircularQueue


class CircularDeque(CircularQueue):
    def __init__(self, capacity):
        super().__init__(capacity)

    def addRear(self, n):
        self.enqueue(n)

    def deleteFront(self):
        self.dequeue()

    def getFront(self):
        self.peek()

    def addFront(self, n):
        if not self.isFull():
            self.items[self.front] = n
            self.front = self.front - 1
            if self.front < 0: self.front = self.capacity - 1

    def deleteRear(self):
        if not self.isEmpty():
            i = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0: self.rear = self.capacity - 1
            return i

    def getRear(self):
        return self.items[self.rear]


def isValidPos(x, y):
    if x < 0 or y < 0 or x >= X_MAX_SIZE or y >= Y_MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'


def DFS():
    stack = CircularDeque(20)
    stack.enqueue((0, 1))
    print('DFS: ')

    while not stack.isEmpty():
        here = stack.dequeue()
        print(here, end='->')
        (x, y) = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): stack.enqueue((x, y - 1))
            if isValidPos(x, y + 1): stack.enqueue((x, y + 1))
            if isValidPos(x - 1, y): stack.enqueue((x - 1, y))
            if isValidPos(x + 1, y): stack.enqueue((x + 1, y))
        print('현재 스택: ', stack)
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

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


n = int(input())
dq = CircularDeque(n)
for i in range(9):
    if i % 2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.display()
for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display()
for i in range(9, 14): dq.addFront(i)
dq.display()

class CircularQueue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = 0
        self.items = [None] * capacity
        self.capacity = capacity

    def __str__(self):
        if self.front < self.rear:
            return str(self.items[self.front + 1:self.rear + 1])
        else:
            # self.items = self.items[self.front+1:self.capacity] + self.items[0:self.rear+1]
            return str(self.items[self.front + 1:self.capacity] + self.items[0:self.rear + 1])

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity

    def clear(self):
        self.front = self.rear

    def enqueue(self, n):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.items[self.rear] = n

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front + 1) % self.capacity]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front + 1: self.rear + 1]
        else:
            out = self.items[self.front + 1:self.capacity] + self.items[0:self.rear + 1]
        print('f=%s,r=%d' % (self.front, self.rear), out)


if __name__ == '__main__':
    n = int(input())
    q = CircularQueue(n)
    for i in range(8): q.enqueue(i)
    # q.display()
    print('q 객체 출력 =', q)
    for i in range(5): q.dequeue()
    # q.display()
    print('q 객체 출력 =', q)
    for i in range(8, 14): q.enqueue(i)
    # q.display()
    print('q 객체 출력 =', q)


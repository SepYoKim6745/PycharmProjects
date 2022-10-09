class LineQueue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return len(self.item) == 0

    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.item.pop(0)


queue = LineQueue()
print(queue.item)
for i in range(1, 6):
    queue.enqueue(i)
print(queue.item)
print(queue.dequeue())
print(queue.item)
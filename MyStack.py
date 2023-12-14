class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class MyQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


# Usage
stackObj1 = MyStack()
stackObj2 = MyStack()
queueObj = MyQueue()

for i in range(0, 5):
    queueObj.enqueue(i*2)
    queueObj.enqueue(i*2 + 1)
    stackObj1.push(queueObj.dequeue())
    stackObj2.push(queueObj.dequeue())

for i in range(0, 5):
    print(stackObj1.pop())

for i in range(0, 5):
    print(stackObj2.pop())

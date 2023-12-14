class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        out = ""
        for i in self.items:
            out = out + str(i) + ", "
        out = out[:-2]

        return "Queue([" + " " + out + "])"

def printerQueue(items):
    q = Queue()
    for i in items:
        q.enqueue(i)
    a = ["A", "B", "C", "D"]
    for i in a:
        q.enqueue(i)
    print(q)
    print(q.dequeue())

# Example usage
printerQueue([1, 2, 3])

class Stack:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __str__(self):
        out = ""
        for i in self._items:
            out = out + str(i) + ", "
        out = out[:-2]

        return "Stack([" + " " + out + "])"

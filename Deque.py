class Deque:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def addFront(self, item):
        self._items.append(item)

    def addRear(self, item):
        self._items.insert(0, item)

    def removeFront(self):
        return self._items.pop()

    def removeRear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def __str__(self):
        return "Deque(" + str(self._items) + ")"

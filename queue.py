# from stack import Stack


class Queue:

    def __init__(self, capacity=-1):
        self.capacity = capacity
        self.items = []

    def insert(self, x, is_list=False):
        if not self.is_full():
            if not is_list:
                self.items.insert(0, x)
            else:
                for i in x:
                    if not self.is_full():
                        self.items.insert(0, i)
                    else:
                        break
            return True
        return False

    def remove(self, how_many=1):
        if not self.is_empty() and how_many:
            return self.items.pop() if how_many == 1 else [self.items.pop() for _ in range(how_many) if not self.is_empty()]
        return None

    def remove_all(self):
        return self.remove(self.size())

    def clear(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_full(self):
        return self.size() == self.capacity

    def is_empty(self):
        return not self.items

    def __str__(self, items=[], join_str=" "):
        if len(items) == 0:
            return join_str.join(str(x) for x in self.items)
        return join_str.join(str(x) for x in items)


# class Queue:
#     items = Stack()
#     items_1 = Stack()
#     items.items = []
#     items_1.items = []
#
#     def insert(self, x):
#         self.items_1.push(x)
#
#     def remove(self):
#         self.items.clear()
#         length = len(self.items_1.items)
#         for i in range(length):
#             self.items.push(self.items_1.items[length - i - 1])
#         ret = self.items.pop()
#         self.items_1.clear()
#         for i in range(length - 1):
#             self.items_1.push(self.items.items[length - i - 2])
#         return ret
#
#     def is_empty(self):
#         return not self.items_1.items
#
#     def __str__(self, items=[], join_str=" "):
#         self.items.clear()
#         length = len(self.items_1.items)
#         for i in range(length):
#             self.items.push(self.items_1.items[length - i - 1])
#         if len(items) == 0:
#             return join_str.join(str(x) for x in self.items.items)
#         return join_str.join(str(x) for x in items)

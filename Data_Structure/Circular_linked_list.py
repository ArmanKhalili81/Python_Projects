class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class circute:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        self.size += 1
        if self.head is None:
            self.head = node
            self.head.next = node
        else:
            node.next = self.head.next
            self.head.next = node
            self.head = node

    def delete(self, data):
        current = self.head.next
        tmp = self.head.next
        for j in range(self.size):
            if current.data == data:
                if current == self.head.next:
                    self.head.next = current.next
                    self.size -= 1
                    return current
                else:
                    tmp.next = current.next
                    self.size -= 1
                    return current
            tmp = current
            current = current.next

    def printAll(self):
        current = self.head.next
        for i in range(self.size):
            print(current.data)
            current = current.next


c = circute()
c.append(15)
c.append(14)
c.append(19)
c.append(20)
res = c.delete(15)
print(f"Data Deleted In This Address ♦ {res} ♦ .")
c.printAll()

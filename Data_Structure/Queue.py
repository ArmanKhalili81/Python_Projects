import re


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1


    def dequeue(self):
        if self.head:
            if self.head.next:
                current = self.head
                data = self.head.data
                self.head = self.head.next
                current.next = None
                self.size -= 1
                return data
            else:
                data = self.head.data
                self.head = None
                self.tail = None
                self.size -= 1
                return data
        else:
            return "♦ Not Exist Any Node For Delete ! ♦"

    def search(self,data):
        current = self.head
        while current :
            if self.head:
                if self.head.next:
                    r = re.search(f"{data}$",current.data)
                    if r:
                        return current.data
                    else :
                        current = current.next
                else :
                    current.data
            else :
                return "♦ Not Exist Any Node For Delete ! ♦"

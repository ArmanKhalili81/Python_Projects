class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class SinglyLinkedlist:
    def __init__(self):
        self.tail = None
    def append(self,data=None):   
        node = Node(data) # در اینجا متغیر نود ، آدرس باکس ساخته شده در کلاس نود را دارد 
        if self.tail == None:
            self.tail = node
        else :
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
    def max(self):
        current = self.tail
        max = self.tail.data
        while current:
            if max < current.data:
                max = current.data
            current = current.next
        return max
    def size(self):
        current = self.tail
        size = 0
        while current:
            size += 1
            current = current.next
        return size
    def delete(self,data):
        current = self.tail
        tmp = self.tail
        while current:
            if current.data == data:
                if current == self.tail :
                    self.tail = current.next
                    current.next = None
                    return
                else :
                    tmp.next = current.next
                    current.next = None
            tmp = current
            current = current.next
    def printAll(self):
        current = self.tail
        while current:
            print(current.data)
            current = current.next
n = SinglyLinkedlist()
n.append(20)
n.append(15)
n.append(35)
n.append(8)
n.append(71)
n.append(19)
n.printAll()
res = n.max()
s = n.size()
n.delete(8)
print("-------------------------------")
n.printAll()
print("-------------------------------")
print(f"MAX : {res}" + "\n" + f"SIZE : {s}")
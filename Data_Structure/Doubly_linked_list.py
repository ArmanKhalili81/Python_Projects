class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,data):
        node = Node(data,None,None)
        if self.head == None :
            self.head = node
            self.tail = node
        else :
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    def delete(self,data):
        current = self.head
        tmp = self.head
        while current:
            if current.data == data:
                tmp = current
                if current == self.head:
                    self.head = current.next
                    current.next = None
                    return tmp
                else :
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    return tmp , tmp.data
                    
            current = current.next
        
    def printAll(self):
        current = self.head
        while current :
            print(f"♦ All Appended Data : {current.data} ♦ Data Address : {current}")
            current = current.next
        print("------------------------------------------------")
        
ob = DoublyLinkedlist()
ob.append(15)
ob.append(29)
ob.append(48)
ob.append(70)
res1 , res2 = ob.delete(48)
ob.printAll()
print(f"♦ Deleted Variable Address : {res1} ♦ Deleted Data : {res2}")
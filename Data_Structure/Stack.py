class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
            #print(f"New Node With Data -> <{data}> Added And In Save This Address -> {node}")
        else:
            node.next = self.top
            self.top = node
            #print(f"New Node With Data -> <{data}> Added And In Save This Address -> {node}")
        self.size += 1
    def pop(self):
        if self.top:
            current  = self.top
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
                current.next = None
                #print(f"<{data}> Deleted From {current} !")
                return data
            else:
                self.top = None
                #print(f"<{data}> Deleted From {current} !")
                return data
        else:
            return "♦ Not Exist Any Node For Delete ! ♦"

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "♦ You Didn't Add Any Node ♦"
        
st = Stack()
st.push(5)
st.push(10)
st.push(8)
st.peek()
st.pop()
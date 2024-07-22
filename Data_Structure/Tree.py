from collections import deque
class Node:
    def __init__(self, data=None):
        self.data = data
        self.right_child = None
        self.left_child = None
        self.mid_child = None


class Tree:
    def __init__(self,data):
        self.root = data
    def bft(self):
        ls_tra = []
        ls2_tra = deque()
        ls2_tra.append(self.root)
        while len(ls2_tra) > 0 :
            current = ls2_tra.popleft()
            ls_tra.append(current.data)
            if current.left_child :
                ls2_tra.append(current.left_child)
            if current.mid_child :
                ls2_tra.append(current.mid_child)
            if current.right_child :
                ls2_tra.append(current.right_child)
        return ls_tra
 
t = Tree()
n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')
n6 = Node('F')
n7 = Node('G')

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4
n2.mid_child = n5
n2.right_child = n6
n3.left_child = n7
ls = t.bft()
print(ls)
class node():
    def __init__(self,val):
        self.val = val
        self.children = []
    def __repr__(self):
        return "n" + str(self.val)

def LCA(root, v, w):
    if not root:
        return None
    if root == v or root == w:
        return root
    count = 0
    lastSubTree = None
    for child in root.children:
        res = LCA(child, v, w)
        if res != None:
            count += 1
            lastSubTree = res
    if count == 2:
        return root
    return lastSubTree

# TEST
n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)
n6 = node(6)
n7 = node(7)
n8 = node(8)
n9 = node(9)
n10 = node(10)
n11 = node(11)
n1.children = [n2, n3]
n2.children = [n4]
n4.children = [n5, n6, n7]
n3.children = [n8]
n8.children = [n9, n10]
n10.children = [n11]

print LCA(n1, n5, n11)
print LCA(n1, n5, n6)
print LCA(n1, n8, n10)
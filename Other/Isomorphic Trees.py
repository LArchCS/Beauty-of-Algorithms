# Isomorphic Trees

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self):
        return "n" + str(self.val)

def isomorphic(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    
    leftLeft = isomorphic(t1.left, t2.left)
    rightRight = isomorphic(t1.right, t2.right)
    if leftLeft == True and rightRight == True:
        return True
    
    leftRight = isomorphic(t1.left, t2.right)
    rightLeft = isomorphic(t1.right, t2.left)
    if leftRight == True and rightLeft == True:
        return True
    
    return False


# TEST
nA1 = TreeNode("A")
nB1 = TreeNode("B")
nC1 = TreeNode("C")
nD1 = TreeNode("D")
nE1 = TreeNode("E")
nF1 = TreeNode("F")
nG1 = TreeNode("G")
nH1 = TreeNode("H")
nA1.left, nA1.right = nB1, nC1
nB1.left, nB1.right = nD1, nE1
nE1.left = nF1
nC1.left = nG1
nG1.left = nH1

nA2 = TreeNode("A")
nB2 = TreeNode("B")
nC2 = TreeNode("C")
nD2 = TreeNode("D")
nE2 = TreeNode("E")
nF2 = TreeNode("F")
nG2 = TreeNode("G")
nH2 = TreeNode("H")
nA2.left, nA2.right = nC1, nB1
nB2.left, nB2.right = nE1, nD1
nE2.left = nF2
nC2.left = nG2
nG2.left = nH2

print isomorphic(nA1, nA2)









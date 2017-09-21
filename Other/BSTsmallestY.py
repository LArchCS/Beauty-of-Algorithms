# -*- coding: utf-8 -*-
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self):
        return "n" + str(self.val)

n2 = TreeNode(2)
n4 = TreeNode(4)
n6 = TreeNode(6)
n8 = TreeNode(8)
n10 = TreeNode(10)
n12 = TreeNode(12)
n14 = TreeNode(14)
n8.left, n8.right = n4, n12
n4.left, n4.right = n2, n6
n12.left, n12.right = n10, n14
'''
           8
         /    \
        4      12
       / \    /  \
     2    6  10   14
'''


def smallestY(root, x):
    if root == None:
        return None
    res = float('inf')
    curt = root
    while curt is not None:
        if x < curt.val < res:
            res = curt.val
        if curt.val >= x:
            curt = curt.left
        else:  # curt.val < x
            curt = curt.right
    if res != float('inf'):
        return res
    return None


# TEST
print smallestY(n8, 10)
print smallestY(n8, 9)
print smallestY(n8, 14)
print smallestY(n8, 0)
print smallestY(n8, 6)

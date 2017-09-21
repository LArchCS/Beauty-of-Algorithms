class node(object):
    def __init__(self, key):
        self.key = key
        self.next = None

n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)

n3.next = n1
n1.next = n4
n4.next = n5
n5.next = n2

def findMax(head):
    if not head:
        return -float('inf')
    nextValue = findMax(head.next)
    return max(nextValue, head.key)

print findMax(n3)
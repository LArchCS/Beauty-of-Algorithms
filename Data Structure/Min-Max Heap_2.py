# -*- coding: utf-8 -*-
# min-max heap
# Fan Di
# 04/13/2017

from math import log, floor

class MinMaxHeap(object):
    """
    an implementation of min-max heap using an array,
    which starts at 1 (ignores 0th element)
    the minimum item is at the top
    the maximum item is at the second level
    """

    def __init__(self):
        self.A = [0]

    # ----- INSERTION - start ----- 
    def insert(self, value):
        """
        place value at an available leaf, then heapify-up from there
        """
        self.A.append(value)
        self.heapify_up(len(self.A) - 1)
    
    def heapify_up(self, i):
        if i / 2 > 0:       # has parent
            parent = self.parent(i)
            if self.depth(i) % 2 == 0:   # on min level
                if self.A[i] > self.A[parent]:
                    self.A[i], self.A[parent] = self.A[parent], self.A[i]  # swap
                    self.heapify_up_max(self.parent(i))
                else:
                    self.heapify_up_min(i)
            else:  # self.depth(i) % 2 == 1    # on max level
                if self.A[i] < self.A[self.parent(i)]:
                    self.A[i], self.A[parent] = self.A[parent], self.A[i]  # swap
                    self.heapify_up_min(self.parent(i))
                else:
                    self.heapify_up_max(i)

    def heapify_up_min(self, i):
        if self.parent(self.parent(i)) > 0:   # has grandparent
            grandparent = self.parent(self.parent(i))
            if self.A[i] < self.A[grandparent]:
                self.A[i], self.A[grandparent] = self.A[grandparent], self.A[i]
                self.heapify_up_min(grandparent)

    def heapify_up_max(self, i):
        if self.parent(self.parent(i)) > 0:   # has grandparent
            grandparent = self.parent(self.parent(i))
            if self.A[i] > self.A[grandparent]:
                self.A[i], self.A[grandparent] = self.A[grandparent], self.A[i]
                self.heapify_up_max(grandparent)
    # ----- INSERTION - end -----
    
    # ----- DELETION - start -----
    def peek_min(self):
        if len(self.A) > 1:
            return self.A[1]

    def peek_max(self):
        if len(self.A) > 1:
            return max(self.A[1: 4])
    
    def delete_min(self):
        m = self.peek_min()
        if len(self.A) > 1:
            self.A[1] = self.A[-1]
            self.A.pop()
            self.heapify_down(1)
        return m
    
    def delete_max(self):
        m = self.peek_max()
        m_i = self.index(m)
        if m_i != -1:
            self.A[m_i] = self.A[-1]
            self.A.pop()
            self.heapify_down(m_i)
        return m

    def heapify_down(self, i):
        if i > 0 and self.depth(i) % 2 == 1:    # min level
            self.heapify_down_min(i)
        else:   # max level
            self.heapify_down_max(i)
    
    def heapify_down_min(self, i):
        if 2 * i  < len(self.A):  # has child
            max_pair = sorted(self.descendants(i))[-1]
            m_i = max_pair[1]  # index of largest descendant
            if 4 * i <= m_i:  # m_i is i's grandchild
                if self.A[m_i] > self.A[i]:
                    self.A[i], self.A[m_i] = self.A[m_i], self.A[i]
                    if self.A[m_i] < self.A[self.parent(m_i)]:
                        self.A[m_i], self.A[self.parent(m_i)] = self.A[self.parent(m_i)] , self.A[m_i]
                    self.heapify_down_min(m_i)
            else:  # m_i must be i's child, if not i's grandchild
                if self.A[m_i] > self.A[i]:
                    self.A[i], self.A[m_i] = self.A[m_i], self.A[i]  
    
    def heapify_down_max(self, i):
        if 2 * i  < len(self.A):  # has child
            min_pair = sorted(self.descendants(i))[0]
            m_i = min_pair[1]  # index of smallest descendant
            if 4 * i <= m_i:  # m_i is i's grandchild
                if self.A[m_i] < self.A[i]:
                    self.A[i], self.A[m_i] = self.A[m_i], self.A[i]
                    if self.A[m_i] > self.A[self.parent(m_i)]:
                        self.A[m_i], self.A[self.parent(m_i)] = self.A[self.parent(m_i)] , self.A[m_i]
                    self.heapify_down_max(m_i)
            else:  # m_i must be i's child, if not i's grandchild
                if self.A[m_i] < self.A[i]:
                    self.A[i], self.A[m_i] = self.A[m_i], self.A[i]
    
    def descendants(self, i):
        """
        return list of children's and grandchildren's indices
        """
        a = []
        # left child
        if 2 * i < len(self.A):
            a = a + [(self.A[2 * i], 2 * i)]  # left child
            if 2 * (2 * i) < len(self.A):
                a = a + [(self.A[2 * (2 * i)], 2 * (2 * i))]  # leftLeft
                if 2 * (2 * i) + 1 < len(self.A):
                    a = a + [(self.A[2 * (2 * i) + 1],2 * (2 * i) + 1)]  # leftRight
        # right child
        if 2 * i + 1 < len(self.A):
            a = a + [(self.A[2 * i + 1], 2 * i + 1)]  # left child
            if 2 * (2 * i + 1) < len(self.A):
                a = a + [(self.A[2 * (2 * i + 1)], 2 * (2 * i + 1))]  # rightLeft
                if 2 * (2 * i + 1) + 1 < len(self.A):
                    a = a + [(self.A[2 * (2 * i + 1) + 1], 2 * (2 * i + 1) + 1)]  # rightRight
        return a
    
    def index(self, value):
        """
        this method is only called to find the index of maximum in the heap
        can be considered as run in a constant time, since at most 3 items to check
        """        
        try:
            return self.A.index(value)
        except ValueError:
            return -1
    # ----- DELETION - end -----
    
    # this method is to build a min-max heap from self.A
    # BUILD-MIN-MAX-HEAP
    def heapify(self):
        """
        heapify a random array as stored in self.A
        """
        for i in range(len(self.A) / 2, 0, -1):  # only heapify_down half of the heap
            self.heapify_down(i)    
    
    def depth(self, i):
        """
        returns the depth of i
        """
        return floor(log(int(i), 2))
    
    def parent(self, i):
        """
        return i's parent index
        """
        return int(i) / 2

# TEST
import random

print "test insert / delete_min"
A = MinMaxHeap()
arr = [i for i in range(100)]
res = []
for i in range(10):
    size = len(arr)
    index = random.choice(range(size))
    num = arr.pop(index)
    res.append(num)
    A.insert(num)
#print res
#print A.A[1:]
heapSort = []
while len(A.A) > 1:
    num = A.delete_min()
    heapSort.append(num)
print sorted(res)
print heapSort 
print sorted(res) == heapSort


print "\ntest heapify / delete_max"
A = MinMaxHeap()
arr = [i for i in range(100)]
res = []
for i in range(10):
    size = len(arr)
    index = random.choice(range(size))
    num = arr.pop(index)
    res.append(num)

heapSort = []
for i in res:
    A.A.append(i)
A.heapify()
#print res
#print A.A[1:]
while len(A.A) > 1:
    num = A.delete_max()
    heapSort.append(num)
res.sort(reverse = True)
print res
print heapSort 
print res == heapSort


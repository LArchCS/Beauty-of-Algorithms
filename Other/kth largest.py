# kth largest

import heapq

def kth(A, k):
    if len(A) < k:
        return None
    S = [-float('inf')] * k
    while A:
        num = A.pop()
        if num > S[0]:
            heapq.heappop(S)
            heapq.heappush(S, num)
    return S[0]

# TEST
A = [5,4,2,1,7,8,9,0,3,6]

print kth(A, 1)
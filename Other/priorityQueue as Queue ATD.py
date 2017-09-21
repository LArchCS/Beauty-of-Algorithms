
import heapq
heap = []
nums = [1,3,5,2,4,8,9,7,6]
key = 0

for num in nums:
    heapq.heappush(heap, (key, num))
    key += 1

while heap:
    print heapq.heappop(heap)[1],

print
print key
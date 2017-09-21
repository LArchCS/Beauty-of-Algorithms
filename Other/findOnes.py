

def findOnes(n):
    if n == 0:
        return 0
    return n % 2 + findOnes(n / 2)


print findOnes(1024)
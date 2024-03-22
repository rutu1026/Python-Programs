import math
class Solution:
    def isPrime (self, N):
        # code here
        
        if N == 1: return 0
        
        l = int(math.sqrt(N)) + 1
        
        for i in range(2, l):
            if N % i == 0:
                return 0
                
        return 1

t = int(input("Enter range:"))

for _ in range(t):
    n = int(input("Enter number:"))

    obj = Solution()
    print(obj.isPrime(n))
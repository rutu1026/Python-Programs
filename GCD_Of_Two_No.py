class Solution:
    def gcd( A, B):
        # code here
        
        if A == B:
            return A
            
        if A>B:
            for i in range(A//2,0,-1):
                if A%i == 0 and B%i == 0:
                    return i
        elif B>A:
            for i in range(B//2,0,-1):
                if A%i == 0 and B%i == 0:
                    return i


ob = Solution
print(ob.gcd(3,6))
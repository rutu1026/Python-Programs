def is_AutomorphicNumber(n):
        # Code here
        sum = n**2
        # print(str(sum)[-1])
        if str(sum)[-1] == str(n)[-1]:
            return 'Automorphic'
        return 'Not Automorphic'

print(is_AutomorphicNumber(76))

# Given a number N, check whether the number is Automorphic number or not.
# A number is called Automorphic number if and only if its square ends in  has the same last digit as the number itself. 

#____________________________________________________________________________________________________



# sum of digits are palindrome or not

# class Solution:
#     def isDigitSumPalindrome(n):
#         #code here
        
#         s = 0
#         no = n
        
#         while n>0:
            
#             temp = n%10
#             s += temp
#             n //= 10
            
#         # r = str(s)
#         # print(r)
            
#         if str(s) == str(s)[::-1]:
#             return 1
#         else:
#             return 0
        
# s = Solution
# print(s.isDigitSumPalindrome(56))



# -----------------  OR

# strg = str(N)
#         sum = 0
#         for i in strg:
#             sum += int(i)
#         if str(sum) == str(sum)[::-1]:
#             return 1
#         return 0
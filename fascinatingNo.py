class Solution:
	
	def fascinating(n):
		no = n
		ans = str(no) + str(n * 2) + str(n * 3)
		return set(ans)==set("123456789") and len(ans)==9
	
o = Solution
print(o.fascinating(192))
		
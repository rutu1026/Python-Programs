class Solution:
    def reciprocalString(S):
        final_str = ''
        for ch in S:
            if ch.isupper():
                final_str += chr(ord('Z') + ord('A') - ord(ch))
            elif ch.islower():
                final_str += chr(ord('z') + ord('a') - ord(ch))
            else:
                final_str += ch
        return final_str

o = Solution
print(o.reciprocalString("Ish"))
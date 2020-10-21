class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length = 0
        i = 0
        for j in range(len(s)):
            if s[j] in substring: 
                if len(substring) > length:
                    length = len(substring)
                    print(length)
                while s[i] != s[j]:
                    substring.remove(s[i])   
                    i+=1
                i+=1
            else:
                substring.add(s[j])        
        if len(substring) > length:
            length = len(substring)  
        return length
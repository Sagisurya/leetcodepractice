class Solution:
    def makeGood(self, s: str) -> str:
        
        while True:
            i= 0;
            temp = len(s)
            while i < len(s)-1:
                if abs(ord(s[i]) - ord(s[i+1])) == 32:
                    if i+2 < len(s):
                        s = s[:i] + s[i+2:]
                    else:
                        s = s[:i]
                i+=1
            if temp == len(s):
                break
        return s
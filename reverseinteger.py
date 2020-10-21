class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            result = -self.reverse(-x)
            return result if result > -(2**31) else 0
            
        result = 0
        digitlist = []  # list to store all the digits of the given integer
         
        while x != 0:
            temp = x%10
            digitlist.append(temp)
            x = x//10
        print(digitlist)
        for i in range(len(digitlist)):
            result += digitlist[i] * (10 ** (len(digitlist)-i-1))
        
        
        return result if result < ((2**31)-1) else 0
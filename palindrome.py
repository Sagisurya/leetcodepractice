class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        if x%10 == x:
            return True
        if x%10 == 0 or x<0:
            return False
        while(x>reversed_num):
            reversed_num = reversed_num *10 + x%10
            x  = x//10
        if x == reversed_num or x == reversed_num//10:
            return True
        else:
            return False
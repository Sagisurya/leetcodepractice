class Solution:
    def isHappy(self, n: int) -> bool:
        results = []
        while n != 1:
            result = 0
            while n != 0:
                temp = n % 10
                result += temp * temp
                n = n//10
                #print(n)
            if result in results:
                return False
            results.append(result)
            print(result)
            n = result
        return True 
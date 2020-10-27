class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        j= 0
        flag = False
        if len(strs) == 0:
            return ""
        while True:
            if j == len(strs[0]):
                break
            temp = strs[0][j] 
            for i in range(1, len(strs)):
                if j >= len(strs[i]):
                    flag = True
                    break
                if strs[i][j] != temp:
                    flag = True
                    break
            if flag:
                break
            else:
                result = result + temp
                print(result)
                j+=1
        return result
class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {}
        dictionary['I'] = 1
        dictionary['V'] = 5
        dictionary['X'] = 10
        dictionary['L'] = 50
        dictionary['C'] = 100
        dictionary['D'] = 500
        dictionary['M'] = 1000
        result = 0
        i = 0
        while i < len(s):
            if i != len(s)-1:
                if dictionary[s[i]] < dictionary[s[i+1]]:
                    result = result + dictionary[s[i+1]] - dictionary[s[i]]
                    i += 1
                else:
                    result = result + dictionary[s[i]]
            else:
                if dictionary[s[i]] > dictionary[s[i-1]]:
                    break;
                else:
                    result = result + dictionary[s[i]]
            i+=1
        return result
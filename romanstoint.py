class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = len(s)
        sum = 0
        visitedIndex = []
        for i in range(n - 1):
            if(i in visitedIndex):
                continue
            if(romans[s[i]] < romans[s[i + 1]]):
                sum = sum + romans[s[i + 1]] - romans[s[i]]
                visitedIndex.append(i + 1)                
            else:  
              sum = sum + romans[s[i]]

        if((n-1) in visitedIndex) == False:
            sum = sum + romans[s[n -1]]
        return sum
s = Solution()

print(s.romanToInt('LVIII'))

    
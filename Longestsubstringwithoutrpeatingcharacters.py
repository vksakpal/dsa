import math

class Solution:

    def areDistinct(self,str, i, j):
 
        # Note : Default values in visited are false
        visited = [0] * (256)
 
        for k in range(i, j + 1):
            if (visited[ord(str[k])] == True):
                return False
    
            visited[ord(str[k])] = True
 
        return True

    def lengthOfLongestSubstring1(self, s: str) -> int:
        n = len(s)
 
        # Result
        res = 0
    
        for i in range(n):
            for j in range(i, n):
                if (self.areDistinct(s, i, j)):
                    res = max(res, j - i + 1)
    
        return res


    def solve(self,str: str) -> int:
        if len(str) == 0:
            return 0
        maxans = -1
        for i in range(len(str)):  # outer loop for traversing the string
            set = {}
            # nested loop for getting different string starting with str[i]
            for j in range(i, len(str)):
                if str[j] in set:  # if element if found so mark it as ans and break from the loop
                    maxans = max(maxans, j - i)
                    break
                set[str[j]] = 1
        return maxans

    def lengthOfLongestSubstring(self, s: str) -> int:

        if(s == ' '):
            return 1
        if(s == ''):
            return 0

        lastchar = ''
        longeststring = ''
        longeststringlist = []
        chars = []
        keepgoing = True
        currentCounter = 0
        while(keepgoing):
            i = currentCounter
            for i  in list(range(currentCounter,len(s))):
                if(len(list(filter(lambda x:x == s[i], chars)))>0):                    
                    break

                if(s[i] != lastchar):
                    longeststring += s[i]
                else:
                    break
                lastchar =s[i]
                chars.append(s[i])
                if(i >= (len(s) - 1)):
                    keepgoing = False

            
            currentCounter += 1            
            longeststringlist.append(longeststring)
            longeststring = ''
            lastchar ='' 
            chars.clear()

        finallength = 0
        for t in longeststringlist:
            if(len(t) > finallength):
                finallength = len(t)

        return finallength   

s = Solution()

#num = s.lengthOfLongestSubstring("loddktdji")
num = s.lengthOfLongestSubstring1("loddktdji")
print(num)
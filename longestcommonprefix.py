from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1 = strs[0]
        size = len(strs)
        prefix = ''
        iscommonchar = False
        end = 0

        if(len(strs) == 1):
            return strs[0]

        for i in range(len(strs)):
           if(i == 0):
              end = len(strs[i])
           elif(len(strs[i]) < end ):
              end= len(strs[i])
              
              
        
        for i in range(end):            
          for j in range(1, len(strs)):
             tempstr = strs[j]
             if(str1[i] == tempstr[i]):
                iscommonchar = True
             else:
                iscommonchar = False
                break

          if (iscommonchar):
             prefix += str1[i]
          else: break

        return prefix
    
s = Solution()
print(s.longestCommonPrefix(["c","acc","ccc"]))
                
             
            
            
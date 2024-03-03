from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = []
        for i in nums:            
            if (i not in duplicates):
                duplicates.append(i)            
        nums = duplicates
        return len(duplicates)
    

s=Solution()
s.removeDuplicates([1,1,2])
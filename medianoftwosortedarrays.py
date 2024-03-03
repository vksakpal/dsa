
from statistics import median
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        finaloutput = float(median(nums3))
        return finaloutput


s = Solution()
s.findMedianSortedArrays([1,1,4,5],[1,5,6])
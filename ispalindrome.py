class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = x
        num1 = 0
        while(s > 0):
            remainder = (int)(s % 10)
            s = (int)(s /10)
            num1 = num1 * 10 + remainder
        if(num1 == x):
          return True
        else:
          return False
    

s = Solution()
s.isPalindrome(152)






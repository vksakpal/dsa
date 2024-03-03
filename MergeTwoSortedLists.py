# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
          llist = ListNode(0)
          tail = llist
          while True:
              if(list1 is None):
                  tail.next = list2
                  break
              if(list2 is None):
                  tail.next = list1
                  break
              if(list1.val < list2.val):
                  tail.next = list1
                  list1 = list1.next
              else:
                  tail.next = list2
                  list2 = list2.next
              tail = tail.next
          
          return llist

              


                    
                
   
s = Solution()

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)

print(a)
 
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

print(b)

print(s.mergeTwoLists(a,b))


                    
                    
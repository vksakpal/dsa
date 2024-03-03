class Node:
  def __init__(self,data) -> None:
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self) -> None:
    self.head = None

  def push(self,new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def  print(self):
    temp = self.head
    while(temp):
      print(temp.data, end=" ")
      temp = temp.next
    
  def printhead(self):
    print(self.head.data)


llist = LinkedList()
llist.push(3)
llist.push(4)
llist.push(2)
llist.print()

llist1 = LinkedList()
llist1.push(4)
llist1.push(6)
llist1.push(5)
llist1.print()


head = llist.head
head1 = llist1.head
remainder = 0
s  = list()

while(head or head1):
   
   num = (head.data if head else 0) + (head1.data if head1 else 0) + remainder
   temp_num = (int)(num / 10)
   if(temp_num > 0):
     temp1 =  (int)(num % 10)
     remainder = (int)(num/10)
     s.append(temp1)
   else:
     s.append(num)

   head = head.next
   head1 = head1.next

finalList = LinkedList()

for j in s:
  finalList.push(j)
     head = l1
        head1 = l2
        remainder = 0
        s  = list()

        while(head or head1):
        
           num = (head.val if head else 0) + (head1.val if head1 else 0) + remainder
           temp_num = (int)(num / 10)
           if(temp_num > 0):
             temp1 =  (int)(num % 10)
             remainder = (int)(num/10)
             s.append(temp1)
           else:
             s.append(num)

            head = head.next
            head1 = head1.next

finalList.print()


     


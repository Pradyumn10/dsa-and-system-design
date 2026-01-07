"""
Date: Jan 7, 2026
Problem: https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# node1=ListNode(2)
# node2=ListNode(4)
# node3=ListNode(3)
# node1.next=node2
# node2.next=node3 

# head=node1
# while head:
#     print(head.val, end=" -> ")
#     head=head.next
# print("None")


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(max(m,n)) where m and n are the lengths of the two linked lists.
        Space Complexity: O(max(m,n)) for the output linked list.
        Example:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
        Time Complexity=O(max(3,3))=O(3)=O(1)
        Space Complexity=O(max(3,3))=O(3)=O(1) 

        """
        number1=""
        while l1:
            #print(l1.val)
            number1=number1+str(l1.val)
            l1=l1.next
        number2=""
        while l2:
            number2=number2+str(l2.val)
            l2=l2.next
        number1F=number1[::-1]
        number2F=number2[::-1]
        sumTotal=int(number1F)+int(number2F) 
        sumTotalF=str(sumTotal)[::-1]
        #print(sumTotal, sumTotalF)
        head=None
        prev=None
        for v in sumTotalF:
            #708
            node=ListNode(int(v))
            if head is None:
                head=node
            else:
                prev.next=node
            prev=node
        return head


# Testing the implementation
solution=Solution()
nodeA1=ListNode(2) 
nodeA2=ListNode(4)
nodeA3=ListNode(3)
nodeA1.next=nodeA2
nodeA2.next=nodeA3
nodeB1=ListNode(5)
nodeB2=ListNode(6)
nodeB3=ListNode(4)
nodeB1.next=nodeB2
nodeB2.next=nodeB3
result=solution.addTwoNumbers(nodeA1, nodeB1)
current=result
while current:
    print(current.val, end=" -> ")
    current=current.next
print("None")

#243+564=807
# Output: 7 -> 0 -> 8 ->
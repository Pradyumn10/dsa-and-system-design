"""
Date: Jan 11, 2026
Problem: https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        completeArray=[]
        while list1:
            completeArray.append(list1.val)
            list1=list1.next
        while list2:
            completeArray.append(list2.val)
            list2=list2.next
        completeArray.sort()
        head=None
        prev=None
        for i,v in enumerate(completeArray):
            node=ListNode(int(v))
            if head is None:
                head=node
            else:
                prev.next=node
            prev=node
        return head


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
mergedList=solution.mergeTwoLists(nodeA1, nodeB1)
while mergedList:
    print(mergedList.val, end=" -> ")
    mergedList=mergedList.next
print("None")
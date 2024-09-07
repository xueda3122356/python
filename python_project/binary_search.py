from typing import List
from collections import deque
from typing import Optional

class ListNode:
     def __init__(self, val=0, left=None, right = None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def reorderList(self, head: ListNode, n: int) -> ListNode:
        prev, front = None, self.createLinkedList(head)

        # check the length of the linked list
        temp = front
        length = 0
        while temp:
            temp = temp.next
            length += 1
        
        # find the position of the node to remove
        position = length - n

        # move to the n-th node
        curr = front
        while position:
            prev = curr
            temp = curr.next
            curr = temp
            position -= 1
        
        # remove the n-th node
        if length == n:
            temp = front.next
            front.next = None
            front = temp

        else:
            prev.next = curr.next
            curr.next = None

        self.printLinkedList(front)
        return front
    
    def createLinkedList(self, list: ListNode) -> ListNode:
        if not list:
            return None
        
        head = ListNode(list[0])
        curr = head

        for i in list[1:]:
            curr.next = ListNode(i)
            curr = curr.next
    
        return head
    
    def printLinkedList(self, list: ListNode):
        while list:
            print(list.val)
            list = list.next


instance = Solution()
print(instance.reorderList([2,4,6,8], 3))

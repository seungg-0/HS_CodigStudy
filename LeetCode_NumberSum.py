# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1 
        b = l2 
        list1 = []
        list2 = []

        while a:
            list1.append(a.val)
            a = a.next

        while b:
            list2.append(b.val)
            b = b.next

        list1.reverse()
        list2.reverse()

        numbera = int("".join(str(x) for x in list1))
        numberb = int("".join(str(x) for x in list2))

        c = list(str(numbera + numberb))

        head = l3 = ListNode(c.pop())

        c.reverse()

        # traverse remaining digits, assigning each to new ListNode
        for i in c:
            l3.next = ListNode(i)
            l3 = l3.next

        return head 

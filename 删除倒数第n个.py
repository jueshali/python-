# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:08:34 2018

@author: Administrator
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
        p = head
        r = head
        while n+1 > 0:
            if r == None:
                return head.next
            r = r.next
            n = n-1
        
        while r != None:
            r = r.next
            p = p.next
        q = p.next
        p.next = q.next
        return head
            
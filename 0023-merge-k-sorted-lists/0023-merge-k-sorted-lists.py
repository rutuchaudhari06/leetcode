# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        pq=[]
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(pq,(node.val,i,node))
        dummy=ListNode(-1)
        curr=dummy
        while pq:
            v,idx,node=heapq.heappop(pq)
            curr.next=node
            curr=curr.next
            if node.next:
                heapq.heappush(pq, (node.next.val, idx, node.next))

        return dummy.next



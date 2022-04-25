class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        lenght, tail = 1, head

        while tail.next:
            tail = tail.next
            lenght += 1
        k = k % lenght
        if k == 0:
            return head
        cur = head
        for i in range(lenght - k - 1):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead
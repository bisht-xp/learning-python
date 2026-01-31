class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: Optional[ListNode]) -> None:
    if not head:
        return 
    
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    second = slow.next
    slow.next = None
    prev = None

    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    
    first, second = head, prev

    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2

    

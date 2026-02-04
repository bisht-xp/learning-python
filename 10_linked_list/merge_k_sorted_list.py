class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeList(nodeA: Optional[ListNode], nodeB: Optional[ListNode]):
    dummy = ListNode(0)
    temp = dummy.next
    while nodeA and nodeB:
        if nodeA.val < nodeB.val:
            temp = nodeA
            nodeA = nodeA.next
        else:
            temp = nodeB 
            nodeB = nodeB.next
        
        temp = temp.next
    
    temp = nodeA or nodeB

    return dummy.next


def divide(lists: list[Optional[ListNode]], l: int,  h: int) -> Optional[ListNode]:
    if(l >= h):
        return lists[l]
    
    mid = (l+h)//2

    left = divide(lists[l:mid], l, mid)
    right = divide(lists[mid:h], mid,h)

    return mergeList(left,right)

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    n = len(lists)
    return divide(lists, 0, n)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Method to add node in the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    # Method to add node in any position
    def insertAtIndex(self, data, pos):
        if (self.size <  pos):
            print("sorry !! can't add at this positon")
            return 
        
        if pos == 0:
            self.insertAtBegin(data)
            return
        
        new_node = Node(data)
        current_node = self.head

        while current_node is not None and pos-1 > 0:
            pos -= 1
            current_node = current_node.next
        
        new_node.next = current_node.next
        current_node.next = new_node
        self.size += 1

    # Method to add node in the last 
    def insertAtLast(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        self.size += 1

    # Update node at given position
    def updateNode(self, data, pos):
        if (self.size < pos):
            print("sorry out of scope")
            return
        
        current_node = self.head
        while (current_node is not None and pos-1 > 0):
            pos -= 1
            current_node = current_node.next
        
        current_node.data = data
    
    def reverse_place_reversal(self, head): 
        if not head or not head.next:
            return

        current_head = self.head
        prev = None

        while current_head:
            nextTemp = current_head.next
            current_head.next = prev
            prev = current_head
            current_head = nextTemp
        
        newhead = prev
        return newhead
    
    def recursive(self, head):
        if not head or not head.next:
            return head
        
        resHead = self.recursive(head.next)
        head.next.next = head
        head.next = None
        return resHead        

    def reverseKGroup(self, head, k): 
        if not head or k == 1:
            return head
        
        dummy = LinkedList()
        dummy.insertAtBegin(-1)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # Check if there are at least k nodes left
            last = prev_group_end
            for _ in range(k):
                last = last.next
                if not last:
                    self.printAll(dummy.next)
                    return dummy.next
            
            # Reverse k nodes
            curr = prev_group_end.next
            new_group_start = last.next
            prev = new_group_start
            original_first = curr
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            

            prev_group_end.next = prev
            prev_group_end = original_first


            



            


    # Print all the Linked List:
    def printAll(self,head):
        current_node = head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next



llist = LinkedList()

# llist.insertAtBegin(4)
# llist.insertAtBegin(3)
# llist.insertAtBegin(2)
# llist.insertAtBegin(1)

# llist.insertAtLast(5)
# llist.insertAtLast(6)


# llist.insertAtIndex(7,1)

# llist.updateNode(8,3)
llist.insertAtBegin(1)
llist.insertAtLast(2)
llist.insertAtLast(3)
llist.insertAtLast(4)
llist.insertAtLast(5)

# llist.recursive(llist.head)
# llist.removeNthNode(1)
# llist.reverse_place_reversal()
llist.reverseKGroup(llist.head, 2)
# llist.swapPair()
# llist.rotateRight(4)

# print List
# llist.printAll()

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def count_element(head, val):
    '''
	IOCE
	    input: head -> start of LL, 
		       val -> which element to find the freq of
		output: frequency of val
		constraints/considerations:
            be able to explain your time and space complexity
			traversing through a LL is O(n)
            is it guaranteed that the head will NOT be None
                or that the val will actually be in the LL
		examples
		    1. LL: 3 -> 1 -> 2 -> 1 ; head = 3, val = 1
                output => 2
	Plan
        curr = head
		freq = 0 (counting the freq of val)
        while (curr != None)
            if (curr.value == val):
                freq++
            curr = curr.next
		return freq
'''
    curr = head
    freq = 0 #(counting the freq of val)
    while curr:
        if (curr.value == val):
            freq+=1
        curr = curr.next
    return freq

# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next
    current.next = None # Remove the last node by setting second-to-last node to None
    return head

def find_middle_element(head):
    '''
    IOCE
        input: head -> root of SLL
        output: Node obj -> middle element in SLL 
                2nd middle obj if len(SLL)%2 == 0
        constraints/considerations
            if the len of LL is even, then return the 2nd mid node
            how to have two pointers in SLL
                we could increment fast pointer by .next.next and slow just by .next
        examples:
            1 -> 2 -> 3 ; head  = 1; return 2
            2 -> 3 -> 4 -> 5; head = 2; return 4 
            
    Plan 
        create fast and slow pointers for SLL
        traverse SLL
            if fast.next == None
                return slow.value
            increment slow
                account for 2nd middle node
            increment fast
        return slow.value'''
    slow_curr = head
    fast_curr = head.next.next
    while fast_curr:
        slow_curr = slow_curr.next
        fast_curr = fast_curr.next
    return slow_curr.value

def is_palindrome(head):
    '''
    IOCE 
        input: Node ->head of SLL
        output: bool ->  indicating if SLL is palindromic
        constraints/considerations:
            use the two-ptr technique
                how to look at first and last ptr.s simultaneously
            space complexity -> 
            time complexity ->

        examples:
            1->2->1; head: 1; out: True
    Plan
        have a slow and fast ptrs for first half of SLL 
            and second half of SLL
        how to traverse to midpoint of SLL
            initially traverse until we indicate the midpoint of SLL
            slow = head
            fast = head.next.next
            while (slow.value == fast.value)
                slow = slow.next
                fast = fast.next
            save slow node as the midpoint
        then traverse until and compare first half with second half
            first = head
            second = slow
            while second.next
                compare first and second values
                    if false return false
                update first and second ptrs
            return true
      '''
    slow_curr = head
    fast_curr = head.next.next
    while fast_curr:
        slow_curr = slow_curr.next
        fast_curr = fast_curr.next
    past_midpoint = slow_curr.next

    before_midpoint = head
    while past_midpoint.next:
        if before_midpoint.value != past_midpoint.value:
            return False
        before_midpoint = before_midpoint.next
        past_midpoint = past_midpoint.next
    return True


node4 = Node(4, Node(3, Node(2, Node(3, Node(4)))))
head2 = Node(3, Node(4, Node(3, Node(5))))
head3 = Node(1, Node(2, Node(3)))
#print(f"{node4.value} -> {node4.next.value} -> {node4.next.next.value}")
#print(count_element(node4, 2)) #this should return 1
#removed_head = remove_tail(node4)
#print_list(removed_head)

# print(find_middle_element(node4))
# print(find_middle_element(head2))
# print(find_middle_element(head3))

#print(is_palindrome(head2))

def is_identical(head_a, head_b):
    #traverse thru both LLs and check for inequality, if so return false
    #after traversing return true
    curr_a = head_a
    curr_b = head_b
    while curr_a and curr_b:
        if curr_a.value != curr_b.value:
            return False
        curr_a = curr_a.next
        curr_b = curr_b.next
    return True

finn = Node(1, Node(2, Node(3)))
fern = Node(1, Node(2, Node(3)))
print(is_identical(finn, fern))

def delete_node():
    pass
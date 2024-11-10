class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def printed_linked_list(head):
    curr_node = head
    sol_str = str(head.value)
    while curr_node.next != None:
        sol_str += f" -> {curr_node.next.value}"
        curr_node = curr_node.next
    print(sol_str)

def add_first(head, new_node):
    '''replace the new_node as the new head of the linked list'''
    new_node.next = head.next
    return new_node

def get_tail(head):
    if head == None:
        return None
    curr_node = head
    while curr_node.next != None:
        curr_node = curr_node.next
    print(curr_node.value)
    return curr_node.value


node_one = Node('a')
node_two = Node('b')
node_one.next = node_two

# print(node_one.value) 
# print(node_one.next.value) 
# print(node_two.value)
# print(node_two.next)        

#this is the Mario Party linked list
toad = Node("Toad")
wario = Node("Wario", toad)
luigi = Node("Luigi", wario)
mario = Node("Mario", luigi)
# print(f"{mario.value} -> {luigi.value} -> {wario.value} -> {toad.value}")
# printed_linked_list(mario)

node_2 = Node("Wigglypuff")
node_1 = Node("Jigglypuff", node_2)
# print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)
# print(node_1.value, "->", node_1.next.value)

# linked list: num1->num2->num3
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
head = num1
tail = get_tail(num1)
print(tail)

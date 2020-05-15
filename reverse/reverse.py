class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list_helper(self, node, prev):
        # make tail head
        if node.next_node is None:
            self.head = node 

            node.next_node = prev
            return 

        nxt = node.next_node 

        node.next = prev 

        self.reverse_list_helper(nxt, node) 
    
    def reverse_list(self):
        if self.head is None:
            return
        self.reverse_list_helper(self.head, None)

        # not sure why this isn't working,
        # # base case where list is empty
        # if head is None:
        #     return None 
        # # second base case where list is only one element
        # elif head.next_node is None:
        #     return head  
        # # split into head and rest like in Haskell
        # rest = self.reverse_list(head.next_node, None)
        # head.next_node.next_node = head
        # head.next_node = None 

        # return rest 



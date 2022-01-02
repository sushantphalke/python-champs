class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


# here now node is created we have to create linked list element shells
class LinkedList:
    # we now creating head
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()
    # Assign item values that are becoming link elements
    linked_list.head = Node(987)
    second = Node(27475)
    third = Node(3)
    fourth = Node(4000)
    # Connect nodes by using .next so they appear as link element with nxt ele. info
    linked_list.head.next = second
    second.next = third
    third.next = fourth
    ' FOR DELETION OF ITEMS IN LINK LIST DELETE ITS CONNECTING .NEXT '
    # Print the linked list item
    while linked_list.head is not None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.head = Node(234)
    linked_list.head.next = Node(45)
    linked_list.head.next.next = Node(235)
    linked_list.head.next.next.next = Node(35)
    print('\nthis is linked list')
    while linked_list.head is not None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next

# def insert_at_index (self, index, data):
#        if index == 1:
#            new_node = Node(data)
#            new_node.ref = self.start_node
#            self.start_node = new_node
#        i = 1
#        n = self.start_node
#        while i < index-1 and n is not None:
#            n = n.ref
#            i = i+1
#        if n is None:
#            print("Index out of bound")
#        else:
#            new_node = Node(data)
#            new_node.ref = n.ref
#            n.ref = new_node

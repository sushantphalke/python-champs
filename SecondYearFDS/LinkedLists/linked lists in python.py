# Create a node
"""creating a node to store items and next item link """

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14]
print(list1.__len__())

class Node:

    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    @staticmethod
    def insertAfter(node, data):

        if node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    # Insert at the end
    def insertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    # Deleting a node
    def deleteNode(self, position):

        if self.head is None:
            return

        temp_node = self.head

        if position == 0:
            self.head = temp_node.next
            temp_node = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp_node = temp_node.next
            if temp_node is None:
                break

        # If the key is not present
        if temp_node is None:
            return

        if temp_node.next is None:
            return

        next = temp_node.next.next
        temp_node.next = None
        temp_node.next = next

    def printList(self):
        temp_node = self.head
        while temp_node:
            print(str(temp_node.item) + " ", end="")
            temp_node = temp_node.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 1000)
    llist.insertAfter(llist.head.next, 2000)
    llist.insertAfter(llist.head.next, 3000)
    llist.insertAfter(llist.head.next, 4000)
    llist.insertAfter(llist.head.next, list1)
    print('Linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    # llist.deleteNode(4)  # uses index for deletion
    # llist.deleteNode(0)
    llist.printList()

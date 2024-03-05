class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node.next != self.head:
            print(current_node.data, end="->")
            current_node = current_node.next
        print(current_node.data)


l_list = LinkedList()

l_list.append(1)
l_list.append(3)
l_list.append(3)
l_list.append(4)
l_list.append(5)
l_list.display()

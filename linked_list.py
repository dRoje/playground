from typing import List, Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def __repr__(self):
        if not self.head:
            return "list empty"

        node = self.head
        retval = "list: " + str(node.data)
        while node.next is not None:
            retval += f" -> {node.next.data}"
            node = node.next

        return retval

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        # get to the last node
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, value):
        while self.head and self.head.data == value:
            self.head = self.head.next

        node = self.head
        while node and node.next is not None:
            while node.next and node.next.data == value:
                node.next = node.next.next
            node = node.next

    def to_list(self) -> List:
        retval = []
        node = self.head
        while node is not None:
            retval.append(node.data)
            node = node.next
        return retval

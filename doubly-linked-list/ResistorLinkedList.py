from Node import Node


class ResistorLinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.previous = None
            self.head = new_node

        else:
            new_node = Node(data)
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            new_node.previous = current_node
            new_node.next = None

    # in ascending order
    def sort_list_by_resistance(self):
        # Check whether list is empty
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                next_node = current_node.next
                while next_node is not None:
                    # Swapping if current_node.data.resistance > next_node.data.resistance
                    if current_node.data.resistance > next_node.data.resistance:
                        temporary_variable = current_node.data
                        current_node.data = next_node.data
                        next_node.data = temporary_variable
                    next_node = next_node.next
                current_node = current_node.next

    # in ascending order
    def sort_list_by_name(self):
        if self.head is None:
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                next_node = current_node.next
                while next_node is not None:
                    if current_node.data.name > next_node.data.name:
                        temporary_variable = current_node.data
                        current_node.data = next_node.data
                        next_node.data = temporary_variable
                    next_node = next_node.next
                current_node = current_node.next

    def print_resistors_with_accuracy_bigger_than(self, input_accuracy: float):
        current_node = self.head

        if self.head is None:
            print("List is empty")
            return

        while current_node is not None:
            # Prints each node by incrementing pointer.
            if input_accuracy < current_node.data.accuracy:
                print(current_node.data)
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        if self.head is None:
            print("List is empty")
            return

        while current_node is not None:
            # Prints each node by incrementing pointer.
            print(current_node.data)
            current_node = current_node.next

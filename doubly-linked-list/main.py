# """
# Created by RoSteik (Telegram: @Rosteik)
# """
#
from ResistorLinkedList import ResistorLinkedList
from Resistor import Resistor

if __name__ == '__main__':
    resistors_list = ResistorLinkedList()

    print()
    resistors_list.add_node(Resistor("D", 3, 3, 0.6))
    resistors_list.add_node(Resistor("A", 7, 4, 0.8))
    resistors_list.add_node(Resistor("C", 6, 5, 0.9))
    resistors_list.add_node(Resistor("B", 5, 6, 0.99))

    print("Original list: ")
    resistors_list.print_list()

    resistors_list.sort_list_by_resistance()

    print()
    print("Sorted list by resistance: ")
    resistors_list.print_list()

    resistors_list.sort_list_by_name()

    print()
    print("Sorted list by name: ")
    resistors_list.print_list()

    print()
    print("Resistors which have accuracy better than input accuracy: ")
    resistors_list.print_resistors_with_accuracy_bigger_than(0.79)

#!/usr/bin/python3

class MyList(list):
    """
    This class inherits from the built-in list class and provides additional functionality.
    """

    def print_sorted(self):
        """
        Print the list in sorted order (ascending).
        """
        sorted_list = sorted(self)
        print(sorted_list)

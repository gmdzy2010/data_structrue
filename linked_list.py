"""
This module contains series of python implementations of linked list.
There's a interesting problem:

Example 1:
>>> a = 1
>>> b = 2
>>> a, b = None, a
>>> print(a, b)
None 1

Example 2:
>>> a, b = None, a
NameError: name 'e' is not defined

>>> a = 1
>>> b = a
>>> print(a, b)
1 1

conclusion: The UNPACK operation is different from variable reference.

"""


class SinglyLinkedListNode:
    """The unit of singly linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Singly linked list."""
    
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def insert_head(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
    
    def insert_tail(self, data):
        if self.head:
            new_node = SinglyLinkedListNode(data)
            temp_node = self.head
            while temp_node:
                temp_node = temp_node.next
            temp_node.next = new_node
    
    def delete_head(self):
        temp_node = self.head
        if self.head:
            self.head = self.head.next
            temp_node.next = None
        return temp_node
    
    def delete_tail(self):
        current_node = self.head
        if self.head:
            if self.head.next:
                while current_node.next.next:
                    current_node = current_node.next
                
                current_node.next, current_node = None, current_node.next
            else:
                self.head = None
        return current_node
    
    def reverse(self):
        previous_node = None
        current_node = self.head
        
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            
            previous_node = current_node
            current_node = next_node
            
        self.head = previous_node


class DoubleLinkedListNode:
    """The unit of double linked list."""
    
    def __init__(self, data):
        self.previous_node = None
        self.next_node = None
        self.data = data


class DoubleLinkedList:
    """double linked list."""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self, data):
        pass
    
    def insert_tail(self, data):
        pass
    
    def delete_head(self, data):
        pass
    
    def delete_tail(self, data):
        pass

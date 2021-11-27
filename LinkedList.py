from Validation import *
from random import randint

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next_node != None:
                s += str(p.data) + " "
                p = p.next_node
            s += str(p.data) + " "
        return s

    def add_front(self, data=None):
        if data is None:
            data = is_integer(input())
        data = is_integer(data)
        new_node = Node(is_integer(data))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.next_node = self.head
            new_node.next_node.prev_node = new_node
            self.head = new_node
            self.size += 1

    def add_back(self, data=None):
        if data is None:
            data = is_integer(input())
        data = is_integer(data)
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.prev_node = self.tail
            new_node.prev_node.next_node = new_node
            self.tail = new_node
            self.size += 1

    def generate_front(self, a, b):
        a = is_integer(a, 'Value A of range [A,B] must be integer number. Enter again:')
        b = is_integer(b, 'Value B of range [A,B] must be integer number. Enter again:')
        if a <= b:
            self.add_front(randint(a, b))
        else:
            self.add_front(randint(b, a))


    def generate_back(self, a, b):
        a = is_integer(a, 'Value A of range [A,B] must be integer number. Enter again:')
        b = is_integer(b, 'Value B of range [A,B] must be integer number. Enter again:')
        if a <= b:
            self.add_back(randint(a, b))
        else:
            self.add_back(randint(b, a))


    def insert(self, data, position):
        data = is_integer(data)
        position = is_positive_int(position, 'Value k of position must be positive integer number. Enter again:')
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            if position == 1:
                self.add_front(data)
            elif position > 1 and position <= self.size:
                new_node.prev_node = self.head
                chain = new_node.prev_node
                for k in range(1, self.size):
                    if k+1 < position:
                        chain = chain.next_node
                        continue
                    new_node.prev_node = chain
                    chain.next_node.prev_node = new_node
                    new_node.next_node = chain.next_node
                    chain.next_node = new_node
                    self.size += 1
                    break
            elif position > self.size:
                self.add_back(data)

    def remove(self, position):
        position = is_positive_int(position, 'Value k of position must be positive integer number. Enter again:')
        if self.head is None:
            print('List is empty. Nothing to remove.')
        elif position == 1 and self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        elif position > self.size:
            print('There is no an element in a list with such position.')
        elif position == self.size:
            self.tail.prev_node.next_node = None
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            self.size -= 1
        elif position == 1 and self.size > 1:
            self.head = self.head.next_node
            self.head.prev_node.next_node = None
            self.head.prev_node = None
        else:
            chain1 = self.head
            for k in range(position-1):
                chain1 = chain1.next_node
            chain2 = chain1.next_node
            chain2.prev_node = chain1.prev_node
            chain1.prev_node.next_node = chain2
            self.size -= 1

    def product(self):
        lastPositive = -1
        chain = self.head
        for i in range(self.size-1):
            if chain.data > 0:
                lastPositive = i+1
            chain = chain.next_node
            if i == self.size-2:
                if chain.data > 0:
                    lastPositive = i+2
        if lastPositive >= 0:
            product = 1
            chain = self.head
            for i in range(lastPositive):
                product *= chain.data
                chain = chain.next_node
            return product
        else:
            return 'There is no positive integer in array.'



from operator import mul
from time import time
from typing import Optional


class Node:
    def __init__(
        self, value: int, quantity: int, next: Optional["Node"], back: Optional["Node"]
    ):
        self.value = value
        self.quantity = quantity
        self.next = next
        self.back = back


class DoubleLinkedList:
    def __init__(self, head: Optional[Node], tail: Optional[Node]):
        self.head = head
        self.tail = tail

    def push(self, node: Node):
        if self.tail is None and self.head is None:
            self.tail = node
            self.head = node
        if self.head == self.tail:
            if self.head:
                self.head.next = node
                node.back = self.head
                self.tail = node
        else:
            if self.tail is not None:
                self.tail.next = node
            node.back = self.tail
            self.tail = node

    def pop_head(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            self.tail = None
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.back = None
        return temp

    def pop_tail(self):
        if self.tail is None:
            return None
        if self.head == self.tail:
            self.head = None
        temp = self.tail
        self.tail = self.tail.back
        if self.tail is not None:
            self.tail.next = None
        return temp

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head


def parte1():
    begin = time()
    with open(r"9\teste.txt", "r") as file:
        line = file.read()
    numbers = DoubleLinkedList(None, None)
    spaces = DoubleLinkedList(None, None)

    z = 0
    for i in range(len(line)):
        if i % 2 == 0:
            numbers.push(Node(z, int(line[i]), None, None))
            z += 1
        else:
            spaces.push(Node(0, int(line[i]), None, None))
    result = []
    while 1:
        node = numbers.pop_head()
        if node is None:
            break
        result.extend([node.value for _ in range(node.quantity)])
        node = numbers.get_tail()
        space = spaces.get_head()
        if space is None:
            continue
        while 1:
            if node is None:
                break
            diff = space.quantity - node.quantity
            if diff > 0:
                space.quantity -= node.quantity
                result.extend([node.value for _ in range(node.quantity)])
                numbers.pop_tail()
                node = numbers.get_tail()
            elif diff == 0:
                result.extend([node.value for _ in range(node.quantity)])
                numbers.pop_tail()
                spaces.pop_head()
                break
            else:
                node.quantity -= space.quantity
                result.extend([node.value for _ in range(space.quantity)])
                spaces.pop_head()
                break
    soma = sum(map(mul, result, range(len(result))))
    print(soma)
    print(time() - begin)


def parte2():
    begin = time()
    with open(r"9\input.txt", "r") as file:
        line = file.read()
    numbers = []
    spaces = []
    result = []

    z = 0
    for i in range(len(line)):
        if i % 2 == 0:
            numbers.append((z, int(line[i]), len(result)))
            result.extend([z for _ in range(int(line[i]))])
            z += 1
        else:
            spaces.append([0, int(line[i]), len(result)])
            result.extend([0 for _ in range(int(line[i]))])

    for number in reversed(numbers):
        for i in range(len(spaces)):
            space = spaces[i]

            if space[2] >= number[2]:
                break
            if space[1] > number[1]:
                space[1] -= number[1]

                for z in range(number[1]):
                    result[space[2] + z] = number[0]
                    result[number[2] + z] = 0
                space[2] += number[1]

                spaces[i] = space
                break
            elif space[1] == number[1]:
                del spaces[i]
                for i in range(number[1]):
                    result[space[2] + i] = number[0]
                    result[number[2] + i] = 0
                break
    soma = sum(map(mul, result, range(len(result))))
    print(soma)
    print(time() - begin)


parte2()

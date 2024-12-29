from time import time
from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional["Node"], back: Optional["Node"]):
        self.value = value
        self.next = next
        self.back = back


class DoubleLinkedList:
    def __init__(self, head: Optional[Node] = None, tail: Optional[Node] = None):
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

    def __len__(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count


def parte1():
    begin = time()
    with open(r"11\input.txt", "r") as file:
        line = file.readline().strip()
    linked = DoubleLinkedList()
    for i in line.split():
        linked.push(Node(int(i), None, None))
    n = 25
    for _ in range(n):
        node = linked.get_head()
        while node:
            if node.value == 0:
                node.value = 1
                node = node.next
            elif len(str(node.value)) % 2 == 0:
                temp = node.next
                value_str = str(node.value)
                len_str = int(len(value_str) / 2)
                node.value = int(value_str[:len_str])
                new_node = Node(int(value_str[len_str:]), temp, node)
                node.next = new_node
                if temp is not None:
                    temp.back = new_node
                node = temp
            else:
                node.value *= 2024
                node = node.next
    print(len(linked))
    print((time() - begin) * 1000)


def parte2():
    begin = time()
    with open(r"11\input.txt", "r") as file:
        line = file.readline().strip()
    dic: dict[int, int] = {}
    for i in line.split():
        dic[int(i)] = dic.get(int(i), 0) + 1
    n = 75
    for _ in range(n):
        new_dic = {}

        for num, qtd in dic.items():
            if num == 0:
                new_dic[1] = new_dic.get(1, 0) + qtd
            elif len(str(num)) % 2 == 0:
                value_str = str(num)
                len_str = int(len(value_str) / 2)
                new_dic[int(value_str[:len_str])] = (
                    new_dic.get(int(value_str[:len_str]), 0) + qtd
                )
                new_dic[int(value_str[len_str:])] = (
                    new_dic.get(int(value_str[len_str:]), 0) + qtd
                )
            else:
                new_dic[num * 2024] = new_dic.get(num * 2024, 0) + qtd
        dic = new_dic
    print(sum(dic.values()))
    print((time() - begin) * 1000)


parte2()

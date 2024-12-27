from operator import mul
from time import time
from typing import Optional


def trailheads(i: int, j: int, number: int, lines: list[str]):
    total: set[str] = set()

    if number == 9:
        total.add(f"{i},{j}")
        return total

    if i - 1 >= 0:
        if int(lines[i - 1][j]) == number + 1:
            total.update(trailheads(i - 1, j, number + 1, lines))
    if len(lines) > i + 1:
        if int(lines[i + 1][j]) == number + 1:
            total.update(trailheads(i + 1, j, number + 1, lines))
    if j - 1 >= 0:
        if int(lines[i][j - 1]) == number + 1:
            total.update(trailheads(i, j - 1, number + 1, lines))
    if len(lines[i]) > j + 1:
        if int(lines[i][j + 1]) == number + 1:
            total.update(trailheads(i, j + 1, number + 1, lines))
    return total


def trailheads2(i: int, j: int, number: int, lines: list[str]):
    if number == 9:
        return 1
    total = 0

    if i - 1 >= 0:
        if int(lines[i - 1][j]) == number + 1:
            total += trailheads2(i - 1, j, number + 1, lines)
    if len(lines) > i + 1:
        if int(lines[i + 1][j]) == number + 1:
            total += trailheads2(i + 1, j, number + 1, lines)
    if j - 1 >= 0:
        if int(lines[i][j - 1]) == number + 1:
            total += trailheads2(i, j - 1, number + 1, lines)
    if len(lines[i]) > j + 1:
        if int(lines[i][j + 1]) == number + 1:
            total += trailheads2(i, j + 1, number + 1, lines)
    return total


def parte1():
    begin = time()
    with open(r"10\input.txt", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    soma = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "0":
                soma += len(trailheads(i, j, 0, lines))
    print(soma)
    print((time() - begin) * 1000)


def parte2():
    begin = time()
    with open(r"10\input.txt", "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    soma = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "0":
                soma += trailheads2(i, j, 0, lines)
    print(soma)
    print((time() - begin) * 1000)


parte1()

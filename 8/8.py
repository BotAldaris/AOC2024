from collections import namedtuple
from time import time


def replace_char_at_index(s, index, new_char):
    if index < 0 or index >= len(s):
        raise ValueError("Índice fora do intervalo da string.")
    # Cria uma nova string com o caractere substituído
    return s[:index] + new_char + s[index + 1 :]


class Vec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        raise "Type is not possible to +"

    def __iadd__(self, other):
        if isinstance(other, Vec2):
            self.x += other.x
            self.y += other.y
            return self
        raise "Type is not possible to +"

    def __sub__(self, other: "Vec2"):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        raise "Type is not possible to -"

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        raise "Type is not possible to *"

    def __str__(self):
        return f"({self.x},{self.y})"

    def inbound(self, x_len: int, y_len: int):
        return 0 <= self.x < x_len and 0 <= self.y < y_len

    def invert(self):
        return Vec2(self.x * -1, self.y * -1)


def generate_antiantenna(vec: Vec2, add: Vec2):
    result = vec + add
    while 1:
        yield result
        result += add


def antiantenna_positions(vec1: Vec2, vec2: Vec2):
    diff = vec1 - vec2
    sig_diff = Vec2(1, 1)
    return [
        generate_antiantenna(vec1, diff * sig_diff),
        generate_antiantenna(vec2, diff * sig_diff.invert()),
        generate_antiantenna(vec1, diff * sig_diff.invert()),
        generate_antiantenna(vec2, diff * sig_diff),
    ]


def parte1():
    with open(r"8\input.txt", "r") as file:
        lines = file.readlines()
    # lines_2 = lines.copy()
    begin = time()
    antennas: dict[str, list[Vec2]] = dict()
    positions: set[str] = set()
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 1):
            char = lines[i][j]
            if char != ".":
                ann = Vec2(i, j)
                atte = antennas.get(char, [])
                for antenna in atte:
                    anti_antennas = antiantenna_positions(ann, antenna)
                    for gen in anti_antennas:
                        while 1:
                            anti_antenna = next(gen)
                            if anti_antenna.inbound(len(lines), len(lines[0]) - 1):
                                # lines_2[anti_antenna.x] = replace_char_at_index(
                                #     lines_2[anti_antenna.x], anti_antenna.y, "#"
                                # )
                                positions.add(str(anti_antenna))
                            else:
                                break
                atte.append(ann)
                antennas[char] = atte
    # with open("result.txt", "w") as file:
    #     file.writelines(lines_2)
    print(time() - begin)
    print(len(positions))


parte1()

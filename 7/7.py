from enum import Enum
from time import time


class Operators(Enum):
    ADD = 1
    MUL = 2
    CON = 3


def calcular(numbers: list[int], result: int, add: Operators) -> bool:
    if len(numbers) == 1:
        return numbers[0] == result
    if numbers[0] > result:
        return False
    if len(numbers) == 2:
        match add:
            case Operators.ADD:
                return numbers[0] + numbers[1] == result
            case Operators.MUL:
                return numbers[0] * numbers[1] == result
            case Operators.CON:
                return int(f"{numbers[0]}{numbers[1]}") == result
    match add:
        case Operators.ADD:
            new_numbers = [numbers[0] + numbers[1], *numbers[2:]]
            return (
                calcular(new_numbers, result, Operators.ADD)
                or calcular(new_numbers, result, Operators.MUL)
                or calcular(new_numbers, result, Operators.CON)
            )
        case Operators.MUL:
            new_numbers = [numbers[0] * numbers[1], *numbers[2:]]
            return (
                calcular(new_numbers, result, Operators.ADD)
                or calcular(new_numbers, result, Operators.MUL)
                or calcular(new_numbers, result, Operators.CON)
            )
        case Operators.CON:
            new_numbers = [int(f"{numbers[0]}{numbers[1]}"), *numbers[2:]]
            return (
                calcular(new_numbers, result, Operators.ADD)
                or calcular(new_numbers, result, Operators.MUL)
                or calcular(new_numbers, result, Operators.CON)
            )
    return False


def parte1():
    with open(r"7\input.txt", "r") as file:
        lines = file.readlines()
    soma = 0
    begin = time()
    for line in lines:
        line_splited = line.split(":")
        result = int(line_splited[0])
        numbers = list(map(int, line_splited[1].strip().split()))
        if (
            calcular(numbers, result, Operators.ADD)
            or calcular(numbers, result, Operators.MUL)
            or calcular(numbers, result, Operators.CON)
        ):
            soma += result
    print(time() - begin)
    print(soma)


parte1()

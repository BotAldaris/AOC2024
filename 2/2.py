def is_report_safe(report: str, loss: bool = False) -> int:
    increment = None
    numeros = [int(i) for i in report.split()]
    UPPER_BOUND = 4
    for i in range(len(numeros) - 1):
        match increment:
            case True:
                if numeros[i] < numeros[i + 1] < numeros[i] + UPPER_BOUND:
                    pass
                else:
                    return remove_try_again(numeros, loss, i)

            case False:
                if numeros[i] - UPPER_BOUND < numeros[i + 1] < numeros[i]:
                    pass
                else:
                    return remove_try_again(numeros, loss, i)

            case _:
                if numeros[i] < numeros[i + 1] < numeros[i] + UPPER_BOUND:
                    increment = True
                elif numeros[i] - UPPER_BOUND < numeros[i + 1] < numeros[i]:
                    increment = False
                else:
                    return remove_try_again(numeros, loss, i)

    return 1


def remove_try_again(
    numeros: list[int], loss: bool,  index: int
) -> int:
    if loss:
        return 0
    numeros2 = [i for i in numeros]
    numeros3 = [i for i in numeros]
    numeros.pop(index + 1)
    numeros2.pop(index)
    numeros3.pop(index - 1)
    return (
        is_report_safe(" ".join([str(z) for z in numeros2]), True, None)
        or is_report_safe(" ".join([str(z) for z in numeros]), True, None)
        or is_report_safe(" ".join([str(z) for z in numeros3]), True, None)
    )


if __name__ == "__main__":
    # Parte 2
    with open(r"2\2.txt", mode="r") as file:
        lines = file.readlines()

    resultado = [is_report_safe(line) for line in lines]
    # print(resultado)
    print(sum(resultado))

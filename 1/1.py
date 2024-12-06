def parte1():
    with open(r"1\1.txt", mode="r") as file:
        linhas = file.readlines()
    coluna_1 = []
    coluna_2 = []
    for linha in linhas:
        linhas_separadas = linha.split()
        coluna_1.append(int(linhas_separadas[0]))
        coluna_2.append(int(linhas_separadas[-1]))
    coluna_1.sort()
    coluna_2.sort()
    diferenca_entre_colunas = [
        abs(coluna_1[i] - coluna_2[i]) for i in range(len(coluna_1))
    ]
    print(sum(diferenca_entre_colunas))


def parte2():
    with open(r"1\1.txt", mode="r") as file:
        linhas = file.readlines()
    coluna_1 = []
    coluna_2 = []
    for linha in linhas:
        linhas_separadas = linha.split()
        coluna_1.append(int(linhas_separadas[0]))
        coluna_2.append(int(linhas_separadas[-1]))
    coluna_1.sort()
    coluna_2.sort()
    diferenca_entre_colunas = [
        abs(coluna_1[i] - coluna_2[i]) for i in range(len(coluna_1))
    ]
    print(sum(diferenca_entre_colunas))
    # Parte 2
    coluna_2_dict = {}
    for i in coluna_2:
        coluna_2_dict[i] = coluna_2_dict.get(i, 0) + 1

    print(sum([i * coluna_2_dict.get(i, 0) for i in coluna_1]))


if __name__ == "__main__":
    parte1()
    parte2()

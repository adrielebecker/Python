linha = int(input())
coluna = int(input())
tabuleiro = list()
for cont in range(0, linha):
    tabuleiro.append(linha)
    for cont in range(0, coluna):
        tabuleiro.append(coluna)
        print(tabuleiro)
    
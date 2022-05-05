def comparacao(termo1, termo2):
    for i, string in ((1, False), (2, False), (3, False), (0, True)):
        if string:
            menor_len = min([len(termo1[i]), len(termo2[i])])
            for k in range(menor_len):
                if termo1[i][k] > termo2[i][k]:
                    return 2
                elif termo1[i][k] < termo2[i][k]:
                    return 1
        else:
            if termo1[i] > termo2[i]:
                return 1
            elif termo1[i] < termo2[i]:
                return 2


def merge_sort(sequencia):
    tam = len(sequencia)
    if tam == 1:
        return sequencia
    meio = tam // 2
    parte1 = merge_sort(sequencia[:meio])
    parte2 = merge_sort(sequencia[meio:])
    final = []
    i, j = 0, 0
    while True:
        if i < len(parte1) and j < len(parte2):
            if comparacao(parte1[i], parte2[j]) == 1:
                final.append(parte1[i])
                i += 1
            else:
                final.append(parte2[j])
                j += 1
        elif i < len(parte1) and j == len(parte2):
            final.append(parte1[i])
            i += 1
        elif i == len(parte1) and j < len(parte2):
            final.append(parte2[j])
            j += 1
        else:
            break
    return final


qt_paises = int(input())

lista_paises = []
for _ in range(qt_paises):
    nome, ouros, pratas, bronzes = input().split()
    lista_paises.append((nome, int(ouros), int(pratas), int(bronzes)))
for pais in merge_sort(lista_paises):
    print(*pais)

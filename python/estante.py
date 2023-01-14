# from multiprocessing.reduction import duplicate


# N, R, K = [int(i) for i in input().split()]
# cont1 = 0 
# cont2 = 0
# if R == 0:
#     print(N)
# else:
#     for i in range(0, R):
#         v1 = [int(i) for i in input().split()]
#         for i in v1:
#             if v:
#                 cont1 = cont1 + 1
#             else:
#                 cont2 = cont2 +1
         
#     livros = (cont1 + cont2)

#     print(livros)
    
#     c = Counter(lista)

# for numero, repeticoes in c.items():
#     if repeticoes > 1:
#         result = [indice for indice, item in enumerate(lista) if item == numero]
#         print(f'O número "{numero}" se repete nos índices {result}.')

# N, R, K = [int(i) for i in input().split()]
# cont1 = 0 
# cont2 = 0
# if R == 0:
#     print(N)
# else:
#     for i in range(0, R):
#         v1 = [int(i) for i in input().split()]
#         for item in v1:
#             if v1 != v1:
#                 cont1 = cont1 + 1
#             else:
#                 cont2 = cont2 + 1
#     livros = (cont1 + cont2)

#     print(livros)

# N, R, K = [int(i) for i in input().split()]
# cont = 0
# cont1 = 0
# if R == 0:
#     print(N)
# else:
#     for i in range(0, R):
#         matriz = [[int(j) for j in input().split()], [int(l) for l in input().split()]]
#         for linha in matriz:
#             if matriz == matriz:
#                 cont = cont + 1
#             else:
#                 cont1 = cont1 + 1
#     print(cont+cont1)

# N, R, K = [int(i) for i in input().split()]
# cont1 = 0 
# cont2 = 0
# if R == 0:
#     print(N)
# else:
#     for i in range(0, R):
#         v1, v2 = [int(j) for j in input().split()]
#         for i in v1, v2:
#             if i != v2 or i != v2:
#                 cont1 = cont1 + 1
#             else:
#                 cont2 = cont2 + 1
#     livros = (cont1 + cont2)
#     print(livros)
    
# from multiprocessing.reduction import duplicate
# from timeit import repeat
# from unicodedata import numeric


# N, R, K = [int(i) for i in input().split()]
# cont1 = 0 
# cont2 = 0
# if R == 0:
#     print(N)
# else:
#     for i in range(0, R):
#         v1, v2 = [int(j) for j in input().split()]
#         for i in v1, v2:
#             if duplicate(v1) in v1 or v2:
#                 cont1 = cont1 + 1
#             else:
#                 cont2 = cont2 + 1
#     livros = (cont1 + cont2)
#     print(livros)

livros = [int(i) for i in input().split()]

if livros[1] == 0:
    print(livros[0])
else:
    for i in range(0, livros[1]):
        genero = [int(j) for j in input().split()]
        for j in range(0, i):
            if genero == [i][j] or genero[0] == genero[1]:
                print(f"{genero[0]} igual a {genero[1]}")
            else:
                print(f"{genero[0]} diferente de {genero[1]}")






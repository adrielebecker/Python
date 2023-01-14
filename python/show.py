# amigos = int(input())
# filas = int(input())
# assentos = int(input())
#linha1 = [[int(input())],[int(input())],[int(input())]]
# print(linha1)
#valores = list(map(int, input('Digite todos os valores: ').split()))
#amigos, filas, assentos = int(input()).split(" ")
# cadeiras = [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# for i in range(5):
#   for j in range(5):
#     if cadeiras[i][j]==0 and cadeiras[i][j+1]==0 and cadeiras[i][j+2]==0: 
#         print(j)
cont = 0
amigos, filas, cadeiras = [int(i) for i in input().split()]
for i in range(0, filas):
  num = [int(cadeiras) for cadeiras in input().split()]
  for i in range(0, amigos):
    if num[i+1]==0:
      cont = cont + 1
print(num[i:]) 
  


# for filas in range(linha1):
#     for assentos in range(linha1):
#         ocupados = int(input()).split(" ")
#         if 0 in ocupados:
#             cont = cont + 1
#         else:
#             cont = 0
# print(cont)

lista = [1,2,3,4,5,6,7,8,9]
lista2 = [9, 10, 11, 7 , 13 , 14, 15 , 16, 17]
cont = 0
for i in range(len(lista)):
  for j in range(len(lista2)):
    if lista[i] == lista2[j]:
      cont = cont + 1

print(cont)

cadeiras = [[1,1,1,1,1],[0,1,0,0,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(len(cadeiras))
print(len(cadeiras[0]))
for i in range(len(cadeiras)):
  for j in range(len(cadeiras[0])):
    if cadeiras[i][j]==0 and cadeiras[i][j+1]==0 and cadeiras[i][j+2]==0:
      print("a")
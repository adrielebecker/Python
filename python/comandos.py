from unittest import result

for caractere in 'Matemática':
    print(caractere)
  
lista = [1, 2, 3, 4, 15]
for item in lista:
    print(item)

# le dois valores inteiros
val1, val2 = [int(i) for i in input().split()]

linha1 = [[int(input())],[int(input())],[int(input())]]
print(linha1)

cadeiras = [[1,1,1,1,1],[0,1,0,0,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
for i in range(5):
  for j in range(5):
    if cadeiras[i][j]==0 and cadeiras[i][j+1]==0 and cadeiras[i][j+2]==0: 
        print

lista = ['a', 'b', 'c', 'd',1]
print(lista[1:3])
#result = ['b', 'c']

x = list(map(int, input("Enter multiple values: ").split())) # inteiros
# x = list(input("Enter multiple values: ").split()) # string
print(x)
#result = Enter multiple values: a b c d e
#['a', 'b', 'c', 'd', 'e']

list(range(10))

lista = [1,2,3,4,5]
len(lista) #ver tamanho

frutas = ['Maça', 'Banana', 'Jaca', 'Melão', 'Abacaxi']
print(frutas[-2]) #result = melao

lista.append('Fulano') #add ao final da lista

lista.insert(1,'Fulano') #add posição especifica

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) #juntar listas

a = [0,2,4,6]
b = [1,3,5,5]
c = a + b
print(c) #justar as listas assim como ta
c.sort()
print(c) #juntar as listas em ordem crescente 
c.sort(reverse=True)
print(c) #juntar as listas em ordem decrescente

lista = ['Cristhian', 'Rodrigo', 'Fulano']
lista.pop()
print(lista) #remove o ultimo elemento 

lista = ['Cristhian', 'Virgulino','Rodrigo', 'Fulano']
del lista[1]
print(lista) #remove posição especifica

lista = ['Cristhian', 'Virgulino','Rodrigo', 'Fulano']
lista.remove('Virgulino')
print(lista) #remove com base no valor

lista = ["Rodrigo", "João", "José", "Luciana", "Cristhian"]

for item in lista:
    print(item)

notas = {
    'Português': 7, 
    'Matemática': 9, 
    'Lógica': 7, 
    'Algoritmo': 7
}
for chave, valor in notas.items():
    print(f"{chave}: {valor}")

matriz = [['Fulano', 'Beltrano'],['Cristhian','Rodrigo']]
print(matriz)

matriz = [['Fulano', 'Beltrano'],['Cristhian','Rodrigo']]
lista = ['Ciclano', 'Virgulino']
matriz.append(lista)
print(matriz) #add lista em matriz

matriz = [['Fulano', 'Beltrano'],['Cristhian','Rodrigo'], ['Ciclano', 'Virgulino']]

for linha in matriz:
  for coluna in linha:
    print(f"{coluna}", end=" ")
  print(" ")
print("Terminou matriz")

n = -1
while n < 0:
  n = int(input("Informe um valor positivo:"))
  if n < 0:
    print("Erro: n deve ser positivo")
print(n)

while True:
  n = int(input("Informe um valor entre 0 e 10:"))
  if n < 0 or n > 10:
    print("Erro: n deve ser entre 0 e 10")
  else:
    break
print(n)

a = []
while True:
  n = int(input("Informe um valor entre 0 e 1000:"))
  if n > 0 and n < 1000:
    a.append(n)
  elif n == 0:
    print("Sair")
    break
  else:
   print("Erro: n deve ser entre 0 e 1000")
print(a)
# Informe um valor entre 0 e 1000:999
# Informe um valor entre 0 e 1000:1001
# Erro: n deve ser entre 0 e 1000
# Informe um valor entre 0 e 1000:0
# Sair
# [999]


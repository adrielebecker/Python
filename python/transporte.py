max = int(input())
min = int(input())
import math

novoMax = max * 30 / 100 

if novoMax > min:
    print(math.floor(novoMax)) #remove casas decimais
else:
    print("0")
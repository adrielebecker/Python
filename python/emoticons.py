frase = input()

cont = 0 
if frase == "divertido" or frase == ":-)" : 
    cont = cont+1
if frase == "chateado" or frase ==":-(" :
    cont = cont-1
if cont > 0:
    print("divertido")
elif cont < 0: 
    print("chateado")
else: 
    print("neutro")


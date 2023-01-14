jogo1 = input()
jogo2 = input()
jogo3 = input()
jogo4 = input()
jogo5 = input()
jogo6 = input()

cont = 0 

if jogo1 == "V":
    cont = cont+1
    if jogo2 == "V":
        cont = cont+1
        if jogo3 == "V":
            cont = cont+1
            if jogo4 == "V":
                cont = cont+1
                if jogo5 == "V":
                    cont = cont+1
                    if jogo6 == "V":
                        cont = cont+1
if cont > 4 or cont == 6:
     print(1)
elif cont > 2 or cont == 4:
    print(2)
elif cont > 1 or cont == 2:
    print(3)
else:
    print(-1)
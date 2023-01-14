#mais da metade, 100 reais; outro pedaço nao vale nada; exatamente metade,
# nenhum dos dois tem valor; felix-esquerda

a =  int(input())
b = int(input())
if a > 50 and a > b:
    print(1)
    if a < 50 and a > b:
        print(0)
elif b > 50 and b > a:
    print(2)
    if b > 50 and b < a: 
        print(0)
else: 
    print (0)

var=10
nome=0
numero="Altro"

ottimo=[1, 2, 3, 4, 5]
esempio=("Uno", nome, var)
nome="Nome proprio"
print(esempio)
ottimo.append(1000)
print(esempio)
ottimo=100000
print(esempio)

exit(-1)

diz={"Nome":var, "Cognome":numero, "Ottimo":ottimo}

doz=[diz, 1 ,2, 3]

for i in range(7, 700, 7):
    print(i)

for i in range(9, 9999, 2):
    print(ottimo[i%len(ottimo)])

infine=[x for x in ottimo]
infine1=[yy for x in ottimo for y in range(y, 10y, 1)]
d = {'pippo':2, 'pluto': 1, 'topolino': 5} 
#d1 = {'pippo': 2/8, 'pluto': 1/8, 'topolino': 5/8}

somma = sum(list(d.values()))
d1 = {}
for k, v in d.items():
    d1[k] = v / somma
print(somma)

l = [1,2,3,4,5,2,2,6,3,7,16]
somme = {'sommaPari': 0, 'sommaDispari': 0}

for n in l:
    if n % 2 == 0:
        somme['sommaPari'] += n
    else:
        somme['sommaDispari'] += n
print(f'la somma dei numeri pari è ', somme['sommaPari'] )
print(f'la somma dei numeri dispari è ', somme['sommaDispari'] )
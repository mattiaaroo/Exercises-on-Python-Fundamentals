# cosa faremo oggi?
# un esempio di progetto segmentato

# sia data una lista <ls> contenente N digit da 1 a N
# non necessariamente tutti presenti quindi con
# eventuali ripetizioni
# [1, 2, 3, 4, 5, 6, 7, 8]
# N=8
# [1,1,2,2,3,5,8,8]

# N=5
# [1,3,5,1,5]

# sia data una seconda lista <lsCheck>, costruita esattamente
# come la precendente, ovviamente con valori diversi,
# ma sempre nel rispetto del valore N
import random


N = 6
ls = [1, 3, 2, 2, 5, 6]
lsCheck = [2, 3, 3, 6, 6, 4]

# Scrivere una funzione alla quale passerete
# come parametri ls e lsCheck e la funzione deve riportare
# due valori
# il primo: tutte le volte che c'è lo stesso digit
# nella stessa posizione di ls e lsCheck
# nel nostro esempio il primo valore tornato dalla funzione
# sarà 1. A questo punto per completare il calcolo, tolgo
# dalle due liste i valori che stanno nella stessa posizione
ls = [1, 3, 2, 2, 5, 6]
lsCheck = [2, 3, 3, 6, 6, 4]

ls = [1, 2, 2, 5, 6]
lsCheck = [2, 3, 6, 6, 4]
# il secondo: tutte le volte in cui un elemento della lista
# lsCheck è presente nella lista ls, ma non nella
# stessa posizione
# Nel nostro esempio la funzione torna:
# c'è il 2 nella ls?
# sì, lo tolgo
ls = [1, 2, 5, 3, 3]
lsCheck = [2, 3, 6, 6, 4]


ls = [
    1,
    4,
    1,
    4,
    1,
]
lsCheck = [5, 5, 5, 3, 6]


ls = [6, 6, 5, 1, 1]
lsCheck = [3, 4, 4, 1, 4]


# Genera una lista che contiene N numeri casuali tra 1 e N
def GeneraLista(N):
    lista = []
    for i in range(N):
        v = random.randint(1, N)
        lista.append(v)
    return lista


# Non più utilizzato
def ContaUguali(ls, lsCheck):
    uguali = 0
    for i in range(len(ls)):
        if ls[i] == lsCheck[i]:
            uguali = uguali + 1
    return uguali


def ContaUgualiInStessoEInAltro(ls, lsCheck):
    # Conteggio e elimino gli elementi nello stesso posto
    stessoPosto = 0
    for i in range(len(lsCheck)):
        if lsCheck[i] == ls[i]:
            stessoPosto += 1
            ls[i] = None
            lsCheck[i] = None

    # Conteggio e elimino gli elementi in posto differente
    altroPosto = 0
    for i in range(len(lsCheck)):
        if lsCheck[i] != None and lsCheck[i] in ls:
            altroPosto += 1
            ls.remove(lsCheck[i])
    return stessoPosto, altroPosto


N = 5
for i in range(4):
    l1 = GeneraLista(N)
    l2 = GeneraLista(N)
    print(l1)
    print(l2)
    stesso, diverso = ContaUgualiInStessoEInAltro(l1, l2)
    print(stesso, diverso)

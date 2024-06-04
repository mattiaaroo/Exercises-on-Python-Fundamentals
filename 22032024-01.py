import random

n=9

def generaLista(n):
    ls = []
    for a in range(n):
        numero = random.randint(1, n)
        ls.append(numero)
    return ls
ls = generaLista(n)
print("La lista(ls) generata è:", ls)


def contaUguali(ls, lsCheck):
    contatore = 0
    for i in range(len(ls)):
        if ls[i] == lsCheck[i]:
            contatore = contatore + 1
    return contatore
lsCheck = generaLista(n)
print("La seconda lista(lsCheck) generata è:", lsCheck)

numeriUguali = contaUguali(ls, lsCheck)
print("I numeri nella stessa posizione nelle due liste sono: ", numeriUguali)


# def correggiLista():
#     lsCorretta = []
#     for i in range(len(ls)):
#         if ls[i] != lsCheck[i]:
#             lsCorretta.append(ls[i])
#     return lsCorretta
# lsCorretta = correggiLista()
# print("La nuova lista corretta senza i numeri identici nella stessa posizione è: ", lsCorretta) 

def correggiLista():
    lsCorretta = []
    for i in range(len(ls)):
        if ls[i] != lsCheck[i]:
            lsCorretta.append(ls[i])
        else :
            return lsCorretta
    return lsCorretta()
lsCorretta = correggiLista()
print("La nuova lista corretta senza i numeri identici nella stessa posizione è: ", lsCorretta) 

stringa='91857'
def StringDigitsToList(sd):
    StringaToLista = []
    for carattere in stringa:
        StringaToLista.append(int(carattere))
    return StringaToLista
lista=StringDigitsToList(stringa)
print(lista)
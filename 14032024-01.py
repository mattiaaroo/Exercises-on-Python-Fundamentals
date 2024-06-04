# def GeneraListaDigit():
#    lista = []
#    for i in range(0,10000):
#        s=str(i)
#        s=s.zfill(4)
#        lista.append(s)
#    return lista 


# def GeneraListaDigit():
#    lista = []
#    for i in range(0,10000):
#        s=str(i)
#       s="0" * (4 - len(s)) + s
#       lista.append(s)
#    return lista


#Problema ho la stringa "123", la voglio trasformare in [1, 2, 3]
#definire una funzione che risolva il problema

# stringa='123'
# def StringaInLista():
#    StringaInLista = []
#    for numero in stringa:
#        StringaInLista.append(int(numero))
#    return StringaInLista 
#    return[int(numero) for numero in stringa]
# lista=StringaInLista()
# print(lista)

#################################################################

#fin = open("/home/studente302/Exercises-on-Python-Fundamentals/alice.txt", "r")
#linee = fin.readline()
#fin.close()


#l1 = []
#for l in linee:
#    l1.append(l.strip())
#    linee = l1
#print(linee)

#################################################################


#ls = ["uno","", "due", "tre", "", "", "", " ", "  ", "fine"]
#lnuova = []
#for i in ls:
#    if len(i) > 0:
#        lnuova.append(i)
#    
#print(lnuova)


#################################################################

fin = open("/home/studente302/Exercises-on-Python-Fundamentals/alice.txt", "r")
testo = fin.read()
fin.close()
contatoreCaratteri = 0
contatoreSpazi = 0
contatoreAlfanumerici = 0

for riga in testo:
        contatoreCaratteri += len(riga)       
        for c in riga:
            if c == ' ':
                contatoreSpazi += 1
            if c.isalnum():
                contatoreAlfanumerici += 1  

print(contatoreCaratteri, "sono i caratteri presenti")
print(contatoreSpazi, "sono gli spazi presenti")
print(contatoreAlfanumerici, "sono i caratteri alfanumerici presenti")
        




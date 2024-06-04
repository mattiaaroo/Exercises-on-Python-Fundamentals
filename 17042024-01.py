#Personal Message
nomePersona = "Eric"
print(f"Hello {nomePersona}, would you like to learn some Python today")

#Name Cases
upperCases = nomePersona.upper()
lowerCases = nomePersona.lower()
print(upperCases)
print(lowerCases)

#Famouse Quote 1 - 2
"Martin Luther King once said: I have a dream"
message = "I have a dream"
famousPerson = "Martin Luher King"
print (message + " once said "  + famousPerson)

#File Extension
fileName = "python_notes.txt"
fileNameCorretto = fileName.removesuffix(".txt")
print(fileNameCorretto)

#Names
names = ["Gianni", "Mario", "Flavio", "Andrea", "Matteo"]
amico1 = names[0]
amico2 = names[1]
amico3 = names[2]
amico4 = names[3]
amico5 = names[4]
listaAmici = [amico1, amico2, amico3, amico4, amico5] #questa lista è stata creata solo a scopo per un check
print (listaAmici)

#Greetings
for name in names:
    print ("Grazie mille per aver partecipato all'attività", name )

#Your own list
veicoli = ["an S2000", "an s13", "an honda civic", "a mitsubishi evo", "a mitsubishi lancer", "an harley davinson"]
for veicolo in veicoli:
    print("Surely", veicolo + "is in my dream garage")
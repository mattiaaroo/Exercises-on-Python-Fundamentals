# master mind
import random

def generaCodiceSegreto(m, n):
    return [random.randint(0, n) for _ in range(m)]

def controlloTentativo(tentativo, codicesegreto):
    correttiPostoGiusto = 0
    correttiPostoSbagliato = 0
    
    for i in range(len(codicesegreto)):
        if tentativo[i] == codicesegreto[i]:
            correttiPostoGiusto += 1
        elif tentativo[i] in codicesegreto:
            correttiPostoSbagliato += 1
            
    return correttiPostoGiusto, correttiPostoSbagliato

def master_mind(n, m):
    print("Indovina la codicesegreto di {} numeri compresi tra 0 e {}.".format(m, n))
    print("Buona fortuna!")
    
    master = generaCodiceSegreto(m, n)
    
    tentativi = 0
    while True:
        tentativi += 1
        print("\nTentativo #{}".format(tentativi))
        
        tentativo = input("Inserisci la tua tentativo ({} numeri separati da spazi): ".format(m))
        tentativo = [int(x) for x in tentativo.split()]
        
        if len(tentativo) != m or not all(1 <= x <= n for x in tentativo):
            print("Inserimento non valido. Assicurati di inserire {} numeri compresi tra 0 e {}.".format(m, n))
            continue
        
        correttiPostoGiusto, correttiPostoSbagliato = controlloTentativo(tentativo, master)
        
        if correttiPostoGiusto == m:
            print("Complimenti! Hai indovinato la codicesegreto: {}".format(master))
            break
        else:
            print("Proposta:", tentativo)
            print("Corretti al posto giusto:", correttiPostoGiusto)
            print("Corretti al posto sbagliato:", correttiPostoSbagliato)

master_mind(9, 4)

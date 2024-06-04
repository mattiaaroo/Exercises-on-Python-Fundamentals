import random
def ColoreCasuale():
    colore=['rosso', 'blu', 'giallo', 'verde', 'ciano']
    return colore[random.randint(0, len(colore)-1)]
print(ColoreCasuale())
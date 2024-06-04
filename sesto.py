import random
import time


############################################################################
# Costruzione del Set

start = time.time_ns()
aSet = set ()
for v in range(1,10000000):
    aSet.add(random.randint(1, 1000))
end = time.time_ns()

print(f"Il tempo richiesto è : {(end-start)/10000000}")


start = time.time_ns()
found = 0
for v in range(1,10000000):
    if random.randint(1, 10000000) in aSet:
        found += 1
end = time.time_ns()

print( f"Il tempo richiesto è : {(end-start)/ 10000000} {found}" )

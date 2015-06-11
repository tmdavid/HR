__author__ = 'dtorrejon'

import math
'''
Sieve of Atkin test?
'''
#until = int(raw_input())

results = list()
results.append(2)
results.append(3)
results.append(5)

sieve = list()
'''
for i in range (len(until)): #false = nonprime
    sieve.append("false")

for x in range (1, until*until+1):
    for y in range (1, until*until+1):
        n  = 4*x**2+y**2
'''
def simplePrime(n):
    limit = int(math.sqrt(n)) + 1
    print limit
    for i in range (2,limit):
        if(n%i==0): return True
    return False
print simplePrime(17)



sieveera = [True]*1000

def sieveerathos(n,sieveera):
    limit = int(math.sqrt(n))+1
    for i in range (2, limit):
        if(sieveera[i] is True):
                for k in range (0,n):
                    if (i**2+k*i<n): sieveera[i**2+k*i] = False


    return sieveera
sieveera = sieveerathos(len(sieveera),sieveera)

for i in range(len(sieveera)):
    if (sieveera[i] is True): print i

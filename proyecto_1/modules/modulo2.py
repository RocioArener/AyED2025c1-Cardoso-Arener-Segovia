import time
import random

def quicksort(lista,izq,der):
    i,j=izq, der
    x=lista[(izq+der)//2]
    while i <=j:
        while lista[i]<x:
            i+=1
        while x < lista[j]:
            j-=1
        if i <=j:
            lista[i],lista[j]=lista[j],lista[i]
            i+=1
            j-=1
    if izq <j:
        quicksort(lista,izq,j)
    if i < der:
        quicksort(lista,i,der)

control=[]
numeros=[]
for i in range(500):   
    x=random.randint(10000,20000)
    numeros.append(x)
    control.append(x)
    
print(f"Lista original: {numeros}")
tiempo1=time.perf_counter()
control.sort()
quicksort(numeros, 0, len(numeros)-1)
tiempo2=time.perf_counter()
print("tiempo: ",tiempo2-tiempo1)
print(f"Lista ordenada: {numeros}")
assert control==numeros
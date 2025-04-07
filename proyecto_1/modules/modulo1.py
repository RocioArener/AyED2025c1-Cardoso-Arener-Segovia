import random
import time
def bubble_sort(lista):
    n=len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j]<lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista
control=[]
numeros=[]
for i in range(500):   
    x=random.randint(10000,20000)
    numeros.append(x)
    control.append(x)
    
print(f"Lista original: {numeros}")
tiempo1=time.perf_counter()
control.sort(reverse=True)
bubble_sort(numeros)
tiempo2=time.perf_counter()
print("tiempo: ",tiempo2-tiempo1)
print(f"Lista ordenada: {numeros}")
assert control==numeros


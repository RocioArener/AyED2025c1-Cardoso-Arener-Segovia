import random
def bubble_sort(lista):
    n=len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista

numeros=[]
for i in range(500):
    
    x=random.randint(10000,20000)
    numeros.append(x)
    
print(numeros)

bubble_sort(numeros)
print(f"ACA EMPIEZA: {numeros}")
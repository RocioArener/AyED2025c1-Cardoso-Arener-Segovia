
import random
import time
def radix_sort(lista):
    def counting_sort(lista,exp):
        contador=[0]*10
        salida=[0]*len(lista)
        
        for num in lista:
            indice=(num//exp)%10
            contador[indice]+=1
        
        for i in range(1,10):
            contador[i]+=contador[i-1]
            
        for i in range(len(lista)-1,-1,-1):
            indice=(lista[i]//exp)%10
            salida[contador[indice]-1]=lista[i]
            contador[indice]-=1

        for i in range(len(lista)):
            lista[i]=salida[i]
    max_val=max(lista)
    exp=1
    while max_val//exp>0:
        counting_sort(lista,exp)
        exp*=10
        
# control=[]
# numeros=[]

# for i in range(500):
#     x=random.randint(10000,20000)
#     numeros.append(x)
#     control.append(x)
# print(f"Lista original: {numeros[:10]}...")
# tiempo1=time.perf_counter()
# control.sort()
# radix_sort(numeros)
# tiempo2=time.perf_counter()
# print("tiempo radix sort",tiempo2-tiempo1)
# print(f"Lista ordenada: {numeros[:10]}...")
# assert control==numeros
    
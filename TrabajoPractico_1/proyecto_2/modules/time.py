import time
import matplotlib.pyplot as plt
from modulo1 import ListaDobleEnlazada

# Función para medir el tiempo de ejecución
def medir_tiempo(metodo, lista):
    inicio = time.time()
    metodo()
    fin = time.time()
    return fin - inicio

# Crear listas de diferentes tamaños
tamanios = [10, 100, 1000, 5000, 10000, 20000]
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for n in tamanios:
    lista = ListaDobleEnlazada()
    for i in range(n):
        lista.agregar_al_final(i)
    
    # Medir tiempo de len
    tiempos_len.append(medir_tiempo(lambda: len(lista), lista))
    
    # Medir tiempo de copiar
    tiempos_copiar.append(medir_tiempo(lista.copiar, lista))
    
    # Medir tiempo de invertir
    tiempos_invertir.append(medir_tiempo(lista.invertir, lista))

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(tamanios, tiempos_len, label="len (O(1))", marker='o')
plt.plot(tamanios, tiempos_copiar, label="copiar (O(N))", marker='o')
plt.plot(tamanios, tiempos_invertir, label="invertir (O(N))", marker='o')
plt.xlabel("Cantidad de elementos (N)")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("N vs Tiempo de ejecución")
plt.legend()
plt.grid()
plt.show()
from matplotlib import pyplot as plt
from random import randint
import time
from modules.modulo2 import quicksort
from modules.modulo1 import bubble_sort
from modules.graficar import graficar_tiempos

from modules.tiempos import medir_tiempos
tamanos = [1, 10, 100, 200, 500, 700, 1000]

tiempos=medir_tiempos(bubble_sort,tamanos)
grafica=graficar_tiempos(tiempos)
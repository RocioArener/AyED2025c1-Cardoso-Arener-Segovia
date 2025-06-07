# Proyecto 3: Palomas mensajeras

Este código utiliza como estructura principal un grafo y como estructura auxiliar un montículo binario. La primera estructura permite almacenar la información de manera eficiente, representando los pueblos como nodos (vértices) y las distancias entre ellos como aristas ponderadas; por otro lado, la segunda estructura actúa como cola de prioridad y proporciona una forma de almacenar temporalmente los pueblos que todavía no han sido visitados; guía la selección del siguiente nodo a visitar, asegurando que siempre se elija opción más cercana según el  algoritmo implementado, en este caso, prim.
El código  tiene  como objetivo encontrar la forma más eficiente de recorrer dicho grafo, pasando por cada nodo sólo una vez; mostrando como resultado el recorrido por cada pueblo y la suma total de las ponderaciones, es decir la distancia que recorrerán las palomas para hacer llegar el mensaje a cada pueblo.


---
## 🏗Arquitectura General

El codigo consta de un modulo principal, PalomasWilliam que utiliza cola_de_prioridad para su correcto funcionamiento.

---
## 📑Dependencias

1. **Sys**

---
## 🚀Cómo Ejecutar el Proyecto
1. **Clonar o descargar** el repositorio.

2. **Crear y activar** un entorno virtual.

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` se encuentran en la carpeta [deps](./deps) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Arener Rocio
- Cardoso Josefina Belen
- Segovia Lucas

---

> **Consejo**: Mantén el README **actualizado** conforme evoluciona el proyecto, y elimina (o añade) secciones según necesites. Esta plantilla es sólo un punto de partida general.

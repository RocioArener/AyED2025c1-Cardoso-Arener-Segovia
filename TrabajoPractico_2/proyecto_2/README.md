# Proyecto 2: Temperaturas_DB 

La estructura interna utilizada en este proyecto es un árbol AVL, este permite almacenar la información de la base de datos proporcionada de forma ordenada y de fácil acceso para la aplicación principal. Para corroborar el correcto funcionamiento de las estructuras se implementan tests correspondientes a cada una.
El objetivo principal del código es almacenar la información que el usuario proporcione, que permita su fácil acceso y modificación; el resultado es una aplicación principal que permite al usuario utilizar funciones relacionadas a la modificación u obtención de información de la base de datos, en este caso la base de datos está compuesta por temperaturas y la forma de acceso a estas es su fecha de registro.

## 🏗Arquitectura General

Explica brevemente cómo está organizado el código:
El codigo costa de un modulo principal llamado abb, que contiene las clases abb(que es un arbol de busqueda balanceado) y nodo arbol. Una aplicacion principal que contiene la clase temperaturas_DB donde las funciones que utiliza el usuario para acceder a la base de datos

El informe completo está disponible en el repositorio.

---
## 📑Dependencias

1. **Datatime**
2. **Numpy**
3. **Unitest**

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

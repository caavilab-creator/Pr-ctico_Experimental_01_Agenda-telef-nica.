# 📞 Agenda Telefónica - Estructura de Datos

## 🎓 Proyecto Académico
**Universidad:** Universidad Estatal Amazónica (UEA)  
**Asignatura:** Estructura de Datos  
**Código:** 2626-UEA-L-UFB-032-C    
**Unidad:** I - Tipos de Datos  
**Período:** 2026-2026  
**Práctica:** Guía de Prácticas #01  

---

## 📋 Descripción

Este proyecto es una aplicación de Agenda Telefónica desarrollada en Python como parte de la asignatura de Estructura de Datos. Aplica los principios de Programación Orientada a Objetos (POO) y utiliza estructuras de datos específicas (vectores, matrices y registros/clases) para gestionar la información de contactos. El sistema permite registrar, listar, buscar y registrar interacciones con los contactos, demostrando la aplicación práctica de los conceptos teóricos vistos en clase.
---

## ✨ Funcionalidades

El sistema implementa las operaciones básicas de reportería y gestión de datos requeridas:

Agregar contacto: Permite registrar un nuevo contacto con sus datos (nombre, teléfono, email, dirección) e inicializa su fila en la matriz de interacciones.

Listar todos los contactos: Muestra en consola la colección completa de contactos almacenados en el vector.

Buscar por nombre: Filtra y muestra los contactos que coincidan total o parcialmente con el nombre ingresado.

Buscar por teléfono: Filtra y muestra los contactos que coincidan con el número de teléfono proporcionado.

Eliminar contacto: Permite remover un contacto del vector y su respectiva fila en la matriz utilizando su teléfono como identificador.

Registrar interacción (Matriz): Permite actualizar la matriz bidimensional registrando una llamada, mensaje o email para un contacto específico.

Ver estadísticas (Matriz): Muestra el recorrido completo de la matriz de interacciones, presentando las estadísticas de comunicación de cada contacto en formato tabular.

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue el patrón **Modelo-Servicio-Interfaz **:

---
<img width="222" height="285" alt="image" src="https://github.com/user-attachments/assets/3027188c-1133-495d-906e-559ae890adf0" />

---

---

## 📦 Estructuras de Datos Utilizadas

Para el desarrollo de la Agenda Telefónica se implementaron tres estructuras de datos.

1. Registro/Clase (Contacto)

Concepto: Estructura que agrupa datos heterogéneos bajo una misma entidad.

Implementación: Clase Contacto con atributos tipados (nombre, telefono, email, direccion) y métodos getter/setter.

Relación con la clase: Equivalente al ejemplo del Estudiante visto en la Semana 3, donde se encapsulan atributos relacionados.

2. Vector/Array (list en Python)

Concepto: Colección de elementos del mismo tipo almacenados en posiciones contiguas de memoria.

Implementación: self.contactos = [] en la clase Agenda, almacena la colección de objetos Contacto.

Operaciones aplicadas: Agregar (append), eliminar (pop), iteración con for, búsqueda secuencial.

Equivalencia: Corresponde al int[] numeros = new int[5]; enseñado en clase.

3. Matriz/Array Bidimensional (list of lists en Python)

Concepto: Array de arrays que forma una estructura bidimensional para representar datos en forma de tabla.

Implementación: self.matriz_interacciones = [[0, 0, 0], ...] donde cada fila representa un contacto y las columnas almacenan [Llamadas, Mensajes, Emails].

Operaciones aplicadas: Acceso por índices matriz[i][j], recorrido con bucles anidados for i / for j.

Equivalencia: Corresponde al int[,] matriz = new int[3, 3]; enseñado en la Semana 3.


---

## ️ Tecnologías

Lenguaje de programación: Python 3.x

Paradigma: Programación Orientada a Objetos (POO)

Interfaz de usuario: Consola 

Control de versiones: Git

Repositorio remoto: GitHub

Entorno de desarrollo: Visual Studio Code

---

## 🚀 Ejecución

Al ejecutar el programa, verás el menú principal:

<img width="318" height="324" alt="image" src="https://github.com/user-attachments/assets/a14dce49-85df-4dcc-8762-f5630e74f52e" />


Agregar contacto:

<img width="261" height="139" alt="image" src="https://github.com/user-attachments/assets/d95ec464-1120-4380-9001-5b3f0dcc5313" />


Interaccion:

<img width="510" height="189" alt="image" src="https://github.com/user-attachments/assets/8a4c5174-c75f-4a1b-bfcf-992409f509f4" />



------------
🤖 Agente de IA Utilizado

Agente: Qwen3.7 

Porcentaje de código asistido: 50%

Descripción: Se utilizó para generar la estructura base del proyecto, implementación de clases y métodos principales. El 50% restante fue código personalizado para adaptación de requerimientos y pruebas.

# Ciclo de Vida del Desarrollo de Software (SDLC)

*Estudiante:* Lizandro Martinez  
*Matricula:* 2630116  

---

## Resumen Ejecutivo (Segun Yo)

Este documento tratara de explicar de la mejor manera que sea posible sobre que es el **Ciclo de Vida del Desarrollo de Software (SDLC (por sus siglas en ingles))** y el por que es una herramienta clave para la ingenieria cuando de software se trata; en terminos mas sencillos, el SDLC es el conjunto de pasos ordenados para que un equipo pueda usarlo para planificar, construir, probar y mantener un sistema de software sin perder el control del tiempo ni del presupuesto.

A lo largo de mi archivo se detallan las 7 fases principales del desarrollo (desde su idea inicial hasta el mantenimiento), donde se explican sus objetivos, las tareas que tiene cada etapa, los entregables que se producen y los riesgos mas comunes a los que nos podemos enfrentar como desarrolladores; al final tambien inclui unas conclusiones sobre su impacto en proyectos reales y las referencias bibliograficas que utilice.

---

---

## Fases del SDLC

### Planificacion (Planning)
* **Objetivo:** Se encarga de definir la idea inicial, ver si el proyecto es viable y de organizar los recursos.
* **Actividades Tipicas:** Se encarga de evaluar costos, analizar riesgos, definir el alcance y armar el calendario de trabajo.
* **Entregables:** Es el plan de trabajo, estudio de viabilidad y la matriz de riesgos.
* **Riesgos comunes:** Tiempos irrealistas y la falta de acuerdo con los clientes.

### Analisis de Requisitos (Requirements/Analysis)
* **Objetivo:** Entender y anotar todo lo que el sistema debe hacer segun el usuario.
* **Actividades Tipicas:** Entrevistar usuarios, reunir requerimientos funcionales y escribir historias de usuario.
* **Entregables:** Documento de Requisitos del Software (SRS) e historias de usuario.
* **Riesgos comunes:** Requisitos confusos, malentendidos y cambios constantes de alcance (Scope Creep).

### Diseño (Design)
* **Objetivo:** Definir la estructura tecnica y visual del software antes de programar.
* **Actividades Tipicas:** Diseñar la arquitectura, definir la base de datos y bocetear las pantallas (UI/UX).
* **Entregables:** Diagramas de arquitectura, modelos de base de datos y bocetos de interfaz.
* **Riesgos comunes:** Diseños dificiles de escalar o se puede complicar innecesariamente la estructura.

### Implementación (Implementation)
* **Objetivo:** Escribir el codigo fuente para construir la aplicacion.
* **Actividades Tipicas:** Programar los modulos, revisar codigo con el equipo y hacer pruebas unitarias basicas.
* **Entregables:** Codigo fuente ya compilado, ejecutables y pruebas unitarias.
* **Riesgos comunes:** Desorganizacion en el codigo, retrasos y falta de estandares al programar.

### Pruebas (Testing)
* **Objetivo:** Es encontrar errores y asegurar que el programa funcione como se esperaba.
* **Actividades Tipicas:** Probar la integracion de modulos, verificar la seguridad y realizar pruebas con usuarios reales.
* **Entregables:** Reporte de fallos (bugs) y plan de pruebas ejecutado.
* **Riesgos comunes:** Puede haber falta de tiempo para probar bien antes de entregar.

### Despliegue (Deployment)
* **Objetivo:** Es instalar el sistema en su entorno final para que los usuarios puedan usarlo.
* **Actividades Tipicas:** Configurar servidores, cargar la base de datos y lanzar la version final.
* **Entregables:** Sistema instalado en produccion, notas de la version y manual de uso.
* **Riesgos comunes:** Puede haber fallos en la migracion de datos o caidas del sistema durante la instalacion.

### Mantenimiento (Maintenance)
* **Objetivo:** Es mantener la aplicacion funcionando bien, corregir errores que aparezcan y hacerle mejoras.
* **Actividades Tipicas:** Corregir errores reportados por usuarios, optimizar codigo y aplicar parches de seguridad.
* **Entregables:** Actualizaciones de software y reportes de soporte.
* **Riesgos comunes:** Falta de documentacion de cambios y perder el control del codigo antiguo.

---

## Conclusiones

Mi conclusion es que el aplicar el SDLC me va ayudar a dejar de programar por instinto o por corazonada y tener que empezar a trabajar de forma ordenada; es una herramienta que en la escuela o el trabajo, nos va a evitar perder tiempo trtando de arreglar cosas que se pudieron prevenir desde la planificacion. 

Aunque a veces el seguir tantas etapas puede sentirse pesado o tedioso en proyectos muy pequeños, al adaptarse a estas fases, se podra tener una estructura clara para no dejar aspectos clave como las pruebas o la seguridad fuera del desarrollo o de lado.

---

## Referencias

1. Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9.ª ed.). McGraw-Hill Education.
2. Somerville, I. (2016). *Ingeniería del Software* (10.ª ed.). Pearson Educación.
3. IEEE Computer Society. (2014). *Guide to the Software Engineering Body of Knowledge (SWEBOK Guide)* (v3.0). IEEE.
4. Beck, K., et al. (2001). *Manifesto for Agile Software Development*. https://agilemanifesto.org/
5. Martin, R. C. (2018). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.
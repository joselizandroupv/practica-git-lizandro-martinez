# Investigación sobre Metodologías Ágiles: Scrum, Kanban y Design Thinking

**Nombre del estudiante:** Jose Lizandro Villarreal Martinez  
**Matrícula:** 2630116  
**Materia:** Metodologías de Programación  

---

## 1.- Introducción y Marco General Ágil

### 1.1 Resumen Ejecutivo

El concepto de **Ágil** en el desarrollo de software se refiere a un tipo de filosofía de trabajo que se enfoca en la flexibilidad, la entrega continua de valor y la adaptación constante hacia algun cambio. Esta surgio a principios de los años 2000 como una respuesta directa a los problemas del modelo tradicional "en cascada" (Waterfall), el cual era muy rígido, requería excesiva documentación inicial y provocaba entregas tardías que muchas veces no coincidían con lo que el cliente necesitaba realmente.

En este documento se analiza a fondo el ecosistema ágil, tambien se exploran sus valores y principios fundamentales, se comparan los marcos de trabajo más utilizados en la industria (Scrum, Kanban y Design Thinking), y se detallan los roles, artefactos, eventos y métricas de cada uno y finalmente, se presenta un mini-caso práctico de Design Thinking y una reflexión sobre la aplicación de estos enfoques en entornos académicos y profesionales.

---

### 1.2 Principios y Valores Ágiles
En 2001, un grupo de desarrolladores redactó el **Manifiesto Ágil**, estableciendo 4 valores fundamentales:

1. **Individuos e interacciones** sobre procesos y herramientas.
2. **Software funcionando** sobre documentación exhaustiva.
3. **Colaboración con el cliente** sobre negociación contractual.
4. **Respuesta ante el cambio** sobre el seguimiento de un plan.

Además, el manifiesto cuenta con 12 principios clave, entre los cuales destacan:

- **Satisfacción del cliente:** Mediante entregas tempranas y continuas de software valioso.
- **Aceptar cambios:** Los requisitos cambiantes son bienvenidos, incluso en etapas avanzadas del desarrollo.
- **Entregas frecuentes:** Entregar código funcional en periodos de pocas semanas.
- **Trabajo diario conjunto:** Desarrolladores y responsables de negocio deben trabajar juntos a diario.
- **Ritmo sostenible:** Los procesos ágiles promueven el desarrollo sostenible a un ritmo constante.

---

### 1.3 Panorama de Marcos Ágiles

| Marco de Trabajo | Enfoque Principal | ¿Cuándo elegirlo? |
| :---: | :---: | :---: |
| **Scrum** | Entregas estructuradas en bloques de tiempo fijos (Sprints). | Proyectos de desarrollo con requisitos cambiantes pero estructurables a mediano plazo. |
| **Kanban** | Visualización del flujo continuo y limitación del trabajo en proceso (WIP). | Entornos de soporte, mantenimiento o equipos con alta variabilidad de tareas entrantes. |
| **Design Thinking** | Innovación centrada en el usuario mediante empatía y prototipado rápido. | Fases iniciales de descubrimiento, cuando el problema del usuario aún no está claro. |

---

### 1.4 Ventajas y Riesgos de las Metodologías Ágiles

| Aspecto | Beneficios / Ventajas | Riesgos / Limitaciones | Trade-offs Típicos |
| :---: | :---: | :---: | :---: |
| **Gobernanza y Control** | Mayor transparencia del progreso real. | Sensación de falta de control formal si no hay entregables rígidos. | Flexibilidad a cambio de menor previsibilidad a largo plazo. |
| **Calidad del Producto** | Detección temprana de errores e integración continua. | Deuda técnica si se prioriza la velocidad sobre la arquitectura. | Velocidad de entrega frente a refactorización profunda. |
| **Gestión del Equipo** | Equipos autoorganizados y motivados. | Requiere alta madurez; puede causar agotamiento si no se respeta el ritmo. | Autonomía del equipo frente a supervisión tradicional. |

---

## 2. Marco de Trabajo Scrum

### 2.1 Conceptos Base
Scrum es un marco de trabajo ligero que ayuda a personas, equipos y organizaciones a generar valor a través de soluciones adaptativas para problemas complejos. Su propósito principal no es solo "construir rápido", sino aprender continuamente mediante ciclos de retroalimentación cortos llamados **Sprints**.

---

### 2.2 Roles en Scrum

- **Product Owner (PO):**
  - *Responsabilidades:* Define la visión del producto, prioriza el Product Backlog y asegura que el equipo entregue el máximo valor al negocio.
  - *Error frecuente:* Actuar como un "jefe de proyecto" tradicional que asigna tareas individuales en lugar de gestionar prioridades de negocio.

- **Scrum Master (SM):**
  - *Responsabilidades:* Facilita los eventos de Scrum, remueve impedimentos y guía al equipo en la adopción de la teoría y práctica de Scrum.
  - *Error frecuente:* Volverse un administrador de micro-gestión o tomar decisiones de desarrollo técnico por el equipo.

- **Development Team (Equipo de Desarrollo):**
  - *Responsabilidades:* Equipo multidisciplinario autoorganizado que diseña, construye y prueba el incremento de software funcional en cada Sprint.
  - *Error frecuente:* Trabajar en "silos" individuales donde los programadores no colaboran en las pruebas o la documentación.

---

### 2.3 Artefactos en Scrum

1. **Product Backlog:** Lista ordenada y dinámica de todas las funcionalidades, mejoras y correcciones necesarias en el producto.
2. **Sprint Backlog:** Conjunto de elementos seleccionados para el Sprint actual, junto con el plan para entregarlos.
3. **Increment:** La suma de todos los elementos completados durante un Sprint que cumplen con el criterio de calidad.

#### Criterios de Calidad:

- **Definition of Done (DoD):** Compromiso formal aplicable a *todo* el incremento (ejemplo: "Código revisado por un par, pruebas unitarias al 80% y desplegado en servidor de pruebas").
- **Criterios de Aceptación:** Condiciones específicas que debe cumplir una *Historia de Usuario individual* para ser considerada terminada (ejemplo: "El usuario debe poder iniciar sesión con Google y recibir un token de autenticación").

---

### 2.4 Eventos de Scrum

| Evento | Objetivo Principal | Duración Sugerida | Antipatrón Típico |
| :---: | :---: | :---: | :---: |
| **Sprint** | Contenedor de todas las actividades para crear un incremento útil. | 1 a 4 semanas (fijo) | Cambiar el objetivo del Sprint a mitad de ejecución. |
| **Sprint Planning** | Definir qué se hará en el Sprint y cómo se logrará. | Max. 8 horas (para Sprint de 1 mes) | Aceptar historias de usuario ambiguas sin criterios claros. |
| **Daily Scrum** | Sincronizar actividades diarias e identificar bloqueos. | 15 minutos diarios | Convertir la sesión en un reporte de estado al Scrum Master. |
| **Sprint Review** | Inspeccionar el incremento con los interesados (stakeholders). | Max. 4 horas | Presentar diapositivas en lugar de mostrar software funcionando. |
| **Sprint Retrospective** | Planificar mejoras en los procesos y la colaboración del equipo. | Max. 3 horas | Culpar a miembros del equipo en lugar de buscar soluciones de sistema. |

---

### 2.5 Métricas en Scrum

- **Velocity (Velocidad):** Cantidad de puntos de historia completados por el equipo en un Sprint.
  - *Uso correcto:* Para planificación interna y proyección de capacidad del equipo.
  - *Uso incorrecto:* Como métrica de productividad para comparar entre diferentes equipos.
- **Burndown Chart:** Gráfico que muestra el trabajo restante a lo largo del tiempo del Sprint.
- **Work in Progress (WIP):** Cantidad de tareas abiertas al mismo tiempo dentro del Sprint.

---

## 3. Marco de Trabajo Kanban

### 3.1 Fundamentos de Kanban

Kanban es un método de gestión de trabajo visual enfocado en el flujo continuo. Se basa en 6 prácticas principales:
1. Visualizar el flujo de trabajo.
2. Limitar el trabajo en progreso (WIP).
3. Gestionar y medir el flujo.
4. Hacer explícitas las políticas del proceso.
5. Implementar bucles de retroalimentación.
6. Mejorar colaborativamente y evolucionar experimentalmente.

---

### 3.2 Propuesta de Tablero Kanban con Límites WIP

A continuación se presenta un diseño de tablero Kanban para un equipo de desarrollo de software:

```text
+----------------+----------------+----------------+----------------+----------------+
| To Do          | In Progress    | Code Review    | Testing        | Done           |
| (Sin límite)   | (WIP: 3)       | (WIP: 2)       | (WIP: 2)       | (Sin límite)   |
+----------------+----------------+----------------+----------------+----------------+
| - Tarea A      | - Tarea B      | - Tarea C      | - Tarea D      | - Tarea E      |
| - Tarea F      |                |                |                | - Tarea G      |
+----------------+----------------+----------------+----------------+----------------+
```

---

### 3.3 Métricas de Flujo

- **Lead Time:** Tiempo total transcurrido desde que el cliente o negocio solicita una tarea hasta que se entrega terminada y lista para usarse.
- **Cycle Time:** Tiempo en el que el equipo de desarrollo trabaja activamente en la tarea (desde que pasa a "In Progress" hasta que se completa).
- **Throughput:** Cantidad de elementos o tareas completadas por unidad de tiempo (por ejemplo, 8 tareas por semana).
- **Cumulative Flow Diagram (CFD):** Gráfico acumulado que muestra la cantidad de tareas en cada columna del tablero a lo largo del tiempo. Sirve para identificar cuellos de botella cuando una franja del gráfico se vuelve muy ancha.

---

### 3.4 Clases de Servicio y Comparativa

#### Clases de Servicio en Kanban:

1. **Expedite (Urgente):** Errores críticos en producción que requieren atención inmediata y pueden saltarse temporalmente los límites WIP.
2. **Fixed Date (Fecha fija):** Tareas con fecha límite estricta o penalización (ej. entregas por normativas o fechas de lanzamiento).
3. **Standard (Estándar):** El flujo de trabajo normal del día a día.

#### ¿Cuándo usar Kanban vs. Scrum?
- **Usar Kanban:** Cuando el trabajo llega de forma continua y no predecible, como en tickets de soporte, mantenimiento o corrección de errores.
- **Usar Scrum:** Cuando hay un proyecto con un objetivo claro a mediano plazo y se pueden definir entregables cada 2 o 3 semanas.

---

## 4. Design Thinking y su Integración en el Desarrollo de Software

### 4.1 Visión General
Design Thinking es una metodología enfocada en entender las necesidades reales de los usuarios antes de ponerse a programar, evitando así construir productos que nadie necesita.

---

### 4.2 Las 5 Fases de Design Thinking

1. **Empatizar:** Conocer al usuario mediante entrevistas y observación directa. *(Entregable: Mapa de empatía / User Persona)*.
2. **Definir:** Analizar la información para identificar el problema principal. *(Entregable: Declaración del problema / Problem Statement)*.
3. **Idear:** Generar muchas ideas de solución sin juzgarlas al inicio. *(Entregable: Lluvia de ideas y matriz de priorización)*.
4. **Prototipar:** Crear versiones rápidas y baratas de la solución. *(Entregable: Wireframes o bocetos)*.
5. **Probar:** Mostrar el prototipo a usuarios reales para recibir retroalimentación. *(Entregable: Reporte de pruebas / Retroalimentación)*.

---

### 4.3 Mini-Caso Práctico: App para Grupos de Trabajo Universitario

#### Problema:

Los estudiantes pierden tiempo buscando compañeros con habilidades específicas para proyectos en materias avanzadas.

#### Actividades por Fase:

1. **Empatizar:** Entrevistas a 8 compañeros sobre cómo eligen a sus equipos.
2. **Definir:** "Los estudiantes necesitan encontrar compañeros con habilidades complementarias porque armar grupos al azar genera entregas desiguales".
3. **Idear:** Se propone una app de perfil rápido para seleccionar compañeros por habilidades de programación.
4. **Prototipar:** Boceto de pantalla de baja fidelidad en texto.
5. **Probar:** Presentar el boceto a 5 alumnos para ver si entienden los botones principales.

#### Boceto en Texto del Prototipo (Baja Fidelidad):

```text
+--------------------------------------------------+
|               APP MATCH ACADÉMICO                |
+--------------------------------------------------+
| [Foto Alumno]  Nombre: Carlos Gómez              |
|                Carrera: Ing. Software            |
|                Habilidades: [Python] [Git] [SQL] |
|                                                  |
|  [ Rechazar / Pass ]       [ Invitar al Equipo ] |
+--------------------------------------------------+
```

---

### 4.4 Relación entre Design Thinking, Scrum y Kanban

Design Thinking se usa en la fase de descubrimiento inicial para definir el producto correcto. Una vez definidas las funciones, esas ideas se convierten en Historias de Usuario que alimentan el Product Backlog de Scrum o el Tablero Kanban para ser programadas.

## 5. Conclusiones

Las metodologías ágiles no son solo reglas rígidas, sino una mentalidad de trabajo basada en adaptarse rápido y colaborar. En proyectos escolares o profesionales, combinar Design Thinking al inicio con Scrum o Kanban durante el desarrollo evita perder tiempo programando cosas inútiles y ayuda a entregar software funcional de forma constante.

## 6. Referencias

1. Beck, K., et al. (2001). *Manifesto for Agile Software Development*. https://agilemanifesto.org/
2. Schwaber, K., & Sutherland, J. (2020). *La Guía de Scrum: Las Reglas del Juego*. Scrum.org.
3. Anderson, D. J. (2010). *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press.
4. Brown, T. (2008). *Design Thinking*. Harvard Business Review, 86(6), 84-92.
5. Kniberg, H., & Skarin, M. (2010). *Kanban and Scrum - making the most of both*. C4Media.
# Práctica de Control de Versiones con Git y GitHub

**Nombre del estudiante:** Lizandro Martínez  
**Matrícula:** 2630116  
**Nombre de la práctica:** Control de Versiones Local y Remoto con Git y GitHub  

---

## 1. Objetivo de la Práctica
El objetivo es poder comprender y dominar el ciclo de vida del control de versiones creando un repositorio local en Git, luego sincronizandolo con un repositorio remoto en GitHub y por ultimo verificando el flujo de trabajo en ambos sentidos (Local a GitHub y GitHub a Local).

---

## 2. Descripción del Procedimiento Realizado

1. **Creacion e Inicializacion Local:** Se creo la carpeta de trabajo practica-git-lizandro-martinez en la terminal de PowerShell, luego se inicializo el repositorio con git init y por ultimo se estableció la rama main.
2. **Registro de Cambios:** Se creó el archivo datos.txt, luego se agregó al área de preparación con git add . y como ultimo paso se guardó en el historial mediante el comando git commit.
3. **Vinculacion Remota:** Se creo un repositorio publico y vacio en GitHub y se vinculo con el entorno local usando git remote add origin.
4. **Prueba GitHub a Local:** Se edito el archivo datos.txt directamente en la web de GitHub y luego se descargo el cambio a la computadora usando git pull.
5. **Prueba Local a GitHub:** Se añadió una nueva línea en datos.txt desde la terminal y ya como ultimo se subió la actualización a GitHub mediante git push.

---

## 3. Comandos de Git Utilizados y su Función

* git init: Inicializa un repositorio de Git en la carpeta actual.
* git branch -M main: Renombra la rama principal a main.
* git status: Muestra el estado actual de los archivos trabajados.
* git add .: Envía todos los archivos nuevos o modificados al Staging Area.
* git commit -m "mensaje": Registra los cambios en el historial local con una breve descripción.
* git remote add origin <URL>: Conecta el repositorio local con la dirección del repositorio en GitHub.
* git remote -v: Muestra la dirección del repositorio remoto vinculado.
* git push -u origin main: Sube los cambios locales a GitHub por primera vez y conecta las ramas.
* git pull origin main: Descarga las modificaciones hechas en GitHub hacia la computadora.
* git push: Sube las nuevas modificaciones locales a GitHub.

---

## 4. Descripción de los Archivos del Repositorio

* **datos.txt:** Archivo de texto utilizado para validar la sincronización de cambios en ambos sentidos.
* **README.md:** Documento en formato Markdown con la explicación detallada y comandos de la práctica.

---

## 5. Conclusión Personal
Nunca habia hecho esto, pero es emocionante conocer este lado de la programacion, esta práctica me sirvió para poder comprender cómo Git puede controlar las versiones de un proyecto de forma local y cómo GitHub te permite respaldarlo y mantenerlo sincronizado en la nube; entender el funcionamiento del Staging Area, los commits y los comandos push y pull, los cuales son fundamentales para coordinar cambios de código de forma ordenada en cualquier desarrollo de software.

# GUIA DE COMANDOS: POWERSHELL Y GIT

---

## 1.- RESUMEN DE COMANDOS POWERSHELL
| Comando | Definición | Ejemplo de uso |
| :---: | :---: | :---:| 
| "cd" | Te permite poder cambiar de directorio en la consola.| `cd ~`<br>`cd "C:\Proyectos"` |
| "ls"| Te muestra la lista de archivos y carpetas que contiene el directorio. | `ls`<br>`ls -Force`|
| "mkdir" | Te permite crear una nueva carpeta en la ubicación que especifiques. | `mkdir MiCarpeta` |
| "clear" | Te permite limpiar el texto visible que tengas en la pantalla de la consola. | `clear` | 
| "pwd" | Te muestra la ruta absoluta del directorio actual. | `pwd` |
| "cat" | Te muestra el contenido que tiene un archivo de texto. | `cat archivo.txt` |
| "cp" | Te permite copiar archivos o carpetas para un nuevo destino. | `cp nota.txt C:\Respaldo\` |
| "mv" | Te permite moverte o poder renombra archivos y directorios. | `mv viejo.txt nuevo.txt` |

---

## 2. COMANDOS BASICOS DE GIT
| Comando | Definición | Ejemplo de Uso |
| :---: | :---: | :---:|
| "git init" | Te permite inicializar un nuevo repositorio de Git en el directorio actual. | `git init`<br>`git init -b main` |
| "git clone" | Te permite descargar una copia completa de un repositorio que ya existe (local o remoto). | `git clone https://github.com/usuario/repo.git` |
| "git diff" | Te muestra los cambios línea por línea entre archivos modificados, el staging area o commits. | `git diff`<br>`git diff --staged` |
| "git status" | Te muestra el estado de tu área de trabajo (archivos modificados, en staging o no rastreados). | `git status`<br>`git status -s` |
| "git merge" | Este fusiona los cambios e historial de una rama especificada en la rama actual. | `git merge rama-feature` |
| "git config" | Este establece parámetros de configuración ya sean globales o locales (nombre, correo o un alias). | `git config --global user.name "Tu Nombre"`<br>`git config --global user.email "tu@email.com"` |
| "git add" | Te permite agregar archivos nuevos o modificados al área de preparación (*staging area*). | `git add index.html`<br>`git add .`<br>`git add -A` |
| "git log" | Te muestra el historial cronológico de confirmaciones (*commits*) realizadas. | `git log`<br>`git log --oneline` |
| "git commit" | Guarda de forma permanente los cambios del *staging area* conteniendo un mensaje descriptivo. | `git commit -m "mensaje inicial"` |
| "git checkout" |Este cambia entre ramas existentes o restaura archivos en el directorio de trabajo. | `git checkout desarrollo`<br>`git checkout -b nueva-rama` |
| "git branch" | Te permite listar, crear o eliminar ramas dentro del repositorio local. | `git branch`<br>`git branch mi-nueva-rama` |
| "git pull" | Este obtiene y fusiona los cambios desde un repositorio remoto a la rama local actual. | `git pull origin main` |
| "git push" | Este sube los commits locales al repositorio remoto especificado. | `git push origin main`<br>`git push -u origin main` |
| "git fetch" | Este descarga referencias y cambios del repositorio remoto sin aplicar fusiones al código local. | `git fetch origin` |

---

## 3. PROCESO PARA CREAR UN REPOSITORIO DE GIT DESDE POWERSHELL

| Paso / Comando | Definición | Ejemplo de Uso |
| :---: | :---: | :---: |
| **Paso 1: `mkdir` y `cd`** | **1. Crear carpeta y entrar en ella:** Crea el directorio del proyecto en el sistema de archivos y navega hacia su interior. | `mkdir MiNuevoProyecto`<br>`cd MiNuevoProyecto` |
| **Paso 2: `git init`** | **2. Inicializar el repositorio:** Crea la carpeta oculta `.git` y habilita el control de versiones en el directorio actual. | `git init` |
| **Paso 3: `git add -A`** | **3. Agregar archivos:** Añade todos los archivos nuevos, modificados o eliminados al área de preparación (*staging area*). | `git add -A` |
| **Paso 4: `git commit`** | **4. Realizar un primer commit:** Guarda de forma permanente la primera captura (*snapshot*) del proyecto en el historial con su mensaje. | `git commit -m "mensaje inicial"` |
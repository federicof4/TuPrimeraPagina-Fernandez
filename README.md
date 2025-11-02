# 🚗 TuPrimeraPagina-Fernandez

Proyecto desarrollado como parte del **Curso de CoderHouse**, representando los primeros pasos en el desarrollo de una aplicación web con **Django** y **Bootstrap 5**.

---

## 🧩 Descripción

**TuPrimeraPagina-Fernandez** es una aplicación web sencilla que permite la gestión de tres entidades principales:

- **Servicios**
- **Clientes**
- **Vehículos**

Cada sección permite **crear nuevos registros** y **visualizar listados** de manera fácil y ordenada.  
Además, cuenta con un módulo de **administración (Django Admin)** para gestionar usuarios y datos desde una interfaz avanzada.

---

## ⚙️ Instalación y configuración

1. Clonar o descargar el repositorio
```bash
git clone https://github.com/tuusuario/TuPrimeraPagina-Fernandez.git
cd TuPrimeraPagina-Fernandez

2. Crear un entorno virtual
python -m venv nombre_entorno

3. Activar el entorno virtual

En Windows:

nombre_entorno\Scripts\activate


En macOS / Linux:

source nombre_entorno/bin/activate

4. Instalar dependencias

pip install -r requirements.txt
5. Aplicar migraciones

python manage.py migrate

6. Ejecutar el servidor

python manage.py runserver

Luego accedé desde tu navegador a 👉 http://127.0.0.1:8000

💻 Uso

La app consta de 3 secciones principales:

Servicios — Crear y listar servicios realizados.

Clientes — Registrar y consultar clientes.

Vehículos — Registrar y consultar vehículos.

Cada sección cuenta con formularios simples y listados con buscador integrado.

🔐 Panel de administración

Podés acceder al módulo de administración en:

http://127.0.0.1:8000/admin


Para crear un usuario administrador, ejecutá:

python manage.py createsuperuser

🧠 Tecnologías utilizadas

Python 3

Django 5

Bootstrap 5

HTML5 / CSS3

SQLite (por defecto)

👨‍💻 Autor

Federico Fernández
Proyecto: TuPrimeraPagina-Fernandez
Curso: CoderHouse - Desarrollo en Python (Django)

📝 Licencia

Este proyecto se distribuye bajo licencia MIT.
Podés usarlo, modificarlo y distribuirlo libremente.

VIDEO Explicativo: 
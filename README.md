# Evaluación 1 - Programación Back End
## Simulación de Importación desde China con Django

Este proyecto de aplicación web de Django permite a los usuarios calcular el costo de una importación desde China a Chile y registrar las simulaciones en una base de datos MariaDB. La aplicación realiza cálculos basados en los datos proporcionados por el usuario y muestra los resultados, incluyendo el costo de envío, impuestos y el costo total de la compra.

### Características

- Registro de simulaciones en una base de datos MariaDB.
- Cálculos de impuestos y costos.
- Integración de DataTables para mostrar simulaciones en una tabla interactiva.
- Validación de datos tanto en el lado del cliente como en el servidor.
- Diseño con Bootstrap para una interfaz atractiva.

### Requisitos

- Python 3.11.4
- Django 4.2.6
- MySQL o MariaDB

### Configuración

1. Clonar este repositorio:

```bash
git clone https://github.com/epunamun/ev1.git
cd ev1
```


2. Crear un entorno virtual e instala las dependencias:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Configurar la base de datos MariaDB en `settings.py`.
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "importaciones",
        "USER": "root",
        "PASSWORD": "12345678",
        "HOST": "localhost",
        "PORT": ""
    }
}
``` 

4. Aplicar las migraciones para crear las tablas de la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Ejecutar la aplicación:
   
```bash
python manage.py runserver
```


6. Acceder a la aplicación en el navegador en `http://localhost:8000`.

### Uso

1. Acceder a la página de inicio.
2. Completar el formulario con los datos de tu importación.
3. Hacer click en "Calcular Importación" para obtener los resultados.
4. La aplicación mostrará los resultados en una tabla y los registrará en la base de datos.
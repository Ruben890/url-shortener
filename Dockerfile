# Usa una imagen base de Python
FROM python:3.11.4-alpine3.18

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos (requirements.txt) al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia todo el contenido del proyecto al contenedor
COPY . .

# Configura las variables de entorno para producción
ENV DJANGO_SETTINGS_MODULE=config.settings


# Realiza las migraciones de la base de datos
RUN python manage.py migrate

# Recopila los archivos estáticos
RUN python manage.py collectstatic --noinput

# Expone el puerto en el que se ejecutará el servidor web de Django
EXPOSE 8000

# Comando para ejecutar el servidor web de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

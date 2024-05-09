# Usar una imagen base de Python
FROM python:3.10.13

# Establecer el directorio de trabajo
WORKDIR /src

# Copiar el archivo de requisitos y instalar las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el resto del código fuente del proyecto
COPY src/ .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["gunicorn", "-b", "0.0.0.0:5000", "src:create_app()"]

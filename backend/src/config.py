import os

class Config:
    # Clave secreta que se utiliza para las sesiones, cookies, CSRF, etc.
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Sin valor por defecto para forzar la configuración en producción

    # URI de conexión a la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # Sin valor por defecto

    # SQLAlchemy config para deshabilitar el seguimiento de modificaciones de objetos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Secret Key para la creación de tokens
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')  # Sin valor por defecto

    # Configuración de eco SQL basada en el entorno
    SQLALCHEMY_ECHO = os.environ.get('SQLALCHEMY_ECHO', 'false').lower() in ['true', '1', 't']

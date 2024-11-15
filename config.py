import os

class Config:
    # Configuración de la base de datos con la URL proporcionada
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://mi_aplicacion_crud_db_user:SwPNgB5jmEMgbyixoh6EiIs9fn7WLuLG@dpg-csrnnpdds78s7383jmeg-a.oregon-postgres.render.com/mi_aplicacion_crud_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



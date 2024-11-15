# app.py
from flask import Flask
from models import db, Producto  # Aquí se importa 'db' y 'Producto' desde models.py

app = Flask(__name__)

# Configuración de la base de datos, puedes poner la URL de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_de_base_de_datos>'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Esto es para desactivar las advertencias innecesarias

# Inicializa la base de datos aquí, después de la importación de 'db' desde 'models.py'
db.init_app(app)

@app.route('/')
def index():
    return 'Hola, Mundo'

if __name__ == '__main__':
    app.run(debug=True)

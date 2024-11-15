from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Producto
from flask_migrate import Migrate

# Inicializa la aplicación
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Configura Flask-Migrate
migrate = Migrate(app, db)

# Ruta principal (índice)
@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

# Ruta para mostrar detalles de un producto
@app.route('/producto/<int:id>')
def show_producto(id):
    producto = Producto.query.get_or_404(id)
    return render_template('show.html', producto=producto)

# Ruta para agregar un nuevo producto
@app.route('/add', methods=['GET', 'POST'])
def add_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])

        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio)
        db.session.add(nuevo_producto)
        db.session.commit()

        flash('Producto agregado exitosamente', 'success')  # Flash message de éxito
        return redirect(url_for('index'))

    return render_template('add.html')

# Ruta para editar un producto existente
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_producto(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = float(request.form['precio'])

        db.session.commit()
        flash('Producto actualizado exitosamente', 'success')  # Flash message de éxito
        return redirect(url_for('index'))

    return render_template('edit.html', producto=producto)

# Ruta para eliminar un producto
@app.route('/delete/<int:id>', methods=['POST'])
def delete_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado exitosamente', 'danger')  # Flash message de error o advertencia
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

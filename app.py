from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Producto

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa db después de la configuración
db.init_app(app)

@app.route('/')
def index():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

@app.route('/producto/<int:id>')
def show_producto(id):
    producto = Producto.query.get_or_404(id)
    return render_template('show.html', producto=producto)

@app.route('/add', methods=['GET', 'POST'])
def add_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])

        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, precio=precio)
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_producto(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.precio = float(request.form['precio'])

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', producto=producto)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

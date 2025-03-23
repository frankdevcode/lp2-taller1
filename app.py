from flask import Flask, render_template
from datos import productos

# Crear la aplicación
app = Flask(__name__)

# Crear la ruta
@app.route("/") # Decorador
def index():
    return render_template('index.html', productos=productos)

@app.route("/producto/<string:nombre>")
def producto(nombre):
    producto = next((p for p in productos if p['nombre'] == nombre), None)
    if producto is None:
        return "Producto no encontrado", 404
    return render_template('producto.html', producto=producto)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
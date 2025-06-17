from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Crear la app
app = Flask(__name__)
CORS(app)

# Configuración de base de datos (RECORDAR CAMBIAR USUARIO, CONTRASEÑA Y NOMBRE DE LA DB SEGUN SEA NECESARIO)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/app_renault'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Modelo de tabla
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

# Crear tablas si no existen
with app.app_context():
    db.create_all()

# 🔽🔽🔽 Rutas para mostrar HTML desde templates 🔽🔽🔽

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/personas_vista")
def personas_vista():
    return render_template("personas.html")

@app.route("/ingresar_persona_vista")
def ingresar_persona_vista():
    return render_template("ingresar_persona.html")

@app.route("/editar_persona_vista")
def editar_persona_vista():
    return render_template("editar_persona.html")


# 🔽🔽🔽 Rutas API para conexión con JS 🔽🔽🔽

@app.route("/registro", methods=['POST'])
def registro():
    nombre_recibido = request.json["nombre"]
    nuevo_registro = Persona(nombre=nombre_recibido)
    db.session.add(nuevo_registro)
    db.session.commit()
    return "Solicitud via POST recibida"

@app.route("/personas", methods=['GET'])
def personas():
    all_registros = Persona.query.all()
    data_serializada = [{"id": r.id, "nombre": r.nombre} for r in all_registros]
    return jsonify(data_serializada)

@app.route('/update/<id>', methods=['PUT'])
def update(id):
    update_persona = Persona.query.get(id)
    update_persona.nombre = request.json["nombre"]
    db.session.commit()
    return jsonify([{"id": update_persona.id, "nombre": update_persona.nombre}])

@app.route('/borrar/<id>', methods=['DELETE'])
def borrar(id):
    delete_persona = Persona.query.get(id)
    db.session.delete(delete_persona)
    db.session.commit()
    return jsonify([{"id": delete_persona.id, "nombre": delete_persona.nombre}])


if __name__ == "__main__":
    app.run(debug=True)


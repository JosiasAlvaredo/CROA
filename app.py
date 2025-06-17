from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Crear la app
app = Flask(__name__)
CORS(app, origins="*", supports_credentials=True)

# Configuración de base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:461315@localhost:3306/app_renault'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Modelo de tabla
"""class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))"""

class Invitado(db.Model):
    __tablename__ = 'invitados'
    
    dni = db.Column(db.BigInteger, primary_key=True)
    id_equipo = db.Column(db.BigInteger, db.ForeignKey('equipos.id'))
    nombre_apellido = db.Column(db.String(255), nullable=False)
    dieta = db.Column(db.String(255), nullable=False)

class Equipo(db.Model):
    __tablename__ = 'equipos'
    
    id = db.Column(db.BigInteger, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(255), nullable=False)
    responsable_1_id = db.Column(db.BigInteger, nullable=True, default=None)
    responsable_2_id = db.Column(db.BigInteger, nullable=True, default=None)
    deporte = db.Column(db.String(255), nullable=False)
    puntaje = db.Column(db.BigInteger, nullable=False)

    invitados = db.relationship('Invitado', backref='equipo', lazy=True)


# Crear tablas si no existen
with app.app_context():
    db.create_all()

# 🔽🔽🔽 Rutas para mostrar HTML desde templates 🔽🔽🔽

@app.route("/equipos")
def personas_vista():
    return render_template("equipos")

"""@app.route("/personas_vista")
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
    return jsonify([{"id": delete_persona.id, "nombre": delete_persona.nombre}])"""

@app.route("/equipos_registro", methods=["GET"])
def equipos_registro():
    
    equipos = Equipo.query.all()
    data = []
    for e in equipos:
        equipo_data = {
            "id": e.id,
            "nombre": e.nombre,
            "categoria": e.categoria,
            "deporte": e.deporte,
            "puntaje": e.puntaje,
            "invitados": [{"dni": i.dni, "nombre_apellido": i.nombre_apellido, "dieta": i.dieta} for i in getattr(e, "invitados", [])],
            "responsable_1_id": e.responsable_1_id,
            "responsable_2_id": e.responsable_2_id
        }
        data.append(equipo_data)
    return jsonify(data)


@app.route("/nuevo_equipo", methods=["POST"])
def nuevo_equipo():
    if request.method == "OPTIONS":
        return '', 204
    data = request.json
    print(data)
    nuevo = Equipo(
        nombre=data["nombre"],
        categoria=data["categoria"],
        deporte=data["deporte"],
        puntaje=data["puntaje"],
        responsable_1_id=None,
        responsable_2_id=None
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Equipo creado"})

@app.route("/nuevo_invitado", methods=["POST"])
def nuevo_invitado():
    data = request.json
    nuevo = Invitado(
        dni=data["dni"],
        nombre_apellido=data["nombre_apellido"],
        dieta=data["dieta"],
        id_equipo=data["id_equipo"]
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Invitado creado correctamente"})


if __name__ == "__main__":
    app.run(debug=True)


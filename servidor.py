from flask import Flask, request, jsonify
from Servicios.autenticacion import Autenticacion
from flask import render_template


app = Flask(__name__)

@app.route('/')
def get_index():
    titulo='pagina_ayudalink'
    return render_template('Pag.Prncipal.html')

@app.route('/usuarios',methods=['POST'])
def crear_usuarios():
    datos_usuario = request.get_json()
    if 'nombre' not in datos_usuario or datos_usuario['nombre'] == '':
        return 'El nombre de usuario es requerido',412
    if 'clave' not in datos_usuario:
        return'la clave es requerida ', 412
    try:
        Autenticacion.crear_usuario(datos_usuario['nombre'],datos_usuario['clave'])
        return 'OK', 200
    except Exception:
        return 'El usuario ya existe', 412



@app.route('/usuarios/<id_usuario>', methods=['PUT'])
def modificar_usuarios(id_usuario):
        datos_usuario = request.get_json()
        if 'nombre' not in datos_usuario or datos_usuario['nombre'] == '':
            return 'El nombre de usuario es requerido', 412
        if 'clave' not in datos_usuario:
            return 'La clave es requerida',412
        Autenticacion.modificar_usuario(id_usuario, datos_usuario)
        return 'OK' , 200


@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(Autenticacion.obtener_usuarios)


@app.route('/usuarios/<id_usuario>',methods=['GET'])
def obtener_usuario(id_usuario):
    try:
        usuario = Autenticacion.obtener_usuario(id_usuario)
        return jsonify(usuario)
    except Exception:
        return 'Usuario no encontrado',404


@app.route('/usuarios/<id_usuario>', methods=['DELELTE'])
def borrar_usuario(id_usuario):
    Autenticacion.borrar_usuario(id_usuario)
    return "Borrado",200


@app.route('/login', methods=['POST'])
def login():
    try:
        datos_usuario=request.get_json()
        if 'nombre' not in datos_usuario:
          return 'El nombre de usuario es requerido', 412
        if 'clave' not in datos_usuario:
         return'La clave es requerida',412

        id_sesion = Autenticacion.login(datos_usuario['nombre'],datos_usuario['clave'])
        return jsonify({"id_sesion":id_sesion})
    except Exception:
        return 'USUARIO NO ENCONTRADO',404


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
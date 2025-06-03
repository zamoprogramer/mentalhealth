from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)

# Permitir llamadas CORS solo desde tu frontend en desarrollo
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

app.config['MYSQL_HOST']     = '127.0.0.1'
app.config['MYSQL_PORT']     = 3306
app.config['MYSQL_USER']     = 'cristianarevalo23@gmail.com'
app.config['MYSQL_PASSWORD'] = 'Cristian12345/'
app.config['MYSQL_DB']       = 'mental_health_db'
app.config['SECRET_KEY']     = 'tu_clave_secreta'
mysql = MySQL(app)


# ----------------------------------
# 1) Ruta de prueba para verificar conexión
# ----------------------------------
@app.route('/test-db', methods=['GET'])
def test_db():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT NOW()')
    resultado = cursor.fetchone()
    cursor.close()
    return jsonify({'servidor_mysql': str(resultado[0])})

# ————— 2) Ruta de registro (/register) —————
@app.route('/api/register', methods=['POST'])
def register():
    datos = request.get_json(force=True)
    nombre   = datos.get('nombre')
    apellido = datos.get('apellido')
    pais     = datos.get('pais')
    email    = datos.get('email')
    clave    = datos.get('password')

    if not all([nombre, apellido, pais, email, clave]):
        return jsonify({'error': 'Todos los campos son obligatorios.'}), 400

    # Hashear la contraseña
    password_hash = generate_password_hash(clave)

    try:
        cursor = mysql.connection.cursor()
        sql = """
            INSERT INTO usuarios (nombre, apellido, pais, email, password)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nombre, apellido, pais, email, password_hash))
        mysql.connection.commit()
        nuevo_id = cursor.lastrowid
        cursor.close()
        return jsonify({'message': 'Usuario creado con éxito', 'id': nuevo_id}), 201

    except Exception as e:
        # Si el email ya existía, por ejemplo, MySQL arrojará un error
        return jsonify({'error': str(e)}), 500

# ————— 3) Ruta de login (/login) —————
@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json(force=True)
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email y contraseña son requeridos'}), 400

        cur = mysql.connection.cursor()
        # Seleccionamos solo el id y el hash de contraseña del usuario
        cur.execute('SELECT id, nombre, apellido, pais, email, password FROM usuarios WHERE email = %s', (email,))
        user = cur.fetchone()
        cur.close()

        # user vendrá como tupla: (id, nombre, apellido, pais, email, password_hash)
        if user and check_password_hash(user[5], password):
            # Generar token JWT (opcional)
            token = jwt.encode({
                'user_id': user[0],
                'email': user[4],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, app.config['SECRET_KEY'], algorithm='HS256')

            return jsonify({
                'message': 'Login exitoso',
                'token': token,
                'user': {
                    'id': user[0],
                    'nombre': user[1],
                    'apellido': user[2],
                    'pais': user[3],
                    'email': user[4]
                }
            }), 200
        else:
            return jsonify({'error': 'Credenciales inválidas'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ————— 4) Rutas CRUD usando la misma tabla `usuarios` —————

# a) Crear usuario (equivalente a register, pero en /usuarios para pruebas)
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json(force=True)
    nombre   = datos.get('nombre')
    apellido = datos.get('apellido')
    pais     = datos.get('pais')
    email    = datos.get('email')
    password = datos.get('password')

    if not all([nombre, apellido, pais, email, password]):
        return jsonify({'error': 'Todos los campos son requeridos'}), 400

    hashed_password = generate_password_hash(password)

    try:
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nombre, apellido, pais, email, password) VALUES (%s, %s, %s, %s, %s)",
            (nombre, apellido, pais, email, hashed_password)
        )
        mysql.connection.commit()
        ultimo_id = cursor.lastrowid
        cursor.close()
        return jsonify({'message': 'Usuario creado exitosamente', 'id': ultimo_id}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# b) Listar todos los usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, nombre, apellido, pais, email, fecha_registro FROM usuarios")
        resultados = cursor.fetchall()
        cursor.close()

        lista = [
            {
                'id': r[0],
                'nombre': r[1],
                'apellido': r[2],
                'pais': r[3],
                'email': r[4],
                'fechaRegistro': str(r[5])
            }
            for r in resultados
        ]
        return jsonify(lista), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# c) Actualizar un usuario por ID
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    datos = request.get_json(force=True)
    nombre   = datos.get('nombre')
    apellido = datos.get('apellido')
    pais     = datos.get('pais')
    email    = datos.get('email')
    password = datos.get('password')  # si no quieres permitir cambiar contraseña, quita esta línea

    if not all([nombre, apellido, pais, email]):
        return jsonify({'error': 'Nombre, apellido, país y email son requeridos'}), 400

    try:
        cursor = mysql.connection.cursor()
        if password:
            hash_pass = generate_password_hash(password)
            cursor.execute(
                "UPDATE usuarios SET nombre=%s, apellido=%s, pais=%s, email=%s, password=%s WHERE id=%s",
                (nombre, apellido, pais, email, hash_pass, id)
            )
        else:
            cursor.execute(
                "UPDATE usuarios SET nombre=%s, apellido=%s, pais=%s, email=%s WHERE id=%s",
                (nombre, apellido, pais, email, id)
            )

        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Usuario actualizado exitosamente', 'id': id}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# d) Eliminar un usuario por ID
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        cursor = mysql.connection.cursor()
        # Verificar si existe
        cursor.execute("SELECT id FROM usuarios WHERE id=%s", (id,))
        if not cursor.fetchone():
            cursor.close()
            return jsonify({'error': 'Usuario no encontrado'}), 404

        cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Usuario eliminado exitosamente', 'id': id}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)

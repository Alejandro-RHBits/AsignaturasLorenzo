#Importación de módulos
#   Flask se encarga de tomar las URLs y asignarle la página correspondiente
#   render_template Toma los datos de python y los ingresa al HTML
#   flash envía notificaciones temporales para avisar que algo se hizo o no
#   pymongo permite que nos comuniquemos con la base de datos
#   bson.objetid sirve para traducir los ids de Mongo a Python y viceversa
#   flask_wtf y los demas sirven para hacer nuestros formularios desde python
from os import getenv
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

load_dotenv()

#Creación de una instancia de la clase Flask
app = Flask(__name__)

client = MongoClient(getenv('MONGO_URI'))

if "escuela" not in client.list_database_names():
    db = client['escuela']
    tabla = db['estudiantes']
    tabla.insert_one({})
else:
    db = client['escuela']
    tabla = db['estudiantes']

@app.route('/', methods=['GET'])

def home():
    return(client.list_database_names())

@app.route('/lista', methods=['GET'])
def lista():
    return (client.list_database_names())

@app.route('/tabla', methods=['GET'])
def tabla():
    documentos = client.escuela.estudiantes.find()
    listado=[]
    for doc in documentos:
        doc['_id'] = str(doc['_id']) 
        listado.append(doc)
    
    # IMPORTANTE: El return debe ir FUERA del for, alineado con el 'for'
    return jsonify(listado)

if __name__ == '__main__':
    app.run()

# --------------------------------------------------MI PROYECTO-----------------------------------------------------------

# #Conexión con la BDD
# client = MongoClient(getenv('MONGO_URI'))
# db = client['nombre_bdd']
# coleccion = db['nombre_coleccion']

# #Definimos el formulario para las personas que se quieran registrar

# class FormularioAgregarPersonas(FlaskForm):
#     nombre = StringField('Nombre', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     edad = IntegerField('Edad', validators=[DataRequired()])
#     submit = SubmitField('Guardar')

# #Definición de los endpoints usando decoradores

# # 1.Página de inicio con portada
# @app.route('/')
# def inicio():
#     return render_template('inicio.html')

# # 2.Página con el listado de personas
# @app.route('/listado')
# def listado():
#     listado = coleccion.find()
#     return render_template('listado.html', listado=listado)

# # 3.Página para Agregar personas
# @app.route('/agregar', methods=['GET', 'POST'])
# def agregar():
#     form = FormularioAgregarPersonas()

#     if form.validate_on_submit():
        
#         nueva_persona = {
#             'nombre': form.nombre.data,
#             'email': form.email.data,
#             'edad': form.edad.data
#         }

#         coleccion.insert_one(nueva_persona)
#         flash('¡Persona agregada exitosamente!', 'success')
#         return redirect(url_for('inicio'))
    
#     return render_template('crear_usuario.html', form=form, titulo="Agregar")

# # 4.Página Editar Usuarios
# @app.route('/editar/<id_usuario>', methods=['GET', 'POST'])
# def editar(id_usuario):
#     usuario_db = coleccion.find_one({'id': ObjectId(id_usuario)})
    

# #Definición del bloque IfName, para controlar la ejecución del módulo principal.
# if __name__ == '__main__':
#     app.run(debug=True)




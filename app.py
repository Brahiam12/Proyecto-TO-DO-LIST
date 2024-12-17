from flask import Flask, render_template, request, redirect, url_for, send_file
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import os

# Configuración de la base de datos
Base = declarative_base()

class Tarea(Base):
    __tablename__ = 'tareas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    estado = Column(Boolean, default=False)  # False = Pendiente, True = Completada

# Crear la conexión a la base de datos SQLite
engine = create_engine('sqlite:///tareas.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Configuración de Flask
app = Flask(__name__)

@app.route('/')
def index():
    tareas = session.query(Tarea).all()
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
    session.add(nueva_tarea)
    session.commit()
    return redirect(url_for('index'))

@app.route('/completar/<int:id_tarea>')
def completar_tarea(id_tarea):
    tarea = session.query(Tarea).get(id_tarea)
    if tarea:
        tarea.estado = True
        session.commit()
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id_tarea>')
def eliminar_tarea(id_tarea):
    tarea = session.query(Tarea).get(id_tarea)
    if tarea:
        session.delete(tarea)
        session.commit()
    return redirect(url_for('index'))

@app.route('/importar', methods=['POST'])
def importar_tareas():
    if 'archivo-json' not in request.files:
        return "Archivo no encontrado", 400
    archivo = request.files['archivo-json']
    if archivo.filename == '':
        return "Archivo vacío", 400
    if archivo:
        datos = json.load(archivo)
        for tarea in datos:
            nueva_tarea = Tarea(
                titulo=tarea.get('titulo', ''),
                descripcion=tarea.get('descripcion', ''),
                estado=tarea.get('estado', False)
            )
            session.add(nueva_tarea)
        session.commit()
    return redirect(url_for('index'))

@app.route('/exportar', methods=['GET'])
def exportar_tareas():
    tareas = session.query(Tarea).all()
    lista_tareas = [
        {
            'id': tarea.id,
            'titulo': tarea.titulo,
            'descripcion': tarea.descripcion,
            'estado': tarea.estado
        } for tarea in tareas
    ]
    archivo_path = 'tareas.json'
    with open(archivo_path, 'w') as archivo:
        json.dump(lista_tareas, archivo)
    return send_file(archivo_path, as_attachment=True)

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)

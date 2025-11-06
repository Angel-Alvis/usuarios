from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.usuario import Usuario

@app.route('/')
def pagInicio():
    print('\n\nruta1\n\n')
    usuarios=Usuario.get_all()
    print(usuarios)
    print(type(usuarios))
    return render_template('inicio.html', total_usuarios=usuarios)

@app.route('/registro')
def pagRegistro():
    print ('\n\nruta registro\n\n')
    return render_template('crear_usuario.html')

@app.route('/crear_usuario', methods=['POST'])
def formularioRegistro():
    datos={
        'nombre':request.form['nombre'],
        'apellido':request.form['apellido'],
        'email':request.form['email']
    }
    Usuario.save(datos)
    return redirect('/')

@app.route('/ver/<int:id>')
def pagVer(id):
    datos={'id':id}
    usuario=Usuario.get_by_id(datos)
    return render_template('ver.html', usuario=usuario)

@app.route('/editar/<int:id>')
def pagEditar(id):
    datos={'id':id}
    usuario=Usuario.get_by_id(datos)
    return render_template('editar.html', usuario=usuario)

@app.route('/editar/<int:id>/cambio', methods=['POST', 'GET'])
def formEditar(id):
    if request.method =='POST':
        datos={
            'id':id,
            'nombre':request.form['nombre'],
            'apellido':request.form['apellido'],
            'email':request.form['email']
            }
        Usuario.edit(datos)
        return redirect('/')
    else:
        return redirect('/')

@app.route('/eliminar/<int:id>')
def eliminar_usuario(id):
    datos={'id':id}
    Usuario.delete(datos)
    return redirect ('/')
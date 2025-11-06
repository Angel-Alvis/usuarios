from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Usuario:
    def __init__(self, data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @staticmethod
    def validacion(datos):
        esCorrecto=True
        if len(datos['nombre']) == 0:
            flash('Nombre inválido', 'nombre')
            esCorrecto = False
        if len(datos['apellido']) == 0:
            flash('Apellido inválido', 'apellido')
            esCorrecto = False
        if not EMAIL_REGEX.match(datos['email']):
            flash('E-mail es invalido','email')
            esCorrecto = False
        if Usuario.get_by_email(datos):
            flash('E-mail ya es usado','email')
            esCorrecto = False
        return esCorrecto

    @classmethod
    def get_all(cls):
        query="select * from usuarios;"
        resultados=connectToMySQL('db_usuarios').query_db(query)
        usuarios=[]
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios

    @classmethod
    def get_by_email(cls, datos):
        query="select email from usuarios where email=%(email)s;"
        resultados=connectToMySQL('db_usuarios').query_db(query, datos)
        if len(resultados) < 1:
            return False
        return True

    @classmethod
    def get_by_id(cls,datos):
        query="select * from usuarios where id=%(id)s;"
        resultado=connectToMySQL('db_usuarios').query_db(query, datos)
        if len(resultado) < 1:
            return False
        return cls(resultado[0])
    
    @classmethod
    def save(cls, datos):
        query='''insert into usuarios(nombre, apellido, email, created_at, updated_at)
        values (%(nombre)s, %(apellido)s, %(email)s, now(), now())'''
        return connectToMySQL('db_usuarios').query_db(query, datos)
    
    @classmethod
    def edit(cls, datos):
        query='''update usuarios 
        set nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, updated_at=now()
        where id=%(id)s
        '''
        print ("exito edit")
        return connectToMySQL('db_usuarios').query_db(query,datos)
    
    @classmethod
    def delete(cls,datos):
        query='''delete from usuarios
        where id=%(id)s'''
        return connectToMySQL('db_usuarios').query_db(query,datos)
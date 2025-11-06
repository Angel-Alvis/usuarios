from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id=data['id']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="select * from usuarios;"
        resultados=connectToMySQL('db_usuarios').query_db(query)
        usuarios=[]
        print('\n\n\nresultados print \n\n\n')
        print(resultados)
        print(type(resultados))
        for usuario in resultados:
            print('\n\n\nusuario print \n\n\n')
            print(usuario)
            print(type(usuario))
            usuarios.append(cls(usuario))
            print('\n\n\nusuarios print \n\n\n')
            print(usuarios)
            print(type(usuarios))
        return usuarios
    
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
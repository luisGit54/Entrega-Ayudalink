import sqlite3

sql_tabla_Usuarios= ''' CREATE TABLE Usuarios(
PRIMARY KEY ID_Usuario INTEGER NOT NULL AUTOINCREMENT ,
Correo_Electronico STRING ,
Edad INTEGER,
Tipo_Rol INTEGER FOREIGN KEY REFERENCES ROL(Visitante) ,
Ubicacion_Pais STRING) '''

sql_tabla_Roles_usuario='''CREATE TABLE Roles_usuario(
PRIMARY KEY ID_Roles_Usuario INTEGER AUTOINCREMENT ,
Visitante STRING ,
Visitante_Creador STRING,
Usuario_ID FOREIGN KEY REFERENCES Usuario(Usuario_ID)) '''

sql_tabla_Aportes=''' CREATE TABLE Aportes(
PRIMARY KEY ID_Aportes STRING ,
Texto STRING ,
PUNTUACION INTEGER ,
ID_Contenido INTEGER FOREIGN KEY REFERENCES Contenido(ID_CONTENIDO),
Usuario_ID INTEGER FOREIGN KEY REFERENCES Usuario(Usuario_ID) '''

sql_tabla_Contenido='''CREATE TABLE Contenido(
PRIMARY KEY ID_Contenido INTEGER AUTOINCREMENT ,
Puntuacion BOOLEAN ,
Texto STRING ,
VIDEO_PATH BOOLEAN ,
ID_Usuario INTEGER FOREIGN KEY REFERENCES Usuario(Usuario_ID) ,
Tema_ID STRING FOREIGN KEY REFERENCES Temas_Usuario(Usuario_ID)
'''

sql_tabla_Temas='''CREATE TABLE Temas(
PRIMARY KEY Tema_ID INTEGER AUTOINCREMENT ,
Nombre_Tema STRING ,
ID_Usuario INTEGER FOREIGN KEY REFERENCES Usuario(Tipo_ROL) ,
Categoria STRING FOREIGN KEY REFERENCES )  
'''

sql_tabla_Temas_Usuario=''' CREATE TABLE Temas_Usuario(
PRIMARY KEY ID_Usuario INTEGER,
Tema_ID STRING FOREIGN KEY REFERENCES tema(Contenido_ID) ,
Nombre_Tema STRING FOREIGN KEY REFERENCES Tema(Tema_ID)
'''



sql_tabla_sesiones= """
CREATE TABLE SESIONES(
ID INTEGER PRIMARY KEY,
ID_USUARIO TEXT,
FECHA_HORA TEXT,
FOREIGN KEY(ID_USUARIO) REFERENCES USUARIOS(ID_USUARIO)
)
"""

if __name__== '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('../../ayudalink.db')

        print('creado tablas..')
        conexion.execute(sql_tabla_Usuarios)
        conexion.execute(sql_tabla_Roles_usuario)
        conexion.execute(sql_tabla_Aportes)
        conexion.execute(sql_tabla_Contenido)
        conexion.execute(sql_tabla_Temas)
        conexion.execute(sql_tabla_Temas_Usuario)


        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        print(f'Error creando base de datos:{e}',e)




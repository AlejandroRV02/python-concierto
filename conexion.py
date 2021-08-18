import pymysql

class Conexion():
    def crear_conexion(self):
        conn = pymysql.connect(host="localhost",user="root",password="",db="conciertos")
        return conn

    def cerrar_conexion(self,conn):          
        try: 
            conn.close() 
        except pymysql.ProgrammingError as err: 
            print(err)
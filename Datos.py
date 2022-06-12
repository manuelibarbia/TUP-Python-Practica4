import sqlite3

class DBConexion():

    def __init__(self, path='Peluqueria'):
        self.__path = path
        self.__miConexion = sqlite3.connect(self.__path)
        self.__miCursor = self.__miConexion.cursor()

        self.__crear_tablas()
        self.__crear_tabla_personal()

    def __del__(self):
        self.__miConexion.close()

    def __crear_tablas(self):
        query = '''CREATE TABLE IF NOT EXISTS perro(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    nombre text,
                                                    dueno text,
                                                    direccion text,
                                                    telefono text,
                                                    baño integer,
                                                    baño_y_corte integer,
                                                    comportamiento text)'''
        self.ejecutar_query(query)
    
    def __crear_tabla_personal(self):
        query = '''CREATE TABLE IF NOT EXISTS personal(codigo_identificatorio integer,
                                                    nombre text,
                                                    apellido text,
                                                    DNI text,
                                                    direccion integer,
                                                    telefono integer,
                                                    email text,
                                                    años_experiencia text,
                                                    sueldo integer)'''
        self.ejecutar_query(query)
       
    def ejecutar_query(self, query):
        self.__miCursor.execute(query)
        self.__miConexion.commit()

    # def fetch_all(self):
    #     self.__miCursor.fetchall()
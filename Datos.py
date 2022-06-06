import sqlite3

class DBConexion():

    def __init__(self, path='Peluqueria'):
        self.__path = path
        self.__miConexion = sqlite3.connect(self.__path)
        self.__miCursor = self.__miConexion.cursor()

        self.__crear_tablas()

    def __del__(self):
        self.__miConexion.close()

    def __crear_tablas(self):
        query = '''CREATE TABLE IF NOT EXISTS perro(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    nombre text,
                                                    dueno text,
                                                    direccion text,
                                                    telefono text)'''
        self.ejecutar_query(query)

    def ejecutar_query(self, query):
        self.__miCursor.execute(query)
        self.__miConexion.commit() 
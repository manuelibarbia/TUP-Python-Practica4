from multiprocessing.connection import Connection
import Datos

class Perro():

    def __init__(self, nombre, dueno, direccion, telefono, baño=0, baño_y_corte=0):
        self.nombre = nombre
        self.dueno = dueno
        self.direccion = direccion
        self.telefono = telefono
        self.baño = baño
        self.baño_y_corte = baño_y_corte
    
    def guardar(self, dbc):
        query = 'INSERT INTO perro (nombre, dueno, direccion, telefono, baño, baño_y_corte) VALUES (\"{}\", \"{}\", \"{}\",\"{}\", \"{}\", \"{}\")'.format(self.nombre, self.dueno, self.direccion, self.telefono, self.baño, self.baño_y_corte)
        dbc.ejecutar_query(query)

    def __str__(self):
        return ('{} {} {} {} {} {}'.format(self.nombre, self.dueno, self.direccion, self.telefono, self.baño, self.baño_y_corte))

class Peluqueria():

    def __init__(self):
        self.conexionDB = Datos.DBConexion()

    def cargar_perro(self, nombre, dueno, direccion, telefono, baño=0, baño_y_corte=0):
        if nombre is None or nombre == '':
            raise Exception('Nombre de perro inválido')
        if dueno is None or dueno == '':
            raise Exception('Nombre de dueño inválido')
        perro = Perro(nombre, dueno, direccion, telefono, baño, baño_y_corte)
        perro.guardar(self.conexionDB)
    
    def editar_perro(self, nombre_perro_a_modificar, dato_a_modificar, domicilio_modificado, telefono_modificado):
        if dato_a_modificar == 1:
            query = 'UPDATE perro SET direccion = "{}" WHERE nombre = "{}"'.format(domicilio_modificado, nombre_perro_a_modificar)
        else:
            query = 'UPDATE perro SET telefono = "{}" WHERE nombre = "{}"'.format(telefono_modificado, nombre_perro_a_modificar)
        self.conexionDB.ejecutar_query(query)

    def borrar_perro(self, nombre_perro_a_borrar):
        query = 'DELETE FROM perro WHERE nombre = "{}"'.format(nombre_perro_a_borrar)
        self.conexionDB.ejecutar_query(query)

    def cargar_motivo_visita(self, perro_cargar_visita, motivo_visita, baño=0, baño_y_corte=0):
        if motivo_visita != 1 and motivo_visita != 2:
            raise Exception('Opción no válida')

        if motivo_visita == 1:
            baño = 1
            query = 'UPDATE perro SET baño = baño + "{}" WHERE nombre = "{}"'.format(baño, perro_cargar_visita)
        else:
            baño_y_corte = 1
            query = 'UPDATE perro SET baño_y_corte = baño_y_corte + "{}" WHERE nombre = "{}"'.format(baño_y_corte, perro_cargar_visita)
        self.conexionDB.ejecutar_query(query)

    # def mostrar_listado_de_perros(self):
    #     query = "SELECT * FROM perro"
    #     self.conexionDB.ejecutar_query(query)
    #     perros = self.conexionDB.fetch_all()
    #     print(perros)
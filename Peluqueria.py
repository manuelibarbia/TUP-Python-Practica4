import Datos

class Perro():

    def __init__(self, nombre, dueno, direccion, telefono):
        self.nombre = nombre
        self.dueno = dueno
        self.direccion = direccion
        self.telefono = telefono
    
    def guardar(self, dbc):
        query = 'INSERT INTO perro (nombre, dueno, direccion, telefono) VALUES (\"{}\", \"{}\", \"{}\",\"{}\")'.format(self.nombre, self.dueno, self.direccion, self.telefono)
        dbc.ejecutar_query(query)

    def __str__(self):
        return ('{} {} {} {}'.format(self.nombre, self.dueno, self.direccion, self.telefono))

class Peluqueria():

    def __init__(self):
        self.conexionDB = Datos.DBConexion()

    def cargar_perro(self, nombre, dueno, direccion, telefono):
        if nombre is None or nombre == '':
            raise Exception('Nombre de perro invalido')
        if dueno is None or dueno == '':
            raise Exception('Nombre de dueno invalido')
        perro = Perro(nombre, dueno, direccion, telefono)
        print(perro)
        perro.guardar(self.conexionDB)
    
    def editar_perro(self, nombre_perro_a_modificar, dato_a_modificar, domicilio_modificado, telefono_modificado):
        if dato_a_modificar == 1:
            query = 'UPDATE perro SET direccion = "{}" WHERE nombre = "{}"'.format(domicilio_modificado, nombre_perro_a_modificar)
        else:
            query = 'UPDATE perro SET telefono = "{}" WHERE nombre = "{}"'.format(telefono_modificado, nombre_perro_a_modificar)
        print(query)
        self.conexionDB.ejecutar_query(query)
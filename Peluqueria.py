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



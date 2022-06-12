from multiprocessing.connection import Connection
import Datos

class Perro():

    def __init__(self, nombre, dueno, direccion, telefono, baño=0, baño_y_corte=0, comportamiento = 0):
        self.nombre = nombre
        self.dueno = dueno
        self.direccion = direccion
        self.telefono = telefono
        self.baño = baño
        self.baño_y_corte = baño_y_corte
        self.comportamiento = comportamiento
    
    def guardar(self, dbc):
        query = 'INSERT INTO perro (nombre, dueno, direccion, telefono, baño, baño_y_corte, comportamiento) VALUES (\"{}\", \"{}\", \"{}\", \"{}\",\"{}\", \"{}\", \"{}\")'.format(self.nombre, self.dueno, self.direccion, self.telefono, self.baño, self.baño_y_corte, self.comportamiento)
        dbc.ejecutar_query(query)

    def __str__(self):
        return ('{} {} {} {} {} {} {}'.format(self.nombre, self.dueno, self.direccion, self.telefono, self.baño, self.baño_y_corte, self.comportamiento))

class Personal():
    def __init__(self, codigo_identificatorio, nombre, apellido, DNI, direccion, telefono, email, años_experiencia, sueldo):
        self.codigo_identificatorio = codigo_identificatorio
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.direccion = direccion  
        self.telefono = telefono
        self.email = email
        self.años_experiencia = años_experiencia
        self.sueldo = sueldo

    def guardar(self, dbc):
        query = 'INSERT INTO personal (codigo_identificatorio, nombre, apellido, DNI, direccion, telefono, email, años_experiencia, sueldo) VALUES (\"{}\", \"{}\", \"{}\", \"{}\",\"{}\", \"{}\", \"{}\", \"{}\", \"{}\")'.format(self.codigo_identificatorio, self.nombre, self.apellido, self.DNI, self.direccion, self.telefono, self.email, self.años_experiencia, self.sueldo)
        dbc.ejecutar_query(query)

    def __str__(self):
        return ('{} {} {} {} {} {} {} {} {}'.format(self.codigo_identificatorio, self.nombre, self.apellido, self.DNI, self.direccion, self.telefono, self.email, self.años_experiencia, self.sueldo))    

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

    def agregar_comportamiento_perro(self, perro_cargar_comportamiento, comportamiento, muy_bueno = 0, bueno =0, malo =0, muy_malo = 0):
        if comportamiento != 1 and comportamiento != 2 and comportamiento != 3 and comportamiento != 4:
            raise Exception('Opción no válida')

        if comportamiento == 1:
            muy_bueno  = "Muy bueno"
            query = 'UPDATE perro SET comportamiento = "{}" WHERE nombre = "{}"'.format(muy_bueno, perro_cargar_comportamiento)
        elif comportamiento == 2:
            bueno  = "Bueno"
            query = 'UPDATE perro SET comportamiento = "{}" WHERE nombre = "{}"'.format(bueno, perro_cargar_comportamiento)    
        elif comportamiento == 3:
            malo  = "Malo"
            query = 'UPDATE perro SET comportamiento = "{}" WHERE nombre = "{}"'.format(malo, perro_cargar_comportamiento)          
        elif comportamiento == 4:
            muy_malo  = "Muy malo"
            query = 'UPDATE perro SET comportamiento = "{}" WHERE nombre = "{}"'.format(muy_malo, perro_cargar_comportamiento)        
        self.conexionDB.ejecutar_query(query)

    
    def cargar_personal(self, codigo_identificatorio, nombre, apellido, DNI, direccion, telefono, email, años_experiencia, sueldo):
        if nombre is None or nombre == '':
            raise Exception('Nombre del personal inválido')
        if apellido is None or apellido == '':
            raise Exception('Apellido del personal inválido')
        empleado = Personal(codigo_identificatorio, nombre, apellido, DNI, direccion, telefono, email, años_experiencia, sueldo)
        empleado.guardar(self.conexionDB)    



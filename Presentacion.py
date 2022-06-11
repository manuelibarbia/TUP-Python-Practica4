from ast import While
import Peluqueria


class Presentacion():

    opciones_menu = {
        0: 'Salir',
        1: 'Cargar perro',
        2: 'Editar perro',
        3: 'Borrar perro',
        4: 'Cargar motivo de visita del perro',
        5: 'Mostrar listado de perros'
    }

    def __init__(self):
        self.peluqueria = Peluqueria.Peluqueria()

    def __mostrar_menu(self):
        print('Programa de datos de Peluquería Canina')
        for k in self.opciones_menu.keys():
            print(k, self.opciones_menu[k])

    def __salir(self):
        exit(0)

    def __cargar_perro(self):
        try:
            nombre = input('Ingrese el nombre del perro: ') 
            dueno = input('Ingrese el nombre del dueño: ') 
            direccion = input('Ingrese la dirección del dueño: ') 
            telefono = input('Ingrese el teléfono del dueño: ')

            self.peluqueria.cargar_perro(nombre, dueno, direccion, telefono)
        except Exception as e:
            print('Error cargando perro {}'.format(e))

    def __editar_perro(self):
        try:
            nombre_perro_a_modificar = input('Ingrese el nombre del perro que desea modificar: ')
            dato_a_modificar = int(input('1- Modificar domicilio 2- Modificar teléfono: '))
            domicilio_modificado = ''
            telefono_modificado = ''

            if dato_a_modificar == 1:
                domicilio_modificado = input('Ingrese el nuevo domicilio: ')
            elif dato_a_modificar == 2:
                telefono_modificado = input('Ingrese el nuevo teléfono: ')
            else:
                print('Opción no válida.')
                return
            self.peluqueria.editar_perro(nombre_perro_a_modificar, dato_a_modificar, domicilio_modificado, telefono_modificado)
        except Exception as e:
            print('Error editando perro {}'.format(e))

    def __borrar_perro(self):
        try:
            nombre_perro_a_borrar = input('Ingrese el nombre del perro que desea borrar: ')

            self.peluqueria.borrar_perro(nombre_perro_a_borrar)
        except Exception as e:
            print('Error borrando perro {}'.format(e))

    def __cargar_motivo_visita(self):
        try:
            perro_cargar_visita = input('Ingrese el nombre del perro para cargar su motivo de visita: ')
            motivo_visita = int(input('Si el perro viene por baño, ingrese 1, si viene por baño y corte, ingrese 2: '))

            self.peluqueria.cargar_motivo_visita(perro_cargar_visita, motivo_visita)
        except Exception as e:
            print('Error cargando motivo de visita {}'.format(e))

    def __mostrar_listado_de_perros(self):
        try:
            self.peluqueria.mostrar_listado_de_perros()
        except Exception as e:
            print('Error mostrando listado {}'.format(e))

    def menu(self):
        while True:
            self.__mostrar_menu()
            opcion = ''
            try:
                opcion = int(input('Elija una opción: '))
            except:
                print('Opción inválida')

            if (opcion == 0):
                self.__salir()
            elif(opcion == 1):
                self.__cargar_perro()
            elif(opcion == 2):
                self.__editar_perro()
            elif(opcion == 3):
                self.__borrar_perro()
            elif(opcion == 4):
                self.__cargar_motivo_visita()
            elif(opcion == 5):
                self.__mostrar_listado_de_perros()
            else:
                print('Opción inválida.')
import Peluqueria


class Presentacion():

    opciones_menu = {
        0: 'Salir',
        1: 'Cargar Perro',
        2: 'Editar Perro'
    }

    def __init__(self):
        self.peluqueria = Peluqueria.Peluqueria()

    def __mostrar_menu(self):
        for k in self.opciones_menu.keys():
            print(k, self.opciones_menu[k])

    def __salir(self):
        exit(0)

    def __cargar_perro(self):
        try:
            nombre = input('Ingrese nombre del perro: ') 
            dueno = input('Ingrese nombre del dueno: ') 
            direccion = input('Ingrese direccion del perro: ') 
            telefono = input('Ingrese telefono del perro: ') 

            self.peluqueria.cargar_perro(nombre, dueno, direccion, telefono)
        except Exception as e:
            print('Error cargando perro {}'.format(e))

    def __editar(self):
        try:
            nombre_perro_a_modificar = input('Ingrese el nombre del perro que se desea modificar: ')
            dato_a_modificar = int(input('1- Modificar domicilio 2- Modificar telefono: '))
            domicilio_modificado = ''
            telefono_modificado = ''
            
            if dato_a_modificar == 1:
                domicilio_modificado = input('Ingrese el nuevo domicilio: ')
            elif dato_a_modificar == 2:
                telefono_modificado = input('Ingrese el nuevo telefono: ')
            else:
                print('Opción no válida.')
                return
            self.peluqueria.editar(nombre_perro_a_modificar, dato_a_modificar, domicilio_modificado, telefono_modificado)
        except Exception as e:
            print('Error editando perro {}'.format(e))

    def menu(self):
        while True:
            self.__mostrar_menu()
            opcion = ''
            try:
                opcion = int(input('Elija opción: '))
            except:
                print('Opcion inválida')

            if (opcion == 0):
                self.__salir()
            elif(opcion == 1):
                self.__cargar_perro()
            elif(opcion == 2):
                self.__editar()
            else:
                print('Opcion invalida')
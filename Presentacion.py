import Peluqueria


class Presentacion():

    opciones_menu = {
        0: 'Salir',
        1: 'Cargar Perro'
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

    def menu(self):
        while True:
            self.__mostrar_menu()
            opcion = ''
            try:
                opcion = int(input('Elija opcion'))
            except:
                print('Opcion invalida')

            if (opcion == 0):
                self.__salir()
            elif(opcion == 1):
                self.__cargar_perro()
            else:
                print('Opcion invalida')
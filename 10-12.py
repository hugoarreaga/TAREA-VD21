class Contacto:
    def __init__(self,nombre,telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.siguiente = None

class ListaContacto:
    def __init__(self):
        self.primero = None

    def add_contact(self,nombre,telefono):
        new_contact = Contacto(nombre,telefono)
        
        if self.primero:
            current_contact = self.primero
            while current_contact.siguiente:
                current_contact = current_contact.siguiente
            current_contact.siguiente = new_contact
            
        else:
            self.primero = new_contact

    def print_all(self):
        current_contact= self.primero
        if current_contact:
            print(' --- LISTADO DE CONTACTOS ---')
        while current_contact:
            print(f'\tNombre: {current_contact.nombre}')
            print(f'\tNombre: {current_contact.telefono}\n')
            current_contact = current_contact.siguiente

if __name__ == '__main__':
    Listado = ListaContacto()

    while True:
        print('''
        OPCIONES DE LISTADO DE CONTACTOS
        1). AGREGAR CONTACTO
        2). MOSTRAR CONTACTOS

        ''')
        opcion = input('    Seleccione una opcion: ')

        if opcion == '1':
            print('  -- Agregar Contacto --')
            nombre = input('   Ingresar nombre:')
            telefono = input('   Ingresar telefono:')
            Listado.add_contact(nombre,telefono)
            print(' Conctacto Agregado')
        elif opcion =='2':
            Listado.print_all()
        elif opcion =='0':

            break
        else:
            print(' Opcion no disponible')
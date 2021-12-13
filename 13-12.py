class Contacto:
    def __init__(self,nombre,apellido,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.siguiente = None

class ListaContacto:
    def __init__(self):
        self.primero = None
    
    def get_contact(self,telefono):
        temp = self.primero
        while temp:
            if temp.telefono == telefono :
                return temp
            temp = temp.siguiente
        return False

    def add_contact(self,nombre,apellido,telefono):
        new_contact = Contacto(nombre,apellido,telefono)

        if self.get_contact(telefono):
            print(f'    ya existe un contacto con el telefono: {telefono}')
            return
        
        if self.primero is None:
            self.primero = new_contact
        elif new_contact.apellido < self.primero.apellido:
            new_contact.siguiente = self.primero
            self.primero = new_contact

        else:
            current_contact = self.primero
            while current_contact.siguiente:
                if new_contact.apellido < current_contact.siguiente.apellido:
                    
                    new_contact.siguiente = current_contact.siguiente
                    current_contact.siguiente = new_contact
                current_contact = current_contact.siguiente
            
            current_contact.siguiente = new_contact            
        

    def print_all(self):
        current_contact= self.primero
        if current_contact:
            print('\n\n --------------------------------')
            print(' ----- LISTADO DE CONTACTOS -----\n')
        while current_contact:
            print(f'\tNombre: {current_contact.nombre}')
            print(f'\tApellido: {current_contact.apellido}')
            print(f'\tTelefono: {current_contact.telefono}\n')
            current_contact = current_contact.siguiente
            
        print('\n --------------------------------')

import xml.etree.ElementTree as ET


def load_file(tree):
    root = tree.getroot()

    for child in root:
        nombre = child.find('nombre').text
        apellido = child.find('apellido').text
        telefono = child.find('telefono').text
        Listado.add_contact(nombre,apellido,telefono)

    return 

Listado = ListaContacto()


if __name__ == '__main__':
    

    while True:
        print('''
        OPCIONES DE LISTADO DE CONTACTOS
        1). AGREGAR CONTACTO
        2). MOSTRAR CONTACTOS
        3). CARGAR CONTACTOS

        ''')
        opcion = input('    Seleccione una opcion: ')

        if opcion == '1':
            print('  -- Agregar Contacto --')
            nombre = input('   Ingresar nombre: ')
            apellido = input('  Ingresar Apellido: ')
            telefono = input('   Ingresar telefono: ')

            Listado.add_contact(nombre,apellido,telefono)
            print(' Conctacto Agregado')
        elif opcion =='2':
            Listado.print_all()
        elif opcion =='3':
            file = input(' Ingrese la ruta del archivo: ')
            tree = ET.parse(file)
            load_file(tree)

            # try:
            #     tree = ET.parse(file)
            #     load_file(tree)

            # except:
            #     print(' Error')
            # pass
        elif opcion =='0':

            break
        else:
            print(' Opcion no disponible')
class nodo:
    def __init__(self,nombre) :
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

class lista:
    def __init__(self) :
        self.primero = None
        self.ultimo = None
    
    def agregar(self,nombre):
        nuevo = nodo(nombre)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.anterior = temp
            self.ultimo = nuevo

    def imprimir(self):
        temp = self.primero
        if temp: print('    LISTA ENCADENADA NORMAL')
        while temp:
            print(f' NOMBRE: {temp.nombre}')
            temp = temp.siguiente

    def imprimir_invertido(self):
        temp = self.ultimo
        if temp: print('    LISTA ENCADENADA INVERTIDA')
        while temp:
            print(f' NOMBRE: {temp.nombre}')
            temp = temp.anterior

if __name__ == '__main__':
    nombres = lista()
    while True:
        print('''
        OPCIONES DE LISTA
        1). AGREGAR NODO
        2). lISTA
        3). LISTA INVERTIDA
        ''')
        opcion = input('    Seleccione una opcion: ')
        if opcion == '1':
            nombre = input('  -- Agregar Contacto --\n   Ingresar nombre: ')
            nombres.agregar(nombre)
            print(' Conctacto Agregado')
        elif opcion =='2':nombres.imprimir()
        elif opcion =='3':nombres.imprimir_invertido()
        elif opcion =='0':break
        else:print(' Opcion no disponible')



class nodo:
    def __init__(self,nombre) :
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

class lista:
    def __init__(self) :
        self.primero = None
        self.ultimo = None
   
    def agregar(self,nombre):
        nuevo = nodo(nombre)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            temp = self.primero
            while temp.siguiente:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.anterior = temp
            self.ultimo = nuevo

    def imprimir(self):
        temp = self.primero
        if temp: print('    LISTA ENCADENADA NORMAL')
        while temp:
            print(f' NOMBRE: {temp.nombre}')
            temp = temp.siguiente

    def imprimir_invertido(self):
        temp = self.ultimo
        if temp: print('    LISTA ENCADENADA INVERTIDA')
        while temp:
            print(f' NOMBRE: {temp.nombre}')
            temp = temp.anterior

if __name__ == '__main__':
    nombres = lista()
    while True:
        print('''
        OPCIONES DE LISTA
        1). AGREGAR NODO
        2). lISTA
        3). LISTA INVERTIDA
        ''')
        opcion = input('    Seleccione una opcion: ')
        if opcion == '1':
            nombre = input('  -- Agregar Contacto --\n   Ingresar nombre: ')
            nombres.agregar(nombre)
            print(' Conctacto Agregado')
        elif opcion =='2':nombres.imprimir()
        elif opcion =='3':nombres.imprimir_invertido()
        elif opcion =='0':break
        else:print(' Opcion no disponible')

from api_conector import API


import os
def limpiarpantalla():
    os.system('cls')

class Menu:
    def __init__():

        print('''
        ====================MENU=================
        = a) Mostrar los productos disponibles  =
        = b) Mostrar un producto en especifico  =
        = c) Crear un nuevo producto            =
        = d) Editar un producto                 =
        = e) Eliminar un producto               =
        = f) Para salir del programa presione   =
        =        cualquier tecla !!!            =
        =========================================
        ''')

        op = input("Ingrese una opcion:\n").capitalize()
        print('\n')
        limpiarpantalla()
        # FUNCIONA
        if op == 'A':
           
            API.mostrar_productos()
            input("presione una tecla para continuar")
            Menu.__init__()
        # FUCNIONA
        elif op == 'B':
            name = (input("Ingrese el nombre del producto que desea mostrar:\n"))
            API.mostrar_producto(name)
            input("presione una tecla para continuar")
            Menu.__init__()
        
        elif op == 'C':
            
            name = input("Ingrese el nombre del nuevo producto:\n")
            price = int(input("Ingrese el precio del nuevo producto:\n"))
            quantity= int(input("Ingrese la cantidad para el nuevo producto:\n"))

            #data = f'{"name": "{name}","price": {price},"quantity": {quantity}}'

            
            API.crear_producto(name, price, quantity)
            input("presione una tecla para continuar")
            Menu.__init__()
            
            

        elif op == 'D':

            name = input("Ingrese el nuevo nombre o mantenga el anterior:\n")
            price = int(input("Ingrese nueva descripción o mantenga la anterior:\n"))
            quantity = int(input("Ingrese una nuevo cantidad o mantenga el anterior:\n"))

            API.actualizar_producto(name,price,quantity)
            input("presione una tecla para continuar")
            Menu.__init__()
            

        elif op == 'E':
            name = (input("Ingrese el id del producto que quiere eliminar:\n"))
            API.eliminar_producto(name)
            input("presione una tecla para continuar")
            Menu.__init__()
        else:
            pass

        

Menu.__init__()
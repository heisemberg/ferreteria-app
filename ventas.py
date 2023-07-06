import os
import core

def CreateData(*args):
    core.crearInfo(args)

def MainMenu():
    os.system("clear")
    isVenRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^17}|".format(' ','ADMINISTRACION DE VENTAS',' '))
    print('+','-'*55,'+')

    print("1. Registrar")
    print("2. Buscar")
    print("3. Devolucion")
    print("4. Anular Factura")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        pass
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isVenRun = False
    if (isVenRun):
        MainMenu()
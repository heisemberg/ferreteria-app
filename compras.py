import os
import core

def CreateData(*args):
    core.crearInfo(args)

def MainMenu():
    os.system("clear")
    isComRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^15}{}{:^17}|".format(' ','ADMINISTRACION DE COMPRAS',' '))
    print('+','-'*55,'+')

    print("1. Registrar")
    print("2. Buscar")
    print("3. Devolucion")
    print("4. Anular Factura Compra")
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
        isComRun = False
    if (isComRun):
        MainMenu()
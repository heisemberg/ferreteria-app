import os
import core

def CreateData(*args):
    core.crearInfo(args)

def MainMenu():
    os.system("clear")
    isProRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^13}{}{:^15}|".format(' ','ADMINISTRACION DE PROVEEDORES',' '))
    print('+','-'*55,'+')

    print("1. Registrar")
    print("2. Buscar")
    print("3. Editar")
    print("4. Eliminar")
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
    elif (opcion == 5):
        isProRun = False
    if (isProRun):
        MainMenu()

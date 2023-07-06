import core
import os
diccCliente = {}
def CreateData(*args):
    return core.LoadInfo("clientes.json")

def MainMenu(dataInfo : dict):
    diccCliente = dataInfo
    os.system("clear")
    isCliRun = True
    os.system("clear")
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CLIENTES',' '))
    print('+','-'*55,'+')

    print("1. Crear cliente")
    print("2. Buscar cliente")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        data = {
            "id":input("ingresa el Id del cliente"),
            "nombre":input("ingresa el nombre del cliente"),
            "email":input("ingresa el email del cliente")
        }
        diccCliente["data"].append(data)
        core.crearInfo("clientes.json",diccCliente)
    elif (opcion == 2):
        pass
    elif (opcion == 3):
        pass
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isCliRun = False
    if (isCliRun):
        MainMenu(diccCliente)

    

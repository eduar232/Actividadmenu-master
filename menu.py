# Generar un menu, con N opciones, cominando diccionarios con tuplas, que permita colocar el valor de la opción,
#  la descripcion de opción y el nombre de al función que ejecutaria dicha opción.

# """------------------------Menu----------------------------"""

def menu():
    salir = False
    while (salir == False):
        try:

            n = int(input("Digite el numero de opciones que tendra el menu? : \n"))
            salir = True

        except:

            print('Error dato invalido')

    diccionario = {}
    for i in range(1, n+1):
        salir = False

        while (salir == False):
             try:

                 print("Funcion numero ", i, ":")
                 funcion = input("Digite el nombre de la funcion: ")
                 descripcionFun = input("Digite la descripcion de la funcion: ")
                 diccionario[i] = (descripcionFun, funcion)
                 sali = True

             except:
                
                print('Error dato invalido')
                print("Bienvenido Al Menu\n\n")
                for x in diccionario:
                 print(f"{x}. {diccionario[x][0]}")
        salida = False 
        while (salida == False):
            try:
                opcion = int(input("Digite una opcion: "))
                salida = True
            except:
                print('Error dato invalido')
        return (opcion, diccionario)  
               
           
def pintarMenu():
     op = menu()
    for clave in op[1]:



if __name__ == '__main__':
    pintarMenu()

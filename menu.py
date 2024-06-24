#Biblioteca
import time as tiempo

#Menu
while True:
    print("\nInventario Tienda");
    print("\n1.-Agregar un producto.\n2.-Ver todos los productos.\n3.-Modificar un producto.\n4.-Eliminar un producto.\n5.-Guardar coleccion en un archivo.\n6.-Salir del programa.")
    try:
        opcion=int(input("\nIngrese una opcion: "))
    except ValueError:
        print("\nDebe ingresar un numero del 1 al 6.")
#Opcion 1
    if opcion==1:
        print("\n¿Que producto desea agregar al iventario de la lista?")
        agregar_producto=input("Ingrese el producto: ")
#Opcion 2
    elif opcion==2:
        print("coleccion")
#Opcion 3
    elif opcion==3:
        print("Usted ingreso a la opcion de modificar un producto.")
        modificar_producto=input("Ingrese el producto que desea modificar: ")
#Opcion 4
    elif opcion==4:
        print("Usted ingreso a la opcion de eliminar producto.")
        print("coleccion")
#Opcion 5
    elif opcion==5:
        print("Usted ingreso a la opcion de guardar coleccion en un archivo.")
#Opcion 6
    elif opcion==6:
        print("Usted ingreso a la opcion de salir del programa.")
        print("Saliendo del programa.")
        tiempo.sleep(2)
        break;
    else:
        print("Debe ingresar un numero del 1 al 6.")

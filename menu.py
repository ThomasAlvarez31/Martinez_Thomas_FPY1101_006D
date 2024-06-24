#Biblioteca
import time as tiempo
import funciones as funcion
import csv

#Menu
while True:
    print("\nInventario Tienda");
    print("\n1.-Agregar un producto.\n2.-Ver todos los productos.\n3.-Modificar un producto.\n4.-Eliminar un producto.\n5.-Salir del programa.")
    try:
        opcion=int(input("\nIngrese una opcion: "))
    except ValueError:
        print("\nDebe ingresar un numero del 1 al 5.")
#Opcion 1
    if opcion==1:
        funcion.agregar_productos()
#Opcion 2
    elif opcion==2:
        funcion.mostrar_productos()
#Opcion 3
    elif opcion==3:
        funcion.mod_producto()
#Opcion 4
    elif opcion==4:
        print("Usted ingreso a la opcion de eliminar producto.")
        funcion.borrar_producto()
#Opcion 5
    elif opcion==5:
        funcion.salir
        tiempo.sleep(2)
        break;
    else:
        print("Debe ingresar un numero del 1 al 5.")

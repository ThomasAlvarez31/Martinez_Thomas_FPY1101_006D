#menu
while True:
    print("\nInventario Tienda");
    print("\n1.-Agregar un producto.\n2.-Ver todos los productos.\n3.-Modificar un producto.\n4.-Eliminar un producto.\n5.-Guardar coleecion en un archivo.\n6.-Salir del programa.")
    try:
        opcion=int(input("\nIngrese una opcion: "))
    except ValueError:
        print("\nDebe ingresar un numero del 1 al 6.")
    if opcion==1:
        print("\n")

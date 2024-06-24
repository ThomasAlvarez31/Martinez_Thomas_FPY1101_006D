import csv
import creacionArchivo as apoyo

lista_productos=[]
def agregar_productos():
    codigo=input("Ingrese el codigo de producto")
    producto=input("Ingrese el nuevo producto")
    lista_productos.append(producto)
    precio=input("Ingrese el precio del producto")
    cantidad=input("Ingrese la cantidad de productos")
    apoyo.agregar_producto
    print("Su producto fue añadido exitosamente")

def mostrar_productos():
    print("")

def mod_producto():
    producto=input("Ingrese el producto a modificar")
    producto_nuevo=input("Ingrese el nuevo producto\n")
    modificar=lista_productos.index(producto)
    lista_productos[modificar]=producto_nuevo
    print(f"El producto {producto} a sido modificado e intercambiado por {producto_nuevo}")

def borrar_producto():
    producto=input("Ingrese el producto a eliminar")
    lista_productos.remove(producto)


def salir():
    print("Usted ingreso a la opcion de salir del programa.")
    print("Saliendo del programa.")
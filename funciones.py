<<<<<<< HEAD
lista_productos=[]
def agregar_productos():    
    producto=input("Ingrese el nuevo producto")
    lista_productos.append(producto)
    print(lista_productos)

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

=======
lista_productos=[]
def login():
    lista_usuarios={        
        "antonk":"1234",
        "thomasm":"5678",
        "caldo":"1133"}
def agregar_productos():    
    producto=input("Ingrese el nuevo producto")
    lista_productos.append(producto)
    print(lista_productos)

def mostrar_productos():
    print("")

def mod_producto():
    producto=input("Ingrese el producto a modificar")
    producto in lista_productos
    lista_productos.remove(producto)

def borrar_producto():
    producto=input("Ingrese el producto a eliminar")
>>>>>>> 4b2dcc800a23cf95d47a62d9997dfc0e634f1dfa

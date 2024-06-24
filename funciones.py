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
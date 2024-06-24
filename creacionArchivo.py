import csv

def agregar_producto(codigo, nombre, precio, cantidad):
    with open ('productos.csv','a',newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([codigo,producto, precio, cantidad])

while True:
    producto = input("Ingrese el nombre")
    precio = float(input("Ingrese el precio"))
    cantidad = int(input("Ingrese la cantidad del producto"))
    codigo = int(input("Ingrese el codigo"))
    agregar_producto(codigo,producto,precio,cantidad)
import csv

def agregar_producto(codigo, nombre, precio, cantidad):
    with open ('productos.csv','a',newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([codigo,nombre, precio, cantidad])
    agregar_producto(nombre,precio,cantidad)
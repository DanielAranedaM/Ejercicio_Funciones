from funciones import *
while True:
    opcion=menu()
    if opcion=="1":
        precio=int(input("Indique Precio: "))
        iva(precio)
    elif opcion=="2":
        precio=int(input("Indique precio: $"))
        desct=int(input("Ingrese descuento: "))
        descuento(precio, desct)
    elif opcion=="3":
        peso=float(input("Indique su peso en kg: "))
        estatura=float(input("indique su estatura en cm: "))
        Imc(peso, estatura)   
    elif opcion=="4":
        break
    else:
        opcionIncorrecta()

import os
while True:
    os.system("cls")
    print("MENU PRINCIPAL:")
    print("1- Calcular IVA")
    print("2- Descuento")
    print("3- Calcular lmc")
    print("4- Salir")
    op=input("INGRESE OPCION: ")
    if op=="1":
        p=int(input("Indique Precio: "))
        def calculo(precio, IVA):
            return  precio * IVA
        mf= (p,0.19)
        print("El IVA a pagar es: ",calculo(*mf))
        print("")
        input("Presione Tecla Para Continuar...")
    elif op=="2":
        p=int(input("Indique Precio   : "))
        d=int(input("Indique Descuento: "))
        def calculo(precio, descuento):
            return precio - (precio * descuento / 100)
        mf = (p,d)
        print("El monto final a pagar es: ",calculo(*mf))
        print("")
        input("Presione Tecla Para Continuar...")
    elif op=="3":
        peso=float(input("Indique Peso (Kg)    : "))
        estatura=float(input("Indique Estatura (Cm): "))
        lmc = 0
        estatura = estatura / 100
        def calculo(peso, estatura):
            return peso / (estatura * estatura)
        lmc = round(calculo(peso, estatura), 1)
        if lmc>=1 and lmc<=18.5:
            print("")
            print ("Segun su IMC su condición es: ")
            print ("Bajo de Peso")
            print("")
            input("Presione Tecla Para Continuar...")
        elif lmc>18.5 and lmc<=24.9:
            print("")
            print ("Segun su IMC su condición es: ")
            print("Adecuado")
            print("")
            input("Presione Tecla Para Continuar...")
        elif lmc>24.9 and lmc<=29.9:
            print("")
            print ("Segun su IMC su condición es: ")
            print("Sobrepeso")
            print("")
            input("Presione Tecla Para Continuar...")
        elif lmc>24.9 and lmc<=34.9:
            print("Obesidad Grado 1")
        elif lmc>34.9 and lmc<=39.9:
            print("Obesidad Grado 2")
            print("")
            input("Presione Tecla Para Continuar...")
        elif lmc>39.9:
            print("")
            print ("Segun su IMC su condición es: ")
            print("Obesidad Grado 3")
            print("")
            input("Presione Tecla Para Continuar...")
    elif op == "4":
        break
    else:
        print("")
        print("Opción incorrecta")
        input("Presione Tecla Para Continuar...")
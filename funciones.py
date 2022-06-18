def menu():
    try:
        print("MENU PRINCIPAL:")
        print("1- Calcular IVA")
        print("2- Descuento")
        print("3- Calcular imc")
        print("4- Salir")
        return input("INGRESE OPCION: ")
    except:
        print("ERROR")
    
def iva(precio):
    try:
        print("el IVA a pagar es: $",round(precio * 0.19))
        print("")
        input("Presione Tecla para continuar.......")
    except:
        print("ERROR")
    
def descuento(precio, descuento):
    try:
        print("el total a pagar es: $",round(precio - (precio * descuento / 100)))
        print("")
        input("Presione Tecla para continuar.......")
    except:
        print("ERROR")

def Imc(peso, estatura):
    try:
        estatura =estatura/100
        imc=round(peso/(estatura*estatura),1)
        if imc>=1 and imc<=18.5:
            print("")
            print ("Segun su IMC su condición es: ")
            print ("Bajo de Peso")
            print("")
            input("Presione Tecla Para Continuar...")
        elif imc>18.5 and imc<=24.9:
            print("")
            print ("Segun su IMC su condición es: ")
            print("Adecuado")
            print("")
            input("Presione Tecla Para Continuar...")
        elif imc>24.9 and imc<=29.9:
            print("")
            print ("Segun su IMC su condición es: ")
            print("Sobrepeso")
            print("")
            input("Presione Tecla Para Continuar...")
        elif imc>24.9 and imc<=34.9:
            print("Obesidad Grado 1")
        elif imc>34.9 and imc<=39.9:
            print("Obesidad Grado 2")
            print("")
            input("Presione Tecla Para Continuar...")
        elif imc>39.9:
            print("")
            print ("Segun su IMC su condición es: ")
            print("Obesidad Grado 3")
            print("")
            input("Presione Tecla Para Continuar...")
    except:
        print("ERROR")

def opcionIncorrecta():
    try:
        print("")
        print("Opción incorrecta")
        input("Presione Tecla Para Continuar...")
    except:
        print("ERROR")
    
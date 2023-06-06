#type() devuelve el tipo del valor/variable entregado
#\n salto de linea
#\t tabulacion
#se debe anteponer un \ si una string dentro de comillas lleva comilla del mismo tipo ejemplo: "esa \"cosa\""

#name =input("Ingresa tu nombre: ")
#mensaje = str("Hola "+name)

name = ""

while name == "":
    name =input("Ingresa tu nombre: ")
    mensaje = str("Hola " + name)
    if name != "":
        print(mensaje)
        print("Bienvenido!!...")
    else:
        name = input("Vuelve a ingresar tu nombre: ")
        mensaje = str("Hola " + name)
        if name != "":
            print(mensaje)
            print("Bienvenido!!...")
        else:
            print("No has ingresado tu nombre")

#print("var mensaje = "+str(type(mensaje)))
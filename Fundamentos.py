# print ('Hello World ')

# variables definidas
nombre = "ronalt stevent"
apellido = "soto alarcon"
edad = 20
altura = 1.90
activo = True
correo = "ronalttalarconQgmail.com"
telefono = "3214830615"
cedula = 123456789

# variables modificadas
edad_float = float(edad)
altura_int = int(altura)
telefono_int = int(telefono)
cedula_str = str(cedula)

# impresion de la variables
print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print(type(telefono_int), telefono)
print(type(altura_int), altura)
print(type(edad_float), edad)
print(type(cedula_str), cedula)


# indemtacion

if 5 > 2: 
    print ("5 es menor que 2")
else:
    print ("5 no es mayor que 2")


# input

nombre_com = input("ingrese su nombre completo: ")

print (nombre_com)

edad_si = int(input("escribe tu edad: "))   
print (edad_si)

if edad_si > 18:
    print("es mayor de edad")
else:
    print ("es menor de edad")


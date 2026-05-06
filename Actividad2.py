#Declaracion de variables
print("\n")
print("="*8,"Calculadora de Promedio",8*"=") 
nota1 = float(input("Ingrese su nota: ")) #Ingresa los datos
nota2 = float(input("Ingrese su nota: ")) #Ingresa los datos
nota3 = float(input("Ingrese su nota: ")) #Ingresa los datos
nota4 = (nota1+nota2+nota3) / 3 #Esta haciendo la operacion
nota_maxima = 5.0 - nota4 #Esta definiendo cuanta nota le falta para llegar a la nota maxima
aprobado = nota4 >= 3.2 #Esta definiendo que se aprueba desde la nota 3.2

# Imprimiendo las variables
print("\n")
print("="*8,"Resultado de Calculadora de Notas",8*"=")
print(f"El promedio es de. {round(nota4, 2)}") #Redondea la nota
print(f"Hace falta para la nota maxima: {round(nota_maxima, 2)}") #Redondea la nota
print("\n")

# Se esta poniemdo la condicion de aprobado y no aprobado
if aprobado:
    print("👏👏 "" Aprobaste, felicidades lograste cumplir tu unica responsabilidad "" 👏👏")
else:
    print("🤣🤣 No aprobaste, fallaste en lo unico que tenias que hacer 🤣🤣")

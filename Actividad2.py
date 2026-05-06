#Declaracion de variables
print("\n")
print("="*8,"Calculadora de Promedio",8*"=")
nota1 = float(input("Ingrese su nota: "))
nota2 = float(input("Ingrese su nota: "))
nota3 = float(input("Ingrese su nota: "))
nota4 = (nota1+nota2+nota3) / 3 
nota_maxima = 5.0 - nota4
aprobado = nota4 >= 3.2


print("\n")
print("="*8,"Resultado de Calculadora de Notas",8*"=")
print(f"El promedio es de. {round(nota4, 2)}")
print(f"Hace falta para la nota maxima: {round(nota_maxima, 2)}")
print("\n")

if aprobado:
    print("👏👏 "" Aprobaste, felicidades lograste cumplir tu unica responsabilidad "" 👏👏")
else:
    print("🤣🤣 No aprobaste, fallaste en lo unico que tenias que hacer 🤣🤣")

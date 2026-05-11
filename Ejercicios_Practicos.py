"""
Ejercicio 1
"""
nombre = input("Ingrese su nombre: ") 
valor_producto = float(input("Cual fue el valor del producto: "))
promedio = float(input("Ingrese su promedio: "))

print (f"{nombre}, {valor_producto}, {promedio}")

"""
Ejercicio 2
"""
valor1 = int(input("Ingrese el valor: "))
valor2 = int(input("Ingrese el valor: "))
valor3 = float(input("Ingrese el valor: "))
valor4 = (input("Ingrese el valor: "))
valor5 = (input("Ingrese el valor: "))

suma = (valor1 + valor2 + valor3)
print(type(f"resultado. {suma}"))

numero_mayor = max (valor1, valor2, valor3) # Aca estamos dicienod que de los 3 numeros escoja el entero mayor, por eso ponemos un "max" para que nos de el numero mayor entero
print(type(f"El numero mayo es: {numero_mayor}"))

prueba = valor1 / valor2
prueba2 = valor3 / prueba
print(type(f"prueba de la forma de andres: {prueba2}"))

division = valor3
division /= (valor1 % valor2)
print(type(f"El resultado es: {division}"))

suma_strings = valor4 + valor5
print(type(f"El resultado es: {suma_strings}"))
"""
Ejercicio 3
"""
base = int(input("Ingrese el dato: "))
exponente = int(input("Ingrese el dato: "))
potencia = base ** exponente
"""
Ejercicio 4
"""
numero = float(input("Escribe el número: "))
print("Resultado:", numero ** 0.5)

"""
Ejercicio 5
"""
estudiante = input("Ingrese el nombre del estudiante: ")
decimal1 = float(input("ingrese el valor: "))
decimal2 = float(input("ingrese el valor: "))
decimal3 = float(input("ingrese el valor: "))
decimal4 = float(input("ingrese el valor: "))
decimal5 = float(input("ingrese el valor: "))

promedio_estudiante = (decimal1 + decimal2 + decimal3 + decimal4 + decimal5) / 5
print(f"Resultado: {estudiante},{promedio_estudiante}")

"""
Ejercicio 6
"""

numeroUno = 8
numeroDos = 2
numero_Uno = numeroDos
numero_Dos = numeroUno
print(numero_Uno, numero_Dos)

"""
Ejercicio 7
"""
estado = (5 == 2) or (2 > 1)
print(estado)

"""
Ejercicio 8
"""
Resultado = ((10 + 5) * 2 / 3) + (4 ** 2) - (15 // 4) + (20 % 3)
print(f"El valor de la variable Resultado es: {Resultado}")

"""
Ejercicio 9
"""
# CUADRADO 
ladoCuadrado = 8
areaCuadrado = ladoCuadrado * ladoCuadrado
perimetroCuadrado = ladoCuadrado * 4

print(f"Cuadrado: Área = {areaCuadrado}, Perímetro = {perimetroCuadrado}")

# TRIANGULO
baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriangulo = 8
ladoDosTriangulo = 8

areaTriangulo = (baseTriangulo * alturaTriangulo) / 2
# El perímetro es la suma de la base + los otros dos lados
perimetroTriangulo = baseTriangulo + ladoUnoTriangulo + ladoDosTriangulo

print(f"Triángulo: Área = {areaTriangulo}, Perímetro = {perimetroTriangulo}")

# RECTÁNGULO 
baseRectangulo = 8
alturaRectangulo = 6

areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = 2 * (baseRectangulo + alturaRectangulo)

print(f"Rectángulo: Área = {areaRectangulo}, Perímetro = {perimetroRectangulo}")
"""
Ejercicio 10
"""
edad = int(input("Introduce la edad: "))

if edad <= 0:
    categoria = "Edad no válida"
elif edad <= 5:
    categoria = "Infante"
elif edad <= 10:
    categoria = "Niño"
elif edad <= 15:
    categoria = "Pre adolescente"
elif edad <= 18:
    categoria = "Adolescente"
elif edad <= 25:
    categoria = "Pre adulto"
elif edad <= 40:
    categoria = "Adulto"
elif edad <= 55:
    categoria = "Pre anciano"
else:
    categoria = "Anciano"
print(f"La categoría para la edad {edad} es: {categoria}")

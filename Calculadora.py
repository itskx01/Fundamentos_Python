# Declarar variables
Valor1 = float(input("Ingrese el valor: "))
Valor2 = float(input("Ingrese el valor: "))
Tipo_operacion = input("Tipo de operacion a hacer: \ 1.suma \ 2.resta \ 3.division \ 4.multiplicacion \ 5.modulo \ 6.division_entera \ 7.potencia: ")

# Operaciones aritmeticas
suma = Valor1 + Valor2
resta = Valor1 - Valor2
division = Valor1 / Valor2
multiplicacion = Valor1 * Valor2
modulo = Valor1 % Valor2
division_entera = Valor1 //Valor2
potencia = Valor1 ** Valor2

# Resultado de las operaciones
if Tipo_operacion == "1":
    print("El resultado es: ",suma)

if Tipo_operacion == "2":
    print("El resultado es: ",division)

if Tipo_operacion == "3":
    print("El resultado es: ",resta)

if Tipo_operacion == "4":
    print("El resultado es: ",multiplicacion)

if Tipo_operacion == "5":
    print("El resultado es: ",modulo)

if Tipo_operacion == "6":
    print("El resultado es: ",division_entera)

if Tipo_operacion == "7":
    print("El resultado es: ",potencia)
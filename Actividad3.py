# Declarar variables
print("\n")
print("="*8,"Calculadora de IMC",8*"=")
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura (Eje. 1.75): "))
peso_corporal = peso / (altura **2)

print("\n")
print("---Resultado del Analisis---")

if (peso_corporal  <= 18.5):
    print("Estas bajo de peso ")
elif 18.5 <= peso_corporal <= 24.9:
    print("Estas en el peso normal ")
elif 25 <= peso_corporal <= 29.9:
    print("Tienes sobre peso ")
else: print("Tienes obesidad")
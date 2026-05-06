# Declarar variables
print("\n")
print("="*8,"Calculadora de IMC",8*"=")
peso = float(input("Ingresa tu peso en kg: ")) #Pide los datos a usar
altura = float(input("Ingresa tu altura (Eje. 1.75): ")) #Pide los datos a usar
peso_corporal = peso / (altura **2) #Esta haciendo la operacion 

print("\n")
print("---Resultado del Analisis---")

#Esta poniendo la condicion de los pesos (bajo peso,normal,sobre peso y obesidad)
if (peso_corporal  <= 18.5):
    print("Estas bajo de peso ")
elif 18.5 <= peso_corporal <= 24.9: #Esta diciendo que es menor o igual a (18.5) y (24.9) es mayor o igual 
    print("Estas en el peso normal ") #Es lo mismo para todos los demas elif
elif 25 <= peso_corporal <= 29.9:
    print("Tienes sobre peso ") #En este caso es porque a partir de (29.9) ya lo toma como obesidad
else: print("Tienes obesidad")
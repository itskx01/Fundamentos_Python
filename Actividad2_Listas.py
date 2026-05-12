# Temperatura registradas durante dos semanas (14 dias)
# indice                  0   1   2   3   4   5   6   7   8   9   10  11  12  13
temperaturaRegistrada = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]

# Impresion de temperaturas
# Dia 1
print(temperaturaRegistrada[0:1])

# Dia 14
print(temperaturaRegistrada[-1:])

# Dia 7
print(temperaturaRegistrada[6:7])

# Penultimo dia 
print(temperaturaRegistrada[-2:-1])

# Semana 1
semana_1 = (temperaturaRegistrada[0:7])
print("Primera semana")

# Semana 2
semana_2 = temperaturaRegistrada[7:15]
print("Segunda semana")

# Dias pares (día 2, 4, 6, 8, 10, 12, 14) - índices 1, 3, 5, 7, 9, 11, 13
print(temperaturaRegistrada[0:14:2])

# Orden invertido
print(temperaturaRegistrada[::-1])

# Semana 1 promedio
promedio_Semana1 = sum(semana_1) / len(semana_1)
print(f"El promedio de la primera semana es: {promedio_Semana1}")

# Semana 2 promedio
promedio_Semana2 = sum(semana_2) / len(semana_2)
print(f"El promedio de la segunda semana es: {promedio_Semana2}")

# BONUS
bonus = max(promedio_Semana1, promedio_Semana2)
print(f"Temperatura promedio mayor: {bonus}")

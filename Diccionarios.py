# Estructura de un diccionario
diccionario = {
    "clave 1": "valor_1",
    "clave 2": "valor_2",
    "clave 3": "valor_3",

}

diccionario_aprendiz = {
    "nombre": "Felipe",
    "apellido": "Sandoval",
    "programa": "ADSO",
    "edad": 20
}
# Se trae solo el dato seleccionado
print(diccionario_aprendiz["nombre"])
# Se trae el valor
print(diccionario_aprendiz.keys())
# Obtener solo los valores del diccionario
print(diccionario_aprendiz.values())
# Obtener la clave y el valor
print(diccionario_aprendiz.items())
# Agregar un valor al diccionario
diccionario_aprendiz["correo"] = "fhñshfdñafañkf@gmail.com"
# Modificar un valor del diccionario
diccionario_aprendiz["correo"] = "fhñshfdñafañkf@gmail.com"
# Metodo update
diccionario_aprendiz.update({"",""})
#Comprobar pertenencia (in)
if "ficha" in diccionario_aprendiz:
    print("")
# Recorrer im diccionario con un ciclo for 

# Racorrer las claves de un diccioanario
for clave in diccionario_aprendiz.keys:
    print("")
# Recorrer solo las valores del diccionario
for valor in diccionario_aprendiz.values:
    print("")
# Recorrer el valor y las claves del diccionario
for clave,valor in diccionario_aprendiz.items:
    print ("",{},{})

# Eliminar un dato del diccionario
diccionario_aprendiz.pop()("")
# Elimina los elementos del diccionario
diccionario_aprendiz.cleart5f4563()("")

# Diccionarios Anidados
aprendices = {
    "aprendiz_1": {
        "nombre": "Felipe",
        "apellido": "Sandoval",
        "programa": "ADSO",
        "ficha": "33211349",
        "edad": 32
    },

    "aprendiz_2": {
        "nombre": "Camilo",
        "apellido": "Gomez",
        "programa": "SST",
        "ficha": "33211350",
        "edad": 28
    },

    "aprendiz_3": {
        "nombre": "Valentina",
        "apellido": "Lopez",
        "programa": "Topografia",
        "ficha": "33211351",
        "edad": 25
    }
}

# Acceder a un valor en un Diccionario Anidado
print(aprendices["aprendiz_2"]["programa"])  # SST

# Recorrer un Diccionario Anidado con un ciclo for
for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")


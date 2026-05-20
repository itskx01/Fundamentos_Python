# --- Creación ---
lenguajes = {"Python", "Java", "C++", "Python", "Java"}
print(lenguajes)  # {'C++', 'Java', 'Python'} - sin duplicados, sin orden fijo

# ¡IMPORTANTE: conjunto vacío vs diccionario vacío!
conjunto_vacio = set()   # conjunto vacío ✓
diccionario_vacio = {}   # diccionario vacío ← no es un set


# --- Métodos de modificación ---
frutas = {"mango", "guayaba", "mora"}

frutas.add("maracuyá")     # Agrega un elemento
frutas.add("mango")        # No hace nada, ya existe

frutas.remove("mora")      # Elimina; lanza KeyError si no existe
frutas.discard("papaya")   # Elimina; NO lanza error si no existe

elem = frutas.pop()        # Elimina y retorna un elemento aleatorio

print(frutas)


# --- Verificar pertenencia: O(1) ---
print("Python" in lenguajes)   # True — instantáneo sin importar tamaño
print("COBOL" in lenguajes)    # False

python_devs = {"Ana", "Luis", "Marta", "Carlos", "Sofia"}
java_devs   = {"Luis", "Carlos", "Pedro", "Laura"}

# ┌────────────────────────────────────────────────────┐
# │  UNIÓN  |  : todos los elementos de ambos conjuntos │
# └────────────────────────────────────────────────────┘

todos = python_devs | java_devs
# o también: python_devs.union(java_devs)

print("Unión:", todos)
# {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro', 'Laura'}


# ┌────────────────────────────────────────────────────┐
# │  INTERSECCIÓN  &  : solo los que están en AMBOS   │
# └────────────────────────────────────────────────────┘

ambos = python_devs & java_devs
# o también: python_devs.intersection(java_devs)

print("Intersección:", ambos)  
# {'Luis', 'Carlos'}


# ┌────────────────────────────────────────────────────┐
# │  DIFERENCIA  -  : los de A que NO están en B      │
# └────────────────────────────────────────────────────┘

solo_python = python_devs - java_devs
# o también: python_devs.difference(java_devs)

print("Solo Python:", solo_python)  
# {'Ana', 'Marta', 'Sofia'}

solo_java = java_devs - python_devs

print("Solo Java:", solo_java)  
# {'Pedro', 'Laura'}


# ┌──────────────────────────────────────────────────────────────────────────┐
# │ DIFERENCIA SIMÉTRICA  ^  :  los que están en uno PERO NO en ambos        │
# └──────────────────────────────────────────────────────────────────────────┘

exclusivos = python_devs ^ java_devs
# o también:  python_devs.symmetric_difference(java_devs)
print("Exclusivos:", exclusivos)
# {'Ana', 'Marta', 'Sofia', 'Pedro', 'Laura'}
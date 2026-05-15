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
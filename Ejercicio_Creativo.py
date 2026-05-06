"""
PARTE 1: Importamos las librerias
"""
import random

"""
PARTE 2: Creamos una funcion "def" para hacer un bloque reutilizable, no tenemos que estar limpiando la consola
"""
def piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"] # Le estamos diciendo que cree opciones para escoger
    # Regla: la clave le gana al valor
    reglas = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"} # Aca le estamos diciendo que escogiendo x opcion le gana a x opcion
    print("\n")
    print("--- PIEDRA, PAPEL O TIJERA ---")
    usuario = input("Elige (piedra, papel, tijera): ").lower() # Aca solo estamos diciendo que escoja una opcion al usuario
    pc = random.choice(opciones) # Aca es para que la pc(la computadora) tenga repuestas aleatorias
    print("\n")
    if usuario not in opciones: # Le estamos diciendo que condiciones debe tener, en este caso es (si usuario no escoge una opcion le debe imprimir "opcion no valida")
        print("Opción no válida.")
        return # Este es para que se repita
    print("\n")
    print(f"PC eligió: {pc}") 
    if usuario == pc:
        print("¡Empate!")
    elif reglas[usuario] == pc:
        print("¡Ganaste!")
    else:
        print("Perdiste.")
"""
PARTE 3: Aca ya cerramos la funcion  
"""
piedra_papel_tijera()
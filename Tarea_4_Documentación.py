import random
import os 
# Variable que define el estado del ahorcado #
juego_terminado = False

# Lisa de las posibles palabras #
palabras = ["HOLA", "BOLA", "SACA", "LALO"]

# Contador de las letras en palabras es decir cuando es cero se restn vidas#
encontrada = 0

# Vidas del jugador #
vidas = 5

# Indice aleatorio para elegir la palabra #
indice = random.randint(0, 3)

# Palabra que el jugador debe adivinar #
palabra_secreta = palabras[indice]

# Longitud de la palabra secreta #
longitud = len(palabras[indice])

# Lista de letras que forman la palabra secreta #
letras_palabra = list(palabra_secreta)

# Lista que muestra el progreso del jugador, inicia con guiones para la base del ahorcadso #
progreso = ["_"] * longitud

while juego_terminado == False:
    os.system("cls")
    
    # Mostrar el progreso actual #
    for i in range(longitud):
        print(progreso[i], end="")
    print()

    # Pedir letra al jugador y convertirla a mayuscula #
    letra = input(f"ingrese una letra para jugar ahorcado, tienes: {vidas} vidas: ").upper()

    # Reiniciar contador por cada letra ingresada #
    encontrada = 0

    # Si la letra esta en la palabra, reemplaza el guion por la letra #
    for i in range(longitud):
        if letra == letras_palabra[i]:
            progreso[i] = letra

    # Contar cuantas veces aparece la letra en la palabra #
    for i in range(longitud):
        if letra == letras_palabra[i]:
            encontrada += 1

    if encontrada == 0:
        vidas -= 1

    if vidas == 0:
        print(f"perdiste, la palabra era: {palabra_secreta}")
        juego_terminado = True

    if progreso == letras_palabra:
        print(f"ganaste, la palabra era: {palabra_secreta}")
        juego_terminado = True



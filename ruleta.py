import random

# Estructura de datos para almacenar información de cada jugador
class Jugador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.dinero = 0

# Frase inicial y palabra oculta
frase = ""
palabra_oculta = ""

# Inicialización de variables
jugadores = []

# Función para inicializar la frase oculta con asteriscos
def inicializar_frase_oculta(frase_original):
    return "".join([c if c.lower() in "aeiou " else "*" for c in frase_original])

# Función para mostrar el estado actual del juego
def mostrar_estado(palabra_oculta, total):
    print("\n-----------------------------------------")
    print(palabra_oculta)
    print("-----------------------------------------")
    print(f"Total: {total}€\n")

# Función para lanzar la ruleta y determinar la casilla
def tirar_ruleta():
    opciones = ["X2", "quiebra", "pierde turno", "saltar turno"] + [random.randint(0, 200) for _ in range(6)]
    return random.choice(opciones)

# Función para comprar consonantes y vocales con la ruleta
def comprar_letra(palabra_oculta, total):
    casilla = tirar_ruleta()

    if casilla == "X2":
        print("¡Doble puntuación en esta ronda!")
        return palabra_oculta, total

    if casilla == "quiebra":
        print("¡Quiebra! Pierdes todo tu dinero ganado en esta ronda.")
        return palabra_oculta, 0

    if casilla == "pierde turno":
        print("¡Pierdes el turno en esta ronda!")
        return palabra_oculta, total

    if casilla == "saltar turno":
        print("Has decidido saltar este turno.")
        return palabra_oculta, total

    letra = input("Ingresa una letra: ").lower()

    if letra.isalpha() and len(letra) == 1:
        if letra in "aeiou":
            print(f"¡Has ingresado una vocal! No puedes ganar dinero con las vocales.")
        elif letra in frase.lower():
            ganancia = int(casilla)  # Convertir a entero
            print(f"¡Letra correcta! Ganaste {ganancia}€")
            total += ganancia
            palabra_oculta = palabra_oculta.replace("*", letra)
        else:
            print("¡Letra incorrecta! Pierdes 25€")
            total -= 25
    else:
        print("Por favor, ingresa una letra válida.")

    mostrar_estado(palabra_oculta, total)
    return palabra_oculta, total

# Función para procesar la opción 2: Comprar vocal
def comprar_vocal(palabra_oculta, total):
    if total >= 10:
        vocal = input("Ingresa una vocal: ").lower()
        if vocal in "aeiou" and len(vocal) == 1:
            total -= 10
            print(f"¡Vocal comprada! Pagaste 10€")
            palabra_oculta = palabra_oculta.replace("*", vocal)
        else:
            print("Por favor, ingresa una vocal válida.")
    else:
        print("No tienes suficiente dinero para comprar una vocal.")

    mostrar_estado(palabra_oculta, total)
    return total

# Función para procesar la opción 3: Resolver
def resolver(palabra_oculta, total):
    respuesta = input("Intenta resolver: ").lower()
    if respuesta == frase.lower():
        print(f"¡Resuelto correctamente! Ganaste {total}€")
        return True
    else:
        print("Respuesta incorrecta. Pierdes el turno.")
        return False

# Función para procesar la opción 4: Saltar Turno
def saltar_turno():
    print("Has decidido saltar este turno.")
    return False

# Función principal del juego
def jugar_pasapalabra():
    global frase, palabra_oculta
    frase = input("Introduce la frase para jugar Pasapalabra: ")
    palabra_oculta = inicializar_frase_oculta(frase)

    # Bucle para cada jugador
    for jugador in jugadores:
        print(f"\nTurno de {jugador.nombre}")

        # Restablecer variables para cada jugador
        palabra_oculta_jugador = palabra_oculta
        total_ganado_jugador = 0

        # Bucle para cada turno
        turno = 1
        while True:
            print(f"\nTurno {turno}")

            # Mostrar la palabra oculta en el menú
            print(f"\nPalabra: {palabra_oculta_jugador}")

            # Menú de opciones
            print("\n1. Comprar letra")
            print("2. Comprar vocal")
            print("3. Resolver")
            print("4. Saltar Turno")

            opcion = input("Elige una opción (1/2/3/4): ")

            if opcion == "1":
                palabra_oculta_jugador, total_ganado_jugador = comprar_letra(palabra_oculta_jugador, total_ganado_jugador)
            elif opcion == "2":
                total_ganado_jugador = comprar_vocal(palabra_oculta_jugador, total_ganado_jugador)
            elif opcion == "3":
                if resolver(palabra_oculta_jugador, total_ganado_jugador):
                    break  # Salir del bucle si se resuelve correctamente
            elif opcion == "4":
                if saltar_turno():
                    break  # Salir del bucle si se decide saltar el turno

            # Actualizar turno
            turno += 1

        # Actualizar el total ganado para el jugador
        jugador.dinero += total_ganado_jugador

# Función para registrar jugadores
def registrar_jugadores(num_jugadores):
    for i in range(1, num_jugadores + 1):
        nombre = input(f"\nJugador {i}, introduce tu nombre: ")
        edad = input("Introduce tu edad: ")
        jugadores.append(Jugador(nombre, edad))

# Función para mostrar resultados finales
def mostrar_resultados():
    print("\n------ Resultados Finales ------")
    for jugador in jugadores:
        print(f"{jugador.nombre} - Edad: {jugador.edad} - Dinero ganado: {jugador.dinero}€")

# Inicio del juego
if __name__ == "__main__":
    # Solicitar la palabra oculta después de ingresar el número de jugadores
    num_jugadores = int(input("Introduce el número de jugadores: "))
    frase = input("Introduce la frase para jugar Pasapalabra: ")
    palabra_oculta = inicializar_frase_oculta(frase)

    # Registrar jugadores
    registrar_jugadores(num_jugadores)

    # Iniciar juego para cada jugador
    for jugador in jugadores:
        print(f"\n¡Bienvenido, {jugador.nombre}! Comencemos el juego.")
        jugar_pasapalabra()

    # Mostrar resultados finales
    mostrar_resultados()

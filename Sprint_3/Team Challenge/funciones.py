# funciones.py

import numpy as np
import random
from variables import TABLERO, AGUA, BARCO, DISPARO, NADA

def crear_tablero():                                                                #Creamos un tablero vacio
    return np.full((TABLERO, TABLERO), AGUA)

def colocar_barco(tablero, eslora):                                                 #Colocamos los barcos de forma aleatoria
    while True:                                                                     #Eslora:longitud del barco
        orientacion = random.choice(["horizontal", "vertical"])
        fila = random.randint(0, TABLERO - 1)
        columna = random.randint(0, TABLERO - 1)
        
        if orientacion == "horizontal" and columna + eslora <= TABLERO:
            if all(tablero[fila, columna + i] == NADA for i in range(eslora)):
                for i in range(eslora):
                    tablero[fila, columna + i] = BARCO
                break
        elif orientacion == "vertical" and fila + eslora <= TABLERO:
            if all(tablero[fila + i, columna] == NADA for i in range(eslora)):
                for i in range(eslora):
                    tablero[fila + i, columna] = BARCO
                break

def disparo(tablero, fila, columna):
    if tablero[fila, columna] == BARCO:
        tablero[fila, columna] = DISPARO
        return True
    elif tablero[fila, columna] == NADA:
        tablero[fila, columna] = NADA
        return False
    return None


# Librería python para las prácticas de megafonía

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio

# tasa de muestro de la señal
rate = 44100

# Crea una onda y la visualiza
def crear_onda_vis(amplitud=2, frecuencia=2, duration=3):
    # Generar los valores del tiempo (t)
    #(0, duration, int(rate * duration), endpoint=False)
    t = np.linspace(0,duration, int(rate * duration))  # Genera 1000 puntos entre 0 y 2*pi
    
    # Generar la onda sinusoidal usando la amplitud y frecuencia dadas
    y = amplitud * np.sin(frecuencia * t)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(t, y)
    plt.title(f"Onda Sinusoidal de {frecuencia} Hz con Amplitud {amplitud}")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()

# Crea una onda y ya está
def crear_onda(amplitud=2, frecuencia=2):
    # Generar los valores del tiempo (t)
    t = np.linspace(0, 2 * np.pi, 1000)  # Genera 1000 puntos entre 0 y 2*pi
    
    # Generar la onda sinusoidal usando la amplitud y frecuencia dadas
    y = amplitud * np.sin(frecuencia * t)

    return y
  

def crea_onda1_y_onda2_alavez_vis(amplitud1, frecuencia1, offset1=0, amplitud2=1, frecuencia2=1, offset2=0):
    # Generar los valores del tiempo (t)
    t = np.linspace(0, 2 * np.pi, 1000)  # Genera 1000 puntos entre 0 y 2*pi
    
    # Generar las dos ondas sinusoidales usando la amplitud, frecuencia y offset dados
    y1 = amplitud1 * np.sin(frecuencia1 * t + offset1)
    y2 = amplitud2 * np.sin(frecuencia2 * t + offset2)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(t, y1, label=f"{frecuencia1} Hz, Amp={amplitud1}, Offset={offset1}")
    plt.plot(t, y2, linestyle='--', label=f"{frecuencia2} Hz, Amp={amplitud2}, Offset={offset2}")
    
    plt.title("Dos Ondas Puras")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def suma_dos_ondas_vis(amplitud1, frecuencia1, offset1=0, amplitud2=1, frecuencia2=1, offset2=0):
    # Generar los valores del tiempo (t)
    t = np.linspace(0, 2 * np.pi, 1000)  # Genera 1000 puntos entre 0 y 2*pi
    
    # Generar las dos ondas sinusoidales usando la amplitud, frecuencia y offset dados
    y1 = amplitud1 * np.sin(frecuencia1 * t + offset1)
    y2 = amplitud2 * np.sin(frecuencia2 * t + offset2)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(t, y1+y2, label=f"{frecuencia1} Hz, Amp={amplitud1}, Offset={offset1}")
    
    
    plt.title("Dos Ondas Puras")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid(True)
    plt.show()

# Devuelve los puntos asociados a la función suma de dos ondas
def suma_dos_ondas(amplitud1, frecuencia1, offset1=0, amplitud2=1, frecuencia2=1, offset2=0):
    # Generar los valores del tiempo (t)
    t = np.linspace(0, 2 * np.pi, 1000)  # Genera 1000 puntos entre 0 y 2*pi

    # Generar las dos ondas sinusoidales usando la amplitud, frecuencia y offset dados
    y1 = amplitud1 * np.sin(frecuencia1 * t + offset1)
    y2 = amplitud2 * np.sin(frecuencia2 * t + offset2)

    return y1+y2

# devuelve el audio
def escuchar_onda (y_data):
    return Audio (data=y_data, rate=44100)


def dibujar_onda(y_data):
    t = np.linspace(0, 2 * np.pi, 1000)  # Genera 1000 puntos entre 0 y 2*pi
    plt.figure(figsize=(10, 6))
    plt.plot(t, y_data)
    plt.title(f"Onda Sinusoidal de {frecuencia} Hz con Amplitud {amplitud}")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()
  

# Test de la función
#crea_onda1_y_onda2_alavez(2, 2, 0, 1, 5, 0)     

# Test de la función
#crear_onda(2, 20)  # Genera una onda sinusoidal de amplitud 2 y frecuencia 2 Hz
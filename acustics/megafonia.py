
# Librería python para las prácticas de megafonía

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio

def crear_onda(amplitud=2, frecuencia=2):
    # Generar los valores del tiempo (t)
    t = np.linspace(0, 2 * np.pi, 1000)  # Genera 1000 puntos entre 0 y 2*pi
    
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
    return y
  

def crea_onda1_y_onda2_alavez(amplitud1, frecuencia1, offset1=0, amplitud2=1, frecuencia2=1, offset2=0):
    # Generar los valores del tiempo (t)
    t = np.linspace(0, 2 * np.pi, 1000)  # Genera 1000 puntos entre 0 y 2*pi
    
    # Generar las dos ondas sinusoidales usando la amplitud, frecuencia y offset dados
    y1 = amplitud1 * np.sin(frecuencia1 * t + offset1)
    y2 = amplitud2 * np.sin(frecuencia2 * t + offset2)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(t, y1, label=f"{frecuencia1} Hz, Amp={amplitud1}, Offset={offset1}")
    plt.plot(t, y2, linestyle='--', label=f"{frecuencia2} Hz, Amp={amplitud2}, Offset={offset2}")
    
    plt.title("Dos Ondas Sinusoidales")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid(True)
    plt.show()


def escuchar_onda (y_data, rate=44100):
    audio_widget = Audio (data=y_data, rate=rate)
    display(audio_widget)


# Test de la función
#crea_onda1_y_onda2_alavez(2, 2, 0, 1, 5, 0)     

# Test de la función
#crear_onda(2, 20)  # Genera una onda sinusoidal de amplitud 2 y frecuencia 2 Hz
# Laboratorio de acústica (ONDAS)

## Antes de resolver los ejercicios debes poner las siguientes líneas en Google Colab

```python
!wget https://raw.githubusercontent.com/AlfonsoDeUna/Laboratorio_Megafonia/main/acustics/megafonia.py

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from megafonia import *

```

## Ejercicios: 

### NOTA: Recuerda que deberás posteriormente subir las respuestas a tu portfolio con imágenes y se tiene que demostrar un buen nivel de adquisición de conocmiento a través de la realización de la tarea

1. **Características básicas de una onda**:
    - a) Utilice la función `crear_onda_vis` para generar y visualizar una onda sinusoidal con amplitud de 1 y frecuencia de 5 Hz. 
    - b) Describe cómo cambia la onda cuando modificas la amplitud. ¿Qué ocurre si aumentas la frecuencia?
    
2. **Exploración de diferentes frecuencias**:
    - a) Genera ondas sinusoidales con frecuencias de 1 Hz, 10 Hz y 50 Hz (mantén la amplitud constante en 2). 
    - b) Describe las diferencias que observas entre estas ondas. ¿Cómo se relaciona la frecuencia con el número de crestas y valles de la onda en un periodo determinado?

3. **Superposición de ondas**:
    - a) Utiliza la función `crea_onda1_y_onda2_alavez_vis` para visualizar la superposición de dos ondas: una con amplitud 2, frecuencia 2 Hz y la otra con amplitud 1 y frecuencia 10 Hz.
    - b) Describe lo que observas en el gráfico. ¿Cómo se combinan las ondas en términos de amplitud?

4. **Suma de ondas**:
    - a) Emplea la función `suma_dos_ondas_vis` para visualizar la suma de dos ondas: una con amplitud 2, frecuencia 2 Hz y la otra con amplitud 1 y frecuencia 5 Hz.
    - b) Compara esta onda resultante con las ondas originales visualizadas por separado. ¿Qué características de la onda resultante puedes relacionar con las ondas originales?

5. **Escucha y compara**:
    - a) Genera una onda utilizando la función `generar_onda` con amplitud 2 y frecuencia 5 Hz. Usa la función `escuchar_onda` para escucharla.
    - b) Genera otra onda con amplitud 2 pero con frecuencia 20 Hz y escúchala. 
    - c) Describe las diferencias que percibes entre los dos sonidos. ¿Cómo se relaciona la frecuencia de la onda con el sonido que escuchas?

6. **Variando la Amplitud**:
    - a) Genera tres ondas sinusoidales con amplitudes de 1, 3 y 5, manteniendo la frecuencia constante en 10 Hz.
    - b) ¿Cómo afecta la amplitud a la altura de las crestas y valles de la onda?

7. **Experimentación con Duración**:
    - a) Utiliza la función `crear_onda_vis` para visualizar una onda de 2 segundos y otra de 5 segundos. 
    - b) ¿Cómo afecta la duración a la longitud total de la onda visualizada?

8. **Influencia del Offset**:
    - a) Genera dos ondas con el mismo valor de amplitud y frecuencia, pero con diferentes valores de offset (por ejemplo, 0 y π/2).
    - b) Describe cómo el offset afecta la fase de la onda.

9. **Exploración de Ondas Combinadas**:
    - a) Usa la función `suma_dos_ondas` para sumar dos ondas con amplitudes y frecuencias distintas.
    - b) ¿Cómo se relaciona la onda resultante con las dos ondas iniciales?

10. **Identificando Ondas por el Sonido**:
    - a) Escucha varias ondas generadas con diferentes frecuencias.
    - b) ¿Eres capaz de adivinar la frecuencia de una onda basándote solo en su sonido?

11. **Relación entre Frecuencia y Tono**:
    - a) Genera ondas de distintas frecuencias y escúchalas.
    - b) ¿Cómo se relaciona la frecuencia con el tono del sonido que escuchas?

12. **Interferencia de Ondas**:
    - a) Utiliza la función `suma_dos_ondas_vis` para sumar dos ondas con la misma amplitud y frecuencia, pero con un offset de π.
    - b) ¿Qué observas? ¿Qué significa esto en términos de interferencia?

13. **Experimentación con Ondas de Baja Frecuencia**:
    - a) Genera y escucha una onda con una frecuencia inferior a 20 Hz.
    - b) ¿Qué percibes? ¿Cómo describirías el sonido (o la falta de él)?

14. **Efecto de la Duración en el Sonido**:
    - a) Crea ondas con distintas duraciones y escúchalas.
    - b) ¿Cómo afecta la duración al sonido que escuchas?

15. **Comparación de Ondas**:
    - a) Utiliza la función `crea_onda1_y_onda2_alavez_vis` para visualizar dos ondas con amplitudes y frecuencias ligeramente distintas.
    - b) ¿Qué patrones o características interesantes observas en la combinación?

16. **Influencia del Offset en la Superposición**:
    - a) Crea y visualiza la suma de dos ondas con idéntica amplitud y frecuencia, pero cambia el offset de una de ellas.
    - b) ¿Qué sucede con la onda resultante cuando varías el offset?

17. **Exploración de Ondas de Alta Frecuencia**:
    - a) Genera y escucha una onda con una frecuencia superior a 20,000 Hz.
    - b) ¿Qué percibes? ¿Cómo se relaciona esto con el rango audible del oído humano?

18. **Interacción de Amplitudes**:
    - a) Crea dos ondas con la misma frecuencia pero con diferentes amplitudes y sumarlas.
    - b) ¿Qué características de la onda resultante se relacionan con las amplitudes de las ondas originales?

19. **Identificación de Características**:
    - a) Visualiza una onda sinusoidal y estima su amplitud y frecuencia basándote en el gráfico.
    - b) Utiliza las funciones para comprobar tus estimaciones. ¿Qué tan cerca estabas?

20. **Onda y Silencio**:
    - a) Combina una onda con su inversa (amplitud negativa). Escucha el resultado.
    - b) Describe lo que escuchas y explica por qué ocurre eso.


# LABORATORIO DE MEGAFONÍA

## Introducción

He creado este código para poder realizar las prácticas de acústica
para alumnos de formación profesional de Instalaciones de Telecomunicaciones para
el módulo profesional Instalaciones de Megafonía y sonorización. 

El código está especialmente diseñado para enfocarnos en los conceptos de megafonía
abstrayendo todo lo que tenga que ver con python. Los alumnos no necesitan saber programar en 
Python. Aunque algún concepto básico, cómo lanzar funciones e importación de funciones, sí que sería
conveniente.

## Google Colab

Las prácticas se realizarán en Google Colab para poder utilizar el código que he creado
para poder realizar las prácticas. Hay que importarlo del siguiente modo.

```python

!wget https://raw.githubusercontent.com/AlfonsoDeUna/Laboratorio_Megafonia/main/acustics/megafonia.py

```
## Funciones principales

**crear_onda_vis(amplitud, frecuencia, duration):** Crea y visualiza una onda sinusoidal con amplitud, frecuencia y duración especificadas.

**generar_onda(amplitud, frecuencia, duration):** Genera y retorna una onda sinusoidal.

**crea_onda1_y_onda2_alavez_vis(amplitud1, frecuencia1, offset1, amplitud2, frecuencia2, offset2):** Crea y visualiza dos ondas sinusoidales con parámetros especificados.

**suma_dos_ondas_vis(amplitud1, frecuencia1, offset1, amplitud2, frecuencia2, offset2):** Visualiza la suma de dos ondas sinusoidales.

**suma_dos_ondas(amplitud1, frecuencia1, offset1, amplitud2, frecuencia2, offset2):** Retorna la suma de dos ondas sinusoidales.

**escuchar_onda(y_data):** Permite escuchar el sonido generado por una onda.

**dibujar_onda(y_data):** Dibuja una onda dada su data.

## Elementos del laboratorio

crear_onda_vis (amplitud, frecuencia, tiempo): Genera una onda con la amplitud, frecuencia y tiempo que tu quieras 

``` python
from megafonia import crear_onda_vis

crear_onda_vis (2,2,3)

crear_onda_vis(2,2000,0.05)


```

onda = generar_onda (amplitud, frecuencia): Crea una gráfica de una señal pura de amplitud y frecuencia modificables

escuchar_onda (onda): Podrás escuchar la onda que has creado.

``` python
import os
from IPython.display import Audio
from megafonia import generar_onda, escuchar_onda

display(Audio (generar_onda(10,5200,3), rate=44100))

```
``` python 
import os
from IPython.display import Audio
from megafonia import crea_onda1_y_onda2_alavez_vis

crea_onda1_y_onda2_alavez_vis(2, 2, 0, 1, 5, 0)
```

## Ejemplos de Uso
Generar y visualizar una onda sinusoidal de amplitud 2 y frecuencia 20 Hz:

```python
crear_onda_vis(2, 20)
```

Crear y visualizar la suma de dos ondas sinusoidales con parámetros específicos:

```python
crea_onda1_y_onda2_alavez_vis(2, 2, 0, 1, 5, 0)
```

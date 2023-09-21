# LABORATORIO DE MEGAFONÍA

## Introducción

He creado este código para poder realizar las prácticas de acústica
para alumnos de formación profesional de Instalaciones de Telecomunicaciones para
el módulo profesional Instalaciones de Megafonía y sonorización. 

El código está especialmente diseñado para enfocarnos en los conceptos de megafonía
abstrayendo todo lo que tenga que ver con python. Los alumnos no necesitan que
sepan programar. Aunque algún concepto básico de cómo lanzar funciones, sí que sería
conveniente.

## Google Colab

Las prácticas se realizarán en Google Colab para poder utilizar el código que he creado
para poder realizar las prácticas. Hay que importarlo del siguiente modo.

```python

!wget https://raw.githubusercontent.com/AlfonsoDeUna/Laboratorio_Megafonia/main/acustics/megafonia.py

```

## Elementos del laboratorio

crear_onda_vis (amplitud, frecuencia, tiempo): Genera una onda con la amplitud, frecuencia y tiempo que tu quieras 

``` python
crear_onda_vis (2,2,3)

crear_onda_vis(2,2000,0.05)


```

onda = generar_onda (amplitud, frecuencia): Crea una gráfica de una señal pura de amplitud y frecuencia modificables

escuchar_onda (onda): Podrás escuchar la onda que has creado.

``` python

y = generar_onda(10,2000,3)
display(Audio (data=y, rate=44100))

```

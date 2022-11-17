import Guía_9_clases_figuras


rectángulo = Guía_9_clases_figuras.Rectángulo(1, 10)
print(rectángulo)
print("base", rectángulo.base)
print("altura", rectángulo.altura)
print("área", rectángulo.área)
print("diagonal", rectángulo.diagonal)
rectángulo.base = 3
print(rectángulo)
rectángulo.altura = 7
print(rectángulo)

cuadrado = Guía_9_clases_figuras.Cuadrado(9)
print(cuadrado)
print("base", cuadrado.base)
print("altura", cuadrado.altura)
print("área", cuadrado.área)
print("diagnoal", cuadrado.diagonal)
cuadrado.lado = 4
print(cuadrado)
cuadrado.base = 5
print(cuadrado)
cuadrado.altura = 6
print(cuadrado)
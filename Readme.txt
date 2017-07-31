Instrucciones de ejecución:

El código fue escrito en Python. Basta colocar la opción "Run" en 
algún IDE (por ej. Pycharm) para ejecutar el programa.

Existen dos clases:
La primera es la clase Montana, que recibe los parámetros ancho, alto
en metros; y h, que es el espaciado de la malla.
Existe un método dentro de esta clase llamado setHeight, que recibe un
parámetro a que representa la columna donde se comienzan a generar las
montañas.

La segunda clase es Paisaje, que recibe un objeto de la clase Montana,
una hora (int), el número de puntos que ocupa el mar horiontalmente 
dentro de la matriz (nMar), la altura del mar (en gral. altMar es 
cero), el ancho y el alto de la matriz como parámetros.
Esta tiene los métodos __str__ que imprime la matriz, iterate(alto, ancho),
que itera sobre la matriz teniendo asignadas las condiciones iniciales, 
y el método plot, que grafica la matriz.

En el método principal (main) se dejan ejemplos (gráficos requeridos 
del problema) para ilustrar como se llama a cada clase y se ocupa cada 
método.


Instrucciones de ejecuci�n:

El c�digo fue escrito en Python. Basta colocar la opci�n "Run" en 
alg�n IDE (por ej. Pycharm) para ejecutar el programa.

Existen dos clases:
La primera es la clase Montana, que recibe los par�metros ancho, alto
en metros; y h, que es el espaciado de la malla.
Existe un m�todo dentro de esta clase llamado setHeight, que recibe un
par�metro a que representa la columna donde se comienzan a generar las
monta�as.

La segunda clase es Paisaje, que recibe un objeto de la clase Montana,
una hora (int), el n�mero de puntos que ocupa el mar horiontalmente 
dentro de la matriz (nMar), la altura del mar (en gral. altMar es 
cero), el ancho y el alto de la matriz como par�metros.
Esta tiene los m�todos __str__ que imprime la matriz, iterate(alto, ancho),
que itera sobre la matriz teniendo asignadas las condiciones iniciales, 
y el m�todo plot, que grafica la matriz.

En el m�todo principal (main) se dejan ejemplos (gr�ficos requeridos 
del problema) para ilustrar como se llama a cada clase y se ocupa cada 
m�todo.


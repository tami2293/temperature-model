# coding=utf-8

import math
import random
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import tqdm
import copy

# Constantes
ITERATIONS = 10000

class Montana(object):

    def __init__(self, ancho, alto, h):
        """
                Constructor
                :param ancho: Ancho del sistema
                :param alto: Alto del sistema
                :param h: Espaciado de la malla
                """

        self.ancho = ancho
        self.alto = alto
        self.dh = h

        self.w = ancho / h
        self.h = alto / h

        self.matrix = np.zeros((self.h, self.w))

        # Porcentaje y altura que ocupa el mar
        self.nMar = int(math.ceil((np.random.random_sample() * 400 + 1200) / 5))
        self.altMar = self.h - 1

        # Montañas
        self.setHeight(self.nMar + 21)

    def setHeight(self, a):
        ya = 399
        self.matrix[ya, a] = np.nan
        for j in range(a, 799):
            if ya >= 397:
                r = 1 #Si la altura es mín, entonces obligatoriamente subir uno
            elif ya == 10:
                r = -1 #Si la altura es máx, entonces obligatoriamente bajar uno
            else:
                r = random.randrange(-3, 4, 1) #Si no, elegir aleatoriamente entre subir o bajar
            ya -= r
            for i in range(ya, 400):
                self.matrix[i, j + 1] = np.nan

class Paisaje(object):

    def __init__(self, montana, hora, nMar, altMar, w, h):

        self.matrix = copy.copy(montana.matrix)

        #Condicion borde de mar
        if (0 <= hora <= 8):
            tMar = 4.0
        elif (8 < hora <= 16):
            tMar = 2.0 * hora - 12
        else:
            tMar = -2.0 * hora + 52

        for j in range(0, nMar + 1):
            self.matrix[altMar, j] = tMar

        #Condicion de borde atmosfera
        for i in range(altMar - 1, -1, -1):
            for j in range(0, w):
                if self.matrix[i,j] == 0:
                    self.matrix[i, j] = 0.03*(i - altMar) + tMar

        #Condicion de borde planta
        for j in range(nMar+1, nMar+21):
            self.matrix[399, j] = 500.0*(math.cos(hora*math.pi/12.0)+2.0)


    def __str__(self):
        """
        Imprime la matriz
        :return:
        """
        print self.matrix
        for j in range(0, 800):
            print self.matrix[399,j]
        return ''

    def iterate(self, h, w):
        """
        Itera
        :return: Retorna nada, hace algo
        """

        for _ in tqdm.tqdm(range(ITERATIONS)):

            # Trabajamos en el interior del sistema
            for i in range(1, h - 1):  # fila
                for j in range(1, w - 1):  # columnas
                    if not np.isnan(self.matrix[i, j]):
                        sumaNan = 0
                        if (np.isnan(self.matrix[i + 1, j])):
                            sumaNan += 15
                        else:
                            sumaNan += self.matrix[i + 1, j]

                        if (np.isnan(self.matrix[i, j - 1])):
                            sumaNan += 15
                        else:
                            sumaNan += self.matrix[i, j - 1]

                        if (np.isnan(self.matrix[i, j + 1])):
                            sumaNan += 15
                        else:
                            sumaNan += self.matrix[i, j + 1]

                        self.matrix[i, j] = 0.25 * (
                            sumaNan + self.matrix[i - 1, j])

    def plot(self):
        """
        Plotea la solución
        :return:
        """

        # Se define el fondo negro
        mpl.rcParams['axes.facecolor'] = '666666'

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # Se agrega grafico al plot
        extnt = [0, 800, 0, 400]
        cax = ax.imshow(self.matrix, cmap = 'gist_stern', vmin = -8, vmax = 1500, extent = extnt)
        fig.colorbar(cax)

        plt.show()


if __name__ == '__main__':
    montana = Montana(4000, 2000, 5)
    paisaje = Paisaje(montana, 0, montana.nMar, montana.altMar, montana.w, montana.h)
    paisaje.iterate(montana.h, montana.w)
    print paisaje
    paisaje.plot()
    paisaje = Paisaje(montana, 8, montana.nMar, montana.altMar, montana.w, montana.h)
    paisaje.iterate(montana.h, montana.w)
    print paisaje
    paisaje.plot()
    paisaje = Paisaje(montana, 12, montana.nMar, montana.altMar, montana.w, montana.h)
    paisaje.iterate(montana.h, montana.w)
    print paisaje
    paisaje.plot()
    paisaje = Paisaje(montana, 16, montana.nMar, montana.altMar, montana.w, montana.h)
    paisaje.iterate(montana.h, montana.w)
    print paisaje
    paisaje.plot()
    paisaje = Paisaje(montana, 20, montana.nMar, montana.altMar, montana.w, montana.h)
    paisaje.iterate(montana.h, montana.w)
    print paisaje
    paisaje.plot()







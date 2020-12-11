"""
.. module:: analisis
   :platform: Linux, Windows
   :synopsis: Generadores de muestras aleatorias.

.. moduleauthor:: Gastón Speciale <gasticai@hotmail.com>,
                  Fernando Quinteros <lordfers@gmail.com>,
                  Alejandro Araneda <eloscurodeefeso@gmail.com>

    El presente módulo :mod:`analisis` contiene las funciones
    que calculan los estadísticos de las muestras.

"""
from math import sqrt, trunc
from collections import Counter

def media_muestral(muestra):
    """
    Calcula la media muestral o promedio de valores de una muestra

    :param muestra: listado de valores de la variable aleatoria
    :type muestra: List[float]
    :return: devuelve la media muestral
    :rtype: float
    """
    return sum(muestra) / len(muestra)

def varianza_muestral(muestra):
    """
    Calcula la varianza muestral insesgada

    :param muestra: listado de valores de la variable aleatoria
    :type muestra: List[float]
    :return: devuelve la varianza muestral
    :rtype: float
    """
    media = media_muestral(muestra)
    return sum([(x - media)**2 for x in muestra]) / (len(muestra) - 1)

def desviacion_estandar_muestral(muestra):
    """
    Calcula la desviación estandar o raiz de la varianza muestral insesgada

    :param muestra: listado de valores de la variable aleatoria
    :type muestra: List[float]
    :return: devuelve la desviación estandar de la muestra
    :rtype: float
    """
    return sqrt(varianza_muestral(muestra))

def frecuencias(muestra, binsize):
    """
    Contabiliza las frecuencias absolutas de los valores 
    de una muestra agrupados por clases del mismo ancho de banda 

    :param muestra: listado de valores de la variable aleatoria
    :type muestra: List[float]
    :param binsize: tamaño del ancho de banda de las clases
    :type binsize: float
    :return: listado de freceuncias absolutas para cada clase
        incluyendo clases con frecuencia cero.
    :rtype: List[float]
    """
    freq = Counter()
    minim = min(muestra)
    for dat in muestra:
        freq[trunc((dat - minim)/binsize)] += 1
    return [freq.get(x, 0) for x in range(max(freq.keys()) + 1)]

def estadist(muestra):
    """
    Funcion auxiliar para la presentacion de la media y varianza muestrales

    :param muestra: listado de valores de la variable aleatoria
    :type muestra: List[float]
    """
    print("Media muestral: %.2f - Varianza muestral: %.2f" %
          (media_muestral(muestra), varianza_muestral(muestra)))


"""
.. module:: simulador
   :platform: Linux, Windows
   :synopsis: Generadores de muestras aleatorias.

.. moduleauthor:: Gastón Speciale <gasticai@hotmail.com>,
                  Fernando Quinteros <lordfers@gmail.com>,
                  Alejandro Araneda <eloscurodeefeso@gmail.com>

    El presente módulo :mod:`simulador` contiene las funciones
    generadoras de muestras aleatorias con cierta distribución.

"""
from random import random, randint
from math import log, trunc, sqrt, cos, sin, pi

def uniformdis(size, min, max):
    """
    Generador de muestra con base en una distribución uniforme discreta.

    :param size: tamaño de la muestra
    :type size: int
    :param min: valor mínimo de la variable aleatoria
    :type min: int
    :param max: valor máximmo de la variable aleatoria
    :type max: int
    :return: una lista con posibles valores de la variable aleatoria
    :rtype: List[int]
    """
    return [randint(min, max) for _ in range(size)]

def uniform(size, min=0, max=1):
    """
    Generador de muestra con base en una distribución uniforme continua.

    :param size: tamaño de la muestra
    :type size: int
    :param min: valor mínimo de la variable aleatoria, defaults to 0
    :type min: float, optional
    :param max: valor máximmo de la variable aleatoria, defaults to 1
    :type max: float, optional
    :return: una lista con posibles valores de la variable aleatoria
    :rtype: List[float]
    """
    return [(max - min) * random() + min for _ in range(size)]

def bernoulli(size, p):
    """
    Generador de una muestra con resultados de un experimento Bernoulli

    :param size: tamaño de la muestra
    :type size: int
    :param p: probabilidad de obtener un éxito
    :type p: float
    :return: una lista con posibles valores de la variable aleatoria
    :rtype: List[bool]
    """
    return [random() <= p for _ in range(size)]

def binomial(size, tries, p):
    """
    Generador de una muestra con base en una distribución binomial

    :param size: tamaño de la muestra
    :type size: int
    :param tries: cantidad de experimentos Bernoulli
    :type tries: int
    :param p: probabilidad de obtener un éxito
    :type p: float
    :return: una lista con posibles valores de la variable aleatoria
    :rtype: List[int]
    """
    return [sum(bernoulli(tries, p)) for _ in range(size)]

def exponencial(size, beta=1):
    """
    Generador de una muestra con base en una distribución exponencial

    :param size: tamaño de la muestra
    :type size: int
    :param beta: media de la distribución exponencial, defaults to 1
    :type beta: float, optional
    :return: una lista con posibles valores de la variable aleatoria
    :rtype: List[float]
    """
    return [-beta * log(1 - x) for x in uniform(size)]

class Normal:
    """
    Clase contenedora para la enumeración de métodos de simulación normal
    """
    Rejection = 1
    """
    Constante correspondiente al método de aceptación y rechazo
    """
    BoxMuller = 2
    """
    Constante correspondiente al métodos de aproximación Box-Müller
    """

def normal(size, mu=0, sigma=1, method=Normal.BoxMuller):
    """
    Generador de muestra con base en una distribución normal.

    :param size: tamaño de la muestra
    :type size: int
    :param mu: media de la distribución normal de base, defaults to 0
    :type mu: float, optional
    :param sigma: desviación estandar de la distribución de base, defaults to 1
    :type sigma: float, optional
    :param method: método de simualción entre :attr:`Normal.Rejection` o 
        :attr:`Normal.BoxMuller`, defaults to :attr:`Normal.Rejection`
    :type method: int, optional
    :return: una lista con posibles valores de la variable aleatoria
    :rtype: List[float]
    :raises: ValueError: si no es uno de los metodos definidos 
        en la clase :class:`simulador.Normal`
    """
    if method == Normal.Rejection:
        func = normal_rejection
    elif method == Normal.BoxMuller:
        func = normal_boxmuller
    else:
        raise ValueError("method must be Normal.Rejection o Normal.BoxMuller")
    return func(size, mu, sigma)

def normal_boxmuller(size, mu=0, sigma=1):
    """
    Implementación de la simulación normal con la aproximación de Box-Müller.

    :param size: tamaño de la muestra
    :type size: int
    :param mu: media de la distribución normal de base, defaults to 0
    :type mu: float, optional
    :param sigma: desviación estandar de la distribución de base, defaults to 1
    :type sigma: float, optional
    :rtype: List[float]
    """
    sample=[]
    while size != 0:
        unif1 = random()
        unif2 = random()
        norm1 = sqrt(-2*log(unif1))*cos(2*pi*unif2) * sigma + mu
        norm2 = sqrt(-2*log(unif1))*sin(2*pi*unif2) * sigma + mu
        if size % 2 == 0:
            size -= 1
            sample.append(norm2)
        size -= 1
        sample.append(norm1)
    return sample

def normal_rejection(size, mu=0, sigma=1):
    """
    Implementación de la simulación normal con el método de aceptación y rechazo.

    :param size: tamaño de la muestra
    :type size: int
    :param mu: media de la distribución normal de base, defaults to 0
    :type mu: float, optional
    :param sigma: desviación estandar de la distribución de base, defaults to 1
    :type sigma: float, optional
    :return: una lista con posibles valores de la variable aleatoria
    :rtype: List[float]
    """ 
    sample = []
    for _ in range(size):
        x = -log(1 - random())
        y = -log(1 - random())
        while x < ((y - 1)**2)/2:
            y = -log(1 - random())
        if random() < 0.5:
            y = -y
        sample.append(y * sigma + mu)
    return sample

def empirica(size, sample):
    """
    Generador de una muestra con base en la distribución empírica de otra.

    :param size: tamaño de la muestra
    :type size: int
    :param sample: muestra que se utilizará como distribución empírica
    :type sample: List
    :return: una lista con posibles valores de la variable aleatoria
    :rtype: List
    """
    return [sorted(sample)[trunc(random() * len(sample))] for _ in range(size)]
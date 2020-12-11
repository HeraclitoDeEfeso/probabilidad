from numpy import arange
import matplotlib.pyplot as plot

def histograma(sample, gaps, relative=False):
    """
    Graficador de histogramas por ancho de bandas

    :param sample: muestra a graficar
    :type sample: List
    :param gaps: listado de anchos de banda para las clases
    :type gaps: List[float]
    :param relative: transforma los pesos en relativos, default to False
    :type relative: bool
    """
    weights = [1/len(sample) for _ in sample] if relative else None
    _, p = plot.subplots(1, len(gaps))
    p = [p] if len(gaps) == 1 else p  
    for i, gap in enumerate(gaps):
        p[i].hist(sample, \
                arange(min(sample), max(sample) + gap, gap), weights=weights)
    plot.figure(num=1, figsize=(8, 18))
    plot.subplots_adjust(wspace=0.5)
    plot.show()
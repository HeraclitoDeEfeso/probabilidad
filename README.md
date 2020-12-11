# Universidad Nacional de Tres de Febrero

## Ingeniería en Computación

### Probabilidad y Estadística

### Trabajo Práctico

| Discución | Resolución
|- |-
| Lenguaje de Desarrollo | Python
| Librerías gráficas | matplotlib
| Estructura de carpetas | ninguna
| Estilo de documentación | Sphix
| Estructura del Informe |
| Formato de Informe |
| Herramienta de test | unittest
| Diseño de clases | no
| División de implementación y test | no

# Informe
| Sección | Persona asignada 
|- |-
| Introducción |
| Resumen |
| Entorno de desarrollo |
| Instrucciones de ejecución |
| Patrones de diseño |
| Descripción de archivos |
| Parte 2 |
| Parte 3 |
| Parte 4 |
| Anexo Autodocumentación |

## Resumen
_TODO_
- [ ] Al finalizar el trabajo elaborar un resumen de un párrafo que describa el objetivo de la práctica de forma que resulte interesante.

## Introducción

_TODO_

- [ ] Explicar el uso de la función aleatoria uniforme normalizada para construir un experimento Bernoulli y una muestra Binomial
- [ ] Explicar el uso del método de función inversa para obtener una muestra de distribución exponencial
- [ ] Explicar el método para obtener una muestra de distribución normal

## Descripción de la práctica

### Enunciado

#### Parte 1: Simulación

En esta primera parte, construiremos varios generadores de números aleatorios que usaremos para obtener muestras con distribu-
ción conocida sobre las que vamos a trabajar posteriormente.
- [X] 1. Utilizando únicamente la función random de su lenguaje (la función que genera un número aleatorio uniforme entre 0 y 1),
implemente una función que genere un número distribuido Bernoulli con probabilidad p.
- [X] 2. Utilizando la función del punto anterior, implemente otra que genere un número binomial con los parámetros n,p.
- [X] 3. Utilizando el procedimiento descrito en el capítulo 6 del Dekking (método de la función inversa o de Monte Carlo), imple-
mentar una función que permita generar un número aleatorio con distribución Exp(λ).
- [X] 4. Investigar como generar números aleatorios con distribución normal. Implementarlo.

#### Parte 2: Estadística descriptiva

Ahora vamos a aplicar las técnicas vistas en la materia al estudio de algunas muestras de datos.
- [X] 1. Generar tres muestras de números aleatorios Exp(0,5) de tamaño n = 10, n = 30 y n = 200. Para cada una, computar la media
y varianza muestral. ¿Qué observa?
- [X] 2. Para las tres muestras anteriores, graficar los histogramas de frecuencias relativas con anchos de banda 0,4, 0,2 y 0,1; es decir,
un total de 9 histogramas. ¿Qué conclusiones puede obtener?
- [X] 3. Generar una muestra de números Bin(10,0,3) de tamaño n = 50. Construir la función de distribución empírica de dicha
muestra.
- [X] 4. A partir de la función de distribución empírica del punto anterior, generar una nueva muestra de números aleatorios utili-
zando el método de simulación de la primera parte. Computar la media y varianza muestral y graficar el histograma.
- [X] 5. Repetir el experimento de los dos puntos anteriores con dos muestras aleatorias más generadas con los mismos parámetros.
¿Qué conclusión saca?

#### Parte 3: Convergencia

El propósito de esta sección es ver en forma práctica los resultados de los teoremas de convergencia.

- [X] 1. Generar cuatro muestras de números aleatorios de tamaño 100, todas con distribución binomial con p = 0,40 y n = 10, n = 20,
n = 50 y n = 100 respectivamente. Graficar sus histogramas. ¿Qué observa?
- [X] 2. Elija la muestra de tamaño 200 y calcule la media y desviación estándar muestral. Luego, normalice cada dato de la muestra
y grafique el histograma de la muestra normalizada. Justifique lo que observa.
- [X] 3. Para cada una de las muestras anteriores, calcule la media muestral. Justifique lo que observa.

#### Parte 4: Estadística inferencial

Para terminar, vamos a hacer inferencia con las muestras que generamos y obtener así información sobre sus distribuciones.
- [ ] 1. Generar dos muestras N(100,5), una de tamaño n = 10 y otra de tamaño n = 30. Obtener estimaciones puntuales de su media
y varianza.
- [ ] 2. Suponga que ya conoce el dato de que la distribución tiene varianza 5. Obtener intervalos de confianza del 95% y 98% para
la media de ambas muestras.
- [ ] 3. Repita el punto anterior pero usando la varianza estimada s2, para la muestra de tamaño adecuado.
- [ ] 4. Probar a nivel 0,99 la hipótesis de que la varianza sea σ2 > 5. Calcular la probabilidad de cometer error tipo II para la hipótesis
alternativa σ2 = 6.
- [ ] 5. Agrupando los datos en subgrupos de longitud 0,5, probar a nivel 0,99 la hipótesis de que la muestra proviene de una distribución normal.

### Entorno de desarrollo
_TODO_
- [ ] Explicitar el entorno y lenguaje de programación elegido. Explicitar las extensiones del lenguaje (librerías) elegidas.
- [ ] Comentar método de documentación elegido y estilo de programación (si hay). Trabajo colaborativo.

En todos los casos agregar a las referencias el software y las normas.

### Instrucciones de ejecución
_TODO_
- [ ] Describir los pasos para clonar, instalar dependencias y correr los test y los módulos/aplicaciones.

## Parte 1: Simulación
_TODO_
- [ ] Referenciar el anexo de autodocumentación de código.
- [ ] Agregar descripción de archivos si no estás

## Parte 2: Estadística descriptiva
_TODO_
- [X] Generar la notebook donde se utilizan los módulos implementados para resolver los ejercición y elaborar conclusiones parciales.

## Parte 3: Convergencia
_TODO_
- [X] Generar la notebook donde se utilizan los módulos implementados para resolver los ejercición y elaborar conclusiones parciales.

## Parte 4: Estadística inferencial
_TODO_
- [X] Generar la notebook donde se utilizan los módulos implementados para resolver los ejercición y elaborar conclusiones parciales.

## Conclusiones
_TODO_
- [ ] Elaborar conclusiones generales sobre el objetivo de la práctica.
- [ ] Elaborar el apartado de Resumen.
- [ ] Comentar la experiencia del trabajo en grupo.
- [ ] Comentar la experiencia con las herramientas elegidas.
- [ ] Opinión sobre la práctica y la cursada virtual (opcional)

## Referencias
_TODO_
- [ ] Agregar las que corresponden a la teoría de simulación.
- [ ] Agregar las que corresponden al software utilizado.
- [ ] Agregar las que corresponden las normas de programación y diseño.
- [ ] Agregar las que correspondan a conceptos de probabilidad en la resolución de la Parte 2.
- [ ] Agregar las que correspondan a conceptos de probabilidad en la resolución de la Parte 3.
- [ ] Agregar las que correspondan a conceptos de probabilidad en la resolución de la Parte 4.

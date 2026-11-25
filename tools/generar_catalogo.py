#!/usr/bin/env python3
"""Compila un catálogo pedagógico legible a JSON y JS sin dependencias."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
M=[]
def add(id,title,area,grades,summary,why,steps,examples,trap,tip,visual,gen,strong=(),weak=(),minutes=25):
    M.append(dict(id=id,title=title,area=area,grades=grades.split(),summary=summary,why=why,
        steps=steps.split(' | '),examples=[dict(q=a,work=b,answer=c) for a,b,c in examples],
        trap=trap,tip=tip,visual=visual,generator=gen,strong=list(strong),weak=list(weak),minutes=minutes))
add('recta-fracciones','Fracciones en la recta numérica','Números','5P 6P 1E',
 'Una fracción nombra cuántas partes iguales tomamos de una unidad. También puede ser mayor que 1.',
 'La recta muestra que una fracción es un número, no dos números aislados.',
 'Identifica el tramo entre 0 y 1. | Divide esa unidad en tantas partes iguales como indica el denominador. | Cuenta desde 0 tantas partes como indica el numerador. | Si el numerador supera al denominador, continúa más allá del 1.',
 [('Sitúa 3/4 entre 0 y 1.','Divide la unidad en 4 intervalos iguales y avanza 3 desde cero.','En el punto 0,75.'),('Sitúa 7/4.','Avanza 7 cuartos: 4/4 + 3/4.','1 y 3/4, entre 1 y 2.')],
 'Dividir el segmento en 3 trozos cuando el denominador es 4. Los extremos se cuentan como puntos, no como tramos.',
 'Para comprobar, piensa: ¿la fracción es menor, igual o mayor que 1?', 'fraction-line','fractionline')
add('fracciones-equivalentes','Fracciones equivalentes','Números','5P 6P 1E 2E',
 'Dos fracciones son equivalentes cuando representan el mismo valor, aunque tengan números diferentes.',
 'Necesitamos equivalencias para comparar y sumar fracciones con denominadores distintos.',
 'Multiplica numerador y denominador por el mismo número. | También puedes dividir ambos por un divisor común. | Comprueba multiplicando en cruz: a/b = c/d si a·d = b·c. | Simplifica hasta que no haya divisor común mayor que 1.',
 [('¿2/3 y 6/9 representan lo mismo?','2×3=6 y 3×3=9; además 2×9=3×6=18.','Sí, son equivalentes.'),('Simplifica 18/24.','Ambos son divisibles entre 6: 18÷6=3 y 24÷6=4.','3/4.')],
 'Multiplicar solo el numerador (2/3 → 4/3) cambia el valor de la fracción.',
 'Imagina dos barras iguales divididas en 3 y 6 partes: colorear 2/3 es lo mismo que colorear 4/6.', 'fractions','equivalence',('recta-fracciones',))
add('comparar-fracciones','Comparación y orden','Números','5P 6P 1E 2E',
 'Comparar fracciones significa decidir cuál representa más de la misma unidad.',
 'Permite ordenar cantidades sin depender de dibujos o calculadora.',
 'Si los denominadores son iguales, compara numeradores. | Si los numeradores son iguales y positivos, el menor denominador da partes mayores. | En el resto, utiliza denominador común o productos cruzados. | Escribe <, > o = y comprueba con una estimación.',
 [('Compara 3/4 y 5/8.','3/4=6/8, y 6/8 es mayor que 5/8.','3/4 > 5/8.'),('Compara 2/3 y 4/6.','2×6=12 y 4×3=12.','=; son equivalentes.')],
 'Pensar que 1/8 es mayor que 1/4 porque 8 es más grande. En realidad, los octavos son trozos más pequeños.',
 'Con dos fracciones positivas a/b y c/d puedes comparar a·d con c·b.', 'fractions','compare',('fracciones-equivalentes',))
add('sumar-restar-fracciones','Suma y resta de fracciones','Números','5P 6P 1E 2E',
 'Solo se suman o restan directamente numeradores si las fracciones tienen el mismo denominador.',
 'Es la base de ecuaciones con fracciones, medidas y proporciones.',
 'Busca un denominador común (mejor, el mínimo común múltiplo). | Reescribe cada fracción de forma equivalente. | Suma o resta los numeradores; deja el denominador común. | Simplifica, comprueba el signo y estima si el resultado tiene sentido.',
 [('Calcula 1/2 + 1/3.','Mínimo común denominador: 6. 1/2=3/6 y 1/3=2/6. 3/6+2/6=5/6.','5/6.'),('Calcula 3/4 − 1/6.','m.c.m.(4,6)=12. 9/12−2/12=7/12.','7/12.')],
 'Sumar también los denominadores: 1/2+1/3 NO es 2/5.',
 'Cuando uses la calculadora, convierte a decimal solo para comprobar, no para sustituir el razonamiento.', 'fraction-ops','fracadd',('fracciones-equivalentes','comparar-fracciones'))
add('multiplicar-fracciones','Producto de fracciones','Números','5P 6P 1E 2E',
 'Multiplicar por una fracción es tomar una parte de otra cantidad.',
 'Permite resolver porcentajes y escalas. Por ejemplo, 2/3 de 3/4 es 1/2.',
 'Multiplica numeradores entre sí. | Multiplica denominadores entre sí. | Simplifica el resultado. | Comprueba si multiplicar por una fracción menor que 1 reduce la cantidad positiva.',
 [('2/3 × 3/4','Numerador: 2×3=6; denominador: 3×4=12; simplifica 6/12.','1/2.'),('1/2 de 18','Tomar la mitad equivale a 18×1/2.','9.')],
 'Multiplicar en cruz; eso puede servir para comparar, pero no para multiplicar fracciones.',
 'Antes de multiplicar puedes simplificar factores cruzados para trabajar con números pequeños.', 'fraction-ops','fracmul',('fracciones-equivalentes',))
add('dividir-fracciones','División de fracciones','Números','6P 1E 2E',
 'Dividir por una fracción no nula equivale a multiplicar por su inversa.',
 'Explica cuántos grupos de una medida caben en otra y reaparece en álgebra.',
 'Conserva la primera fracción. | Invierte el numerador y denominador de la segunda. | Multiplica como en un producto de fracciones. | Simplifica y comprueba que el divisor no sea cero.',
 [('3/4 ÷ 1/2','Multiplica 3/4 × 2/1 = 6/4.','3/2.'),('¿Cuántos medios hay en 3?','3 ÷ 1/2 = 3 × 2.','6 medios.')],
 'Invertir las dos fracciones o dividir numerador entre numerador sin justificación.',
 'Piensa: dividir por 1/2 da el doble, porque hay dos mitades en cada unidad.', 'fraction-ops','fracdiv',('multiplicar-fracciones',))
add('enteros-signos','Números enteros y signos','Números','6P 1E 2E 3E',
 'Los enteros incluyen negativos, cero y positivos; los signos indican posición y operaciones.',
 'Evita errores en ecuaciones, coordenadas y funciones.',
 'Representa negativos a la izquierda del 0. | Para sumar signos distintos, compara valores absolutos. | Restar equivale a sumar el opuesto. | En productos y divisiones, signos iguales dan positivo y distintos negativo.',
 [('−4 + 7','Desde −4 avanza 7 unidades a la derecha.','3.'),('−3 × (−5)','Dos factores negativos producen positivo: 3×5.','15.')],
 'Confundir −(−5)=5 con −5, o aplicar la regla de signos de productos a las sumas.',
 'Para una suma de enteros, una recta numérica suele ser más clara que memorizar una regla mal entendida.', 'number-line','integers',('recta-fracciones',))
add('potencias','Potencias y raíces: inicio','Números','5P 6P 1E 2E 3E',
 'Una potencia repite una multiplicación del mismo factor; una raíz cuadrada deshace un cuadrado perfecto.',
 'Aparecen en áreas, escalas, notación científica, polinomios y parábolas.',
 'Lee base y exponente: 3⁴ significa cuatro factores 3. | No confundas 3⁴ con 3×4. | Recuerda que (−2)²=4 y −2²=−4. | Para √25 busca el número no negativo cuyo cuadrado es 25.',
 [('3⁴','3×3×3×3.','81.'),('√49','7×7=49 y √ nombra la raíz principal.','7.')],
 'Leer 2⁶ como 2×6 (12) en lugar de 2×2×2×2×2×2 (64).',
 'Expande una potencia pequeña con sus factores antes de usar una regla.', 'squares','powers',('enteros-signos',))
add('porcentajes','Porcentajes de una cantidad','Números','5P 6P 1E 2E 3E',
 'Un porcentaje es una fracción de cien: 25 % = 25/100 = 1/4.',
 'Sirve para descuentos, impuestos, estadísticas y aumentos.',
 'Convierte el porcentaje en fracción o decimal. | Multiplica por la cantidad de referencia. | Si piden precio final con descuento, resta lo calculado. | Comprueba: el 10 % de 80 es 8; el 50 % es 40.',
 [('25 % de 80','25/100 × 80 = 1/4 × 80.','20.'),('Un descuento del 15 % sobre 60 €','Descuento: 0,15×60=9; precio: 60−9.','51 €.')],
 'Calcular el 20 % de una cantidad y tomarlo directamente como precio final tras un descuento.',
 'El 1 % es dividir entre 100; el 10 %, dividir entre 10.', 'percent','percent',('multiplicar-fracciones',))
add('proporcionalidad','Proporcionalidad y regla de tres','Números','6P 1E 2E 3E',
 'Dos magnitudes son directamente proporcionales si se multiplican por el mismo factor.',
 'Permite resolver recetas, escalas, precios y velocidades sencillas.',
 'Comprueba que las magnitudes sean realmente proporcionales. | Escribe parejas de valores con sus unidades. | Halla el valor unitario o el factor de escala. | Calcula y verifica si la respuesta aumenta o disminuye de forma coherente.',
 [('3 cuadernos cuestan 6 €. ¿Cuánto cuestan 5?','Cada cuaderno cuesta 6÷3=2 €. Por cinco: 5×2.','10 €.'),('4 personas necesitan 12 vasos. ¿Y 6 personas?','12÷4=3 vasos/persona; 6×3.','18 vasos.')],
 'Usar regla de tres directa para una relación inversa sin comprobar el contexto.',
 'El método del valor unitario suele ser más fácil que una fórmula memorizada.', 'bars','proportion',('fracciones-equivalentes','porcentajes'))
add('coordenadas','Plano cartesiano y puntos','Funciones y gráficas','6P 1E 2E 3E 4E 1B',
 'Un punto se escribe (x,y): primero te desplazas horizontalmente y después verticalmente.',
 'Es el lenguaje gráfico de rectas, parábolas, geometría analítica y estadística.',
 'Dibuja dos ejes perpendiculares y marca el origen (0,0). | Lee la primera coordenada x (derecha +, izquierda −). | Lee la segunda y (arriba +, abajo −). | Comprueba los puntos sobre los ejes: allí una coordenada es 0.',
 [('Sitúa A(−2,3).','Desde el origen: 2 a la izquierda y 3 hacia arriba.','Cuadrante II.'),('¿Dónde está C(0,2)?','x=0: no te mueves horizontalmente; subes dos.','En el eje Y.')],
 'Intercambiar x e y; el punto (3,−1) no es el punto (−1,3).',
 'Repite siempre: primero x, después y.', 'coordinates','coords',('enteros-signos',))
add('traslaciones','Traslaciones de figuras','Geometría','6P 1E 2E',
 'Una traslación mueve todos los puntos la misma distancia y sentido sin girar la figura.',
 'Ayuda a comprender vectores y transformaciones sin perder la forma.',
 'Dibuja y nombra los vértices A, B y C. | Identifica el desplazamiento horizontal y vertical. | Mueve CADA vértice desde su posición original. | Une los puntos nuevos. | Comprueba que AA’, BB’ y CC’ son flechas iguales y paralelas.',
 [('A(1,2) se desplaza +3 en x y −1 en y.','A’=(1+3,2−1).','A’(4,1).'),('Un triángulo se traslada 4 unidades.','Todos sus lados y ángulos se conservan.','Misma forma y tamaño.')],
 'Mover B desde A’ o cambiar la longitud del desplazamiento a mitad de la construcción.',
 'Dibuja flechas entre cada punto y su imagen para revisar.', 'transforms','translate',('coordenadas',))
add('giros','Rotaciones o giros','Geometría','6P 1E 2E',
 'Un giro cambia la orientación alrededor de un centro sin alterar las distancias a él.',
 'Prepara las bases de trigonometría y simetrías.',
 'Marca el centro O, que permanece fijo. | Traza el radio desde O hasta cada vértice. | Mide el mismo ángulo desde O, con el mismo sentido. | Conserva cada distancia al centro. | Une imágenes y comprueba longitud y orientación.',
 [('Gira (2,1) 90° antihorario alrededor de O.','Regla de 90°: (x,y) → (−y,x).','(−1,2).'),('Gira (3,−2) 180°.','Regla de media vuelta: (x,y)→(−x,−y).','(−3,2).')],
 'Medir el ángulo desde un vértice en lugar del centro O.',
 'En un giro de 90° horario: (x,y)→(y,−x).', 'transforms','rotate',('coordenadas',))
add('reflexiones','Reflexión respecto a un eje','Geometría','6P 1E 2E 3E',
 'La reflexión coloca cada punto al otro lado de un eje, a igual distancia perpendicular.',
 'Relaciona geometría, simetría de funciones y transformaciones en el plano.',
 'Traza el eje de reflexión. | Desde cada vértice, dibuja una perpendicular hasta el eje. | Mide la distancia y prolóngala la misma cantidad al otro lado. | Une los reflejos. | Comprueba que el eje es mediatriz de cada par de puntos.',
 [('Refleja (3,2) en el eje Y.','Respecto al eje Y cambia el signo de x.','(−3,2).'),('Refleja (−1,4) en el eje X.','Respecto al eje X cambia el signo de y.','(−1,−4).')],
 'Medir distancias en diagonal al eje; se miden perpendicularmente.',
 'Respecto a y=x se intercambian las coordenadas (x,y)→(y,x).', 'transforms','reflect',('coordenadas',))
add('simetria','Simetría axial de una figura','Geometría','5P 6P 1E 2E',
 'Una figura tiene un eje de simetría si las dos mitades coinciden al doblarla por ese eje.',
 'Distinguir una propiedad de una figura de una transformación geométrica.',
 'Propón una recta candidata a eje. | Imagina doblar la figura sobre esa recta. | Empareja los puntos correspondientes y comprueba distancias. | Si todos coinciden, la recta es un eje de simetría.',
 [('¿Cuántos ejes de simetría tiene un cuadrado?','Dos diagonales y dos rectas que unen puntos medios opuestos.','4 ejes.'),('¿Y un rectángulo no cuadrado?','Las rectas centrales horizontal y vertical.','2 ejes.')],
 'Confundir «la figura se puede mover» con «la figura tiene eje de simetría».',
 'Para comprobar un eje, observa puntos lejos del centro, no solo el centro de la figura.', 'transforms','symmetry',('reflexiones',))
add('jerarquia','Jerarquía de operaciones','Álgebra','6P 1E 2E 3E',
 'El orden de las operaciones evita que una misma expresión tenga varios resultados.',
 'Es indispensable para operar con fracciones, polinomios y ecuaciones.',
 'Resuelve primero paréntesis. | Calcula potencias y raíces. | Multiplicaciones y divisiones de izquierda a derecha. | Finalmente sumas y restas de izquierda a derecha. | Relee cada signo antes de cerrar.',
 [('3+2×5','Primero 2×5=10, luego 3+10.','13.'),('(3+2)×5','Primero el paréntesis 3+2=5, luego 5×5.','25.')],
 'Leer de izquierda a derecha sin priorizar: 3+2×5 no es 25.',
 'Una línea por transformación ayuda a detectar dónde cambió el resultado.', 'bars','order',('enteros-signos','potencias'))
add('distributiva','Propiedad distributiva','Álgebra','1E 2E 3E 4E 1B',
 'La multiplicación se distribuye sobre una suma: a(b+c)=ab+ac.',
 'Es clave para simplificar expresiones, resolver ecuaciones y expandir productos.',
 'Identifica el factor exterior. | Multiplícalo por cada término dentro del paréntesis. | Respeta signos. | Agrupa términos semejantes cuando proceda.',
 [('3(x+4)','3×x+3×4.','3x+12.'),('−2(x−3)','−2×x+(−2)×(−3).','−2x+6.')],
 'Multiplicar solo el primer término del paréntesis o perder el signo negativo.',
 'Comprueba sustituyendo x=1 en la expresión original y la desarrollada: deben coincidir.', 'bars','distribute',('jerarquia',))
add('ecuaciones-1','Ecuaciones de primer grado','Álgebra','1E 2E 3E 4E 1B',
 'Una ecuación es una igualdad que se cumple para ciertos valores de una incógnita.',
 'Permite hallar cantidades desconocidas y prepara funciones y sistemas.',
 'Simplifica ambos miembros y aplica distributiva si es necesario. | Suma o resta lo mismo en ambos miembros. | Multiplica o divide ambos miembros por la misma cantidad NO nula. | Despeja x. | Sustituye el valor para comprobar.',
 [('3x−6=9','Suma 6 a ambos lados: 3x=15; divide entre 3.','x=5.'),('2(x+1)=10','Divide ambos miembros entre 2: x+1=5; resta 1.','x=4.')],
 '«Pasar» un número al otro lado cambiando signos de memoria sin entender la operación.',
 'La balanza es una metáfora: lo que haces a la izquierda debes hacerlo también a la derecha.', 'balance','equations',('distributiva','enteros-signos'))
add('polinomios','Polinomios y productos notables','Álgebra','2E 3E 4E 1B 2B',
 'Un polinomio combina sumas de potencias enteras no negativas de x con coeficientes.',
 'Sin álgebra básica no se pueden factorizar cuadráticas ni estudiar funciones.',
 'Identifica los términos y sus grados. | Suma solo términos semejantes. | Aplica la distributiva para multiplicar. | Para factorizar, busca factor común y luego identidades conocidas. | Comprueba desarrollando de nuevo.',
 [('Simplifica 2x²+3x−x²+2x.','Agrupa x²: 2−1=1; agrupa x: 3+2=5.','x²+5x.'),('Factoriza x²−4x+3.','Busca dos números que sumen −4 y multipliquen 3: −1 y −3.','(x−1)(x−3).')],
 'Sumar exponentes al sumar términos: x²+x²=2x², NO x⁴.',
 'Después de factorizar, vuelve a multiplicar para comprobar.', 'squares','polynomials',('distributiva','potencias'))
add('rectas','Rectas, pendiente y cortes','Funciones y gráficas','2E 3E 4E 1B 2B',
 'Una recta y=mx+b tiene pendiente m y corte con el eje Y en (0,b).',
 'Aprender a leer rectas prepara funciones de cualquier tipo.',
 'Identifica m y b. | Calcula el corte Y poniendo x=0. | Para el corte X, pon y=0 y despeja x (si m≠0). | Elige otro valor x y calcula y. | Une dos puntos y revisa si la recta crece (m>0), decrece (m<0) o es horizontal (m=0).',
 [('y=3x−6','Corte Y (0,−6). Para y=0: 3x=6, x=2.','Cortes (0,−6) y (2,0).'),('Recta por (1,4) y (3,8)','m=(8−4)/(3−1)=2. Sustituye (1,4): 4=2+b.','y=2x+2.')],
 'Buscar siempre un corte con X: la recta y=1 no corta ese eje.',
 'Si no tienes un punto con x=0, calcula m con dos puntos y despeja b sustituyendo uno.', 'line-graph','lines',('coordenadas','ecuaciones-1'))
add('dominio','Dominio de funciones y restricciones','Funciones y gráficas','3E 4E 1B 2B',
 'El dominio son todos los valores de x para los que la expresión está definida en números reales.',
 'Evita dibujar puntos donde una función no existe.',
 'Si es un polinomio, no hay restricciones: dominio ℝ. | Si hay fracción algebraica, excluye los valores que anulan el denominador. | Si hay raíz cuadrada, exige radicando ≥0. | Combina restricciones y escribe intervalos o conjunto.',
 [('Dominio de 1/(x²−9)','x²−9=(x−3)(x+3). El denominador es 0 en ±3.','ℝ sin {−3,3}.'),('Dominio de √(3−x)','El interior de la raíz debe ser ≥0: 3−x≥0 → x≤3.','(−∞,3].')],
 'Confundir dominio con recorrido: el dominio se refiere a los valores que puede tomar x.',
 'Empieza preguntando «¿qué operación podría ser imposible?»', 'domain-graph','domain',('ecuaciones-1','polinomios'),('rectas',))
add('parabolas','Parábolas: de cero al vértice','Funciones y gráficas','3E 4E 1B 2B',
 'La gráfica de y=ax²+bx+c es una parábola; su vértice marca un mínimo o máximo.',
 'Conecta potencias, coordenadas, simetría, dominio, recorrido, cortes y factorización.',
 'Identifica si a>0 (abre arriba) o a<0 (abre abajo). | Calcula x del vértice: −b/(2a) y luego sustituye en la función para hallar y. | Dibuja el eje de simetría x=xv. | Haz tabla con puntos simétricos a ambos lados del vértice. | Calcula corte Y con x=0 y cortes X resolviendo y=0. | Dominio ℝ; recorrido según el vértice y la apertura.',
 [('y=x²−4x+3','xv=−(−4)/(2·1)=2; yv=4−8+3=−1; abre arriba.','Vértice (2,−1); recorrido [−1,+∞).'),('y=−x²+4','Abre abajo, eje x=0, corte Y (0,4). Si y=0, x²=4.','Vértice (0,4); cortes X (−2,0) y (2,0).')],
 'Tomar el dominio como solo el tramo visible del dibujo; una cuadrática tiene dominio ℝ.',
 'El vértice es el punto de giro, pero no siempre está en el eje Y: calcula primero su abscisa.', 'parabola','parabolas',('coordenadas','potencias','polinomios','ecuaciones-1'),('rectas',),40)
add('ecuaciones-2','Ecuaciones cuadráticas y raíces','Álgebra','3E 4E 1B 2B',
 'Resolver ax²+bx+c=0 equivale a encontrar dónde su parábola corta el eje X.',
 'Une factorización y geometría de forma comprobable.',
 'Escribe la ecuación igualada a cero. | Busca factorización sencilla cuando sea posible. | Si no, aplica x=(−b±√(b²−4ac))/(2a). | Comprueba cada solución sustituyendo. | Recuerda que si el discriminante es negativo no hay soluciones reales.',
 [('x²−4x+3=0','(x−1)(x−3)=0. Un producto es 0 si alguno de sus factores es 0.','x=1 o x=3.'),('x²−4=0','Diferencia de cuadrados: (x−2)(x+2)=0.','x=−2 o x=2.')],
 'Olvidar el ± de la fórmula general o dividir entre 2 y no entre 2a.',
 'Comprueba los resultados: cada raíz debe producir 0 al sustituir.', 'parabola','quadratic',('polinomios','ecuaciones-1','potencias'),('parabolas',))
add('intervalos','Intervalos y desigualdades','Álgebra','3E 4E 1B 2B',
 'Los intervalos describen subconjuntos de la recta real con extremos abiertos o cerrados.',
 'Necesarios para expresar dominios, recorridos y soluciones de inecuaciones.',
 'Resuelve la desigualdad como una ecuación, manteniendo el sentido. | Si multiplicas por un número negativo, invierte el signo. | Dibuja extremo abierto (<,>) o cerrado (≤,≥). | Escribe el intervalo y combina con ∪ o ∩ según corresponda.',
 [('x≤3','Incluye el 3 y todos los menores.','(−∞,3].'),('x>−1','Excluye −1 e incluye los mayores.','(−1,+∞).')],
 'Poner corchetes con infinito: ±∞ nunca se incluyen como extremos reales.',
 'Dibuja la recta primero, y luego tradúcela a notación.', 'number-line','intervals',('enteros-signos','ecuaciones-1'),('dominio',))
add('radicales','Raíces cuadradas y radicandos','Álgebra','2E 3E 4E 1B 2B',
 'La raíz cuadrada principal √x existe en números reales solo si x≥0.',
 'Prepara simplificación algebraica y dominio de funciones con raíces.',
 'Comprueba que el radicando no sea negativo. | Reconoce cuadrados perfectos. | Separa factores cuadrados cuando simplifiques. | Si hay variable, exige radicando ≥0 y resuelve.',
 [('√81','9²=81 y se toma la raíz positiva.','9.'),('¿Cuándo existe √(5−x)?','5−x≥0; por tanto x≤5.','x≤5.')],
 'Escribir √36=±6: la raíz principal vale 6. Al resolver x²=36 sí hay dos soluciones.',
 'Diferencia entre «calcular √a» y «resolver x²=a».', 'squares','radicals',('potencias','enteros-signos'),('dominio',))
add('pendiente-dos-puntos','Pendiente a partir de dos puntos','Funciones y gráficas','3E 4E 1B 2B',
 'La pendiente es el cambio vertical dividido entre el cambio horizontal de una recta.',
 'Permite construir una ecuación incluso sin conocer el corte con Y.',
 'Nombra A(x₁,y₁) y B(x₂,y₂). | Calcula el cambio vertical y₂−y₁. | Calcula el cambio horizontal x₂−x₁. | Divide si x₂−x₁ ≠0. | Sustituye uno de los puntos en y=mx+b y despeja b.',
 [('P(1,4), Q(3,8)','m=(8−4)/(3−1)=4/2=2. 4=2·1+b, b=2.','y=2x+2.'),('A(0,−2),B(2,4)','m=(4−(−2))/(2−0)=6/2=3. Con A, b=−2.','y=3x−2.')],
 'Restar y de un punto con x del otro: ambos cambios deben respetar el mismo orden.',
 'Si las dos x son iguales, la recta es vertical: tiene pendiente no definida.', 'line-graph','slope',('coordenadas','rectas','enteros-signos'))
add('recorrido-parabola','Recorrido y transformaciones de parábolas','Funciones y gráficas','4E 1B 2B',
 'La forma y=a(x−h)²+k muestra el vértice (h,k), la apertura y el recorrido.',
 'Hace visible cómo se transforma la gráfica sin memorizar dibujos.',
 'Identifica h y k (ojo al signo dentro del paréntesis). | Marca el vértice (h,k). | Si a>0, el recorrido empieza en k; si a<0, termina en k. | Cambia x en pasos simétricos h−2,h−1,h,h+1,h+2. | Comprueba que el dominio sigue siendo ℝ.',
 [('y=(x−2)²−1','Vértice (2,−1), abre arriba.','Recorrido [−1,+∞).'),('y=−(x+1)²+4','h=−1,k=4, abre abajo.','Recorrido (−∞,4].')],
 'Leer (x−2)² como desplazamiento dos unidades a la izquierda. Es a la derecha.',
 'Si la parábola abre hacia abajo, no existe mínimo global, sino máximo.', 'parabola','range',('parabolas','intervalos'))

# metadata of grade + availability, do not promise entire curriculum
catalog=dict(version='1.1.0',published='2026-11-25',method='Academia Teseracto · enfoque MAER',
    stages=[dict(id='primaria',label='Primaria',grades=['5P','6P']),dict(id='eso',label='ESO',grades=['1E','2E','3E','4E']),dict(id='bach',label='Bachillerato',grades=['1B','2B'])],
    courses={'5P':'5.º Primaria','6P':'6.º Primaria','1E':'1.º ESO','2E':'2.º ESO','3E':'3.º ESO','4E':'4.º ESO','1B':'1.º Bachillerato','2B':'2.º Bachillerato'},
    modules=M)
(R/'data/catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(R/'data/catalog.js').write_text('/* Archivo generado: ejecutar python tools/generar_catalogo.py */\nwindow.TESERACTO_CATALOG = '+json.dumps(catalog,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(f'{len(M)} temas creados; {sum(len(m["examples"]) for m in M)} ejemplos, {sum(len(m["steps"]) for m in M)} pasos')

#!/usr/bin/env python3
"""Genera el combo MAER de fracciones en PDF, con contenidos propios. Requiere reportlab."""
from pathlib import Path
import zipfile
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether, HRFlowable, Flowable
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'materiales';OUT.mkdir(exist_ok=True)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
pdfmetrics.registerFont(TTFont('DejaVu',FONT));pdfmetrics.registerFont(TTFont('DejaVuBold',BOLD));pdfmetrics.registerFontFamily('DejaVu',normal='DejaVu',bold='DejaVuBold',italic='DejaVu',boldItalic='DejaVuBold')
NAVY=colors.HexColor('#172554');VIO=colors.HexColor('#5e55d8');MUT=colors.HexColor('#63738a');PALE=colors.HexColor('#f0efff');GOLD=colors.HexColor('#f59e0b')
ST={
 'title':ParagraphStyle('t',fontName='DejaVuBold',fontSize=23,leading=31,textColor=NAVY,spaceAfter=11),
 'sub':ParagraphStyle('s',fontName='DejaVuBold',fontSize=14,leading=19,textColor=NAVY,spaceBefore=12,spaceAfter=9),
 'head':ParagraphStyle('h',fontName='DejaVuBold',fontSize=11,leading=17,textColor=NAVY,spaceBefore=8,spaceAfter=6),
 'normal':ParagraphStyle('n',fontName='DejaVu',fontSize=9.2,leading=15,textColor=colors.HexColor('#253247'),spaceAfter=7),
 'small':ParagraphStyle('sm',fontName='DejaVu',fontSize=8.1,leading=12,textColor=MUT,spaceAfter=5),
 'statement':ParagraphStyle('st',fontName='DejaVuBold',fontSize=9.3,leading=16,textColor=NAVY,spaceBefore=7,spaceAfter=4),
 'steps':ParagraphStyle('steps',fontName='DejaVu',fontSize=8.7,leading=15,textColor=colors.HexColor('#34445d'),leftIndent=12,spaceAfter=7),
}
def para(s,style='normal'):
 return Paragraph(escape(s).replace('\n','<br/>'),ST[style])
def p_rich(s,style='normal'):return Paragraph(s,ST[style])
def hr():return HRFlowable(width='100%',thickness=.7,color=colors.HexColor('#dce1ec'),spaceAfter=10,spaceBefore=7)

def header_footer(c,doc):
 W,H=A4;c.saveState();c.setStrokeColor(VIO);c.setLineWidth(1.4);c.line(18*mm,H-20*mm,W-18*mm,H-20*mm)
 c.setFont('DejaVuBold',8.7);c.setFillColor(NAVY);c.drawString(18*mm,H-17*mm,'ACADEMIA TESERACTO  /  MATEMÁTICAS  /  MAER')
 c.setFont('DejaVu',7);c.setFillColor(MUT);c.drawString(18*mm,13*mm,'Material original de estudio · 25/11/2026 · academiateseracto.es')
 c.drawRightString(W-18*mm,13*mm,f'Página {doc.page}');c.restoreState()
def pdf(name,story):
 doc=SimpleDocTemplate(str(OUT/name),pagesize=A4,rightMargin=19*mm,leftMargin=19*mm,topMargin=25*mm,bottomMargin=21*mm,title=name.replace('_',' ').replace('.pdf',''),author='Academia Teseracto')
 doc.build(story,onFirstPage=header_footer,onLaterPages=header_footer)
 print(name,(OUT/name).stat().st_size)

def answer_lines(num=2,space=7):
 arr=[]
 for _ in range(num):
  arr.extend([Spacer(1,space),HRFlowable(width='100%',thickness=.35,color=colors.HexColor('#c8d0dd')),Spacer(1,space)])
 return arr

sections=[
 ('A','MIRAR · fracciones y recta numérica','10 min',[
  ('A1','Dibuja una recta de 0 a 1, divídela en tres partes iguales y coloca 2/3.','Divide entre 3; marca el segundo intervalo desde 0. El punto se ubica aproximadamente en 0,667.'),
  ('A2','Sitúa 5/4 en la recta entre 0 y 2. Explica por qué es mayor que 1.','5/4 = 4/4 + 1/4 = 1 y 1/4, por eso queda a la derecha de 1.'),
  ('A3','Escribe una fracción equivalente al número 0,75 y represéntala en una barra.','0,75 = 75/100 = 3/4. Colorea tres de cuatro partes iguales.')]),
 ('B','ACLARAR · fracciones equivalentes','15 min',[
  ('B1','Completa: 2/3 = ?/12.','Multiplica ambos términos por 4: 2×4=8, 3×4=12; falta 8.'),
  ('B2','Completa: 3/4 = 15/?.','Numerador ×5, por tanto denominador ×5: 4×5=20.'),
  ('B3','Simplifica 12/18 a su forma irreducible.','Divide arriba y abajo entre m.c.d.(12,18)=6: 12/18=2/3.'),
  ('B4','Simplifica 8/20 y comprueba con productos cruzados.','8/20=2/5 (÷4). Comprobación: 8×5=2×20=40.'),
  ('B5','¿Son equivalentes 4/6 y 6/9? Justifica.','4×9=36; 6×6=36. Sí; ambas son equivalentes a 2/3.')]),
 ('C','ENTRENAR · comparar y ordenar','15 min',[
  ('C1','Compara: 3/4 ___ 5/8.','3/4=6/8, y 6/8>5/8; por tanto 3/4>5/8.'),
  ('C2','Compara: 2/3 ___ 4/6.','2×6=12 y 4×3=12; son iguales.'),
  ('C3','Compara: 3/10 ___ 2/5.','2/5=4/10, por tanto 3/10<2/5.'),
  ('C4','Compara: 7/12 ___ 5/8.','7×8=56 < 5×12=60; 7/12<5/8.'),
  ('C5','Compara: 9/10 ___ 8/9.','9×9=81 > 8×10=80; 9/10>8/9.')]),
 ('D','ENTRENAR · sumas y restas','25 min',[
  ('D1','1/2 + 1/3','m.c.m.=6. 3/6+2/6=5/6.'),
  ('D2','3/4 − 1/6','m.c.m.=12. 9/12−2/12=7/12.'),
  ('D3','2/5 + 1/10','4/10+1/10=5/10=1/2.'),
  ('D4','5/6 − 1/4','10/12−3/12=7/12.'),
  ('D5','7/8 + 1/4','7/8+2/8=9/8=1 y 1/8.'),
  ('D6','2/3 + 3/4','8/12+9/12=17/12=1 y 5/12.'),
  ('D7','4/9 − 1/6','m.c.m.=18. 8/18−3/18=5/18.')]),
 ('E','ENTRENAR · productos y divisiones','15 min',[
  ('E1','2/3 × 3/4','6/12=1/2.'),('E2','5/6 × 2/5','10/30=1/3.'),
  ('E3','3/4 ÷ 1/2','3/4×2/1=6/4=3/2.'),('E4','2/5 ÷ 4/5','2/5×5/4=10/20=1/2.'),
  ('E5','3 × 2/3','3/1×2/3=6/3=2.'),('E6','1/2 × 18','1/2×18/1=18/2=9.')]),
 ('F','REVISAR · transferir a situaciones nuevas','10 min',[
  ('F1','Quedan 3/4 de pizza y llega otra porción de 1/8. ¿Cuánta pizza hay ahora?','3/4=6/8; 6/8+1/8=7/8 de pizza.'),
  ('F2','Una excursión mide 12 km. Has recorrido 2/3. ¿Cuántos kilómetros llevas?','12×2/3=24/3=8 km.'),
  ('F3','Tienes 5/6 L de zumo. Cada vasito contiene 1/6 L. ¿Cuántos vasitos llenas?','(5/6)÷(1/6)=(5/6)×(6/1)=5 vasitos.'),
  ('F4','Se cultivan 2/3 de los 3/4 de una parcela. ¿Qué fracción de la parcela total es?','2/3×3/4=6/12=1/2 de la parcela.')])
]

# Cuaderno: espaciado para trabajar sin calculadora.
work=[para('COMBO MAER · 6.º Primaria / puente hacia ESO','small'),para('Fracciones: ver, comprender y operar','title'),para('CUADERNO DEL ALUMNO · 90 MINUTOS','sub'),
      para('Objetivo: representar, reconocer equivalencias, comparar y operar con fracciones, mostrando cómo llegas al resultado.'),
      para('Nombre (opcional): _______________________    Fecha: _______________________','small'),
      para('Material: lápiz, goma, regla y colores. Haz los cálculos en este mismo cuaderno. No necesitas calculadora.'),hr(),
      para('MAER en este cuaderno: Miro lo que entiendo → aclaro el paso difícil → practico de forma guiada → reviso aplicándolo. No lleva nota escolar.','small')]
for index,(label,title,duration,items) in enumerate(sections):
 if index>0:work.append(PageBreak())
 work.extend([para(f'{label} · {title}','sub'),para(f'Tiempo orientativo: {duration} · Haz los cálculos y justifica cada respuesta.','small'),hr()])
 for n,txt,ans in items:
  work.append(para(f'{n}. {txt}','statement'))
  work+=answer_lines(3 if label in 'ACF' else 2,8 if label in 'ACF' else 7)
 work.append(Spacer(1,12))
 work.append(para('Antes de continuar: marca qué paso dominas y cuál quieres revisar después.','small'))
 work.append(para('Me ha salido bien: ______________________________    Voy a revisar: ______________________________','small'))
work.extend([PageBreak(),para('Mi registro de revisión','title'),para('Resolver ejercicios hoy no garantiza que estén consolidados. Anota el resultado y vuelve una semana después con números diferentes.'),
       para('Primera práctica: fecha __________  Tema __________  Aciertos ____ / 5  ¿Con ayuda? __________','statement'),*answer_lines(2),
       para('Segunda práctica: fecha __________  Tema __________  Aciertos ____ / 5  ¿Con ayuda? __________','statement'),*answer_lines(2),
       para('Aplicación en situación nueva: ¿qué problema resolví y qué procedimiento utilicé?','statement'),*answer_lines(4),
       para('Un tema se propone como consolidado cuando puedes resolver al menos 4 de 5 ejercicios sin ayuda en dos días separados por una semana y al menos uno contiene aplicación diferente. Esta es una referencia operativa de la propuesta MAER v0.1.','small')])
pdf('01_Cuaderno_Fracciones_Alumno.pdf',work)

sol=[para('COMBO MAER · FRACCIONES','small'),para('Solucionario y criterios de observación','title'),para('Uso docente · respuestas con razonamiento','sub'),
     para('No corrijas solo el resultado. Observa si interpreta el problema, utiliza equivalencias válidas, conserva el denominador correcto y comprueba el proceso.'),hr()]
for label,title,duration,items in sections:
 sol.append(para(f'{label} · {title}','sub'))
 for id,statement,answer in items:
  sol.append(para(f'{id}. {statement}','statement'))
  sol.append(para('Solución razonada: '+answer))
 sol.append(hr())
sol.extend([PageBreak(),para('Lectura pedagógica de errores','title'),
 para('No reconoce el lugar 5/4 en la recta: revisar el significado de la unidad y la partición (recta numérica).','steps'),
 para('Completa 2/3 = 2/12: se ha cambiado solo el denominador; trabajar equivalencias con barras y el factor común.','steps'),
 para('Compara 1/8 > 1/4 por tener denominador 8: necesita comprender el tamaño de las partes iguales.','steps'),
 para('Suma 1/2 + 1/3 = 2/5: revisar denominador común con un mismo dibujo de referencia.','steps'),
 para('En 3/4 ÷ 1/2 invierte ambas fracciones: practicar por qué solo se invierte el divisor.','steps'),
 para('Responde sin mostrar cálculo: pedir una justificación corta o representación antes de cambiar la dificultad.','steps'),
 para('Formato de registro de clase (2–3 minutos)','sub'),
 para('Diana trabajada: ______________________________________________________________'),
 para('Evidencia observable (qué hizo, con qué ayuda): __________________________________'),
 para('Decisión siguiente: continuar / reforzar / volver a prerrequisito / cambiar estrategia / revisar.','small'),
 para('Privacidad: utiliza un alias o identificador anónimo; no incluyas diagnósticos clínicos ni datos personales de menores.','small')])
pdf('02_Solucionario_Fracciones_Docente.pdf',sol)

# Guía de tres clases de 60 min
plan=[
 ('CLASE 1 · Visualizar y construir equivalencias','Objetivo: interpretar una fracción en una unidad y localizar su valor; construir equivalencias sin cambiar la cantidad.',
  [('0–8 min','Entrada: 3 preguntas de recuperación sobre partes iguales, 1/2 y 3/4.'),('8–20 min','Modelado visual con dos barras: 2/3 = 4/6. Mostrar por qué se multiplican arriba y abajo.'),('20–45 min','Práctica en 3 fases: yo hago B1; hacemos B2 y B3; alumno resuelve B4 y B5; pedir pasos.'),('45–55 min','Regreso al objetivo: interpretar una suma 1/2+1/3 en una misma unidad, aunque todavía no opere.'),('55–60 min','Cierre: qué significa «equivalente» y registro de una diana y una evidencia.')],
  'Diana principal: equivalencias. Si falla, comprobar partición de la unidad y recta numérica antes de continuar.'),
 ('CLASE 2 · Comparar y sumar con sentido','Objetivo: comparar sin reglas contradictorias; sumar/restar mediante denominadores equivalentes.',
  [('0–8 min','Recuperar equivalencias 2/3=4/6, 3/4=6/8, y 1/2=3/6 sin mirar el cuaderno.'),('8–20 min','Comparaciones con barras: 1/8 frente a 1/4; modelar 3/4 frente a 5/8.'),('20–45 min','Parejas y trabajo autónomo: C1–C5; D1–D4, detallando m.c.m. o múltiplo común.'),('45–55 min','Regreso al objetivo: problema de receta con 1/2+1/3; justificar unidad y resultado.'),('55–60 min','Cierre: error típico de sumar denominadores; registro de observación.')],
  'Diana principal: denominador común. Si la operación falla por multiplicaciones básicas, revisar ese paso sin abandonar el problema.'),
 ('CLASE 3 · Operaciones y transferencia','Objetivo: resolver operaciones mixtas y explicar qué operación representa cada problema.',
  [('0–8 min','Tres ejercicios de entrada: 1/2+1/4, 3/5 frente a 4/10, 2/3×3/4.'),('8–20 min','Modelado del producto como «parte de» y de la división como «cuántos grupos caben».'),('20–45 min','E1–E6 y D5–D7 en fases; practicar variantes de la web autocorregible.'),('45–55 min','Problemas F1–F4 de transferencia: el alumno debe justificar la elección de operación.'),('55–60 min','Cierre: plan de revisión a 7 días, comprobar procedimiento, registro F3.')],
  'Diana principal: distinguir suma, producto y división en contextos reales. Evitar evaluar solo acierto por casualidad.')]
guide=[para('COMBO MAER · FRACCIONES','small'),para('Guía de tres clases de 60 minutos','title'),para('Academia Teseracto · Primaria y puente a ESO','sub'),
 para('Secuencia: lo hago yo → lo hacemos juntos → lo haces tú → regreso al objetivo → revisión. El ritmo se adapta a la evidencia observable, no al número de ejercicios terminados.'),
 para('Se trabaja una diana principal por tramo. Si se detecta un prerrequisito, se desciende lo estrictamente necesario y se vuelve al problema del curso en la misma sesión.','normal'),hr()]
for i,(title,objective,blocks,decision) in enumerate(plan):
 if i: guide.append(PageBreak())
 guide.extend([para(title,'sub'),para(objective),hr()])
 for tm,task in blocks:
  guide.append(p_rich(f'<b>{escape(tm)}:</b> {escape(task)}','normal'))
 guide.extend([Spacer(1,12),para('Decisión pedagógica y comprobación','head'),para(decision),
    para('Rellena una ficha de sesión al terminar: diana, evidencia concreta y decisión siguiente. Menos de tres minutos.','small'),
    para('Recomendación práctica','head'),
    para('El portal contiene barras de fracciones y generadores de preguntas nuevas. Úsalos para pasar del modelo visual al ejercicio independiente y a una variante de aplicación.'),
    para('Acceso en el portal: Inicio → Temario → Fracciones equivalentes / Comparación / Suma y resta → Entrenar.','small')])
guide.extend([PageBreak(),para('Mapa mínimo de prerrequisitos','title'),
 para('Operar con fracciones necesita entender la unidad, el tamaño de cada parte y las equivalencias. No todos los fallos exigen volver al mismo paso.'),
 para('RECTA FRACCIONARIA → FRACCIONES EQUIVALENTES → COMPARAR → SUMAR/RESTAR → MULTIPLICAR/DIVIDIR','head'),
 para('Señal: suma de denominadores. Hipótesis: no ha igualado unidades. Comprobación: 1/2+1/3 sobre dos barras iguales.','steps'),
 para('Señal: 1/8>1/4. Hipótesis: interpreta denominador como valor y no como número de partes. Comprobación: compara 1/2 y 1/4 con papel doblado.','steps'),
 para('Señal: división por 1/2 disminuye la cantidad. Hipótesis: no interpreta cuántas medias unidades caben. Comprobación: ¿cuántas mitades hay en dos enteros?','steps'),
 para('Regla de los tres límites (propuesta de trabajo)','sub'),
 para('Descender solo si el prerrequisito bloquea al menos dos tareas distintas; no consumir más de un tercio de las sesiones disponibles en ese descenso; y no bajar más de dos niveles de profundidad en el mismo tramo sin renegociar el objetivo.','normal'),
 para('Criterio de revisión (propuesta MAER v0.1)','sub'),
 para('4 de 5 sin ayuda, en dos días distintos separados al menos una semana y una tarea de aplicación diferente. Es orientación en evaluación pedagógica, no un diagnóstico clínico.','normal'),
 para('Nota de gobernanza','sub'),
 para('«MAER Capa 2 Ejecución Operativa v0.1» figura como PROPUESTA PARA VALORACIÓN. Su incorporación al documento canónico está pendiente de aprobación expresa. Esta guía es un uso piloto de sus criterios, no una aprobación automática.','small')])
pdf('03_Guia_MAER_3_Clases_Fracciones.pdf',guide)

# D1: puntuación pedagógica interna por bloques y nodos; alumno recibe perfil, no calificación.
d1=[para('ACADEMIA TESERACTO · D1 / FRACCIONES','small'),para('Exploración inicial de Matemáticas','title'),
    para('PRUEBA DIAGNÓSTICA PEDAGÓGICA · 20–25 MINUTOS','sub'),
    para('Esta prueba no es un examen y no lleva nota escolar. Escribe cómo piensas cada pregunta: los pasos nos ayudan a elegir por dónde empezar.'),
    para('Código o alias: ___________________   Curso: _________________   Fecha: ______________','small'),hr()]
ditems=[
 ('1','B2 · Prerrequisito','Representa 1/2 coloreando una barra dividida en cuatro partes iguales. Explica cuántas coloreas.','2/4; se colorean 2 de las 4 partes porque 1/2=2/4.','fracciones-equivalentes'),
 ('2','B1 · Nivel curso','Calcula 1/2 + 1/3 y muestra el denominador común.','5/6; 1/2=3/6, 1/3=2/6.','sumar-restar-fracciones'),
 ('3','B2 · Prerrequisito','Sitúa 5/4 en la recta de 0 a 2. ¿Está antes o después de 1?','Después de 1, a un cuarto de distancia.','recta-fracciones'),
 ('4','B1 · Nivel curso','Compara 3/4 y 5/8 con >, < o =. Justifica.','3/4 > 5/8; 3/4=6/8.','comparar-fracciones'),
 ('5','B2 · Prerrequisito','Completa la equivalencia 3/5 = ?/20.','12, porque 5×4=20 y 3×4=12.','fracciones-equivalentes'),
 ('6','B1 · Nivel curso','Calcula 2/3 × 3/4 y simplifica.','1/2; 6/12=1/2.','multiplicar-fracciones'),
 ('7','B2 · Prerrequisito','Compara 1/4 y 1/8. ¿Cuál es más grande y por qué?','1/4; las partes en cuartos son mayores que en octavos.','comparar-fracciones'),
 ('8','B1 · Nivel curso','Calcula 3/4 ÷ 1/2 y explica qué fracción se invierte.','3/2; se invierte solo el divisor 1/2.','dividir-fracciones'),
 ('9','B3 · Transferencia','Una receta necesita 3/4 L y añades 1/8 L. ¿Cuántos litros tienes?','7/8 L; 3/4=6/8; 6/8+1/8=7/8.','sumar-restar-fracciones'),
 ('10','B3 · Transferencia','Un recipiente contiene 2/3 de su capacidad y vacías la mitad de esa cantidad. ¿Qué fracción de la capacidad vacías?','1/3; (1/2)×(2/3)=1/3.','multiplicar-fracciones')]
for i,(n,b,text,ans,node) in enumerate(ditems):
 if i in (5,):d1.append(PageBreak())
 d1.append(para(f'{n}. {text}','statement'));d1.append(para(f'{b} · Nodo: {node}','small'));d1+=answer_lines(2 if len(text)<100 else 3,8)
d1.extend([PageBreak(),para('Registro interno del docente · D1','title'),
 para('Distribución: B1 nivel de curso (4 ítems, 40 %); B2 prerrequisitos (4 ítems, 40 %); B3 transferencia (2 ítems, 20 %). El porcentaje es estructura de la prueba, NO una nota para comunicar a la familia.','normal')])
for n,b,t,a,node in ditems:d1.append(para(f'{n} / {node}: {a}','small'))
d1.extend([hr(),para('Observación del procedimiento','sub'),
 para('¿En qué paso se detuvo? ___________________________________________________'),*answer_lines(2),
 para('¿Qué explicación dio? ______________________________________________________'),*answer_lines(2),
 para('Prerrequisito prioritario y justificación: ____________________________________'),*answer_lines(2),
 para('Próximo objetivo y revisión: _______________________________________________'),*answer_lines(2),
 para('Se sugiere valorar el resultado por nodo y proceso; no atribuir rasgos clínicos ni redactar juicios sobre la persona.','small')])
pdf('04_Diagnostico_Fracciones_D1.pdf',d1)

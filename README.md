# Academia Teseracto · Portal de Matemáticas

**Versión 1.1.0 · 25 de noviembre de 2026**

Una biblioteca de Matemáticas para **Primaria, ESO y Bachillerato** basada en conocimiento compartido entre cursos, explicaciones paso a paso, gráficas manipulables, práctica autocorregible y rutas orientativas MAER.

## Actualizar el repositorio existente (importante)

Esta entrega está pensada como **actualización acumulativa** de `academia-teseracto/matematicas`, rama `main`. No es necesario crear otro repositorio.

1. Antes de subir, descarga una copia del repositorio desde **Code → Download ZIP**.
2. Descomprime este ZIP y sube sus archivos y carpetas a la raíz con **Add file → Upload files**. Conserva los archivos antiguos no incluidos en el ZIP.
3. Confirma el cambio en `main`. No borres `temas/`, `catalogo.js` ni `assets/logo.svg` del repositorio anterior. En particular, debe conservarse `temas/funciones/parabolas.html`, la guía V3 original, que se ha enlazado desde el catálogo y desde la lección nueva. Este ZIP no contiene los bytes de ese archivo preexistente.
4. Si GitHub Pages está configurado con `main` y `/(root)`, se actualizará automáticamente. Comprueba el curso 6.º Primaria, la búsqueda de parábolas, la guía V3 y el cuaderno de fracciones.

La URL permanece `https://academia-teseracto.github.io/matematicas/`. Para una instalación nueva en un repositorio vacío, recupera también la guía original y su logo desde la copia del repositorio existente; de lo contrario su enlace no funcionará. El resto del portal no depende de esos archivos.

**No subas el ZIP como un solo archivo.** GitHub Pages publica los archivos descomprimidos. El sitio es público: los PDF de docentes y sus respuestas también podrán ser consultados por el alumnado.

## Novedades de la versión 1.1

- Acceso directo a los ocho cursos con contenidos desde la portada, con recuento de temas y bloques temáticos.
- Búsqueda por palabras sin necesidad de tildes y términos alternativos (vértice, rotación, función cuadrática, etc.). Filtros combinados y opción de ampliar la búsqueda a todos los cursos.
- Seis bloques: fracciones, números y cálculo, porcentajes y proporcionalidad, geometría y movimientos, álgebra y ecuaciones, funciones y gráficas.
- Guía V3 de parábolas enlazada a su archivo original en el repositorio, sin reemplazarla. Acceso al cuaderno imprimible desde las seis lecciones de fracciones.
- Los cursos 1.º–4.º de Primaria se indican como pendientes; no se simula un currículo completo. Conservamos la clave de progreso local y los 27 identificadores de las lecciones de v1.0.

## Contenido de esta entrega

- **27 temas compartidos** por etapas y cursos. Los cursos son etiquetas de acceso, no certificados de adecuación a una programación concreta.
- **54 ejemplos resueltos**, **120 pasos** de explicación. El banco JavaScript genera conjuntos variables de cinco ejercicios por tanda, con pistas y solución razonada. El archivo de pruebas genera y verifica 24.300 variantes.
- Gráficos manipulables de fracciones, recta numérica, coordenadas, rectas, parábolas y traslaciones, además de representaciones de operaciones, porcentajes y ecuaciones.
- Tres modos de entrenamiento: con apoyo, yo solo y aplicar. Un contenido se considera **consolidado** en el registro local solo tras dos tandas de al menos 4/5 separadas siete días, incluyendo una de transferencia.
- Exploración inicial por curso (12 ejercicios) y ruta de repaso sugerida. No es un diagnóstico clínico, no reemplaza una evaluación del profesor y no otorga calificación escolar.
- Marcadores, seguimiento, exportación/importación JSON de progreso, sin cuentas ni envío de datos personales a servidores.
- **Cuatro PDF originales**: cuaderno de 90 minutos, solucionario, guía MAER 3×60 minutos y prueba D1 con guía de corrección.
- Imagen corporativa original de Academia Teseracto, aportada en el ZIP de marca. No se redistribuye el paquete completo de la identidad visual.

## Estructura de carpetas

```text
index.html                 Portal desplegable sin compilación
assets/                    CSS, JS, marca y favicons
  styles.css
  app.js
  logo-teseracto.svg
  logo-teseracto-inverso.svg
  favicon.svg
  icono-192.png
  icono-512.png
data/
  catalog.json             Catálogo de conocimiento editable y legible
  catalog.js               Copia generada para ejecutarse sin servidor
  practice.js              Generadores, evaluación y semilla de ejercicios
materiales/                PDFs originales de alumno, docente y D1
docs/
  GUIA_DE_AMPLIACION.md    Convenciones para los siguientes despliegues
  TRAZABILIDAD_Y_PENDIENTES.md
  CHANGELOG.md
tools/
  generar_catalogo.py     Catálogo editable y compilador a JSON/JS
  generar_combo_maer.py   Código reproducible de PDF (requiere reportlab)
tests/
  test_generadores.cjs    Prueba automática de generación y corrección
  test_web.py             Prueba visual funcional, si hay Chromium y Playwright
```

## Reglas de privacidad y accesibilidad

Los datos del avance se guardan en `localStorage` de cada navegador bajo `teseracto-matematicas-v1`. **No hay analítica, cookies de seguimiento, anuncios, registro ni backend.** La exportación JSON se descarga directamente desde el navegador y debe mantenerse privada. No introduzcas datos personales de menores.

Los controles se pueden utilizar con teclado, hay navegación móvil, botones de tamaño accesible y opción de movimiento reducido. Los gráficos contienen alternativa textual. Este primer lanzamiento se revisará y ampliará; no es una certificación formal de conformidad WCAG.

## Sobre MAER

Se ha utilizado la propuesta facilitada «MAER Capa 2 - Ejecución Operativa v0.1» como orientación de diseño, manteniendo explícita su condición de **propuesta pendiente de aprobación**. El software no atribuye decisiones pedagógicas a un algoritmo y no formula diagnósticos clínicos. La prueba digital no sustituye a D1 en papel para observar los pasos.

## Limitación de la recuperación de materiales previos

La arquitectura recrea y conecta los conceptos de proyectos anteriores (Matemáticas 6.º Primaria, movimientos geométricos, materiales previos de funciones y parábolas) y crea contenido original de fracciones desde las fotografías aportadas. **No debe interpretarse que todos los HTML o PDF anteriores se hayan incorporado literalmente**: la recuperación de archivos exactos antiguos no estaba habilitada para todos los paquetes. Consulta `docs/TRAZABILIDAD_Y_PENDIENTES.md` para el inventario y prioridades de integración. Es preferible declarar esta diferencia a publicar como «integrado» material que aún no ha sido cotejado.

## Desarrollo futuro

1. Añadir un tema en `tools/generar_catalogo.py` con ID estable, contenidos y prerrequisitos.
2. Regenerar catálogo: `python tools/generar_catalogo.py`.
3. Añadir una función `case '<id>'` en `data/practice.js` que produzca pregunta, respuesta, pista y razonamiento.
4. Ejecutar `node tests/test_generadores.cjs` y probar en móvil y escritorio.
5. Publicar mediante commit sin romper IDs ni la clave de progreso.

*Academia Teseracto · Carabanchel, Madrid · academiateseracto.es*

# Guía técnica y pedagógica para ampliar el portal

## Arquitectura y objetivo

El portal prioriza una **única fuente de conocimiento por concepto**, reutilizada desde varios cursos. «Fracciones equivalentes» es un nodo; 6.º de Primaria, 1.º y 2.º de ESO lo consultan con distintas rutas. Las nuevas variantes de profundidad pueden añadirse como `versions` o lecciones específicas sin duplicar las definiciones canónicas.

Cada nodo de `data/catalog.json` debe incluir `id` inmutable, título, área, cursos (`grades`), resumen, por qué se estudia, pasos, al menos dos ejemplos razonados, error típico, método de comprobación, tipo de gráfico, generador, dependencias fuertes y débiles, y tiempo aproximado. El catálogo actualmente se redacta en `tools/generar_catalogo.py`, que compila JSON y JavaScript.

### Protocolo de publicación de nuevos contenidos

1. Redactar el concepto con lenguaje adecuado a los cursos de destino.
2. Definir dependencias fuertes (impiden avanzar) y débiles (conviene conocerlas).
3. Explicar el *porqué* del procedimiento y acompañarlo de al menos dos ejemplos y un contraejemplo o error típico.
4. Elegir o añadir gráfico con alternativa accesible y controlar que su escala sea matemáticamente correcta.
5. Crear ejercicios *con respuesta calculada por el mismo generador*, aceptar equivalencias numéricas y decimales con coma, y mostrar la justificación.
6. Incluir al menos un problema contextualizado real en la modalidad «Aplicar», no solamente cambiar números.
7. Probar casos límite: cero, negativos, signos, denominadores no nulos, fracciones impropias, parámetros, rectas horizontales, cortes inexistentes y restricciones de dominio.
8. No garantizar consolidación por una única práctica. Mantener revisión espaciada y evidencia de aplicación.
9. Etiquetar claramente la lección como **disponible** o **pendiente**, nunca mostrar ejercicios vacíos como contenido existente.
10. Verificar teclado, móvil 360–390 px, tableta 768 px y escritorio; ejecutar pruebas y publicar.

### Niveles y versiones

Las etiquetas de curso permiten encontrar contenido. No son una afirmación de que se haya completado el programa didáctico oficial de ese curso. Si una lección tiene variantes, se prioriza enlazarlas desde el mismo nodo con una progresión clara: fundamentos → uso funcional → aplicación → conexión.

### Pruebas

```bash
python tools/generar_catalogo.py
node tests/test_generadores.cjs
python tests/test_web.py
```

El test web usa Chromium instalado localmente, sin internet. Si el navegador restringe `http://localhost` o `file://`, se cargan los archivos en memoria para poder comprobar eventos y diseño.

### Publicación

GitHub Pages publica el contenido estático del repositorio; no admite backend Python. Los scripts de Python se emplean únicamente para **construir** catálogo y PDF, y no son necesarios en el servidor. En caso de querer cuentas, clases sincronizadas entre dispositivos o informes docentes centralizados, hay que diseñar un backend seguro, con cumplimiento de protección de datos y consentimiento correspondiente; **no** almacenar datos de menores de forma pública en GitHub.

### Versión de progreso

Los datos locales se guardan en `localStorage` bajo la clave estable `teseracto-matematicas-v1`. El JSON exportado declara `format: "teseracto-matematicas-progreso"` y `version: 1`. Los IDs deben permanecer estables entre despliegues o se perderán los vínculos con el progreso anterior.

### MAER

Las notas de diseño de «Capa 2 v0.1» tienen estado **propuesto**, no aprobado. La ruta digital es una orientación de estudio; evita cualquier atribución automática de trastornos, dificultades psicológicas o diagnósticos. Comunica observaciones de tareas, no rasgos de persona. La consolidación se confirma mejor con observación docente y tareas de transferencia.

## Navegación v1.1

Al incorporar temas, añade sus IDs a `groups` y términos de búsqueda a `aliases` en `assets/app.js`. Los temas sin grupo explícito se muestran bajo su área en el catálogo. Los cursos y recuentos se generan a partir de los metadatos del catálogo; cuando se añadan 1.º–4.º de Primaria, ampliar sus metadatos, la prueba orientativa y retirar el aviso correspondiente. Conservar los archivos antiguos que se enlazan desde el portal.

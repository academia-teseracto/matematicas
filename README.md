# Academia Teseracto · Matemáticas

Biblioteca estática de materiales interactivos para ESO y Bachillerato. Primera lección: Parábolas, desde cero.

## Publicación en GitHub Pages

1. Crea un repositorio público llamado `matematicas` en la cuenta de la academia.
2. Descomprime el ZIP y sube el contenido (no el ZIP ni la carpeta que lo contiene). `index.html` debe estar en la raíz junto a `catalogo.js`, `assets/` y `temas/`.
3. Confirma los cambios en `main` (Commit changes).
4. Settings → Pages → Source: Deploy from a branch → Branch: main → /(root) → Save.
5. Una vez publicado, abre el enlace indicado en Pages.

## Añadir un tema

- Guarda su HTML en `temas/<bloque>/<tema>.html` (nombres en minúsculas, sin espacios ni tildes).
- Incluye un enlace relativo a `../../index.html` para volver a la biblioteca.
- Añade un objeto al array `window.TEMAS` de `catalogo.js`, copiando el formato existente y asignando un id único. Las etapas admitidas son `ESO` y `Bachillerato`. Se puede incluir en ambas. El nivel describe el uso didáctico y no presupone un curso obligatorio.
- Usa rutas relativas, nunca rutas que empiecen por `/`, para que funcione en GitHub Pages y al abrir archivos locales.
- Comprueba en escritorio y móvil antes de confirmar los cambios. No publiques nombres, registros personales ni fichas docentes privadas.

La portada se actualiza al añadir una entrada al catálogo. No hay dependencias externas, cuentas ni servidor. Los ejercicios de la primera lección conservan su funcionamiento original; no se almacena el progreso de forma permanente.

© Academia Teseracto. Material educativo de la academia.


V3: leccion autocontenida por bloques de consulta y 14 ejercicios originales con soluciones razonadas.

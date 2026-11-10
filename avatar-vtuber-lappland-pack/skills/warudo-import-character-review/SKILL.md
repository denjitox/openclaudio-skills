---
name: warudo-import-character-review
description: "Carga un VRM o .warudo en Warudo y revisa expresiones, blendshapes y animaciones. Usar cuando el usuario quiera importar su avatar a Warudo, probar si los blendshapes ARKit aparecen o diagnosticar que una expresión no responde."
---

# W2 · Importar y revisar el personaje en Warudo

> Grupo: Warudo · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Es la prueba real: ahí se ve si el avatar funciona con el tracking.

## Procedimiento
1. Copiá el archivo `.vrm` o `.warudo` a la subcarpeta `Characters` del data folder de Warudo (*Menu → Open Data Folder*), o agregá un personaje desde el menú *Add Asset*.
2. Seleccionalo en el desplegable del asset de personaje.
3. Abrí la lista de expresiones del personaje: Warudo muestra *Target Material Properties* y *Default BlendShapes*/*Default Material Properties* (se usan cuando no hay expresión ni tracking activos). El fundido por defecto al cambiar de expresión es de 0,4 s.
4. Probá con una *idle animation* (hay galería de previsualización) y comprobá que el tracking se mezcla con ella.
5. **No verificado:** cómo Warudo mapea exactamente los blendshapes ARKit de un VRM exportado. Probalo primero con un modelo simple (3 o 4 shape keys) antes de hacer los 20+. La documentación de OpenSeeFace en Warudo aclara que ciertas sensibilidades requieren blendshapes ARKit presentes en el modelo.

## Cómo verificar
- [ ] El personaje carga y aparece en el desplegable.
- [ ] Al mover la cara, el avatar responde con las expresiones esperadas.

## Errores comunes
- Archivo en una carpeta equivocada.
- Nombres de shape keys con mayúsculas distintas.

## Skills relacionadas
`blender-arkit-shapekeys`, `warudo-mediapipe-tracking`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Character](https://docs.warudo.app/docs/assets/character)
- ✅ [Warudo Docs – Tutorial (readme-1)](https://docs.warudo.app/docs/tutorials/readme-1)
- ✅ [Warudo Docs – OpenSeeFace](https://docs.warudo.app/docs/mocap/openseeface)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

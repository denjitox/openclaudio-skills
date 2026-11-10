---
name: warudo-troubleshooting
description: "Diagnostica problemas de tracking y de personaje en Warudo (tracker negro, temblor, el avatar no se mueve, faltan expresiones). Usar cuando el usuario diga que algo no funciona, está roto, tiembla, está negro o no responde."
---

# W6 · Diagnóstico de problemas comunes

> Grupo: Warudo · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Casi todos los problemas de tracking tienen causas conocidas y rápidas de revisar.

## Procedimiento
1. Ventana de MediaPipe **negra o en 'Loading...'**: la documentación de Warudo lo describe como una limitación conocida de MediaPipe pendiente de que Google lo corrija.
2. **Tracking tembloroso:** comprobá FPS reales de la cámara (30+), luz de la habitación, *GPU Acceleration* y el suavizado (`warudo-blueprints-smoothing`).
3. **La ventana del tracker se ve pero el avatar no se mueve:** revisá si el antivirus bloquea la cámara o el firewall bloquea los datos de tracking; agregá Warudo a la lista de permitidos.
4. **Faltan expresiones:** revisá nombres exactos de los shape keys y su mapeo en el personaje (`blender-arkit-shapekeys`, `warudo-import-character-review`).
5. Si nada funciona, anotá la versión de Warudo y los pasos exactos y pedile al usuario que consulte la documentación o la comunidad oficial.

## Cómo verificar
- [ ] Se identificó la causa y se documentó la solución.

## Errores comunes
- Cambiar varias cosas a la vez sin saber cuál arregló el problema.

## Skills relacionadas
`warudo-mediapipe-tracking`, `warudo-onboarding`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – MediaPipe](https://docs.warudo.app/docs/mocap/mediapipe)
- ✅ [Warudo Docs – OpenSeeFace](https://docs.warudo.app/docs/mocap/openseeface)
- ✅ [Warudo Docs – Motion capture (overview)](https://docs.warudo.app/docs/mocap/overview)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

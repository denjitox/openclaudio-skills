---
name: avatar-qa-checklist
description: "Ejecuta la revisión final del avatar antes de usarlo en stream: triángulos, texturas, expresiones, física, licencia y pruebas en Warudo y en un segundo programa. Usar cuando el usuario diga que terminó, pida revisar el avatar o prepare el stream."
---

# T3 · Checklist de calidad (QA) del avatar

> Grupo: Transversal · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Una revisión ordenada evita descubrir fallos en pleno stream.

## Procedimiento
1. Triángulos dentro del presupuesto (`blender-lowpoly-modeling`).
2. Texturas con Point filter, sin mipmaps y sin compresión (`unity-texture-import-pixel`).
3. Shape keys ARKit con nombres exactos (mínimo ~20) (`blender-arkit-shapekeys`).
4. Todas las expresiones VRM funcionan (`unity-expression-review`).
5. Orejas, cola y pelo con física sin atravesamientos (`unity-spring-bones`).
6. Metadata de licencia completa en el VRM (`avatar-licensing-check`).
7. Probado en Warudo con tracking real, con la prueba rápida: cara neutra quieta, parpadeos, boca (a, i, u, e, o) y sonrisa, cejas, mejillas y lengua si existen, giros de cabeza.
8. Probado el VRM base en un segundo programa (VSeeFace o VNyan) para confirmar portabilidad.
9. Informá al usuario un resumen con cada punto en estado ✅ / ⚠️ / ❌.

## Cómo verificar
- [ ] Todos los puntos revisados y reportados.

## Errores comunes
- Marcar como hecho algo que no se probó.

## Skills relacionadas
`unity-export-vrm`, `warudo-troubleshooting`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – MediaPipe](https://docs.warudo.app/docs/mocap/mediapipe)
- ✅ [vrm.dev – How to make VRM](https://vrm.dev/en/vrm/how_to_make_vrm/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

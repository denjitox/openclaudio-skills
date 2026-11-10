---
name: unity-expression-review
description: "Prueba cada expresión VRM y cada blendshape ARKit del avatar en Unity antes de exportar. Usar cuando el usuario quiera verificar expresiones, parpadeo, visemas, o diagnosticar que una expresión deforma raro."
---

# U5 · Revisión de expresiones

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Es mucho más barato corregir una expresión en Unity que descubrir el problema en pleno stream.

## Procedimiento
1. Importá el VRM y entrá en Play Mode (el flujo oficial de vrm.dev recomienda comprobar los ajustes en Play Mode).
2. Recorré las expresiones: en VRM 0.x se manejan con `VRMBlendShapeProxy` y en VRM 1.0 con `Vrm10Instance` (`Runtime.Expression`).
3. Compará con el checklist de pruebas del tracking de la guía principal (sección 7.8).
4. Anotá qué expresión falla y volvé a Blender para corregir el shape key.

## Cómo verificar
- [ ] Ninguna expresión deforma de forma inesperada.
- [ ] Los nombres ARKit aparecen tal cual en el modelo.

## Errores comunes
- Probar solo parpadeo y boca y olvidar cejas y mejillas.
- Mezclar API de VRM 0.x y 1.0.

## Skills relacionadas
`blender-arkit-shapekeys`, `warudo-import-character-review`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [vrm.dev – How to make VRM](https://vrm.dev/en/vrm/how_to_make_vrm/)
- ✅ [Context7 – UniVRM (API de expresiones VRM 0.x y 1.0)](https://context7.com/vrm-c/univrm)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

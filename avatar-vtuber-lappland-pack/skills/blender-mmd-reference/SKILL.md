---
name: blender-mmd-reference
description: "Importa un modelo PMX de MMD a Blender solo como referencia de proporciones. Usar cuando el usuario mencione PMX, MMD, mmd_tools, sus modelos de Texas o Lappland alter, o quiera usarlos como guía de proporciones o de diseño."
---

# B10 · Referencia con PMX (mmd_tools)

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Los PMX del usuario sirven como guía visual, pero tienen licencias propias y el modelo final debe ser original.

## Procedimiento
1. Instalá MMD Tools desde el repositorio `MMD-Blender/blender_mmd_tools`. Su README indica **usar la versión que corresponde a tu Blender LTS** (v4.x para Blender 4.2 LTS, v2.x para 3.6 LTS): confirmalo antes de instalar.
2. Importá el PMX con el panel de MMD Tools y ponelo en una colección separada, bloqueada y oculta del render.
3. Usalo solo para comparar proporciones (altura, cabeza/cuerpo, largo de piernas, tamaño de orejas y cola).
4. No lo uses como base de la malla ni lo exportes. Leé el readme del modelo antes de cualquier uso.
5. Dato útil: la documentación de Warudo dice que modelos que no son VRM (por ejemplo MMD) se pueden exportar a `.warudo` con el Mod SDK. Si el usuario solo quiere usar sus PMX en Warudo, no hace falta pasar por VRM (sujeto a la licencia de cada modelo). Ver `unity-warudo-sdk-export`.

## Cómo verificar
- [ ] El PMX está en una colección bloqueada y no se exporta.
- [ ] El usuario confirmó que la licencia del PMX permite el uso que quiere.

## Errores comunes
- Instalar una versión de MMD Tools incompatible con la versión de Blender.
- Copiar la malla o texturas del PMX 'por comodidad'.

## Skills relacionadas
`avatar-licensing-check`, `unity-warudo-sdk-export`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [GitHub – MMD-Blender/blender_mmd_tools](https://github.com/MMD-Blender/blender_mmd_tools)
- ✅ [Warudo Docs – Character](https://docs.warudo.app/docs/assets/character)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

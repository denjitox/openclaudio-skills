---
name: blender-flat-shading
description: "Configura el sombreado plano (caras facetadas) del avatar para el look PSX en Blender. Usar cuando el usuario mencione shade flat, normales, caras facetadas, suavizado, 'se ve redondeado' o quiera el aspecto retro de PS1."
---

# B2 · Sombreado plano (flat)

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Las caras facetadas sin suavizado son parte central de la estética PSX.

## Procedimiento
1. En Object Mode seleccioná las mallas del avatar y aplicá *Object → Shade Flat*.
2. Revisá que ningún material dependa de suavizado automático (la opción exacta cambia entre versiones de Blender: verificá en tu versión).
3. Probá en el viewport con la textura visible (ver `blender-pixel-preview`).
4. Después de exportar, confirmá en Unity que las normales se mantuvieron (`unity-materials-mtoon-unlit`).

## Cómo verificar
- [ ] En el viewport se ven las caras facetadas, sin degradados entre polígonos.
- [ ] El resultado se mantiene tras exportar a VRM y abrir en Unity.

## Errores comunes
- Un modificador o ajuste de normales heredado que re-suaviza al exportar.
- Esperar el mismo look en un shader MToon que suaviza por su cuenta: revisalo en Unity.

## Skills relacionadas
`blender-lowpoly-modeling`, `unity-materials-mtoon-unlit`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- 🧠 [Blender Manual (índice)](https://docs.blender.org/manual/en/latest/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

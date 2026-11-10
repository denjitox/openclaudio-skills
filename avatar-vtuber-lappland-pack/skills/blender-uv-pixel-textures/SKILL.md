---
name: blender-uv-pixel-textures
description: "Prepara el UV unwrap y la plantilla de textura para pixel art del avatar en Blender. Usar cuando el usuario hable de UV, costuras (seams), texturas pixeladas, resolución de textura, texel density, plantilla UV o pintar en Aseprite/LibreSprite/Krita."
---

# B3 · UV para texturas pixeladas

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El pixel art solo se ve bien si las islas UV están ordenadas y los píxeles tienen un tamaño consistente en todo el modelo.

## Procedimiento
1. Marcá costuras (seams) en lugares poco visibles y desplegá (Unwrap).
2. Ordená las islas aprovechando el espacio. Objetivo de resolución del proyecto: 64×64 a 128×128 por parte, o una sola textura de 256×256.
3. Igualá la densidad de píxeles entre piezas: un píxel de textura debería medir parecido en la cara, la ropa y el pelo.
4. Alineá bordes de islas a la cuadrícula de píxeles cuando sea posible.
5. Exportá la plantilla UV como imagen y pasala al programa de pixel art. Guardá el resultado como PNG sin suavizado.
6. Probá con una textura de cuadrícula: los cuadros deben tener tamaño parecido en todo el modelo.

## Cómo verificar
- [ ] La textura de cuadrícula se ve uniforme.
- [ ] No hay islas superpuestas por error.
- [ ] La textura final es PNG y tiene la resolución prevista.

## Errores comunes
- Islas con escalas muy distintas (píxeles enormes junto a otros diminutos).
- Costuras en medio de la cara.
- Guardar en JPG (introduce artefactos).

## Skills relacionadas
`blender-pixel-preview`, `unity-texture-import-pixel`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- 🧠 [Blender Manual (índice)](https://docs.blender.org/manual/en/latest/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

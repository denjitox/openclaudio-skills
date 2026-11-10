---
name: unity-texture-import-pixel
description: "Configura las texturas del avatar en Unity para que se vean pixeladas y nítidas: Filter Mode Point, sin mipmaps y sin compresión. Usar siempre que el usuario diga que las texturas se ven borrosas en Unity o Warudo, hable de Point filter, mipmaps, compresión o pixel art."
---

# U2 · Import de texturas pixeladas (Point filter)

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Con filtro bilineal o trilineal, o con mipmaps, Unity suaviza el pixel art y se pierde el efecto PSX (el manual describe que Bilinear se ve borroso de cerca).

## Procedimiento
1. Seleccioná la textura en Unity y abrí el Inspector.
2. **Filter Mode:** `Point (no filter)` (la documentación de Unity describe que la textura se ve 'blocky' de cerca).
3. **Generate Mip Maps:** desactivado.
4. **Compression:** `None`.
5. **Max Size:** igual a la resolución real de la textura.
6. Para aplicarlo a todas las texturas nuevas de una carpeta, usá `unity-editor-scripts`.
7. Nota: la página del manual consultada es de una versión antigua (5.6). Los nombres de las opciones se mantienen, pero revisá el manual de tu versión.

## Cómo verificar
- [ ] Al acercar la cámara en Unity los píxeles se ven como bloques nítidos.
- [ ] Ninguna textura del avatar quedó con compresión.

## Errores comunes
- Olvidar desactivar mipmaps: de lejos se ve borroso.
- Dejar compresión activada: aparecen artefactos en pixel art.

## Skills relacionadas
`unity-editor-scripts`, `blender-pixel-preview`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Unity Manual (documentación legacy 5.6) – Texture types](https://docs.unity3d.com/es/560/Manual/TextureTypes.html)
- ✅ [Unity Script Reference – AssetPostprocessor.OnPreprocessTexture](https://docs.unity.com/en-us/engine/6000.0/script-reference/unityeditor/assetpostprocessor/onpreprocesstexture)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

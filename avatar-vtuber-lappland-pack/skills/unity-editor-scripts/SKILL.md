---
name: unity-editor-scripts
description: "Automatiza ajustes repetitivos en Unity con scripts de editor en C# (por ejemplo, un AssetPostprocessor que pone Point filter, sin mipmaps y sin compresión a las texturas nuevas). Usar cuando el usuario pida automatizar importaciones, validar materiales o evitar configurar texturas a mano."
---

# U9 · Scripts de editor en C#

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Evita configurar a mano cada textura y reduce el error humano.

## Procedimiento
1. Probá siempre en una **copia del proyecto**.
2. Copiá `scripts/PixelArtTexturePostprocessor.cs` dentro de una carpeta `Editor` del proyecto. Solo afecta a texturas ubicadas bajo una carpeta llamada `PixelTextures`.
3. Importá una textura nueva en esa carpeta y comprobá en el Inspector que quedó con Point, sin mipmaps y sin compresión.
4. Tené en cuenta que el postprocesador pisa los ajustes manuales cada vez que se reimporta la textura.
5. El script **no se compiló en esta sesión**: puede requerir ajustes según tu versión de Unity.

## Scripts incluidos
- `scripts/PixelArtTexturePostprocessor.cs`: AssetPostprocessor para texturas bajo una carpeta `PixelTextures` (Point filter, sin mipmaps, sin compresión).
- Estado: **sin probar dentro de la aplicación en esta sesión** (probar en una copia).

## Cómo verificar
- [ ] Una textura nueva en `PixelTextures` se importa con los ajustes correctos sin tocar nada a mano.
- [ ] Texturas fuera de esa carpeta no cambian.

## Errores comunes
- Poner el script fuera de una carpeta `Editor`.
- Afectar sin querer texturas de otros proyectos.

## Skills relacionadas
`unity-texture-import-pixel`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Unity Script Reference – AssetPostprocessor.OnPreprocessTexture](https://docs.unity.com/en-us/engine/6000.0/script-reference/unityeditor/assetpostprocessor/onpreprocesstexture)
- ✅ [Unity Manual (documentación legacy 5.6) – Texture types](https://docs.unity3d.com/es/560/Manual/TextureTypes.html)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

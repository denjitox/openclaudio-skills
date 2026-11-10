---
name: unity-warudo-sdk-export
description: "Exporta el avatar al formato .warudo con el Warudo SDK (Mod SDK) en Unity, para shaders personalizados, scripts C# o modelos que no son VRM (MMD, FBX). Usar cuando el usuario hable de .warudo, Warudo SDK, mods de personaje, Build Mod o shaders personalizados en Warudo."
---

# U7 · Exportar .warudo con el SDK de Warudo

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El `.warudo` permite shaders y scripts propios, y también cargar modelos no VRM como MMD.

## Procedimiento
1. Instalá el SDK siguiendo la guía oficial **'Unity & Warudo SDK Installation'** (enlazada desde la página Mod SDK). Los pasos y la versión de Unity los define esa guía.
2. Colocá el personaje en la escena y seleccionalo. Menú **Warudo → Setup Character...** y elegí *Setup selected GameObject as character mod*. Se genera un prefab `Character` en la carpeta del mod.
3. Si los huesos quedan torcidos, es probable que el modelo no tuviera huesos normalizados. La documentación sugiere normalizarlos antes; el método más probado es crear un VRM a partir del FBX e importar ese VRM a Unity (los VRM garantizan huesos normalizados).
4. Menú **Warudo → Build Mod** y dejá el `.warudo` generado en la carpeta `Characters` del data folder de Warudo (se abre desde *Menu → Open Data Folder* en Warudo).
5. Los scripts C# dentro de la carpeta del mod se compilan e incluyen. Las *assembly definitions* (`.asmdef`) **no están soportadas**.
6. **Hacé backup regular** del proyecto (o usá Unity Version Control) y del archivo `ExportSettings.asset` (Assets/Packages/UMod). Warudo avisa que perderlo obliga a rehacer los mods y que hubo reportes de pérdida de ajustes tras exportar.
7. Warudo **no soporta** `.vsfavatar`; ese formato es de VSeeFace/VNyan. Mantené el VRM como versión portable y el `.warudo` como extra.

## Cómo verificar
- [ ] El `.warudo` aparece en la lista de personajes de Warudo.
- [ ] El avatar carga con los materiales y la física esperados.
- [ ] Hay backup de `ExportSettings.asset`.

## Errores comunes
- Huesos no normalizados.
- Usar assembly definitions.
- No hacer backup del proyecto del SDK.

## Skills relacionadas
`unity-psx-shader`, `unity-export-vrm`, `blender-mmd-reference`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Mod SDK](https://docs.warudo.app/docs/modding/mod-sdk)
- ✅ [Warudo Docs – Character Mod](https://docs.warudo.app/docs/modding/character-mod)
- ✅ [Warudo Docs – Character](https://docs.warudo.app/docs/assets/character)
- ✅ [Warudo Docs – Tutorial (readme-1)](https://docs.warudo.app/docs/tutorials/readme-1)
- ✅ [Warudo Docs – Getting started](https://docs.warudo.app/docs/tutorials/getting-started)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

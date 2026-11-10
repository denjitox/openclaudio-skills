---
name: unity-univrm-setup
description: "Prepara un proyecto de Unity con UniVRM para importar, revisar y exportar VRM. Usar cuando el usuario hable de instalar UniVRM, crear el proyecto de Unity para el avatar, errores de importación de VRM o versiones de Unity."
---

# U1 · Proyecto Unity y UniVRM

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
UniVRM es la herramienta estándar para ajustar licencia, expresiones y spring bones de un VRM antes de usarlo.

## Procedimiento
1. Elegí la versión de Unity: UniVRM indica que soporta **Unity 2021.3 LTS o posterior**. Si el proyecto también va a exportar `.warudo`, la versión exacta la define la guía 'Unity & Warudo SDK Installation' de Warudo: leela antes de crear el proyecto.
2. Instalá UniVRM desde su página de releases (UnityPackage o UPM). Paquetes: `com.vrmc.gltf` y `com.vrmc.vrmshaders` (base), `com.vrmc.vrm` para VRM 1.0 y `com.vrmc.univrm` para VRM 0.x.
3. Importá el VRM y revisá metadata, humanoide y expresiones.
4. Evitá rutas de proyecto con caracteres raros o espacios si algún paquete lo exige (algunas herramientas de la comunidad lo advierten).

## Cómo verificar
- [ ] El VRM se importa sin errores en la consola.
- [ ] El avatar humanoide figura como válido.

## Errores comunes
- Mezclar paquetes de VRM 0.x y 1.0 sin saberlo.
- Crear el proyecto con una versión de Unity que el SDK de Warudo no admite.

## Skills relacionadas
`unity-export-vrm`, `unity-warudo-sdk-export`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [GitHub – vrm-c/UniVRM (releases)](https://github.com/vrm-c/UniVRM/releases)
- ✅ [vrm.dev – How to make VRM](https://vrm.dev/en/vrm/how_to_make_vrm/)
- ✅ [Warudo Docs – Mod SDK](https://docs.warudo.app/docs/modding/mod-sdk)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

---
name: unity-materials-mtoon-unlit
description: "Define cómo se ilumina y se dibuja el avatar en Unity (MToon, unlit, lilToon, sombreado plano). Usar cuando el usuario hable de materiales, shaders, outline, sombras suaves, look anime o que el avatar se ve muy oscuro/brillante en Warudo."
---

# U3 · Materiales: MToon o unlit

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El material decide si el look pixelado y plano se conserva en la escena de Warudo.

## Procedimiento
1. Para VRM estándar usá **MToon** (viene con UniVRM) o un shader unlit con sombreado plano.
2. Si el destino es un `.warudo`, podés usar cualquier shader compatible con el **Built-in Render Pipeline** (la documentación de Warudo cita lilToon y Poiyomi). URP solo está soportado en Warudo Pro.
3. Desactivá o simplificá sombras suaves y outline según el look buscado.
4. Probá con distintas luces de la escena de Warudo.

## Cómo verificar
- [ ] El avatar se ve consistente con distintas luces.
- [ ] El shader elegido es compatible con el destino (VRM estándar o `.warudo`).

## Errores comunes
- Usar un shader de URP en Warudo sin ser Pro.
- Esperar que un shader personalizado viaje dentro de un VRM estándar.

## Skills relacionadas
`unity-psx-shader`, `unity-export-vrm`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Mod SDK](https://docs.warudo.app/docs/modding/mod-sdk)
- ✅ [GitHub – vrm-c/UniVRM (releases)](https://github.com/vrm-c/UniVRM/releases)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

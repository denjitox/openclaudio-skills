---
name: unity-psx-shader
description: "Aplica o crea un shader estilo PS1/PSX (vertex snapping, deformación de textura) para el avatar en Unity. Usar cuando el usuario pida el efecto PSX completo, vértices que tiemblan, look retro de PlayStation 1 o shaders personalizados para el avatar."
---

# U8 · Shader PSX (vértices que tiemblan, texturas afines)

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El pixelado de textura se logra sin shaders especiales, pero el efecto PSX completo sí los necesita.

## Procedimiento
1. Confirmá primero el destino: un VRM estándar **no** guarda shaders personalizados. Para Warudo hay que exportar `.warudo` (ver `unity-warudo-sdk-export`); para VSeeFace/VNyan existe `.vsfavatar`.
2. El shader debe ser compatible con el **Built-in Render Pipeline** (URP solo en Warudo Pro), según la documentación de Warudo.
3. Buscá un shader PSX para Unity con licencia que permita uso en streams y modificación, o crealo con Shader Graph/HLSL (verificá antes qué pipeline admite cada opción). Guardá la licencia.
4. Aplicalo solo a los materiales del avatar y probá en Warudo, no solo en Unity.
5. Tené un plan B: si el efecto da problemas, el avatar con Point filter ya conserva buena parte del look.

## Cómo verificar
- [ ] El efecto se ve igual en Unity y en Warudo.
- [ ] El shader tiene licencia compatible y está registrada.

## Errores comunes
- Esperar el shader dentro de un VRM estándar.
- Usar un shader de URP con Warudo gratis.
- No probar la versión final dentro de Warudo.

## Skills relacionadas
`unity-warudo-sdk-export`, `avatar-licensing-check`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Mod SDK](https://docs.warudo.app/docs/modding/mod-sdk)
- 🔎 [Studio Jimbly – formatos por programa (.vsfavatar / .warudo)](https://studiojimbly.carrd.co)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

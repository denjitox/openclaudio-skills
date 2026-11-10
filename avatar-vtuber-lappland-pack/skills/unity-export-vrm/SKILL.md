---
name: unity-export-vrm
description: "Exporta el VRM final desde Unity con UniVRM siguiendo el flujo oficial de dos pasadas. Usar cuando el usuario hable de exportar VRM, normalizar el modelo, T-pose o 'el VRM sale con huesos torcidos'."
---

# U6 · Exportar VRM desde Unity

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El flujo oficial normaliza el modelo y deja ajustar licencia, expresiones y física en el VRM ya generado.

## Procedimiento
1. Importá el modelo 3D a Unity, configurá materiales, dejalo en **T-pose** y activá la **normalización** del modelo.
2. Exportá como VRM.
3. Importá ese VRM al proyecto y personalizá licencia, spring bones, expresiones, eye look y first person.
4. Verificá el resultado en Play Mode.
5. Exportá el VRM otra vez: esa es la versión final.
6. Probá el VRM en Warudo y, para comprobar portabilidad, en VSeeFace o VNyan.

## Cómo verificar
- [ ] El VRM final abre en Warudo sin errores.
- [ ] También abre en un segundo programa (portabilidad).

## Errores comunes
- Saltarse la normalización.
- Exportar una sola vez y no revisar la licencia.

## Skills relacionadas
`unity-univrm-setup`, `avatar-qa-checklist`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [vrm.dev – How to make VRM](https://vrm.dev/en/vrm/how_to_make_vrm/)
- ✅ [GitHub – vrm-c/UniVRM (releases)](https://github.com/vrm-c/UniVRM/releases)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

---
name: avatar-versioning-backups
description: "Mantiene copias numeradas y backups del proyecto del avatar (Blender, Unity, SDK de Warudo). Usar al terminar cada fase, antes de ejecutar scripts o cambios grandes, o cuando el usuario hable de perder archivos, versiones o backups."
---

# T2 · Versionado y copias de seguridad

> Grupo: Transversal · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Los scripts y las exportaciones pueden romper archivos, y el SDK de Warudo avisa de pérdidas de ajustes de exportación.

## Procedimiento
1. Guardá versiones numeradas de Blender: `avatar_v01.blend`, `avatar_v02.blend`...
2. Si usás Git, hacé un commit al final de cada fase. En Unity ignorá las carpetas generadas (`Library`, `Temp`, `Logs`) y no ignores `Assets` ni `Packages`.
3. Para el proyecto del SDK de Warudo, la documentación recomienda hacer backups regulares o usar Unity Version Control, y respaldar `ExportSettings.asset`.
4. Antes de ejecutar un script del agente: copia del proyecto y confirmación del usuario.

## Cómo verificar
- [ ] Existe una copia reciente de cada archivo fuente.
- [ ] Los backups están fuera de la carpeta de trabajo (otro disco o nube).

## Errores comunes
- Trabajar sobre el único original.
- Hacer backup solo al final.

## Skills relacionadas
`unity-warudo-sdk-export`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Mod SDK](https://docs.warudo.app/docs/modding/mod-sdk)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

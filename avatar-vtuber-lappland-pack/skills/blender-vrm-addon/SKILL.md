---
name: blender-vrm-addon
description: "Configura y exporta VRM desde Blender con el add-on 'VRM format': humanoide, expresiones, spring bones y metadata de licencia. Usar cuando el usuario hable de exportar VRM, asignar huesos humanoides, expresiones VRM, metadata de licencia o instalar el add-on VRM."
---

# B7 · Add-on VRM de Blender

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El add-on convierte tu armature y shape keys en un VRM válido que Warudo, VSeeFace y VNyan pueden usar.

## Procedimiento
1. Instalá el add-on desde Blender Extensions (página 'VRM format') o desde el repositorio `saturday06/VRM-Addon-for-Blender`. Antes de instalar, **confirmá que la versión del add-on es compatible con tu versión de Blender**: el listado oficial indica compatibilidad por versión.
2. Asigná cada hueso a su rol humanoide (bone mapping).
3. Mapeá las expresiones VRM (`blink`, `aa`, `ih`, `ou`, `ee`, `oh`, emociones) a tus shape keys. Los release notes mencionan migración de expresiones de VRM 0.x a 1.0: elegí una versión de VRM y mantenela en todo el flujo.
4. Marcá los huesos de pelo, orejas, cola y capa como spring bones.
5. Completá la metadata: autor, usos permitidos, créditos y licencia.
6. Exportá y abrí el VRM en Unity (UniVRM) o en Warudo para comprobarlo.

## Cómo verificar
- [ ] El VRM exportado carga sin errores.
- [ ] La metadata de licencia está completa.
- [ ] Las expresiones y los spring bones funcionan en una app de prueba.

## Errores comunes
- Olvidar la metadata de licencia.
- Huesos humanoides sin asignar.
- Instalar una versión del add-on que no corresponde a la versión de Blender.

## Skills relacionadas
`blender-rig-weights`, `unity-export-vrm`, `avatar-licensing-check`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Blender Extensions – VRM format add-on](https://extensions.blender.org/add-ons/vrm)
- ✅ [GitHub – saturday06/VRM-Addon-for-Blender (releases)](https://github.com/saturday06/VRM-Addon-for-Blender/releases)
- 🔎 [VIVERSE – VRM models explained](https://news.viverse.com/post/vrm-models-explained)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

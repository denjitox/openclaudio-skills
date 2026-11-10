---
name: blender-pixel-preview
description: "Muestra las texturas sin suavizado (pixel art nítido) dentro de Blender. Usar cuando el usuario diga que la textura se ve borrosa en Blender, pida previsualizar el pixel art o mencione interpolación Closest."
---

# B4 · Previsualizar pixel art en Blender

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Si Blender suaviza la textura, no se puede juzgar el look real que tendrá en Warudo.

## Procedimiento
1. En el editor de materiales (Shading), en el nodo *Image Texture* cambiá *Interpolation* a **Closest** (sin interpolación, vecino más cercano; el manual lo describe como útil para pixel art).
2. Acercá la cámara y comprobá que los píxeles se ven nítidos.
3. Recordá que esto solo afecta a Blender: en Unity hay que configurar Point filter aparte (`unity-texture-import-pixel`).

## Cómo verificar
- [ ] Los píxeles se ven como bloques nítidos al acercar la cámara.

## Errores comunes
- Creer que ya está resuelto en Unity porque se ve bien en Blender.

## Skills relacionadas
`blender-uv-pixel-textures`, `unity-texture-import-pixel`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Blender Manual – Image Texture node](https://docs.blender.org/manual/en/4.0/render/shader_nodes/textures/image.html)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

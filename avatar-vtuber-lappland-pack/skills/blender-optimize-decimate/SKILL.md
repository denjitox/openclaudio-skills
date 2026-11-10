---
name: blender-optimize-decimate
description: "Reduce polígonos, materiales y texturas del avatar en Blender sin romper las expresiones. Usar cuando el usuario diga que el modelo es pesado, tiene muchos polígonos, quiera aplicar Decimate, unir materiales o mejorar el rendimiento en Warudo."
---

# B8 · Optimización y Decimate

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Con gráficos integrados (sin GPU dedicada) cada polígono y material cuenta.

## Procedimiento
1. Hacé una copia del `.blend` antes de empezar.
2. *Merge by Distance* para soldar vértices duplicados.
3. Aplicá el modificador *Decimate* en cuerpo, ropa y pelo.
4. **No decimes la cara ni mallas con shape keys** sin cuidado: se rompen los morphs. Reducí la cara a mano.
5. Unificá materiales y bajá la resolución de texturas.
6. Comparé triángulos antes y después, y volvé a probar las expresiones.

## Cómo verificar
- [ ] Triángulos antes/después anotados.
- [ ] Todas las expresiones siguen funcionando.

## Errores comunes
- Aplicar Decimate sobre mallas con shape keys.
- Reducir tanto que se pierde la silueta distintiva.

## Skills relacionadas
`blender-lowpoly-modeling`, `unity-performance-igpu`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- 🧠 [Blender Manual (índice)](https://docs.blender.org/manual/en/latest/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

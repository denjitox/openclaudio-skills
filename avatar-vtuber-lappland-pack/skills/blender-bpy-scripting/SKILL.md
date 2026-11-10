---
name: blender-bpy-scripting
description: "Automatiza tareas repetitivas en Blender con Python (bpy): crear shape keys ARKit, revisar nombres de shape keys y huesos, contar triángulos. Usar cuando el usuario pida un script de Blender, automatizar, renombrar en lote o validar el modelo."
---

# B9 · Scripting con bpy

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Crear 20 a 52 shape keys con nombres exactos a mano es lento y propenso a errores de tipeo.

## Procedimiento
1. Trabajá siempre sobre una **copia** del `.blend` y mostrale el código al usuario antes de ejecutarlo.
2. Para crear los shape keys ARKit faltantes usá `scripts/create_arkit_shapekeys.py` (selecciona la malla de la cara y corré el script desde el editor de texto de Blender).
3. Para revisar nombres y triángulos usá `scripts/check_names_and_tris.py`. Informa shape keys ARKit faltantes o con nombre casi igual, huesos duplicados y triángulos por objeto.
4. Estos scripts **no se probaron dentro de Blender en esta sesión** (solo se verificó que la sintaxis de Python sea válida). Probalos primero en una escena de prueba.

## Scripts incluidos
- `scripts/create_arkit_shapekeys.py`: crea los shape keys ARKit que falten en la malla activa (no borra ni modifica los existentes).
- `scripts/check_names_and_tris.py`: informa shape keys ARKit faltantes o con nombre casi igual, huesos duplicados y triángulos por objeto.
- Estado: **sin probar dentro de la aplicación en esta sesión** (probar en una copia).

## Cómo verificar
- [ ] El script informa qué cambió y no toca nada fuera de lo pedido.
- [ ] Los nombres creados coinciden con la lista ARKit.

## Errores comunes
- Ejecutar scripts sin copia del archivo.
- Asumir que la API de Blender no cambió entre versiones: revisá la documentación de tu versión.

## Skills relacionadas
`blender-arkit-shapekeys`, `blender-optimize-decimate`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- 🧠 [Blender Python API](https://docs.blender.org/api/current/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

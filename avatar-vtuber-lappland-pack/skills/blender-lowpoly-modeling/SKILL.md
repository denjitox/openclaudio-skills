---
name: blender-lowpoly-modeling
description: "Modela el avatar low poly (estilo PSX, 3.000 a 10.000 triángulos) en Blender con piezas separadas. Usar siempre que el usuario hable de modelar cuerpo, cabeza, pelo, orejas, cola o accesorios, de extruir, loop cuts, bajar polígonos o de un presupuesto de triángulos, aunque no diga 'low poly'."
---

# B1 · Modelado low poly del avatar

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El estilo PSX depende de una geometría simple, y con GPU integrada un modelo liviano rinde mejor en Warudo.

## Procedimiento
1. Activá las estadísticas del viewport (Overlays → Statistics) para ver el conteo de triángulos mientras modelás.
2. Empezá con formas básicas (cubos, cilindros) y extruí. Evitá modificadores de subdivisión.
3. Respetá este presupuesto orientativo (viene de la guía del proyecto, no es un límite técnico de Warudo): cabeza 800–1.500, cuerpo 1.000–2.500, pelo 500–2.000, ropa y accesorios 500–2.500; total 3.000–10.000 triángulos.
4. Mantené piezas separadas con nombres claros (`Body`, `Head`, `Hair`, `Ears`, `Tail`, `Outfit`, `Accessory_*`). Se unen bajo un mismo armature recién al riggear.
5. Aplicá escala y rotación (`Ctrl+A`) y dejá el modelo en pose T o A, de frente.
6. Dejá topología limpia alrededor de ojos y boca: ahí van los shape keys (ver `blender-arkit-shapekeys`).

## Cómo verificar
- [ ] El conteo de triángulos está dentro del presupuesto.
- [ ] Escala 1 y rotación 0 en todos los objetos.
- [ ] Cada pieza tiene un nombre descriptivo.

## Errores comunes
- Subdividir de más 'por si acaso'.
- Unir todo en una sola malla: después cuesta separar ropa y pelo.
- Modelar la cara sin pensar en las expresiones.

## Skills relacionadas
`blender-flat-shading`, `blender-uv-pixel-textures`, `blender-rig-weights`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- 🧠 [Blender Manual (índice)](https://docs.blender.org/manual/en/latest/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

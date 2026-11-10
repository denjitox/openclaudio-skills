---
name: blender-arkit-shapekeys
description: "Crea y revisa los shape keys con nombres ARKit exactos (parpadeo, boca, cejas, mejillas) para que el tracking de webcam mueva la cara del avatar. Usar siempre que el usuario hable de expresiones, blendshapes, shape keys, ARKit, tracking facial, visemas o 'la cara no se mueve', aunque no mencione Blender."
---

# B6 · Shape keys ARKit

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Con webcam el modelo hace gran parte del trabajo: si no tiene los blendshapes, el tracking no tiene qué mover. MediaPipe en Warudo rastrea más de 40 blendshapes ARKit, pero solo se ven los que el modelo tiene.

## Procedimiento
1. Creá el *Basis* y después cada shape key con el **nombre ARKit exacto** (respetá mayúsculas y minúsculas). Para automatizarlo usá `blender-bpy-scripting`.
2. Empezá por el conjunto mínimo (tabla de abajo) y ampliá después.
3. Hacé un lado (por ejemplo `mouthSmileLeft`) y espejalo al otro. Usá grupos de vértices izquierda/derecha para separar los lados con precisión.
4. Atención con los lados: según Apple, izquierda y derecha son relativas a la cara del personaje (`eyeBlinkRight` es el ojo derecho de la cara, no el de la pantalla).
5. Exagerá cada forma: con pocos vértices los cambios chicos no se notan.
6. Probá cada slider al 100 % y revisá que no se crucen polígonos.
7. Si usás ojos pintados en la textura, el parpadeo puede ser un párpado modelado o un cambio de UV. La mirada (`eyeLook*`) se puede resolver con huesos de ojos o desplazando la UV en lugar de 8 shape keys.

## Lista completa (52) y versión mínima

| Grupo | Blendshapes ARKit |
|---|---|
| Ojos (14) | `eyeBlinkLeft/Right`, `eyeLookDownLeft/Right`, `eyeLookInLeft/Right`, `eyeLookOutLeft/Right`, `eyeLookUpLeft/Right`, `eyeSquintLeft/Right`, `eyeWideLeft/Right` |
| Mandíbula (4) | `jawForward`, `jawLeft`, `jawRight`, `jawOpen` |
| Boca (23) | `mouthClose`, `mouthFunnel`, `mouthPucker`, `mouthLeft`, `mouthRight`, `mouthSmileLeft/Right`, `mouthFrownLeft/Right`, `mouthDimpleLeft/Right`, `mouthStretchLeft/Right`, `mouthRollLower`, `mouthRollUpper`, `mouthShrugLower`, `mouthShrugUpper`, `mouthPressLeft/Right`, `mouthLowerDownLeft/Right`, `mouthUpperUpLeft/Right` |
| Cejas (5) | `browDownLeft/Right`, `browInnerUp`, `browOuterUpLeft/Right` |
| Mejillas (3) | `cheekPuff`, `cheekSquintLeft/Right` |
| Nariz (2) | `noseSneerLeft/Right` |
| Lengua (1) | `tongueOut` |

Versión mínima recomendada para un modelo low poly (unos 20 a 24):

| Prioridad | Blendshapes |
|---|---|
| Imprescindibles | `eyeBlinkLeft/Right`, `jawOpen`, `mouthSmileLeft/Right`, `mouthFunnel`, `mouthPucker`, `mouthClose` |
| Muy recomendables | `browDownLeft/Right`, `browInnerUp`, `browOuterUpLeft/Right`, `eyeWideLeft/Right`, `mouthFrownLeft/Right` |
| Extras con personalidad | `eyeSquintLeft/Right`, `cheekPuff`, `mouthLowerDownLeft/Right`, `tongueOut` |

## Cómo verificar
- [ ] Los nombres de los shape keys coinciden exactamente con la lista ARKit (usá el script de revisión).
- [ ] Cada slider al 100 % se ve bien.
- [ ] En Warudo la cara responde (ver `warudo-import-character-review`).

## Errores comunes
- Mayúsculas/minúsculas distintas a las de ARKit.
- Invertir izquierda y derecha.
- Shape keys con polígonos cruzados al 100 %.
- Decimar la cara después de hacer los shape keys.

## Skills relacionadas
`blender-bpy-scripting`, `unity-expression-review`, `warudo-mediapipe-tracking`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Apple Developer – ARFaceAnchor.BlendShapeLocation](https://developer.apple.com/documentation/arkit/arfaceanchor/blendshapelocation)
- ✅ [Warudo Docs – MediaPipe](https://docs.warudo.app/docs/mocap/mediapipe)
- ✅ [Warudo Docs – OpenSeeFace](https://docs.warudo.app/docs/mocap/openseeface)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

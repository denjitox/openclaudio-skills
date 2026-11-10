---
name: warudo-blueprints-smoothing
description: "Ajusta los blueprints de tracking de Warudo y el suavizado (Smooth Time) para equilibrar fluidez y reactividad. Usar cuando el usuario diga que el avatar tiembla, que responde con retardo, o pida personalizar los nodos de tracking."
---

# W4 · Blueprints y suavizado

> Grupo: Warudo · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El suavizado define si el avatar se siente fluido o con lag.

## Procedimiento
1. Abrí el blueprint de tracking (por ejemplo *Face Tracking - MediaPipe*).
2. Buscá los nodos *Smooth BlendShape List*, *Smooth Rotation List*, *Smooth Position List* y *Smooth Transform*.
3. **Subir el *Smooth Time*** suaviza el movimiento pero agrega retardo; **bajarlo** lo vuelve más reactivo pero con más temblor.
4. Buscá un punto medio probándolo con tu cámara real.
5. Si ciertas expresiones (cejas, sonrisa, ojos muy abiertos) casi no se ven, la documentación de OpenSeeFace muestra que hay parámetros de sensibilidad por blendshape; revisá si tu tracker tiene opciones equivalentes en pantalla.

## Cómo verificar
- [ ] Movimiento fluido sin retardo molesto.

## Errores comunes
- Suavizar de más y perder reacciones rápidas como el parpadeo.

## Skills relacionadas
`warudo-mediapipe-tracking`, `warudo-troubleshooting`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Motion capture (overview)](https://docs.warudo.app/docs/mocap/overview)
- ✅ [Warudo Docs – OpenSeeFace](https://docs.warudo.app/docs/mocap/openseeface)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

---
name: warudo-mediapipe-tracking
description: "Configura y calibra el tracking de webcam con MediaPipe en Warudo y mejora su calidad con luz, encuadre y ajustes. Usar siempre que el usuario hable de tracking con webcam, calidad de seguimiento, calibración, que el avatar tiembla o que 'no se parece al ARKit del iPhone'."
---

# W3 · Tracking facial con MediaPipe

> Grupo: Warudo · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
MediaPipe es el sistema de webcam integrado en Warudo y el que la documentación recomienda frente a OpenSeeFace.

## Procedimiento
1. MediaPipe viene integrado: no hace falta instalar nada. Rastrea más de 40 blendshapes ARKit, rotación y posición de la cabeza.
2. Cámara **encima de la pantalla**, con la cabeza ligeramente por encima del centro de la imagen.
3. Calibrá con **Character → Motion Capture → Quick Calibration → Calibrate MediaPipe** (o *Calibrate* en el asset *MediaPipe Tracker*), con la cara neutra mirando al frente.
4. Con webcam 720p/30 fps la luz pesa más que la resolución: luz frontal y difusa. Si la sala está oscura, la cámara puede bajar los FPS reales.
5. Comprobá que la webcam corra a 30+ FPS reales con una web de test de FPS.
6. Si la ventana del tracker muestra FPS mucho más bajos que la cámara, probá activar o desactivar *GPU Acceleration* en el asset *MediaPipe Tracker* y medí.
7. Para la mano, la documentación recomienda calibrar también el tracking de manos.

## Cómo verificar
- [ ] Cara neutra quieta, parpadeo correcto y sonrisa/boca con respuesta clara.
- [ ] FPS del tracker estables.

## Errores comunes
- Mala luz o contraluz.
- Flequillo o sombras tapando cejas y ojos.
- Calibrar con expresión no neutra.

## Skills relacionadas
`warudo-blueprints-smoothing`, `warudo-troubleshooting`, `warudo-external-tracking`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – MediaPipe](https://docs.warudo.app/docs/mocap/mediapipe)
- ✅ [Warudo Docs – Motion capture (overview)](https://docs.warudo.app/docs/mocap/overview)
- 🔎 [VIVERSE – Best VTuber software setup for beginners 2026](https://news.viverse.com/post/best-vtuber-software-setup-for-beginners-in-2026)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

---
name: unity-performance-igpu
description: "Mantiene el avatar y la escena livianos mientras no haya GPU dedicada (Ryzen 5 5600G con gráficos integrados). Usar cuando el usuario hable de FPS bajos, lag, rendimiento, optimizar o de la futura RTX 3060."
---

# U10 · Rendimiento con GPU integrada

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Hoy la CPU y los gráficos integrados comparten recursos con el tracking, OBS y Warudo.

## Procedimiento
1. Reducí materiales (idealmente uno por pieza o menos), tamaño de texturas y cantidad de luces; evitá sombras pesadas.
2. Usá el Profiler de Unity para ver dónde se va el tiempo (verificá cómo abrirlo en tu versión).
3. Con la ventana del tracker de MediaPipe con pocos FPS, probá activar/desactivar *GPU Acceleration* en Warudo: no se sabe de antemano cuál rinde mejor en una GPU integrada, hay que medir.
4. Cerrá programas pesados durante el stream.
5. Con la RTX 3060 (a futuro) mejorará el render y la codificación del stream; que el tracking de NVIDIA funcione en Warudo **no está verificado** (ver `warudo-external-tracking`).

## Cómo verificar
- [ ] FPS estables en Warudo con el stream abierto.
- [ ] Se anotó el FPS con y sin GPU Acceleration.

## Errores comunes
- Asumir que una opción rinde mejor sin medir.
- Comprar hardware esperando una función que Warudo quizá no tenga.

## Skills relacionadas
`blender-optimize-decimate`, `warudo-mediapipe-tracking`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – MediaPipe](https://docs.warudo.app/docs/mocap/mediapipe)
- 🧠 [Unity Manual (índice)](https://docs.unity3d.com/Manual/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

---
name: warudo-onboarding
description: "Guía la primera configuración de Warudo con el Onboarding Assistant: importar el personaje, elegir el tracking y generar los blueprints. Usar cuando el usuario empiece una escena nueva, no sepa cómo configurar el tracking o diga que su personaje no se mueve tras cargarlo."
---

# W1 · Asistente inicial (Onboarding) de Warudo

> Grupo: Warudo · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
El asistente deja el tracking funcionando con pocos pasos y genera los blueprints de base.

## Procedimiento
1. Cada escena de Warudo incluye un asset *Onboarding Assistant*. Iniciá desde **Basic Setup → Get Started** y seguí las instrucciones (los menús pueden cambiar con la versión: verificá en pantalla).
2. Warudo puede **recomendar un setup de mocap** haciendo algunas preguntas. Para webcam, la documentación recomienda empezar con MediaPipe.
3. Durante el onboarding Warudo importa automáticamente las expresiones VRM del personaje y genera un blueprint con hotkeys para ellas.
4. Al terminar se generan blueprints de tracking, por ejemplo *Face Tracking - MediaPipe*. Se pueden editar para personalizar.

## Cómo verificar
- [ ] Aparecen los blueprints de tracking en la escena.
- [ ] El personaje responde a la webcam.

## Errores comunes
- Saltar el onboarding y configurar todo a mano sin necesidad.
- Firewall o antivirus bloqueando datos o cámara (ver `warudo-troubleshooting`).

## Skills relacionadas
`warudo-mediapipe-tracking`, `warudo-blueprints-smoothing`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Motion capture (overview)](https://docs.warudo.app/docs/mocap/overview)
- ✅ [Warudo Docs – Getting started](https://docs.warudo.app/docs/tutorials/getting-started)
- ✅ [Warudo Docs – Character](https://docs.warudo.app/docs/assets/character)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

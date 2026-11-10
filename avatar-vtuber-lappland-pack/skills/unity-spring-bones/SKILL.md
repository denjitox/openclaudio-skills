---
name: unity-spring-bones
description: "Configura la física secundaria (spring bones) de pelo, orejas, cola y capa en Unity. Usar cuando el usuario hable de física, orejas o cola que se mueven, pelo que atraviesa el cuerpo, colliders o 'parece gelatina'."
---

# U4 · Spring bones (física de pelo, orejas y cola)

> Grupo: Unity · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
Las orejas y la cola con física son lo que más personalidad da a un avatar tipo lobo.

## Procedimiento
1. Importá el VRM en Unity (UniVRM) y abrí la configuración de spring bones.
2. Definí los grupos para pelo, orejas, cola y capa, y ajustá rigidez y gravedad.
3. Agregá colliders en cabeza, cuello y cuerpo para evitar atravesamientos.
4. Probá en Play Mode moviendo el avatar.
5. Si en el `.warudo` querés otro sistema, la documentación de Warudo menciona Dynamic Bone y Magica Cloth, pero **esos paquetes no vienen incluidos**: hay que importarlos aparte (y revisar sus licencias).

## Cómo verificar
- [ ] Orejas y cola responden sin atravesar el cuerpo.
- [ ] El movimiento no es excesivo ni inexistente.

## Errores comunes
- Rigidez muy baja (gelatina) o muy alta (sin movimiento).
- Colliders ausentes o mal ubicados.

## Skills relacionadas
`blender-rig-weights`, `unity-export-vrm`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Character Mod](https://docs.warudo.app/docs/modding/character-mod)
- ✅ [vrm.dev – How to make VRM](https://vrm.dev/en/vrm/how_to_make_vrm/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

---
name: blender-rig-weights
description: "Crea el esqueleto humanoide y los pesos (weight paint) del avatar en Blender, incluidas orejas, cola y pelo. Usar cuando el usuario hable de armature, huesos, rigging, pesos, deformaciones raras, orejas o cola que se mueven, o prepare el modelo para VRM."
---

# B5 · Rig humanoide y weight paint

> Grupo: Blender · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
VRM exige un esqueleto humanoide estándar, y las orejas y la cola necesitan huesos propios para tener física.

## Procedimiento
1. Creá un armature humanoide en pose T o A con huesos estándar (hips, spine, chest, neck, head, brazos, piernas, manos).
2. Agregá huesos extra: 2 a 4 para cada oreja y para la cola, y los que hagan falta para pelo largo o capa. Nombres únicos y simétricos.
3. Parentá las mallas al armature con *Automatic Weights* y corregí hombros, cadera y cuello en Weight Paint. Normalizá los pesos.
4. Mové cada hueso principal para detectar deformaciones raras (codos, rodillas, cuello).
5. Si el destino final es Warudo vía Unity, tené en cuenta que los huesos deben estar normalizados: la documentación de Warudo dice que los VRM garantizan huesos normalizados, y que una forma probada de normalizar es crear un VRM a partir del FBX.

## Cómo verificar
- [ ] Todas las poses de prueba deforman sin estirar la malla.
- [ ] Los nombres de huesos no tienen duplicados.
- [ ] Las orejas y la cola tienen sus propias cadenas de huesos.

## Errores comunes
- Huesos con nombres duplicados (`.001`).
- Pesos que 'se contagian' entre pelo y cuello.
- Exportar FBX con rotaciones de hueso incorrectas (el exportador FBX de Blender tiene problemas conocidos según Warudo).

## Skills relacionadas
`blender-arkit-shapekeys`, `blender-vrm-addon`, `unity-spring-bones`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- ✅ [Warudo Docs – Character Mod](https://docs.warudo.app/docs/modding/character-mod)
- 🧠 [Blender Manual (índice)](https://docs.blender.org/manual/en/latest/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

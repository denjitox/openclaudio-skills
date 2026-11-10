# Pack: avatar low poly PSX inspirado en Lappland (Blender · Unity · Warudo)

Conjunto de documentación y **31 skills** para crear un avatar **original** de estilo low poly pixelado (PSX), inspirado en la estética de Lappland (Arknights), y usarlo en **Warudo**, con tracking de webcam lo más cercano posible a ARKit.

Preparado el 2026-11-01. Idioma de trabajo: **español**.

## Contenido

```
avatar-vtuber-lappland-pack/
├── README.md                     ← este archivo (leer primero)
├── FUENTES.md                    ← todas las fuentes y su estado de verificación
├── docs/
│   ├── guia-avatar-low-poly-lappland.md            ← guía principal paso a paso
│   └── recopilacion-skills-blender-unity-warudo.md ← explicación de las skills (versión para humanos)
└── skills/
    └── <nombre-de-skill>/SKILL.md  ← 31 skills, una por carpeta (+ scripts/ en 2 de ellas)
```

## Orden de lectura para el agente
1. Este README (contexto y reglas).
2. `docs/guia-avatar-low-poly-lappland.md` (flujo completo).
3. Las skills de `skills/` según la fase en la que esté el usuario.

## Cómo instalar las skills
- **Claude Code:** copiá las carpetas de `skills/` a `.claude/skills/` dentro del proyecto, o a `~/.claude/skills/` para tenerlas disponibles en todos los proyectos (según lo que describe la documentación de un proyecto de la comunidad; confirmalo en la documentación oficial de tu agente).
- **Otros agentes:** tratá cada `SKILL.md` como un documento de instrucciones y leelo cuando corresponda a la tarea.

## Contexto del usuario
- Hace streams con avatares 3D en **Warudo** y empezó a convertir modelos MMD (.pmx) a VRM.
- **Equipo:** Ryzen 5 5600G **sin GPU dedicada** (planea una RTX 3060 de 12 GB), webcam 720p/30 fps.
- **Software:** Blender, Unity, Warudo.
- **Archivos propios:** dos PMX (Texas y Lappland alter), **solo como referencia de proporciones**.
- **Prioridades:** simple, no depender solo de Warudo (el VRM base debe funcionar también en VSeeFace/VNyan) y tracking de webcam lo más cercano posible a ARKit.

## Reglas generales para el agente
1. **No uses los PMX como base** del modelo: tienen licencias propias y el modelo debe ser original.
2. **Licencias:** no descargues ni uses assets de terceros sin confirmar que permiten modificar y usar en streams (y uso comercial si el canal se monetiza). Guardá una captura con fecha (`avatar-licensing-check`).
3. **Preguntá antes de instalar** programas, addons o paquetes, y antes de borrar, sobrescribir o mover archivos del usuario.
4. **Trabajá sobre copias** y versioná (`avatar-versioning-backups`). Probá los scripts primero en una copia.
5. **No inventes** versiones, menús ni URLs. Si algo de este pack no coincide con lo que ves en pantalla o en la documentación oficial, confiá en lo que ves y avisale al usuario.
6. **Avanzá por fases** y esperá la confirmación del usuario al terminar cada una.
7. **No cambies el diseño artístico** por tu cuenta: proponé opciones y dejá que elija el usuario.
8. Los **conectores MCP** (`agent-mcp-connectors`) pueden ejecutar código en la PC: usalos solo con copias y con aprobación del usuario.

## Qué se verificó (2026-11-01) y qué cambió respecto a documentos anteriores
Se consultó documentación oficial de Warudo, UniVRM, vrm.dev, Blender, Unity y Apple. Cambios y datos nuevos:

- **Warudo no soporta `.vsfavatar`**; usa `.warudo`, exportado con el Mod SDK. `.vsfavatar` es de VSeeFace/VNyan.
- **Shaders personalizados en Warudo:** deben ser compatibles con el **Built-in Render Pipeline**; URP solo en **Warudo Pro**.
- **Modelos no VRM:** la documentación de Warudo indica que modelos MMD o FBX se pueden exportar a `.warudo` con el Mod SDK, sin pasar por VRM. Si el usuario solo quiere sus PMX en Warudo, es un camino más corto (sujeto a licencias).
- **Pasos del SDK de Warudo:** `Warudo → Setup Character...` y `Warudo → Build Mod`; el `.warudo` va en la carpeta `Characters` del data folder. **Los huesos deben estar normalizados**; `.asmdef` no están soportados; hacer backup de `ExportSettings.asset`.
- **UniVRM:** soporta Unity 2021.3 LTS o posterior. Flujo oficial de VRM en **dos pasadas** (exportar, importar el VRM, ajustar licencia/expresiones/spring bones, volver a exportar).
- **MMD Tools:** el repositorio activo es `MMD-Blender/blender_mmd_tools`; hay que usar la versión que corresponde a tu Blender LTS (v4.x para 4.2 LTS, v2.x para 3.6 LTS).
- **Add-on VRM de Blender:** se publica como "VRM format" en Blender Extensions y su compatibilidad depende de la versión de Blender: confirmala antes de instalar.
- **ARKit (Apple):** izquierda y derecha de los blendshapes son **relativas a la cara del personaje**.
- **Onboarding de Warudo:** importa automáticamente las expresiones VRM y genera un blueprint con hotkeys.
- **Cantidad de skills:** son **31** (en un mensaje anterior se dijo 28 por error).

## Lo que sigue **sin verificar**
- Cómo Warudo mapea exactamente los blendshapes ARKit de un VRM exportado (probar con un modelo simple).
- Si Warudo integra el tracking facial de **NVIDIA** (relevante para la futura RTX 3060).
- Cómo se conecta **MeowFace** (Android) con Warudo.
- El método actual para llevar Warudo a **OBS**.
- Si *GPU Acceleration* de MediaPipe rinde mejor con la GPU integrada (medir).
- La política de fan content de **Arknights** (Hypergryph/Yostar).
- Los conectores **MCP** de Blender y Unity (no se probaron).
- Los **scripts** incluidos: solo se verificó la sintaxis de Python; el script de C# no se compiló.
- Páginas de manual citadas "de memoria" (🧠) en cada skill.

## Índice de skills
| ID | Skill | Grupo | Tema |
|---|---|---|---|
| B1 | [`blender-lowpoly-modeling`](skills/blender-lowpoly-modeling/SKILL.md) | Blender | Modelado low poly del avatar |
| B2 | [`blender-flat-shading`](skills/blender-flat-shading/SKILL.md) | Blender | Sombreado plano (flat) |
| B3 | [`blender-uv-pixel-textures`](skills/blender-uv-pixel-textures/SKILL.md) | Blender | UV para texturas pixeladas |
| B4 | [`blender-pixel-preview`](skills/blender-pixel-preview/SKILL.md) | Blender | Previsualizar pixel art en Blender |
| B5 | [`blender-rig-weights`](skills/blender-rig-weights/SKILL.md) | Blender | Rig humanoide y weight paint |
| B6 | [`blender-arkit-shapekeys`](skills/blender-arkit-shapekeys/SKILL.md) | Blender | Shape keys ARKit |
| B7 | [`blender-vrm-addon`](skills/blender-vrm-addon/SKILL.md) | Blender | Add-on VRM de Blender |
| B8 | [`blender-optimize-decimate`](skills/blender-optimize-decimate/SKILL.md) | Blender | Optimización y Decimate |
| B9 | [`blender-bpy-scripting`](skills/blender-bpy-scripting/SKILL.md) | Blender | Scripting con bpy |
| B10 | [`blender-mmd-reference`](skills/blender-mmd-reference/SKILL.md) | Blender | Referencia con PMX (mmd_tools) |
| U1 | [`unity-univrm-setup`](skills/unity-univrm-setup/SKILL.md) | Unity | Proyecto Unity y UniVRM |
| U2 | [`unity-texture-import-pixel`](skills/unity-texture-import-pixel/SKILL.md) | Unity | Import de texturas pixeladas (Point filter) |
| U3 | [`unity-materials-mtoon-unlit`](skills/unity-materials-mtoon-unlit/SKILL.md) | Unity | Materiales: MToon o unlit |
| U4 | [`unity-spring-bones`](skills/unity-spring-bones/SKILL.md) | Unity | Spring bones (física de pelo, orejas y cola) |
| U5 | [`unity-expression-review`](skills/unity-expression-review/SKILL.md) | Unity | Revisión de expresiones |
| U6 | [`unity-export-vrm`](skills/unity-export-vrm/SKILL.md) | Unity | Exportar VRM desde Unity |
| U7 | [`unity-warudo-sdk-export`](skills/unity-warudo-sdk-export/SKILL.md) | Unity | Exportar .warudo con el SDK de Warudo |
| U8 | [`unity-psx-shader`](skills/unity-psx-shader/SKILL.md) | Unity | Shader PSX (vértices que tiemblan, texturas afines) |
| U9 | [`unity-editor-scripts`](skills/unity-editor-scripts/SKILL.md) | Unity | Scripts de editor en C# |
| U10 | [`unity-performance-igpu`](skills/unity-performance-igpu/SKILL.md) | Unity | Rendimiento con GPU integrada |
| W1 | [`warudo-onboarding`](skills/warudo-onboarding/SKILL.md) | Warudo | Asistente inicial (Onboarding) de Warudo |
| W2 | [`warudo-import-character-review`](skills/warudo-import-character-review/SKILL.md) | Warudo | Importar y revisar el personaje en Warudo |
| W3 | [`warudo-mediapipe-tracking`](skills/warudo-mediapipe-tracking/SKILL.md) | Warudo | Tracking facial con MediaPipe |
| W4 | [`warudo-blueprints-smoothing`](skills/warudo-blueprints-smoothing/SKILL.md) | Warudo | Blueprints y suavizado |
| W5 | [`warudo-scene-obs-output`](skills/warudo-scene-obs-output/SKILL.md) | Warudo | Escena, cámara y salida a OBS |
| W6 | [`warudo-troubleshooting`](skills/warudo-troubleshooting/SKILL.md) | Warudo | Diagnóstico de problemas comunes |
| W7 | [`warudo-external-tracking`](skills/warudo-external-tracking/SKILL.md) | Warudo | Tracking externo (iFacialMocap, MeowFace, NVIDIA) |
| T1 | [`avatar-licensing-check`](skills/avatar-licensing-check/SKILL.md) | Transversal | Verificación de licencias |
| T2 | [`avatar-versioning-backups`](skills/avatar-versioning-backups/SKILL.md) | Transversal | Versionado y copias de seguridad |
| T3 | [`avatar-qa-checklist`](skills/avatar-qa-checklist/SKILL.md) | Transversal | Checklist de calidad (QA) del avatar |
| T4 | [`agent-mcp-connectors`](skills/agent-mcp-connectors/SKILL.md) | Transversal | Conectar un agente a Blender y Unity (MCP) |

Ruta recomendada: B1–B4 → B5–B7 → U1–U3 → W1–W4 → U4–U6, B8 → extras (U7, U8, W7) → automatización (B9, U9, T4). En paralelo: T1 (licencias), T2 (copias), T3 (calidad).

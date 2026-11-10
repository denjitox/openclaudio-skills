# Guía: avatar low poly original inspirado en Lappland (Blender → Unity → Warudo)

Guía paso a paso para crear un avatar **original**, de estilo low poly pixelado (tipo PS1/PSX), inspirado en la estética de Lappland (Arknights), y usarlo en **Warudo**.

---

## Contexto para el agente (leer primero)

Este documento fue escrito para que lo lea un agente que ayuda al usuario en su PC. No asumas nada que no esté acá: si falta información, preguntale al usuario.

### Usuario y objetivo
- **Idioma:** español. Respondé y documentá en español.
- **Perfil:** hace streams con avatares 3D en **Warudo** y está empezando a convertir modelos MMD (.pmx) a VRM.
- **Objetivo:** crear un avatar **original** (no una copia) de estilo **low poly pixelado tipo PSX**, inspirado en la estética de Lappland (Arknights), listo para Warudo.
- **Prioridades:** que sea **simple**, que **no dependa solo de Warudo** (el VRM base debe funcionar también en VSeeFace/VNyan), y que el **tracking con webcam** se acerque lo más posible al de ARKit.

### Equipo y software del usuario
| Elemento | Detalle |
|---|---|
| CPU / GPU | Ryzen 5 5600G, **sin GPU dedicada** por ahora (gráficos integrados). Planea comprar una RTX 3060 de 12 GB |
| Webcam | 720p, 30 fps |
| Software | Blender, Unity, Warudo |
| Archivos propios | Dos modelos PMX (Texas y Lappland alter). **Solo como referencia de proporciones**, no como base |

### Reglas para el agente
1. **No uses los PMX como base** del modelo. Tienen licencias propias y el modelo debe ser original.
2. **Licencias:** no descargues ni uses modelos, texturas o assets de terceros sin confirmar que su licencia permite modificar y usar en streams (y uso comercial si el canal se monetiza). Guardá una captura de la licencia.
3. **Preguntá antes de instalar** programas, addons o paquetes, y antes de borrar, sobrescribir o mover archivos del usuario.
4. **Versioná:** guardá copias numeradas (`avatar_v01.blend`, `avatar_v02.blend`...) y no trabajes sobre el único original.
5. **No inventes** versiones, rutas de menús ni URLs. Si algo de este documento no coincide con lo que ves en pantalla o en la documentación oficial, **confiá en lo que ves** y avisale al usuario.
6. **Avanzá por fases** (ver "Orden recomendado de trabajo" al final): al terminar cada una, resumí qué hiciste y esperá la confirmación del usuario antes de seguir.
7. **No cambies el diseño artístico** (colores, silueta, estética) por tu cuenta: proponé opciones y dejá que elija el usuario.

### Qué está verificado y qué no
| Tema | Estado |
|---|---|
| MediaPipe integrado en Warudo, recomendado sobre OpenSeeFace, calibración, suavizado y consejos de luz/FPS | Verificado en la documentación oficial de Warudo |
| Recomendación de iPhone 12+ con iFacialMocap como mejor tracking facial | Verificado en la documentación oficial de Warudo |
| Warudo soporta VRM 0.x y 1.0; VSeeFace solo VRM 0.x | Informado por una guía de terceros: confirmar |
| URLs de herramientas (sección 0) | Escritas de memoria: **verificar** antes de usarlas |
| Warudo usa `.warudo` vía Mod SDK (no soporta `.vsfavatar`); los shaders personalizados deben ser Built-in RP (URP solo en Warudo Pro); los huesos deben estar normalizados | Verificado en la documentación oficial de Warudo (2026-11-01) |
| UniVRM soporta Unity 2021.3 LTS o posterior; flujo oficial de VRM en dos pasadas | Verificado en releases de UniVRM y vrm.dev (2026-11-01) |
| Apple: izquierda/derecha de los blendshapes ARKit son relativas a la cara del personaje | Verificado en documentación de Apple (2026-11-01) |
| Que Warudo integre el tracking facial de NVIDIA | **No verificado** |
| Cómo Warudo lee los blendshapes ARKit de un VRM exportado (nombres, mapeo) | **No verificado**: probar con un modelo simple |
| Si "GPU Acceleration" de MediaPipe rinde mejor en la GPU integrada | **No verificado**: medir FPS con y sin |
| Cómo se conecta MeowFace (Android) con Warudo | **No verificado** |

### Cosas que el agente puede ayudar a automatizar
Son ideas, no tareas ya hechas. Proponelas al usuario antes de ejecutarlas:
- Un **script de Blender (Python/`bpy`)** que cree shape keys vacíos con los nombres ARKit exactos y los ordene.
- Un script que **revise nombres** de shape keys y huesos y avise de duplicados o errores de mayúsculas.
- Un **script de editor de Unity** que ponga en las texturas `Filter Mode: Point`, `Generate Mip Maps: off`, `Compression: None`.
- Un **checklist de pruebas** del tracking (sección 7.8) para ir marcando resultados.

### Lo que requiere decisión o trabajo artístico del usuario
- Diseño final del personaje, paleta y detalles propios.
- Pintado de las texturas pixeladas.
- Ajuste fino de las expresiones y de la "personalidad" del avatar.

---

## 0. Antes de empezar

### Licencias (importante)
- **Tu modelo original** es tuyo, pero **no copies** el diseño exacto de Lappland (ropa, accesorios, rostro). Tomá la esencia y cambiá detalles.
- **Tus PMX de Texas y Lappland alter:** usalos solo como **referencia de proporciones** y no como base. Tienen sus propias licencias y harían que tu modelo deje de ser original.
- Si más adelante convertís un PMX a VRM, leé el readme: convertir es modificar, y muchos autores lo prohíben.
- Si usás una **malla base de terceros**, confirmá que su licencia permita modificar, usar en streams y (si monetizás) uso comercial. Guardá una captura de la licencia con la fecha.
- Lappland es un personaje con copyright de Hypergryph/Yostar. Para un diseño original inspirado, evitá usar su nombre como nombre del avatar.

### Herramientas (todas gratuitas)
| Herramienta | Para qué | Dónde |
|---|---|---|
| Blender | Modelado, rig, shape keys | blender.org |
| VRM Add-on for Blender (saturday06) | Rig humanoide y exportación VRM | github.com/saturday06/VRM-Addon-for-Blender |
| Aseprite / LibreSprite / Krita | Texturas pixeladas | aseprite.org · libresprite.github.io · krita.org |
| Unity | Revisar, materiales, exportar | unity.com |
| UniVRM | Importar/exportar VRM en Unity | github.com/vrm-c/UniVRM |
| Warudo + SDK de Warudo | Usar el avatar y exportar `.warudo` | warudo.app |

---

## 1. Diseño del personaje

### Qué tomar de la estética de Lappland
- Pelo plateado o blanco.
- Orejas y cola de lobo.
- Paleta negro / rojo / blanco o plata.
- Actitud: mirada intensa y sonrisa de loca.

### Qué hacer propio (para que sea original)
- **Silueta distintiva:** un accesorio grande y reconocible (sombrero, capa corta, bufanda larga, capucha).
- **Un acento de color propio** (neón, dorado, violeta).
- **Un detalle gráfico propio:** un símbolo, un texto o un patrón pintado en la textura de la ropa.
- **Prop opcional:** espada, bate o accesorio low poly.

### Hoja de diseño mínima
Antes de modelar, hacé un boceto de frente y de perfil con:
1. Silueta general y proporciones (cabeza grande suele funcionar bien en este estilo).
2. Paleta de **5 a 8 colores**.
3. Lista de piezas separadas: cuerpo, cabeza, pelo, orejas, cola, ropa, accesorios.

---

## 2. Modelado en Blender

### Presupuesto de polígonos
| Parte | Triángulos aprox. |
|---|---|
| Cabeza | 800 – 1.500 |
| Cuerpo | 1.000 – 2.500 |
| Pelo | 500 – 2.000 |
| Ropa y accesorios | 500 – 2.500 |
| **Total** | **3.000 – 10.000** |

### Pasos
1. Empezá con formas simples (cubos, cilindros) y extruí. Evitá subdivisiones.
2. Mantené las piezas como **mallas separadas** (pelo, ropa, accesorios), todas dentro de un mismo armature al final.
3. Usá **flat shading** o normales duras. Para el look PSX no uses suavizado.
4. Aplicá escala y rotación (`Ctrl + A`) antes de riggear.
5. **Pose en T o A**, de frente, mirando hacia -Y en Blender.
6. Orejas y cola con **pocos huesos** (2 a 4 cada una) para que se muevan bien.

### Consejo
Mantené la cara con topología limpia alrededor de ojos y boca, porque ahí van las shape keys.

---

## 3. Texturas pixeladas

### Reglas del estilo
- Resolución baja: **64×64 a 128×128** por parte (o una sola de 256×256 para todo).
- **Sin antialiasing**, sin degradados suaves.
- Pocos colores y mucho contraste.
- Detalles pintados en la textura (texto, patrones, brillos de gafas, símbolos) en lugar de modelarlos.

### Flujo
1. En Blender, hacé el **UV unwrap** y ordená las islas para aprovechar toda la textura.
2. Exportá la plantilla UV y pintá en Aseprite, LibreSprite o Krita (pincel de 1 píxel, sin suavizado).
3. Guardá como PNG.
4. Cargá la textura en el material de Blender para previsualizar.

---

## 4. Rig y expresiones

### Rig humanoide
1. Creá un armature humanoide estándar (o usá el generador del VRM Add-on).
2. En el addon VRM, asigná cada hueso a su rol humanoide (hips, spine, chest, neck, head, brazos, piernas, manos).
3. Pesos (weight paint): usá **Automatic Weights** y corregí hombros, cadera y cuello.

### Shape keys para VRM
Creá estas expresiones en la malla de la cara:

| Expresión VRM 1.0 | Equivalente VRM 0.x | Descripción |
|---|---|---|
| `blink` | Blink | Ojos cerrados |
| `aa` | A | Boca abierta |
| `ih` | I | Boca "i" |
| `ou` | U | Boca "u" |
| `ee` | E | Boca "e" |
| `oh` | O | Boca "o" |
| `happy` / `angry` / `sad` / `surprised` | Joy / Angry / Sorrow | Emociones |

Warudo soporta VRM 0.x y 1.0. Para este estilo funcionan muy bien las expresiones **exageradas** (sonrisa enorme, ojos en espiral, etc.).

### Spring Bones
Marcá en el addon VRM los huesos de **pelo, orejas, cola y capa/bufanda** como spring bones para que tengan física.

---

## 5. Unity: lograr el look pixelado

### Importar texturas
En cada textura (Inspector):
- **Filter Mode:** `Point (no filter)`
- **Generate Mip Maps:** desactivado
- **Compression:** `None`
- **Max Size:** la resolución real de la textura

Sin esto la textura se ve borrosa y se pierde el efecto.

### Materiales
- Usá **MToon** o un shader **unlit** con sombreado plano para un look limpio.
- Desactivá sombras suaves y outline si querés el estilo PSX puro.

### Efecto PS1 completo (opcional)
Para los vértices que "tiemblan" y la deformación de textura propios de PS1 necesitás un **shader específico** (buscá "PSX shader Unity"). Como VRM no soporta shaders personalizados, en ese caso exportá como **`.warudo`** con el SDK de Warudo.

---

## 6. Exportar y usar en Warudo

### Opción A: VRM (simple)
1. Exportá el VRM desde Blender (VRM Add-on) o desde Unity (UniVRM).
2. Importalo en Warudo (arrastrar el archivo o desde el panel de personajes).
3. Revisá expresiones, tracking de cara y física.

### Opción B: `.warudo` (shaders personalizados)
1. Instalá el SDK de Warudo en Unity siguiendo su documentación oficial.
2. Armá el personaje con tus materiales y shaders.
3. Exportá el `.warudo` y cargalo en Warudo.

### Checklist final
- [ ] Texturas con filtro Point, sin mipmaps
- [ ] Todas las expresiones VRM funcionan
- [ ] Shape keys ARKit con nombres exactos (mínimo ~20)
- [ ] Tracking MediaPipe calibrado, buena luz y suavizado ajustado
- [ ] Orejas, cola y pelo con física
- [ ] Mano y brazos sin deformaciones raras
- [ ] Metadata de licencia del VRM completada (autor, uso permitido, créditos)
- [ ] Probado con tracking en Warudo

---

## 7. Tracking con webcam (lo más cercano a ARKit)

El tracking ARKit del iPhone usa un sensor de profundidad (TrueDepth), así que una webcam común no lo iguala. Pero con un buen modelo, buena luz y la configuración correcta, se puede acercar bastante.

### 7.1 Tu equipo actual
| Componente | Situación | Qué implica |
|---|---|---|
| Webcam 720p / 30 fps | Suficiente para empezar | La luz y el encuadre pesan más que la resolución |
| Ryzen 5 5600G (sin GPU dedicada) | Gráficos integrados | El tracking de MediaPipe corre en CPU; conviene tener el modelo liviano (tu low poly ayuda) |
| RTX 3060 12 GB (a futuro) | Mejora el render y la codificación | Libera la CPU y permite probar el tracking de NVIDIA (ver 7.6) |

### 7.2 Usá MediaPipe en Warudo
- Es el sistema de tracking de webcam **integrado en Warudo** y la documentación lo recomienda sobre OpenSeeFace porque rastrea más blendshapes y con mejor calidad.
- Rastrea más de 40 blendshapes ARKit, rotación y posición de cabeza.
- Calibralo desde `Character → Motion Capture → Quick Calibration → Calibrate MediaPipe`, mirando de frente y con cara neutra.
- Si la ventana del tracker va con pocos FPS, probá activar o desactivar **GPU Acceleration** en el asset *MediaPipe Tracker*. Con gráficos integrados puede ir mejor en un modo u otro, así que probá ambos.

### 7.3 Mejoras que más rinden con una webcam 720p/30
1. **Luz frontal y difusa.** Es lo más importante: con poca luz muchas webcams bajan los FPS reales y el tracking tiembla. Una lámpara con pantalla o una ventana frente a vos funciona bien.
2. **Verificá los FPS reales** de la cámara con una web de test de FPS, y que superen los 30.
3. **Cámara arriba del monitor**, con tu cabeza un poco por encima del centro de la imagen.
4. **Encuadre:** tu cara debe ocupar una parte buena del cuadro (no muy lejos), sin contraluz.
5. **Fondo y pelo:** evitá flequillos o sombras que tapen cejas y ojos.
6. **Cerrá programas pesados** mientras hacés stream (el 5600G comparte memoria con la parte gráfica).

### 7.4 Suavizado y sensibilidad (Warudo)
En el blueprint de tracking (por ejemplo *Face Tracking - MediaPipe*) buscá los nodos **Smooth BlendShape List**, **Smooth Rotation List** y **Smooth Position List**:
- **Smooth Time más alto** = movimiento más suave pero con más retardo.
- **Smooth Time más bajo** = más reactivo pero con más temblor.
- Buscá un punto medio y ajustalo con la cámara que usás para stream.
- Si ciertas expresiones (cejas, sonrisa, ojos muy abiertos) casi no se ven, subí su sensibilidad en los ajustes del tracker.

### 7.5 Que tu modelo aproveche los blendshapes ARKit
Con webcam el modelo hace gran parte del trabajo: si no tiene los blendshapes, el tracking no tiene qué mover.

**Regla clave:** creá los shape keys en Blender con los **nombres ARKit exactos** (respetá mayúsculas y minúsculas). Después de exportar, revisá en Warudo que aparezcan en la lista de blendshapes del personaje.

#### Lista completa (52)
| Grupo | Blendshapes |
|---|---|
| Ojos (14) | `eyeBlinkLeft/Right`, `eyeLookDownLeft/Right`, `eyeLookInLeft/Right`, `eyeLookOutLeft/Right`, `eyeLookUpLeft/Right`, `eyeSquintLeft/Right`, `eyeWideLeft/Right` |
| Mandíbula (4) | `jawForward`, `jawLeft`, `jawRight`, `jawOpen` |
| Boca (23) | `mouthClose`, `mouthFunnel`, `mouthPucker`, `mouthLeft`, `mouthRight`, `mouthSmileLeft/Right`, `mouthFrownLeft/Right`, `mouthDimpleLeft/Right`, `mouthStretchLeft/Right`, `mouthRollLower`, `mouthRollUpper`, `mouthShrugLower`, `mouthShrugUpper`, `mouthPressLeft/Right`, `mouthLowerDownLeft/Right`, `mouthUpperUpLeft/Right` |
| Cejas (5) | `browDownLeft/Right`, `browInnerUp`, `browOuterUpLeft/Right` |
| Mejillas (3) | `cheekPuff`, `cheekSquintLeft/Right` |
| Nariz (2) | `noseSneerLeft/Right` |
| Lengua (1) | `tongueOut` |

#### Versión mínima para un modelo low poly (unos 20 a 24)
No hace falta hacer los 52. Con estos ya se nota una gran mejora:

| Prioridad | Blendshapes |
|---|---|
| Imprescindibles | `eyeBlinkLeft/Right`, `jawOpen`, `mouthSmileLeft/Right`, `mouthFunnel`, `mouthPucker`, `mouthClose` |
| Muy recomendables | `browDownLeft/Right`, `browInnerUp`, `browOuterUpLeft/Right`, `eyeWideLeft/Right`, `mouthFrownLeft/Right` |
| Extras con mucha personalidad | `eyeSquintLeft/Right`, `cheekPuff`, `mouthLowerDownLeft/Right`, `tongueOut` |

La dirección de la mirada (`eyeLook...`) se puede resolver con **huesos de ojos** o desplazando la UV de los ojos en lugar de hacer 8 shape keys.

#### Cómo hacerlos en Blender
1. Hacé primero las formas de **un solo lado** (por ejemplo `mouthSmileLeft`) y duplicá/espejá para el otro lado.
2. Usá **grupos de vértices** izquierda/derecha para separar lados con precisión.
3. En low poly, **exagerá** cada forma: con pocos vértices los cambios chicos no se ven.
4. Para ojos pixelados pintados en la textura, el parpadeo puede ser un párpado modelado que se desliza, o un cambio de UV (textura de ojo cerrado).
5. Probá cada shape key con el slider al 100% y revisá que no se crucen polígonos.

### 7.6 Cuando tengas la RTX 3060 (12 GB)
- **Seguro:** mejora el rendimiento de Warudo y OBS. Podés codificar el stream con la GPU y dejar la CPU libre para el tracking.
- **Posible, para verificar antes de contar con eso:** el tracking facial de NVIDIA (basado en RTX). Aparece en guías como alternativa de alta calidad con webcam, y VTube Studio/VBridger lo soportan, pero **no confirmé que Warudo lo integre directamente**. Revisá la documentación de Warudo antes de comprar pensando en eso.
- La webcam sigue siendo el límite: una de 1080p con buen enfoque y más FPS suele mejorar más que cualquier otro ajuste de software.

### 7.7 Alternativas con teléfono (si el resultado no te alcanza)
| Opción | Notas |
|---|---|
| iPhone 12 o más nuevo (puede ser usado, sin plan) + app iFacialMocap | Es el que recomienda Warudo como mejor calidad de tracking facial |
| Teléfono Android + MeowFace | Envía tracking facial a software de VTuber; confirmá en su documentación cómo se conecta con Warudo |

### 7.8 Prueba rápida de calidad
1. Cara neutra: el avatar debe quedarse quieto, sin temblar.
2. Parpadeo lento y rápido.
3. Boca: `aa`, `ih`, `ou`, `ee`, `oh` y sonrisa.
4. Cejas arriba y abajo.
5. Inflar mejillas y sacar la lengua (si los hiciste).
6. Girar la cabeza a los lados y hacia arriba/abajo.

Si algo no responde, revisá primero el nombre del shape key, luego la luz y por último el suavizado.

---

## 8. Referencias y sugerencias

### Estilo
- Buscá referencias de **"PSX style character"**, **"low poly VRM"** y **"PS1 aesthetic avatar"** para inspirarte.
- Tutoriales útiles: *PSX style texturing en Blender*, *Point filtering textures Unity*, *VRM export Blender*.

### Modelos para estudiar la estructura
- Modelos de **Raildo GameArt** (itch.io) tienen estilo low poly VRM y licencia CC0, aunque son de pago (desde $50).
- Modelos gratuitos en VRoid Hub, Booth e itch.io con licencia que permita uso en stream sirven para analizar rigs y expresiones.

### Si te trabás
- Empezá por un modelo **muy simple** (cabeza + cuerpo + pelo) y agregá detalles de a poco.
- Probá en Warudo **desde temprano**, no solo al final.
- Guardá versiones numeradas (`avatar_v01.blend`, `avatar_v02.blend`...).

---

## Orden recomendado de trabajo
1. Hoja de diseño y paleta
2. Modelado base en Blender
3. UV y texturas pixeladas
4. Rig humanoide y pesos
5. Shape keys de expresiones (mínimo ARKit, ver sección 7.5)
6. Exportar VRM de prueba y probar en Warudo
7. Calibrar MediaPipe, mejorar luz y ajustar suavizado (sección 7)
8. Ajustes en Unity (texturas, materiales, spring bones)
9. Versión final (VRM o `.warudo`)

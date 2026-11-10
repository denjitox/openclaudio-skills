# Recopilación de skills: Blender, Unity y Warudo

Compañero de `guia-avatar-low-poly-lappland.md`. Reúne las habilidades que hacen falta para crear y usar un avatar low poly pixelado (estilo PSX) en Warudo, explicadas para la persona y estructuradas para que las use un agente.

---

## Parte 1: Explicación para el usuario

### Qué significa "skill" acá
La palabra se usa de dos maneras y este documento cubre las dos:

1. **Skill como habilidad o técnica:** algo que sabés hacer (por ejemplo, "hacer shape keys" o "configurar texturas en Unity"). Cada ficha de este documento describe una.
2. **Skill como instrucción para un agente:** un archivo de instrucciones (normalmente llamado `SKILL.md`) que le enseña a un agente a hacer bien una tarea concreta. Cada ficha de acá está escrita para poder convertirse fácilmente en uno.

### Cómo usar este documento
- **Para aprender:** mirá la tabla del mapa rápido y empezá por las de prioridad **Alta**. La ruta recomendada está al final.
- **Para delegar al agente:** pasale este archivo junto con la guía principal. Cada skill dice qué hacer, cómo verificar que salió bien y qué errores evitar.
- **Para pedir más:** si querés, cada ficha se puede convertir en un `SKILL.md` independiente.

### Qué esperar del agente y qué no
| El agente puede ayudar bien con | Queda mejor en tus manos |
|---|---|
| Scripts de Blender (`bpy`) y de Unity (C#) | Diseño del personaje y estética |
| Revisar nombres, huesos, shape keys y ajustes de import | Pintar las texturas pixeladas |
| Checklists, diagnóstico de errores, documentación | Decidir el "look" final y la personalidad del avatar |
| Tareas repetitivas y de verificación | Aprobar cualquier instalación o cambio importante |

---

## Parte 2: Instrucciones para el agente

- Leé primero la sección "Contexto para el agente" de `guia-avatar-low-poly-lappland.md`; sus reglas valen acá también.
- Cada skill indica **qué verificar** al terminar. Hacé esa verificación y reportá el resultado al usuario antes de pasar a la siguiente.
- Donde diga **[verificar]**, no asumas: confirmá en la documentación oficial o en pantalla.
- Ante duda sobre licencias, instalaciones o borrado de archivos, preguntá al usuario.

---

## Mapa rápido

| ID | Skill | Software | Prioridad | Fase |
|---|---|---|---|---|
| B1 | Modelado low poly | Blender | Alta | Modelado |
| B2 | Sombreado plano (flat) | Blender | Media | Modelado |
| B3 | UV para texturas pixeladas | Blender | Alta | Texturas |
| B4 | Previsualizar pixel art en Blender | Blender | Media | Texturas |
| B5 | Rig humanoide y weight paint | Blender | Alta | Rig |
| B6 | Shape keys ARKit | Blender | Alta | Expresiones |
| B7 | VRM Add-on (humanoide, expresiones, licencia) | Blender | Alta | Exportar |
| B8 | Optimización y Decimate | Blender | Media | Optimizar |
| B9 | Scripting con `bpy` | Blender | Media | Automatizar |
| B10 | Referencia con PMX (mmd_tools) | Blender | Baja | Diseño |
| U1 | Proyecto Unity y UniVRM | Unity | Alta | Preparar |
| U2 | Import de texturas (Point filter) | Unity | Alta | Look |
| U3 | Materiales (MToon / unlit) | Unity | Alta | Look |
| U4 | Spring bones | Unity | Media | Física |
| U5 | Revisión de expresiones | Unity | Alta | QA |
| U6 | Exportar VRM | Unity | Alta | Exportar |
| U7 | Exportar `.warudo` con el SDK | Unity | Media | Exportar |
| U8 | Shader PSX | Unity | Baja | Look avanzado |
| U9 | Scripts de editor en C# | Unity | Media | Automatizar |
| U10 | Rendimiento con GPU integrada | Unity | Media | Optimizar |
| W1 | Asistente inicial (Onboarding) | Warudo | Alta | Setup |
| W2 | Importar y revisar el personaje | Warudo | Alta | QA |
| W3 | Tracking con MediaPipe | Warudo | Alta | Tracking |
| W4 | Blueprints y suavizado | Warudo | Alta | Tracking |
| W5 | Escena, cámara y salida a OBS | Warudo | Media | Stream |
| W6 | Diagnóstico de problemas comunes | Warudo | Alta | Soporte |
| W7 | Tracking externo (iFacialMocap, etc.) | Warudo | Baja | Futuro |
| T1 | Licencias | Todos | Alta | Siempre |
| T2 | Versionado y copias | Todos | Alta | Siempre |
| T3 | Checklist de calidad (QA) | Todos | Alta | Final |
| T4 | Conectar un agente a las apps (MCP) | Todos | Media | Opcional |

---

## Skills de Blender

### B1. Modelado low poly
- **Qué es:** construir formas con pocos polígonos usando extrusiones, loop cuts y mallas simples.
- **Para qué en tu proyecto:** el estilo PSX depende de una geometría simple. Además, con GPU integrada, un modelo liviano rinde mejor.
- **Pasos clave:**
  1. Activá las estadísticas (Overlays → Statistics) para ver triángulos.
  2. Partí de formas básicas (cubos, cilindros) y extruí.
  3. Presupuesto orientativo total: 3.000 a 10.000 triángulos (ver tabla de la guía principal).
  4. Mantené piezas separadas: cuerpo, cabeza, pelo, ropa, accesorios.
- **Errores comunes:** subdividir de más; mezclar todo en una sola malla; olvidar aplicar escala (`Ctrl+A`).
- **Verificar:** conteo de triángulos dentro del presupuesto y escala/rotación aplicadas.

### B2. Sombreado plano (flat)
- **Qué es:** que cada cara se vea facetada, sin suavizado.
- **Para qué:** da el look PSX característico.
- **Pasos clave:** seleccioná las mallas → *Shade Flat*. Revisá que el material no dependa de suavizado automático.
- **Verificar:** en vista previa se ven las caras facetadas.

### B3. UV para texturas pixeladas
- **Qué es:** desplegar la malla en 2D para pintar sobre ella.
- **Para qué:** el pixel art solo se ve bien si las islas UV están ordenadas y con tamaño de píxel consistente.
- **Pasos clave:**
  1. Marcá costuras (seams) en lugares poco visibles.
  2. Desplegá (Unwrap) y ordená las islas aprovechando el espacio.
  3. Mantené una **densidad de píxeles similar** entre piezas (que un píxel mida parecido en cara y ropa).
  4. Alineá bordes de islas a la cuadrícula de píxeles cuando sea posible.
- **Errores comunes:** islas con escalas muy distintas, que hacen que unos píxeles se vean enormes y otros diminutos.
- **Verificar:** al aplicar una textura de cuadrícula de prueba, los cuadros tienen tamaño parecido en todo el modelo.

### B4. Previsualizar pixel art en Blender
- **Qué es:** ver la textura sin suavizado dentro de Blender.
- **Pasos clave:** en el nodo *Image Texture*, poné la interpolación en **Closest**.
- **Verificar:** los píxeles se ven nítidos al acercar la cámara.

### B5. Rig humanoide y weight paint
- **Qué es:** crear el esqueleto y definir cómo deforma la malla.
- **Para qué:** VRM exige un esqueleto humanoide estándar; orejas y cola necesitan huesos propios.
- **Pasos clave:**
  1. Armature humanoide en pose T o A.
  2. Huesos extra: 2 a 4 para cada oreja y para la cola; también para pelo largo o capa.
  3. Parentá con *Automatic Weights* y corregí hombros, cadera y cuello.
  4. Normalizá pesos.
- **Errores comunes:** huesos con nombres duplicados; pesos que se "estiran" en codos y rodillas.
- **Verificar:** mové cada hueso principal y revisá que no haya deformaciones raras.

### B6. Shape keys ARKit
- **Qué es:** formas de la cara (parpadeo, sonrisa, boca abierta...) que el tracking activa.
- **Para qué:** con webcam, el modelo hace gran parte del trabajo; sin shape keys el tracking no tiene qué mover.
- **Pasos clave:**
  1. Creá el *Basis* y luego cada shape key con el **nombre ARKit exacto** (ver sección 7.5 de la guía principal).
  2. Hacé un lado (por ejemplo `mouthSmileLeft`) y espejalo al otro; usá grupos de vértices izquierda/derecha para separar lados.
  3. Exagerá las formas: con pocos vértices los cambios chicos no se notan.
  4. Empezá por el conjunto mínimo (~20) y ampliá después.
- **Errores comunes:** mayúsculas y minúsculas distintas a las de ARKit; shape keys con polígonos cruzados al 100%.
- **Verificar:** cada slider al 100% se ve bien y los nombres coinciden exactamente con la lista ARKit.

### B7. VRM Add-on for Blender
- **Qué es:** el addon que permite asignar el esqueleto humanoide, definir expresiones, spring bones y metadata de licencia, y exportar VRM.
- **Pasos clave:**
  1. Instalarlo desde su repositorio oficial **[verificar URL y compatibilidad con la versión de Blender del usuario]**.
  2. Asignar cada hueso a su rol humanoide.
  3. Mapear expresiones (`blink`, `aa`, `ih`, `ou`, `ee`, `oh`, emociones).
  4. Completar la metadata: autor, usos permitidos, créditos.
  5. Exportar.
- **Errores comunes:** olvidar la metadata de licencia; exportar con huesos humanoides sin asignar.
- **Verificar:** abrir el VRM exportado en Unity (UniVRM) o en Warudo y comprobar que carga sin errores.

### B8. Optimización y Decimate
- **Qué es:** reducir polígonos, materiales y texturas.
- **Pasos clave:**
  1. *Merge by Distance* para soldar vértices duplicados.
  2. Modificador *Decimate* en cuerpo, ropa y pelo.
  3. **No decimar** la cara ni mallas con shape keys sin cuidado: se rompen los morphs.
  4. Unificar materiales y bajar la resolución de texturas.
- **Verificar:** conteo de triángulos antes y después, y que las expresiones sigan funcionando.

### B9. Scripting con `bpy`
- **Qué es:** automatizar tareas en Blender con Python.
- **Ideas útiles para este proyecto:**
  - Crear shape keys vacíos con los nombres ARKit.
  - Revisar nombres de shape keys y huesos, y reportar duplicados o errores.
  - Contar triángulos por objeto y comparar con el presupuesto.
- **Precaución:** ejecutá los scripts sobre una **copia** del `.blend` y mostrale el código al usuario antes de correrlo.
- **Verificar:** el script informa qué cambió y no toca nada fuera de lo pedido.

### B10. Referencia con PMX (mmd_tools)
- **Qué es:** importar un PMX para usarlo solo como guía de proporciones.
- **Pasos clave:** importá con MMD Tools (repositorio `MMD-Blender/blender_mmd_tools`; su README indica usar la versión que corresponde a tu Blender LTS), ponelo en una colección separada, bloqueala y ocultala del render. No lo uses como base ni lo exportes.
- **Dato útil:** la documentación de Warudo dice que modelos que no son VRM (por ejemplo MMD) se pueden exportar a `.warudo` con el Mod SDK, sin pasar por VRM (sujeto a la licencia de cada modelo).
- **Regla:** respetá las licencias de los PMX. El modelo final debe ser original.

---

## Skills de Unity

### U1. Proyecto Unity y UniVRM
- **Qué es:** preparar un proyecto limpio con UniVRM para importar y exportar VRM.
- **Pasos clave:**
  1. Crear un proyecto nuevo con una versión de Unity compatible: UniVRM indica que soporta Unity 2021.3 LTS o posterior; la versión exacta que pide el SDK de Warudo hay que leerla en su guía de instalación **[verificar]**.
  2. Instalar UniVRM desde su repositorio oficial.
  3. Importar el VRM y revisar metadata y humanoide.
- **Errores comunes:** versiones de Unity incompatibles; rutas de proyecto con caracteres raros.
- **Verificar:** el VRM se importa sin errores en consola.

### U2. Import de texturas (Point filter)
- **Qué es:** configurar cada textura para que se vea pixelada y sin suavizado.
- **Ajustes:**
  - Filter Mode: **Point (no filter)**
  - Generate Mip Maps: **desactivado**
  - Compression: **None**
  - Max Size: la resolución real de la textura
- **Verificar:** al acercar la cámara en Unity, los píxeles se ven nítidos, no borrosos.

### U3. Materiales (MToon / unlit)
- **Qué es:** definir cómo se ilumina y se dibuja el modelo.
- **Pasos clave:** usá MToon o un shader unlit con sombreado plano; desactivá o simplificá sombras suaves y outline según el look buscado.
- **Verificar:** el avatar se ve consistente con distintas luces de la escena.

### U4. Spring bones
- **Qué es:** física de huesos (pelo, orejas, cola, capa).
- **Pasos clave:** definí los grupos de spring bones, ajustá rigidez y gravedad, y agregá colliders en cabeza y cuerpo para evitar atravesamientos.
- **Errores comunes:** demasiado movimiento (parece gelatina) o demasiado poco.
- **Verificar:** movés el avatar y revisás que orejas y cola respondan sin atravesar el cuerpo.

### U5. Revisión de expresiones
- **Qué es:** probar cada blendshape y expresión VRM en el editor.
- **Pasos clave:** recorré la lista de expresiones y los shape keys ARKit, comparando con el checklist de la sección 7.8 de la guía principal.
- **Verificar:** ninguna expresión deforma de forma inesperada y los nombres ARKit aparecen tal cual.

### U6. Exportar VRM
- **Qué es:** generar el archivo VRM final desde Unity.
- **Pasos clave:** completar metadata y licencia, comprobar humanoide y expresiones, y exportar.
- **Verificar:** el VRM abre en Warudo y, como prueba de portabilidad, en VSeeFace o VNyan.

### U7. Exportar `.warudo` con el SDK
- **Qué es:** formato propio de Warudo que permite shaders personalizados.
- **Pasos clave (verificados en la documentación de Warudo):** instalar el SDK según la guía "Unity & Warudo SDK Installation"; en Unity usar `Warudo → Setup Character...` ("Setup selected GameObject as character mod") y luego `Warudo → Build Mod`; dejar el `.warudo` en la carpeta `Characters` del data folder de Warudo.
- **Importante:** los huesos deben estar normalizados (los VRM ya lo están); las assembly definitions (`.asmdef`) no están soportadas; hacer backup de `ExportSettings.asset`.
- **Nota:** el VRM base sigue siendo la versión portable; el `.warudo` es el extra. Warudo **no** soporta `.vsfavatar`.

### U8. Shader PSX (opcional, avanzado)
- **Qué es:** efectos como vértices que "tiemblan" (snapping) y deformación de textura propios de PS1.
- **Pasos clave:** buscar un shader PSX para Unity con licencia compatible **[verificar licencia]** o crear uno con Shader Graph.
- **Limitación:** no se puede guardar en un VRM estándar. Warudo usa `.warudo` (no soporta `.vsfavatar`); VSeeFace/VNyan usan `.vsfavatar`. En Warudo el shader debe ser compatible con el Built-in Render Pipeline (URP solo en Warudo Pro).
- **Verificar:** el efecto se ve igual en Unity y en Warudo.

### U9. Scripts de editor en C#
- **Qué es:** automatizar ajustes en Unity.
- **Ideas útiles:**
  - Un `AssetPostprocessor` que ponga Point filter, sin mipmaps y sin compresión a toda textura nueva de una carpeta.
  - Un validador que liste materiales sin asignar o huesos sin mapear.
- **Precaución:** probalo primero en una copia del proyecto.
- **Verificar:** una textura nueva se importa con los ajustes correctos sin tocar nada a mano.

### U10. Rendimiento con GPU integrada
- **Qué es:** mantener la escena liviana mientras no haya GPU dedicada.
- **Pasos clave:** pocos materiales, texturas chicas, pocas luces, sin sombras pesadas; revisar con el Profiler.
- **Verificar:** FPS estables en Warudo con el stream abierto.

---

## Skills de Warudo

### W1. Asistente inicial (Onboarding)
- **Qué es:** cada escena de Warudo incluye un asset llamado *Onboarding Assistant* que guía la configuración del tracking.
- **Pasos clave:** *Basic Setup → Get Started* y seguir las instrucciones; después se puede refinar en los assets de tracking. Los pasos exactos pueden cambiar con la versión **[verificar en pantalla]**.
- **Resultado:** se generan blueprints de tracking (por ejemplo, *Face Tracking - MediaPipe*).

### W2. Importar y revisar el personaje
- **Pasos clave:** cargar el VRM o `.warudo`, abrir la lista de blendshapes del personaje y comprobar que aparezcan los nombres ARKit.
- **No verificado:** cómo Warudo mapea los blendshapes ARKit de un VRM exportado. Probar con un modelo simple antes de hacer todos los shape keys **[verificar]**. Sí está verificado que, en el onboarding, Warudo importa las expresiones VRM del personaje y genera un blueprint con hotkeys.
- **Verificar:** al mover el tracking, el avatar responde con las expresiones esperadas.

### W3. Tracking con MediaPipe
- **Qué es:** el sistema de tracking de webcam integrado en Warudo; rastrea más de 40 blendshapes ARKit, además de rotación y posición de cabeza.
- **Pasos clave:**
  1. Cámara arriba del monitor, con la cabeza un poco por encima del centro de la imagen.
  2. Calibrar: *Character → Motion Capture → Quick Calibration → Calibrate MediaPipe*.
  3. Luz frontal y difusa; comprobar que la webcam llegue a 30+ FPS reales.
  4. Con FPS bajos en la ventana del tracker, probar activar/desactivar *GPU Acceleration*.
- **Verificar:** cara neutra quieta, parpadeo correcto y sonrisa y boca con respuesta clara.

### W4. Blueprints y suavizado
- **Qué es:** los blueprints son los grafos de nodos que conectan el tracking con el personaje.
- **Pasos clave:** en el blueprint de tracking, ajustar los nodos *Smooth BlendShape List*, *Smooth Rotation List* y *Smooth Position List*. Más "Smooth Time" = más suave pero con retardo; menos = más reactivo pero con temblor.
- **Verificar:** movimientos fluidos sin retardo molesto.

### W5. Escena, cámara y salida a OBS
- **Qué es:** preparar el encuadre y mandar la imagen a OBS.
- **Pasos clave:** configurar cámara y fondo en Warudo y capturar en OBS con el método recomendado en la documentación oficial **[verificar el método actual]**.
- **Verificar:** el avatar se ve con fondo correcto y sin retardo en OBS.

### W6. Diagnóstico de problemas comunes
| Síntoma | Qué revisar |
|---|---|
| Ventana de MediaPipe negra o en "Loading..." | Limitación conocida de MediaPipe, según la documentación de Warudo |
| Tracking tembloroso | FPS reales de la cámara, luz de la habitación, *GPU Acceleration* y suavizado |
| El tracker se ve pero el avatar no se mueve | Antivirus o firewall bloqueando la cámara o los datos; agregar Warudo a la lista de permitidos |
| Faltan expresiones | Nombres exactos de los shape keys y su mapeo en el personaje |

### W7. Tracking externo (futuro)
- **iFacialMocap:** la app de iPhone que Warudo recomienda como mejor calidad de tracking facial; la documentación sugiere un iPhone 12 o más nuevo.
- **MeowFace (Android):** hay referencias en el ecosistema VTuber; **[verificar cómo se conecta con Warudo]**.
- **Warudo Pro:** la documentación menciona sistemas de mocap adicionales exclusivos de esa versión. Revisá qué incluye antes de pagar.

---

## Skills transversales

### T1. Licencias
- Revisá siempre la licencia de modelos, texturas, shaders y addons. Guardá una captura con fecha.
- Confirmá: ¿permite streaming?, ¿monetización?, ¿modificación?, ¿requiere crédito?
- El personaje de inspiración tiene copyright de sus dueños; el diseño final debe ser propio y evitar su nombre.

### T2. Versionado y copias
- Guardá versiones numeradas (`avatar_v01.blend`, `avatar_v02.blend`...).
- Si usás control de versiones (por ejemplo Git), hacé commits al final de cada fase. En Unity, ignorá las carpetas generadas (`Library`, `Temp`).
- Trabajá siempre sobre copias cuando un agente ejecute scripts.

### T3. Checklist de calidad (QA)
- [ ] Triángulos dentro del presupuesto
- [ ] Texturas con Point filter, sin mipmaps, sin compresión
- [ ] Nombres de shape keys ARKit exactos (mínimo ~20)
- [ ] Todas las expresiones VRM funcionan
- [ ] Orejas, cola y pelo con física sin atravesamientos
- [ ] Metadata de licencia completa en el VRM
- [ ] Probado en Warudo con tracking real
- [ ] Probado en otro programa (VSeeFace o VNyan) con el VRM base

### T4. Conectar un agente a las apps (MCP) — opcional
MCP es un protocolo que permite a un agente usar herramientas de otras aplicaciones. En mi búsqueda aparecen opciones de la comunidad:

| App | Opciones encontradas | Notas |
|---|---|---|
| Blender | `blender-mcp` (repositorio `ahujasid/blender-mcp`) | Requiere Blender 3.0+ y Python 3.10+; se instala un addon y se inicia el servidor desde el panel lateral (tecla N) |
| Unity | `CoplayDev/unity-mcp`, `IvanMurzak/Unity-MCP`, `akiojin/unity-mcp-server` | El último incluye skills para Claude Code y más de 100 herramientas, según su descripción |
| Warudo | No encontré un MCP específico | Hacer a mano o con scripts, o investigar si existe una opción nueva |

**Precauciones importantes:**
- Estas herramientas permiten **ejecutar código** dentro de Blender o Unity. Usalas solo con proyectos de los que tengas copia.
- Revisá la reputación, la licencia y el código del repositorio antes de instalar.
- Pedí confirmación del usuario antes de ejecutar acciones que modifiquen o borren archivos.
- **Nada de esto lo verifiqué por mi cuenta**: confirmá compatibilidad con las versiones del usuario en la documentación de cada proyecto.

---

## Ruta de aprendizaje recomendada

1. **Base visual:** B1, B2, B3, B4
2. **Rig y cara:** B5, B6, B7
3. **Unity para el look:** U1, U2, U3
4. **Probar en Warudo:** W1, W2, W3, W4
5. **Pulido:** U4, U5, U6, B8
6. **Extras:** U7, U8 (shader PSX), W7
7. **Automatización:** B9, U9, T4

Siempre en paralelo: **T1** (licencias), **T2** (copias) y **T3** (calidad).

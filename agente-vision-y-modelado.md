# Cómo lograr que tu agente entienda, vea y modele con detalle

Versión para personas de la skill `agent-visual-feedback-modeling`.

## ¿Es posible?
**Sí, en parte.** Un agente puede entender el proyecto, ver capturas de Blender y modelar paso a paso con código. Pero el detalle artístico fino (caras, manos, topología cuidada) sigue siendo difícil y necesita tu aprobación en cada hito. La combinación más realista:

> **Base humana de VRoid + el agente modela orejas, cola y accesorios low poly, adapta texturas y automatiza lo repetitivo.**

## Las tres capacidades

| Capacidad | Cómo se logra | Estado |
|---|---|---|
| **Entender** | Darle el pack (README, guía, skills), una especificación escrita y referencias | Se puede hacer ya |
| **Ver** | Un conector (MCP) que le entregue capturas del viewport de Blender, desde varios ángulos | Existe; falta confirmar que tu cliente recibe las imágenes |
| **Modelar** | Que escriba y ejecute código de Blender en pasos pequeños | Existe; con riesgos de seguridad |

## Herramientas encontradas (no probadas)
| Conector | Qué ofrece |
|---|---|
| `ahujasid/blender-mcp` (original) | Información de escena y objetos, captura del viewport, ejecución de código Python, integraciones opcionales (Poly Haven, Sketchfab, Hyper3D, Hunyuan3D). Menciona telemetría anónima |
| `naab007/blender_mcp` (fork, licencia MIT) | Unas 91 herramientas: captura de ángulos, hoja de contactos, mapa de profundidad, guardar y comparar imágenes de referencia, diferencias entre imágenes. Pide Blender 4.0+ y `uv`. Dice haber quitado la telemetría |
| Fork de IAmMarcellus | Perfiles de herramientas (`minimal`, `standard`, `full`) y `execute_ops`, una lista de operaciones permitidas que se describe como más segura que ejecutar Python arbitrario |

Para Unity encontré varios conectores (ver skill `agent-mcp-connectors`), pero **no verifiqué** si entregan capturas.

## El ciclo de trabajo
```
especificación → pieza pequeña → código → capturas (varios ángulos)
      ↑                                              ↓
 guardar versión ← corregir ← criticar con lista ← comparar con referencia
                          ↓
                   hito: tu aprobación
```

## Cómo conseguir más detalle
1. **Hoja de referencia** con frente, perfil, 3/4 y espalda (tu dibujo o capturas de VRoid).
2. **Especificación escrita:** proporciones, presupuesto de triángulos (3.000 a 10.000), paleta, lista de piezas con nombres.
3. **Pasos chicos:** una pieza por vez, empezando por volúmenes (blockout).
4. **Varias vistas:** frente, perfil, 3/4 y wireframe, no solo el frente.
5. **Lista de crítica fija:** silueta, proporciones contra la referencia, flujo de aristas, triángulos, nombres, escala aplicada.
6. **Hitos contigo:** blockout, silueta, detalle y texturas.
7. **Una versión guardada por hito.**

## Qué esperar
| Rinde bien | Es más difícil |
|---|---|
| Blockout de volúmenes | Caras y manos detalladas |
| Accesorios y props low poly | Topología fina y limpia |
| Orejas, cola, capa, sombreros | Criterio estético (lo decidís vos) |
| Rig, shape keys por script, UV | |
| Texturas pixeladas y validaciones | |

## Seguridad
- Estos conectores pueden **ejecutar código** en tu PC. Guardá el `.blend` antes y trabajá en copias.
- Si el conector tiene perfiles, empezá por el más restringido.
- Revisá reputación, licencia y código del repositorio antes de instalar.
- Pedí que el agente te consulte antes de borrar o sobrescribir cualquier cosa.

## Checklist de preparación
- [ ] Copiar `AGENTE.md` del pack como `CLAUDE.md` o `AGENTS.md` en la carpeta del proyecto (según tu agente).
- [ ] Copiar las carpetas de `skills/` donde tu agente las lea (en Claude Code, `.claude/skills/`).
- [ ] Preparar la hoja de referencia y cargarla en Blender.
- [ ] Instalar un conector de Blender (probar primero en un proyecto de prueba).
- [ ] Confirmar que tu agente **recibe las capturas** (pedile que describa lo que ve en el viewport).
- [ ] Definir con el agente la especificación y los hitos.

## Estado de verificación
- Las capacidades de los conectores salen de sus descripciones públicas; no los probé.
- No verifiqué que tu cliente reciba imágenes ni que el modelo del agente las interprete en tu entorno.
- Ver `FUENTES.md` para las fuentes y su estado.

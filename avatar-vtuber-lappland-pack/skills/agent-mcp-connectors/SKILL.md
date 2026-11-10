---
name: agent-mcp-connectors
description: "Explica y evalúa conectores MCP de la comunidad para que un agente controle Blender o Unity, con precauciones de seguridad. Usar cuando el usuario pregunte cómo conectar el agente a Blender/Unity, qué es MCP o cómo automatizar el editor."
---

# T4 · Conectar un agente a Blender y Unity (MCP)

> Grupo: Transversal · Proyecto: avatar original low poly (estilo PSX) inspirado en Lappland, para Warudo. Leer `README.md` del pack para el contexto y las reglas generales. Idioma de trabajo: español.

## Por qué importa
MCP permite que un agente use herramientas dentro de las aplicaciones, pero esas herramientas pueden ejecutar código en la PC del usuario.

## Procedimiento
1. **Blender:** hay un proyecto de la comunidad, `blender-mcp` (repositorio `ahujasid/blender-mcp`). Según la descripción consultada requiere Blender 3.0+ y Python 3.10+, un addon instalado en Blender y arrancar el servidor desde el panel lateral (tecla N).
2. **Unity:** hay varias opciones de la comunidad (`CoplayDev/unity-mcp`, `IvanMurzak/Unity-MCP`, `akiojin/unity-mcp-server`, `xikelabs/unity-mcp`). El de akiojin dice incluir skills para Claude Code y más de 100 herramientas.
3. **Warudo:** no se encontró un conector MCP específico.
4. **Precauciones:** estas herramientas pueden ejecutar código dentro de Blender o Unity. Usalas solo con **copias** de los proyectos, revisá reputación, licencia y código del repositorio, y pedí confirmación al usuario antes de acciones que modifiquen o borren archivos.
5. Estado: **ninguna de estas herramientas se probó en esta sesión.** Verificá compatibilidad con las versiones del usuario.
6. Instalación de estos skills en un agente: en Claude Code se copian carpetas a `.claude/skills/` (proyecto) o `~/.claude/skills/` (global). En otros agentes, tratá cada `SKILL.md` como documentación.

## Cómo verificar
- [ ] El conector elegido se probó primero en un proyecto de prueba.
- [ ] El usuario aprobó cada acción que modifica archivos.

## Errores comunes
- Instalar conectores sin revisar el código.
- Dar al agente acceso a proyectos sin copia de seguridad.

## Skills relacionadas
`avatar-versioning-backups`

## Fuentes
Leyenda: ✅ consultada · 🔎 apareció en búsqueda, no abierta · 🧠 de memoria (verificar).

- 🔎 [GitHub – ahujasid/blender-mcp (mencionado en una configuración de Claude Code)](https://github.com/wsuratt/claude-code-configs)
- 🔎 [LobeHub – CoplayDev/unity-mcp](https://lobehub.com/mcp/coplaydev-unity-mcp)
- 🔎 [Skillselion – akiojin/unity-mcp-server (incluye skills para Claude Code)](https://skillselion.com/skills/akiojin/unity-mcp-server/.claude-plugin/plugins/unity-mcp-server)
- 🔎 [GitHub – xikelabs/unity-mcp](https://github.com/xikelabs/unity-mcp)
- 🔎 [Playbooks – Unity MCP server (Ivan Murzak)](https://playbooks.com/mcp/ivanmurzak-unity)
- 🔎 [PyPI – mcp-printable (explica dónde copiar skills de Claude Code)](https://pypi.org/project/mcp-printable/0.1.7/)

_Investigación hecha el 2026-11-01. Las páginas y versiones pueden haber cambiado: si algo no coincide con lo que ves en pantalla, confiá en lo que ves y avisale al usuario._

# De VRoid Studio a look PS1

Cómo llevar un avatar hecho en VRoid Studio hacia el aspecto PS1 (texturas pixeladas, paleta reducida, menos polígonos). Es la versión para personas de la skill `vroid-to-psx-pipeline` del pack.

## Respuesta corta
Sí se puede, pero no con un único filtro. Son **dos procesos separados**:
1. **Texturas:** reducir resolución sin suavizado y reducir la paleta de colores.
2. **Polígonos:** reducirlos en VRoid al exportar y con *Decimate* en Blender.

El resultado será "PSX-like", no un modelo PS1 puro: la topología de VRoid es suave y de bastantes polígonos.

## Flujo paso a paso

### 1. Antes de exportar (dentro de VRoid)
- Peinado simple, pocos ítems de ropa, sin capas transparentes innecesarias.
- Si usás ítems preestablecidos, anotá cuáles y revisá sus licencias (no se verificaron).

### 2. Exportar el VRM
- En el cuadro de exportación probá la opción de **reducir polígonos** (según una guía de usuario, puede eliminar mallas transparentes) y la de **reducir materiales** (esa guía probó con 2).
- Los nombres exactos pueden variar con la versión de VRoid: verificá en pantalla.
- Exportá **VRM 1.0** y guardá también una versión **sin reducción** para comparar.

### 3. Importar en Blender
- Usá el add-on VRM (confirmá que su versión sea compatible con tu versión de Blender).

### 4. Extraer las texturas
- En el Image Editor guardá cada imagen con *Save As* (cara, cuerpo, pelo, ropa), o desempaquetá los recursos desde *File → External Data → Unpack* (verificá el menú en tu versión).
- Ponelas en una carpeta `texturas_originales/`.

### 5. Pixelar y reducir la paleta
Con el script `pixelate_textures.py` (incluido en el pack, requiere Python y Pillow: `pip install pillow`):

```
python pixelate_textures.py texturas_originales texturas_psx --size 128 --face-size 256 --colors 32
```

| Parte | `--size` / `--face-size` | `--colors` |
|---|---|---|
| Cuerpo, ropa, pelo | 128 (probar 64) | 16 a 32 |
| Cara y ojos | 256 (probar 128) | 32 a 64 |

- `--dither` agrega puntillado, típico del estilo.
- El script nunca sobrescribe la carpeta de entrada y deja la transparencia en 0 o 255.
- Usa `--face-size` para las texturas cuyo nombre contenga `face`, `eye`, `mouth`, `iris`, `highlight`, `brow`, `cheek` o `tongue`.

### 6. Volver a poner las texturas
- Reemplazalas en Blender (Image Editor → *Replace*; verificá el nombre del comando).
- En cada nodo *Image Texture* poné la interpolación **Closest**.

### 7. Reducir polígonos
- *Decimate* en cuerpo, ropa y pelo.
- **No** apliques Decimate en la cara: tiene shape keys y se romperían las expresiones.
- El pelo de VRoid son tiras planas: si se deforma, es mejor simplificar el peinado en VRoid.

### 8. Reexportar
- Revisá expresiones y huesos, completá la metadata de licencia y exportá con el add-on VRM.

### 9. Probar en Warudo
- Comprobá si el pixelado se mantiene. **No está verificado** que Warudo respete el filtro de textura de un VRM.
- Si se ve suavizado, la alternativa es Unity: Point filter y exportar `.warudo` (skills `unity-texture-import-pixel` y `unity-warudo-sdk-export`).

## Qué esperar
- Texturas pixeladas y paleta reducida: se logra bien.
- Menos polígonos: depende de cuánto reduzca VRoid y de cuánto decimes sin romper el modelo.
- Shaders de VRoid (MToon, contorno, sombras): siguen aplicándose y cambian el look. Para uno más plano, ajustalos en Unity.
- Efecto PS1 completo (vértices que tiemblan): requiere shader personalizado y `.warudo` (skill `unity-psx-shader`).

## Problemas frecuentes
| Problema | Causa probable | Qué hacer |
|---|---|---|
| Ojos y boca ilegibles | Cara a muy baja resolución | Subir `--face-size` (128 → 256) |
| El pelo pierde forma | Decimate agresivo sobre tiras | Bajar el ratio o simplificar el peinado en VRoid |
| Expresiones rotas | Decimate aplicado a la cara | Volver a una versión guardada; no decimar la cara |
| Se ve borroso en Warudo | Filtro suavizado en destino | Point filter en Unity o `.warudo` |
| Colores muy planos | Pocos colores | Subir `--colors` o probar `--dither` |

## Estado de verificación
- El script se probó con imágenes de prueba; **no** con texturas reales de VRoid.
- Los nombres de opciones de VRoid y de menús de Blender pueden variar: verificá en pantalla.
- Fuentes consultadas: guía de usuario de CLIP STUDIO sobre exportación desde VRoid, documentación de CineV sobre VRoid, manual de Blender (nodo Image Texture, interpolación Closest). Ver `FUENTES.md`.

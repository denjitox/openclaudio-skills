"""Crea en la malla activa los shape keys ARKit que falten.

Uso: en Blender, seleccioná la malla de la cara, abrí el editor de texto,
pegá este script y ejecutalo. No borra ni modifica shape keys existentes.
Estado: no probado dentro de Blender; probalo en una copia del .blend.
"""
import bpy

# Cambiá a True para crear solo el conjunto mínimo recomendado
ONLY_MINIMAL = False

ARKIT = [
    "eyeBlinkLeft",
    "eyeBlinkRight",
    "eyeLookDownLeft",
    "eyeLookDownRight",
    "eyeLookInLeft",
    "eyeLookInRight",
    "eyeLookOutLeft",
    "eyeLookOutRight",
    "eyeLookUpLeft",
    "eyeLookUpRight",
    "eyeSquintLeft",
    "eyeSquintRight",
    "eyeWideLeft",
    "eyeWideRight",
    "jawForward",
    "jawLeft",
    "jawRight",
    "jawOpen",
    "mouthClose",
    "mouthFunnel",
    "mouthPucker",
    "mouthLeft",
    "mouthRight",
    "mouthSmileLeft",
    "mouthSmileRight",
    "mouthFrownLeft",
    "mouthFrownRight",
    "mouthDimpleLeft",
    "mouthDimpleRight",
    "mouthStretchLeft",
    "mouthStretchRight",
    "mouthRollLower",
    "mouthRollUpper",
    "mouthShrugLower",
    "mouthShrugUpper",
    "mouthPressLeft",
    "mouthPressRight",
    "mouthLowerDownLeft",
    "mouthLowerDownRight",
    "mouthUpperUpLeft",
    "mouthUpperUpRight",
    "browDownLeft",
    "browDownRight",
    "browInnerUp",
    "browOuterUpLeft",
    "browOuterUpRight",
    "cheekPuff",
    "cheekSquintLeft",
    "cheekSquintRight",
    "noseSneerLeft",
    "noseSneerRight",
    "tongueOut"
]

MINIMAL = [
    "eyeBlinkLeft", "eyeBlinkRight", "jawOpen", "mouthSmileLeft", "mouthSmileRight",
    "mouthFunnel", "mouthPucker", "mouthClose", "browDownLeft", "browDownRight",
    "browInnerUp", "browOuterUpLeft", "browOuterUpRight", "eyeWideLeft", "eyeWideRight",
    "mouthFrownLeft", "mouthFrownRight",
]

obj = bpy.context.active_object
if obj is None or obj.type != "MESH":
    raise SystemExit("Seleccioná una malla (objeto activo) antes de ejecutar el script.")

if obj.data.shape_keys is None:
    obj.shape_key_add(name="Basis", from_mix=False)

existing = {kb.name for kb in obj.data.shape_keys.key_blocks}
names = MINIMAL if ONLY_MINIMAL else ARKIT
created = []
for name in names:
    if name not in existing:
        obj.shape_key_add(name=name, from_mix=False)
        created.append(name)

print(f"Shape keys creados: {len(created)}")
for n in created:
    print(" +", n)

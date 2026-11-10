"""Revisa nombres de shape keys ARKit, huesos duplicados y triángulos por objeto.

Uso: en Blender, abrí el editor de texto, pegá este script y ejecutalo.
Solo lee e imprime; no modifica nada.
Estado: no probado dentro de Blender; probalo en una copia del .blend.
"""
import difflib
import re
import bpy

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
ARKIT_LOWER = {n.lower(): n for n in ARKIT}

print("=== Triángulos por objeto ===")
total = 0
for obj in bpy.data.objects:
    if obj.type == "MESH":
        tris = sum(len(p.vertices) - 2 for p in obj.data.polygons)
        total += tris
        print(f"{obj.name}: {tris} triángulos")
print(f"TOTAL: {total} triángulos")

print("\n=== Shape keys ===")
for obj in bpy.data.objects:
    if obj.type != "MESH" or obj.data.shape_keys is None:
        continue
    names = [kb.name for kb in obj.data.shape_keys.key_blocks if kb.name != "Basis"]
    present = set(names)
    for name in names:
        if name in ARKIT:
            continue
        if name.lower() in ARKIT_LOWER:
            print(f"[{obj.name}] '{name}' difiere en mayúsculas de '{ARKIT_LOWER[name.lower()]}'")
        else:
            close = difflib.get_close_matches(name, ARKIT, n=1, cutoff=0.8)
            if close:
                print(f"[{obj.name}] '{name}' se parece a '{close[0]}'")
    missing = [n for n in ARKIT if n not in present]
    print(f"[{obj.name}] ARKit presentes: {len(ARKIT) - len(missing)}/52")

print("\n=== Huesos ===")
pattern = re.compile(r"\.\d{3}$")
for obj in bpy.data.objects:
    if obj.type == "ARMATURE":
        for bone in obj.data.bones:
            if pattern.search(bone.name):
                print(f"[{obj.name}] hueso con sufijo numérico (posible duplicado): {bone.name}")

// Colocar dentro de una carpeta "Editor" del proyecto de Unity.
// Afecta solo a texturas cuya ruta contiene "/PixelTextures/".
// Estado: no compilado en esta sesión; probar en una copia del proyecto.
using UnityEditor;
using UnityEngine;

public class PixelArtTexturePostprocessor : AssetPostprocessor
{
    // Subir este número cada vez que cambie el comportamiento del postprocesador.
    public override uint GetVersion() { return 1; }

    void OnPreprocessTexture()
    {
        if (!assetPath.Contains("/PixelTextures/")) return;

        var importer = (TextureImporter)assetImporter;
        importer.filterMode = FilterMode.Point;                          // Point (no filter)
        importer.mipmapEnabled = false;                                  // sin mipmaps
        importer.textureCompression = TextureImporterCompression.Uncompressed; // sin compresión
    }
}

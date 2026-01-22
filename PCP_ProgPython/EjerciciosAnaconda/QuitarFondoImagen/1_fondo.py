from rembg import remove
from PIL import Image
import aspose.words as aw

import os

# Obtener la ruta del directorio donde está este script
script_dir = os.path.dirname(os.path.abspath(__file__))

path_in = os.path.join(script_dir, "HenryFoto.jpg")
path_out = os.path.join(script_dir, "Henry_sin_fondo.png")
path_svg = os.path.join(script_dir, "Henry_sin_fondo.svg")

def quitar_fondo(path_in, path_out):
    data=Image.open(path_in)
    salida=remove(data)
    salida.save(path_out)

#Funcion para convertir la imagen a svg
def convertir_a_svg(path_in, path_out):
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    shape = builder.insert_image(path_in)
    shape.get_shape_renderer().save(path_out, aw.saving.ImageSaveOptions(aw.SaveFormat.SVG))

quitar_fondo(path_in, path_out)
convertir_a_svg(path_out, path_svg)
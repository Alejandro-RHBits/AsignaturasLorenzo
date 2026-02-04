from rembg import remove
from PIL import Image
import aspose.words as aw
import cv2
import os

# Obtener la ruta del directorio donde está este script
script_dir = os.path.dirname(os.path.abspath(__file__))

path_in = os.path.join(script_dir, "imagenJake.jpg")
path_out = os.path.join(script_dir, "imagenJake_sin_fondo.png")
#path_svg = os.path.join(script_dir, "imagenJake_sin_fondo.svg")

#def quitar_fondo(path_in, path_out):
#    data=Image.open(path_in)
#    salida=remove(data)
#    salida.save(path_out)

#Funcion para quitar ruido con cv2 antes de convertir a svg

def quitar_ruido(path_in, path_out):
    img = cv2.imread(path_in)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path_out, img)

#Funcion para convertir la imagen a svg
#def convertir_a_svg(path_in, path_out):
#    doc = aw.Document()
#    builder = aw.DocumentBuilder(doc)
#    shape = builder.insert_image(path_in)
#    shape.get_shape_renderer().save(path_out, aw.saving.ImageSaveOptions(aw.SaveFormat.SVG))



#quitar_fondo(path_in, path_out)
quitar_ruido(path_in, path_out)
#convertir_a_svg(path_out, path_svg)
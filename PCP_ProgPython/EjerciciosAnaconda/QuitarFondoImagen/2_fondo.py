from rembg import remove
from PIL import Image

path_in="./HenryFoto.jpg"
path_out="./Henry_sin_fondo_preciso.png"

data=Image.open(path_in)

# Activar alpha matting y post-processing para mejor detalle en bordes (pelo, etc.)
salida=remove(
    data,
    alpha_matting=True,
    alpha_matting_foreground_threshold=240,
    alpha_matting_background_threshold=10,
    alpha_matting_erosion_size=10,
    post_process_mask=True
)

salida.save(path_out)

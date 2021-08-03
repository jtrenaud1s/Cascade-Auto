from PIL import Image, ImageOps
from os.path import splitext


def resize_image(image, screen_size='desktop', dpi=72, alignment=(0.5, 0.5)):
    name = image
    image = Image.open(image)
    dim = 300
    if screen_size == 'mobile':
        dim = 100

    filename = splitext(name)[0]
    ext = splitext(name)[1]

    new_name = filename + '-' + screen_size + ext

    image = ImageOps.fit(image, (dim, dim), Image.ANTIALIAS, centering=alignment)
    image = image.convert('RGB')
    image.save(new_name, dpi=(dpi, dpi))
    return new_name

import StringIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile


def scale_to_max_size(image, max_width, max_height):
    """Returns an image, that isn't bigger than max_width and max_height.

    That means one side is exactly given value and the other is smaller. In
    other words the image fits at any rate in the given box max_width x
    max_height.
    """
    width, height = image.size

    prop_width = float(max_width) / width
    prop_height = float(max_height) / height

    if prop_height < prop_width:
        width = int(prop_height * width)
        image = image.resize((width, max_height), Image.ANTIALIAS)
    else:
        height = int(prop_width * height)
        image = image.resize((max_width, height), Image.ANTIALIAS)

    return image

def generate_thumb(img, thumb_size, format):
    """
    Generates a thumbnail image and returns a ContentFile object with the thumbnail

    Parameters:
    ===========
    img         File object

    thumb_size  desired thumbnail size, ie: (200,120)

    format      format of the original image ('jpeg','gif','png',...)
                (this format will be used for the generated thumbnail, too)
    """
    img.seek(0)
    image = Image.open(img)

    # Convert to RGB if necessary
    if image.mode not in ('L', 'RGB', 'RGBA'):
        image = image.convert('RGB')

    new_image = scale_to_max_size(image, *thumb_size)
    thumb_io = StringIO.StringIO()

    # # PNG and GIF are the same, JPG is JPEG
    if format.upper() == 'JPG':
        format = 'JPEG'

    new_image.save(thumb_io, format)
    # return ContentFile(io.getvalue())

    img_file = InMemoryUploadedFile(thumb_io, None, img.name, 'image/jpeg', thumb_io.len, None)
    img_file.seek(0)
    return img_file

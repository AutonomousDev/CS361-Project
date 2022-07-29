import requests
import base64
from PIL import Image
from io import BytesIO
from django.conf import settings


def black_white(my_image_file):
    image_file = my_image_file.open("rb")
    encoded_image = base64.b64encode(image_file.read())

    r = requests.post("http://127.0.0.1:5000/bwconv", data={"image": encoded_image})

    with Image.open(BytesIO(base64.b64decode(r.json()["image"]))) as bw_image:
        bw_image.save(settings.MEDIA_ROOT + "end.jpeg", format="JPEG")

    r = requests.post(
        "http://127.0.0.1:5000/resize",
        data={
            "image": encoded_image,
            "width": 500,
            "height": 500
        })

    with Image.open(BytesIO(base64.b64decode(r.json()["image"]))) as resized_im:
        resized_im.save(settings.MEDIA_ROOT + "resized.jpeg", format="JPEG")

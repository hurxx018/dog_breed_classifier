import PIL.Image as Image


def dog_detector(
    img_filename
    ):

    img = Image.open(img_filename).convert("RGB")


    return 
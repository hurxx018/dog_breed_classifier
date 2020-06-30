import PIL.Image as Image


def dog_detector(
    img_filename
    ):

    img = Image.open(img_filename).convert("RGB")


    return


def human_detector(
    img_filename
    ):
    """ Detect human faces in an image.

    Inputs:
    image file name : String

    Outputs:
    if a human face exists, True. Otherwise, False : bool
    
    """
    img = Image.open(img_filename).convert("RGB")

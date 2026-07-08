from monovision.utils import slugify


def test_slugify():
    assert slugify("Poof Shirt CSS") == "poof-shirt-css"

from opaseety.blend import ImageBlend
import pytest # type: ignore
import numpy as np

def test_blend_validates_same_sized_input_images():
    images = [np.zeros((3,3)), np.zeros((3,3))]
    ImageBlend(images)
    assert True

def test_blend_invalidates_different_sized_input_images():
    images = [np.zeros((3,3)), np.zeros((4,4))]
    with pytest.raises(ValueError):
        ImageBlend(images)

from pathlib import Path
import sys,os
import numpy as np
import pytest

project_root = Path(__file__).parent.parent
print(project_root)
sys.path.append(os.path.realpath(project_root))
test_resources = os.path.join(project_root,"test_resources")
from app.helpers.data_processing.img_utils import bytes_to_numpy_array

@pytest.fixture
def image_data():
    image_path = os.path.join(test_resources , "test-image.jpg")
    with open(image_path, "rb") as image:
        f = image.read()
    return f


def test_check_data_type_is_numpy_array(image_data):
    array_check = np.array([1, 2, 3, 4])
    array_type = type(array_check)
    
    array = bytes_to_numpy_array(image_data,scale=True)
    print(array)
    assert type(array) == array_type


def test_scale_feature(image_data):
    array = bytes_to_numpy_array(image_data,scale=True)
    scale_conversion = (array <= 1)
    unique_values = np.unique(scale_conversion)
    if len(unique_values) == 1:
        assert bool(unique_values[0]) == True
    else:
        assert len(unique_values) == 1



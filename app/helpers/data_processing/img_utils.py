"""
Functions to help work with Azure Blob Storage
"""
# Author: Viraj Vaitha

# Import Libaries
from io import BytesIO
from PIL import Image
import numpy as np
import os


# 1. Convert bytes data to a NumPy array
def bytes_to_numpy_array(data_obj, scale:bool = True)-> np.ndarray:
    """
    Parameters
    ----------
    data_obj : data like object that can be accepted by BytesIO() function
    scale: default = True. This ensures the NumPy array is scaled between a value of 0-1 as opposed to 0-255.
    -------
    response_json: json message with a relevant status message
    """
    if scale:
        image = np.array(Image.open(BytesIO(data_obj)))/255
        return image
        
    else:
        image = np.array(Image.open(BytesIO(data_obj)))
        return image

def np_array_to_pil_img(array,home_dir,img_dir_name):
    image_dir = os.path.join(home_dir,img_dir_name)
    filepath = os.path.join(image_dir,"output_image")

    if np.amax(array) <= 1:
         # Convert to PIL Image and save locally
          im = Image.fromarray((array * 255).astype(np.uint8))
          im.save(filepath)
          print("Image saved in " + str(filepath))
          return str(filepath)
    else:
         im = Image.fromarray(array)
         im.save(filepath)
         print("Image saved in " + str(filepath))
         return str(filepath)


# 2. Ensure output resolution matches input resolution
def resolution_matcher(image_array:np.array, dpi:int = 100) -> tuple:
    """
    Parameters
    ----------
    image_array: Image stored as an NumPy array
    dpi: resolution
    
    -------
    figsize: tuple = (width, height)
    """
    height, width, nbands = image_array.shape                    
    dpi = 100

    # 
    figsize = width / float(dpi), height / float(dpi)
    return figsize


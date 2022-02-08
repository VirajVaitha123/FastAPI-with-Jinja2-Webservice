"""
Author: Viraj Vaitha

Description:
API clustering_examples - Gallery showcasing applications of clustering usecases from the browser. 

Storing seperate GET/POST request in routers to better organise and prevent clutter in the main.py file.
"""
import os 
from pathlib import Path

current_file = Path(__file__)
current_file_dir = current_file.parent
project_root = current_file_dir.parent
template_root_absolute = os.path.join(project_root,"templates")
static_root_absolute = os.path.join(project_root,"static")

from app.helpers.background_tasks.background_tasks import clean_directory
from app.helpers.data_processing.img_utils import bytes_to_numpy_array
# from app.helpers.data_processing.azure_blob_wrapper import upload_blob
from app.helpers.machine_learning.image_segmentation import cluster_image
from skimage.transform import  resize


from fastapi import APIRouter, BackgroundTasks
from fastapi import Request, File, Form,UploadFile
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from PIL import Image
import numpy as np


router = APIRouter(
    prefix="/machine_learning_gallery",         
    tags=["machine_learning_gallery"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


templates = Jinja2Templates(directory=template_root_absolute)
router.mount("/static", StaticFiles(directory=static_root_absolute), name = "static")

# clustering_examples html page
@router.get('/', response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("machine_learning_gallery.html",
                                     {"request": request})

# Image Segmentation
@router.post('/submit', response_class=HTMLResponse)
async def post_form(request: Request, background_tasks:BackgroundTasks, k_cluster: int = Form(...), file: UploadFile = File(...)):
    # Read uploaded file as bytes
    data = await file.read()
    
   
    # Convert Bytes to numpy (great to work with images and processing for machine learning)
    img_array = bytes_to_numpy_array(data, scale = True)
    
    # Scale down if it is a large image
    if img_array.shape[0] > 3500:
        print("Large Image - Scale down to reduce processing time")
        img_array = resize(img_array, (img_array.shape[0] // 15, img_array .shape[1] // 15),
                        anti_aliasing=True)


    # Segment Image
    segmented_img = cluster_image(k_cluster,img_array)

    # Convert to PIL Image and save locally
    im = Image.fromarray((segmented_img * 255).astype(np.uint8))

    
    figures_root_absolute = os.path.join(project_root,"figures")
    
    isExist = os.path.exists(figures_root_absolute)
    if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(figures_root_absolute)

    filepath = os.path.join(figures_root_absolute,"segmented_image_{0}.jpg".format(k_cluster))
    im.save(filepath)

    filename = file.filename
    background_tasks.add_task(clean_directory,filepath)
    # upload_blob(filename,"public",filepath)
   
    return FileResponse(path=filepath, filename=filename, media_type='image/jpg/png')

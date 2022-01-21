"""
routing code for clustering_examples usecase in our FastAPI webservice. 

Storing seperate GET/POST request in routers to better organise and prevent clutter in the main.py file.
"""
import sys
import os 
from pathlib import Path

current_file = Path(__file__)
current_file_dir = current_file.parent
project_root = current_file_dir.parent
template_root_absolute = os.path.join(project_root,"templates")
static_root_absolute = os.path.join(project_root,"static")


from app.helpers.data_processing.img_utils import bytes_to_numpy_array, resolution_matcher
from app.helpers.data_processing.azure_blob_wrapper import upload_blob
from app.helpers.machine_learning.image_segmentation import cluster_image
import matplotlib.pyplot as plt
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean


from fastapi import APIRouter
from fastapi import Request, File, Form,UploadFile
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from PIL import Image

tags_metadata = [
    {
        "name": "clustering_examples",
        "description": "APIs to showcase unsupervised learning applications",
    }
]



router = APIRouter(
    prefix="/clustering_examples",
    tags=["clustering_examples"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


templates = Jinja2Templates(directory=template_root_absolute)
router.mount("/static", StaticFiles(directory=static_root_absolute), name = "static")

@router.get('/', response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("clustering_examples.html",
                                     {"request": request})


@router.post('/submit', response_class=HTMLResponse)
async def post_form(request: Request,k_cluster: int = Form(...), file: UploadFile = File(...)):
    # Read uploaded file as bytes
    data = await file.read()

   
    # Convert Bytes to numpy (great to work with images and processing for machine learning)
    img_array = bytes_to_numpy_array(data, scale = True)
    
    if img_array.shape[0] > 3500:
        print("Large Image - Scale down to reduce processing time")
        img_array = resize(img_array, (img_array.shape[0] // 5, img_array .shape[1] // 5),
                       anti_aliasing=True)

    fig_size = resolution_matcher(img_array,dpi=50)

    
    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=fig_size)
    segmented_img = cluster_image(k_cluster,img_array)

    plt.subplots_adjust(0,0,1,1)
    plt.axis('off')
    plt.imshow(segmented_img,interpolation='nearest')
    # plt.title("new image")

    figures_root_absolute = os.path.join(project_root,"figures")
    filepath = os.path.join(figures_root_absolute,"segmented_image_{0}.jpg".format(k_cluster))
    plt.savefig(filepath,  dpi=100)

    # seg_image = Image.open(filepath)

    filename = file.filename
    # upload_blob(filename,"public",filepath)
    # return FileResponse(path=filepath, filename=filename, media_type='image/jpg')
    return FileResponse(path=filepath, filename=filename, media_type='image/jpg')
    return templates.TemplateResponse(r"clustering_examples.html",
                                     {'request': request})

# @router.post('/submit', response_class=HTMLResponse)
# async def post_form(request: Request,k_cluster: int = Form(...), file: UploadFile = File(...)):
    
#     return FileResponse(path=filepath, filename=filename, media_type='image/jpg')
"""
 Author: Viraj Vaitha
 Description: main file
 - Imports routers to keep main file tidy
 - description for docs
 - setting paths using os so solutions works locally as well as in a docker image
 - Mounting templates and static files to render html pages correctly
"""


## TO DO: Add unit tests and more try/except statements
##      : Responsive? can't even tell it is downloading, loading bar, new page or spinner atleast!
##      : Incorporate mlflow to your solution to store an artifact demonstrating performance (time) for each function

# Import Libaries
import sys
import os 
from pathlib import Path

current_file = Path(__file__)
current_file_dir = current_file.parent
project_root = current_file_dir.parent
static_root_absolute = os.path.join(project_root,"app/static")
template_root_absolute = os.path.join(project_root,"app/templates")
sys.path.append(os.path.realpath(project_root))

from fastapi import FastAPI, Request, File, UploadFile, Depends, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from app.routers import machine_learning_gallery
import matplotlib.pyplot as plt

description = """
Machine Learning gallery provides a variety of different examples of machine learning applications. 

## Unsupervised Learning

KMeans clustering for **image segmentation**.

"""


# Descriptions (optional) - adds name and description in docs
tags_metadata = [
    {
        "name": "machine_learning_gallery",
        "description": "APIs to showcase unsupervised learning applications",
    }
]


# Initiate your FastAPI application
app = FastAPI(title="Machine Learning Gallery",
              description=description,
              version="0.0.1",
            #   terms_of_service="http://example.com/terms/",
              contact={
                        "name": "Viraj Vaitha",
                        # "url": "",
                        "email": "virajvaitha1995@gmail.com",
                    },
            #   license_info={
                            # "name": "Apache 2.0",
                            # "url": "https://www.apache.org/licenses/LICENSE-2.0.html",}
                            )

# Import gallery service
app.include_router(machine_learning_gallery.router)


# HTML Rendering and static files
templates = Jinja2Templates(directory=template_root_absolute)
app.mount("/static", StaticFiles(directory=static_root_absolute), name = "static")


# temporary hello world landing page
@app.get("/")
async def root():
    return {"message": "Hello World"}




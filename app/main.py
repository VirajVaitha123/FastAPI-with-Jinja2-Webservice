"""
application entry point:
 - Initiates FastAPI server 
 - Connects to static files and templates directory (Jinga2)
 - Includes all API end points from router directory
 - hello_world placeholder for landing page
"""

# Author: Viraj Vaitha

## TO DO: Add unit tests and more try/except statements
##      : Optimise KMeans application to run faster?
##      : Responsive? can't even tell it is downloading, loading bar, new page or spinner atleast!
##      : Incorporate mlflow to your solution to store an artifact demonstrating performance (time) for each function
##      : Add an simple architecture diagram to demonstrate libaries,softwares and cloud services used for the solution.
##      : GIF instead of phone on the right showcasing application
##      : Create docker image

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


from app.routers import clustering_examples
import matplotlib.pyplot as plt


# Initiate your FastAPI application
app = FastAPI()

app.include_router(clustering_examples.router)


# HTML Rendering and static filesfa
templates = Jinja2Templates(directory=template_root_absolute)
app.mount("/static", StaticFiles(directory=static_root_absolute), name = "static")


# temporary hello world landing page
@app.get("/")
async def root():
    return {"message": "Hello World"}




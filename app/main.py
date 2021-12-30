"""
application entry point:
 - Initiates FastAPI server 
 - Connects to static files and templates directory (Jinga2)
 - Includes all API end points from router directory
 - hello_world placeholder for landing page
"""

# Author: Viraj Vaitha

# Import Libaries
from fastapi import FastAPI, Request, File, UploadFile, Depends, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from routers import clustering_examples
import matplotlib.pyplot as plt


# Initiate your FastAPI application
app = FastAPI()

app.include_router(clustering_examples.router)


# HTML Rendering and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name = "static")


# temporary hello world landing page
@app.get("/")
async def root():
    return {"message": "Hello World"}




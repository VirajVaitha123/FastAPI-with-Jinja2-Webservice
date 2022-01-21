# Portfolio

### Introduction
Webservice created using FastAPI (with Jinga2 Templates). Below is a gif to showcase the service.


![gif-summary](https://github.com/VirajVaitha123/portfolio/blob/app/images_gifs/Animation.gif)
<br>

The main purpose of this project is to demonstrate the following concepts:
1. FastAPI + Jinja2 templates
- FastAPI folder structure (router for larger project)
- Render HTML page (jinga2 templates and mounting static files)
- Users can uploading an image from the webpage. Machine learning (or any function of your choice) is then applied to the image and returned to the customer via download
- Upload image to Azure Blob Storage (since large applications wouldn't reply on the local storage)
- Leverage FastAPI to run cleaning steps (removing downloaded images) as a background task to improve performance.

2. Docker
- Practice building a docker image for FastAPI application to serve as a template for future projects
- Allows developers to view and use the service locally.
- Sets up for deployment (Azure/AWS and optionally use of Kubernetes)

3. Frontend
- I'm not a frontend developer- however this project allowed me to use templates from online, alter them and learn the basics of html,css and javascript.

This solution is great when your client/customer requires your service to be accessed from a website. FastAPI should be used for microservices (most commonly without the user interface) and for full scale web applications Django is preferred. 

This application uses KMeans clustering on image data and propogates the centroid RGB value to all other pixels that are within the same cluster.

<br>

### Other benefits

This project is an opportunity to experiment with a full stack project. We have the opportunity to download static files for the frontend (HTML, CSS and Javascript and customized to our liking) and backend (FastAPI). In addition, using Azure (Azure Blob Storage, Secrets, Azure App service ect..) and packaging an application that be packaged with Docker/Kubernetes. 

In addition the Machine Learning model can be downloaded from AzureML/mlflow.

### Folder Structure

From my research the ideal structure for a FastAPI application can be seen below:
```
📦app
 ┣ main.py ⭐
 ┣ 📂routers 
 ┃ ┣ 📜clustering_examples.py   #API routes - keeps main.py clean
 ┣ 📂helpers
 ┃  ┣ 📂 data_processing.py   #API routes - keeps main.py clean
 ┃  ┃  ┣  📜azure_blob_wrapper.py
 ┃  ┃  ┣  📜img_utils.py
 ┃  ┃  ┗  📜schemas.py
 ┃  ┣ 📂 machine_learning.py
 ┃  ┃  ┗ 📜image_segmentation.py
 ┃  ┣ 📂responses.py
 ┃  ┃  ┗ 📜responses_json.py
 ┣ 📂static
 ┃ ┣ 📂home_page
 ┃ ┃  ┣ 📂assets
 ┃ ┃  ┣ 📂css
 ┃ ┃  ┗ 📂js
 ┗ 📂templates
  ┗ 📜clustering_examples.html
```
Key Points:
- Main file imports routers from routers dir
- css,js and assets (images etc..) imported from static
- Jinga2 templates renders HTML files from templates folder


### Getting Started



```

```

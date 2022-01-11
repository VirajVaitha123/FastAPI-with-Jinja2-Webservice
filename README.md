# Portfolio

### Introduction
Webservice created using FastAPI (with Jinga2 Templates). The main purpose of this project is to show how FastAPI can be used to create your own API. In addition, we can leverage Jinja2 templates to render HTML pages. This solution is great when your client/customer requires your service to be accessed from a website. For full scale web applications another framework such as Django is preferred. 

This application uses KMeans clustering on image data and propogates the centroid RGB value to all other pixels that are within the same cluster.

### Other benefits

This project is an opportunity to experiment with a full stack project. We have the opportunity to download static files for the frontend (HTML, CSS and Javascript and customized to our liking) and backend (FastAPI). In addition, using Azure (Azure Blob Storage, Secrets, Azure App service ect..) and packaging an application that be packaged with Docker/Kubernetes. 

In addition the Machine Learning model can be downloaded from AzureML/mlflow.

### Folder Structure

From my research the ideal structure for a FastAPI application can be seen below:
📦app
 ┣ 📂detection ⭐
 ┃ ┣ 📂routers
 ┃ ┃ ┣ 📜clustering_examples.py   #API routes - keeps main.py clean
 ┃ ┣ 📂helpers
 ┃ ┃ ┣ 📜data_processing.py   #API routes - keeps main.py clean
 ┃ ┃ ┣ 📜machine_learning.py
 ┃ ┃ ┣ 📜responses.py
 ┃ ┣ 📂static
 ┃ ┃ ┣ 📂home_page
 ┃ ┃ ┃  ┣ 📂assets
 ┃ ┃ ┃  ┣ 📂css
 ┃ ┃ ┃  ┣ 📂js
 ┃ ┣ 📂templates
 ┃ ┃ ┣ clustering_examples.html

Key Points:
- Main file imports routers from routers dir
- css,js and assets (images etc..) imported from static
- Jinga2 templates renders HTML files from templates folder


### Getting Started



```

```
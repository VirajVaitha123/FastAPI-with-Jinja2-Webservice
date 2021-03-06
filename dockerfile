FROM python:3.9

# creates /code folder and sets to working directory
WORKDIR /code

# copies requirements.txt locally to code/ in docker container
COPY ./requirements.txt /code/requirements.txt
 
# pip installs requirements.txt (uses full path) and --no-cache-dir helps keep size of docker image small since we don't need to cache here
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copies the app directory into docker
COPY ./app /code/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

# Pulling all updated images from google cloud registery & redis 
docker pull gcr.io/de2022-362611/flask-celery-ml-celery
docker pull gcr.io/de2022-362611/flask-celery-ml-app
docker pull redis

# Deploy images based on docker-compose including all env variables
docker compose up -d
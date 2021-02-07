# Docker Basic Commands

service docker status

sudo docker ps -a #get all container dtails sudo docker images sudo docker rm container_id # delete container sudo
docker rm container_id1 container_id_2 # delete multiple container sudo docker rmi image_id # delete image sudo docker
rmi image_id1 image_id2 # delete multiple image

touch Dockerfile #create docker file cat Dockerfile #create docker file, 2 ways: cat or touch

sudo docker build -t raka:1.0 . # build image sudo docker run image_id

sudo docker stop container_id # stop docker container

# Build Image and run docker image on local browser

sudo docker build -t raka:latest . #build image

sudo docker run --name flaskapp -v$PWD/app:/app -p5000:5000 raka:latest

# push Image on DockerHub

sudo docker login Username : ra****06**4 Password : Ra*******4

sudo docker tag imageName:Tag username/imageName sudo docker tag raka:Tag ra****06**4/raka

sudo docker push userName/imageName sudo docker push ra****06**4/raka

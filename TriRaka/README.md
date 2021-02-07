# Build Image and run docker image on local browser

sudo docker build -t raka:latest .

sudo docker run --name flaskapp -v$PWD/app:/app -p5000:5000 raka:latest

# push Image on DockerHub

sudo docker tag imageName:Tag rakesh06184/imageName

sudo docker push userName/imageName

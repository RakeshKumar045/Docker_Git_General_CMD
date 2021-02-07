# Build Image and run docker image on local browser

sudo docker build -t raka:latest .

sudo docker run --name flaskapp -v$PWD/app:/app -p5000:5000 raka:latest
# Flask Hello World

docker build -t flask-hello-world .

docker run -d -p 8123:80 --name hello1 --hostname hello1 flask-hello-world


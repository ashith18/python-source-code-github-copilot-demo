# DockerDemo

git clone http://gitlab.10.16.85.156.nip.io/devops-solutions/dockerdemo.git
cd dockerdemo
docker build -t flaskApp:latest .
docker run --name FlaskApp -it -p 5000:5000 -d flaskApp:latest
curl localhost:5000

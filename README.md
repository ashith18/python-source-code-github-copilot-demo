# To test docker image

1. git clone http://gitlab.10.16.85.156.nip.io/devops-solutions/dockerdemo.git
2. cd dockerdemo
3. docker build -t flaskApp:latest .
4. docker run --name FlaskApp -it -p 5000:5000 -d flaskApp:latest
5. curl localhost:5000



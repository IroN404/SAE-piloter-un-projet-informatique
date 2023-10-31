#!/bin/bash
# Create a container for the app
docker build -t todo_docker
# Run the container we juste created, setting up with the environments var
docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v $(pwd)/app:/app --rm todo_docker

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<h1 align = "center">
    <br>
    <img src="media/logo_night.png" alt="Sans-titre-3" border="0" width="300">
    <br>
    SAE-3.02-Piloter un projet informatique
    <br>
</h1>

<h4 align="center">A To-Do app made with Python and based on the Qt framework.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#Set-up">Set-Up</a> •
  <a href="#Usage">Usage</a> •
  <a href="#Authors">Authors</a>
</p>

<h1 align = "center">
    <img alt="Version" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" />
    <img alt="PyCharm" src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/>
    <img alt="logo Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    <img alt="QT logo" src="https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white"/>

</h1>


## Key Features

* An easy to use minimalist app
* Possibility to attribute
      - Tags
      - Priority level
      - Due date
* The data of the app is stored on an external database ( so you can juste give this file to someone to share your list )
* Change from dark to light mode with a simple button
* Possibility to check and delete accomplished tasks

## Set-UP

### Using python interpreter 

You just need to download this repository as a zip file and extract it wherever you want.
Or you can use git in order to clone the repository on your computer :
```bash
    git clone https://github.com/IroN404/SAE-piloter-un-projet-informatique/tree/main
```
Then, open pycharm and in File > open, choose the folder you juste downloaded.
From now just start the app inside of the IDE when the environment finished to load.

### Using Docker

If you want to run this Python tkinter application using Docker, follow the steps below:

1. **Prerequisites:** Make sure you have Docker installed on your system. If you don't have it, you can [download Docker here](https://docs.docker.com/get-docker/).
2. Clone this repository to your local system using the following command:
   ```bash
       git clone https://github.com/your-username/your-repo.git
   ```
3. Navigate to the folder directory :
```bash
       cd repository
   ```
4. Make the run.sh script executable :
```bash
    sudo chmod +x run.sh
```
5. Run the script, it will automatically do everything needed :
```
    ./run.sh
```
***
Otherwise, you can actually do all of this by yourself following theses steps : 
1. Build the container :
```
    docker build -t todo_docker
```
2. Run the container :
```
    docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v $(pwd)/app:/app --rm todo_docker
```

## Usage

/// Part in build ///


***
## Authors
👤 **Yassem Mohareb Product Owner**
<br>
👤 **Bahir Boudouma-Lambarki Scrum Master**
<br>
👤 **Julien Losser**
<br>
👤 **Fayçal Bloul**
<br>
👤 **Gregory Maitre**
<br>
👤 **Ivan Tefang**

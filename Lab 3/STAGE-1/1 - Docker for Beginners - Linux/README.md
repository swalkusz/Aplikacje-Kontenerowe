# Docker for Beginners - Linux  

## Task 0: Prerequisites

Clone the Lab’s GitHub Repo:  
![alt text](image.png)

## Task 1: Run some simple Docker containers  

### Run a single task in an Alpine Linux container  
Run the following command in your Linux console:  
![alt text](image-1.png)  
<br>

List all containers:  
![alt text](image-2.png)  

### Run an interactive Ubuntu container  
Run a Docker container and access its shell:  
![alt text](image-3.png)  
<br>

list the contents of the root directory in the container:  
![alt text](image-4.png)  
<br>

show running processes in the container:  
![alt text](image-5.png)  
<br>

show which Linux distro the container is running:  
![alt text](image-6.png)  
<br>

leave the shell session:  
![alt text](image-7.png)  
<br>

check the version of our host VM:  
![alt text](image-8.png)  

### Run a background MySQL container  
Run a new MySQL container:  
![alt text](image-9.png)  
<br>

List the running containers:  
![alt text](image-10.png)  
<br>

check what’s happening in your containers:  
![alt text](image-11.png)
![alt text](image-12.png)  
<br>

List the MySQL version:  
![alt text](image-13.png)  
<br>

connect to a new shell process inside an already-running container:  
![alt text](image-14.png)  
<br>

check the version number again:  
![alt text](image-15.png)  
<br>

leave the interactive shell session:  
![alt text](image-16.png)  

## Task 2: Package and run a custom app using Docker  

### Build a simple website image  
get in linux_tweet_app directory:  
![alt text](image-17.png)  
<br>

Display the contents of the Dockerfile:  
![alt text](image-18.png)  
<br>

export an environment variable containing DockerID:  
![alt text](image-19.png)  
<br>

Echo the value of the variable:  
![alt text](image-20.png)  
<br>

create a new Docker image using the instructions in the Dockerfile:  
![alt text](image-21.png)  
<br>

start a new container from the image:  
![alt text](image-22.png)  
<br>

running website:  
![alt text](image-23.png)  
<br>

remove container:  
![alt text](image-24.png)  

## Task 3: Modify a Running Website

### Start our web app with a bind mount
start the web app and mount the current directory into the container:  
![alt text](image-25.png)  
<br>

running website:  
![alt text](image-26.png)  

### Modify the running website  
Copy a new index.html into the container:  
![alt text](image-27.png)  
<br>

running changed website:  
![alt text](image-28.png)  
<br>

Stop and remove the currently running container:  
![alt text](image-29.png)  
<br>

Rerun the current version without a bind mount:  
![alt text](image-30.png)  
<br>

wesite went back to first version:  
![alt text](image-31.png)  
<br>

Stop and remove the current container:  
![alt text](image-32.png)  

### Update the image
Build a new image and tag it:  
![alt text](image-33.png)  
<br>

images on the system:  
![alt text](image-34.png)  

### Test the new version
Run a new container from the new version of the image:  
![alt text](image-35.png)  
<br>

website 80:  
![alt text](image-36.png)  
<br>

Run another new container, this time from the old version of the image:  
![alt text](image-37.png)  
<br>

website 8080:  
![alt text](image-38.png)  

### Push your images to Docker Hub
List the images on your Docker host:  
![alt text](image-39.png):  
<br>

log into Docker Hub:  
![alt text](image-40.png)  
<br>

Push version 1.0:  
![alt text](image-41.png)  
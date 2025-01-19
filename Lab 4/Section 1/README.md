# Section 1

## Exercise 1.1: Getting started

* Start 3 containers from an image that does not automatically exit (such as nginx) in detached mode.  
![alt text](image.png)  
* Stop two of the containers and leave one container running.  
![alt text](image-1.png)  
* Submit the output for docker ps -a which shows 2 stopped containers and one running.  
![alt text](image-2.png)  

## Exercise 1.2: Cleanup  

* We have containers and an image that are no longer in use and are taking up space. Running `docker ps -a` and `docker image ls` will confirm this.  
![alt text](image-3.png)  
![alt text](image-2.png)  
* Clean the Docker daemon by removing all images and containers.  
![alt text](image-4.png)  
* Submit the output for `docker ps -a` and `docker image ls`  
![alt text](image-5.png)
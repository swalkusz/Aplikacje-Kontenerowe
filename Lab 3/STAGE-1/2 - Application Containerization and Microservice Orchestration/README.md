# Application Containerization and Microservice Orchestration  

## Stage Setup

>cloning the demo code repository, changing the working directory, and checking the demo branch out:  
![alt text](image.png)  

## Step 0: Basic Link Extractor Script

>Checkout the step0 branch and list files in it:  
![alt text](image-1.png)  
<br>
linkextractor.py content:  
![alt text](image-2.png)  
<br>
current permissions on this:  
![alt text](image-3.png)  

## Step 1: Containerized Link Extractor Script

>Checkout the step1 branch and list files in it:  
![alt text](image-4.png)  
<br>
Dockerfile content:  
![alt text](image-5.png)  
<br>
build docker image:  
![alt text](image-6.png)  
<br>
preview of running images:  
![alt text](image-7.png)  
<br>
run a one-off container with this image and extract links from some live web pages:  
![alt text](image-8.png)  
<br>
try it on a web page with more links in it:  
![alt text](image-9.png)  

## Step 2: Link Extractor Module with Full URI and Anchor Text

>Checkout the step2 branch and list files in it:  
![alt text](image-10.png)  
<br>
preview of the updated script:  
![alt text](image-11.png)  
<br>
build a new image:  
![alt text](image-12.png)  
<br>
existed images:  
![alt text](image-13.png)  
<br>
Running a one-off container using the linkextractor:step2 image:  
![alt text](image-14.png)  
<br>
Running a container using the previous image linkextractor:step1:  
![alt text](image-15.png)  

## Step 3: Link Extractor API Service

>Checkout the step3 branch and list files in it:  
![alt text](image-16.png)  
<br>
Dockerfile:  
![alt text](image-17.png)  
<br>
preview main.py:  
![alt text](image-18.png)  
<br>
build a new image:  
![alt text](image-19.png)  
<br>
run the container:  
![alt text](image-20.png)  
<br>
list the rinning containers:  
![alt text](image-21.png)  
<br>
HTTP request in the form /api/< url >:  
![alt text](image-22.png)  
<br>
container logs:  
![alt text](image-23.png)  
<br>
kill and remove this container:  
![alt text](image-24.png)  

## Step 4: Link Extractor API and Web Front End Services

>Checkout the step4 branch and list files in it:  
![alt text](image-25.png)  
<br>
preview docker-compose.yml:  
![alt text](image-26.png)  
<br>
bring these services up in detached mode using docker-compose utility:  
![alt text](image-27.png)  
<br>
Checking for the list of running containers:  
![alt text](image-28.png)  
<br>
talk to the API service:  
![alt text](image-29.png)  
<br>
modify the www/index.php file to replace all occurrences of Link Extractor with Super Link Extractor:  
![alt text](image-30.png)  
<br>
![alt text](image-31.png)  
![alt text](image-32.png)  

## Step 5: Redis Service for Caching

>Checkout the step5 branch and list files in it:  
![alt text](image-33.png)  
<br>
inspect the newly added Dockerfile under the ./www folder:  
![alt text](image-34.png)  
<br>
API server’s api/main.py file where we are utilizing the Redis cache:  
![alt text](image-35.png)  
<br>
updated docker-compose.yml file:  
![alt text](image-36.png)  
<br>
boot these services up:
![alt text](image-37.png)  
<br>
check whether or not the Redis service is being utilized:  
![alt text](image-38.png)  
<br>
![alt text](image-39.png)  
<br>
![alt text](image-40.png)  
![alt text](image-41.png)  

## Step 6: Swap Python API Service with Ruby

>![alt text](image-42.png)  
![alt text](image-43.png)  
![alt text](image-44.png)  
![alt text](image-45.png)  
![alt text](image-46.png)  
![alt text](image-47.png)  


# Lab 2 - Exercise 3: Building images  

## Getting setup  

![alt text](image.png)  

![alt text](image-1.png)  

## Creating a Dockerfile

![alt text](image-2.png)  
```echo. > Dockerfile``` - creates new *Dockerfile* file.  

![alt text](image-3.png)  
The `-y` flag avoids that prompt by always answering "*Y*".  

## Building the Dockerfile

![alt text](image-4.png)  
`.` - indicates the current directory of the *Dockerfile*. If the *Dockerfile* is named else, change it.    
`delner/ping:version` - image tag  
Note: You can repeat aboved command, to create more builds, but it doesn't affect to number of images. Images are not overwritten.  

![alt text](image-5.png)  

## Optimizing the Dockerfile  

![alt text](image-6.png)  

![alt text](image-7.png)  

![alt text](image-8.png)  
167MB vs 139MB  
Now the new image is only 4MB larger in size.  

## Other Dockerfile directives  

![alt text](image-9.png)  

![alt text](image-10.png)  

![alt text](image-11.png)  

![alt text](image-12.png)  

# Skopiuj wybrany plik tekstowy z hosta (swojego komputera) do kontenera Dockerowego.  

```bash
docker run -dit --name zad2 ubuntu
```

skopiowanie pliku *`file-zad2.txt`* do kontenera *`zad2`* do fildetu *`tmp`*:  
```bash
docker cp C:\Users\szymo\Desktop\EGZAMIN-Docker\zad2\file-zad2.txt zad2:/tmp/
```  

sprawdzenie zawartości kontenera:
```bash
docker exec -it zad2 /bin/bash
```

```bash
cd /tmp
ls
cat file-zad2.txt
```
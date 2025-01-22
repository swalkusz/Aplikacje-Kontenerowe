# 3. Skopiuj wybrany plik tekstowy z kontenera Dockerowego do hosta (swojego komputera).  

```bash
docker run -dit --name zad3 ubuntu
```

```bash
docker exec -it zad3 /bin/bash
```

utworzenie pliku w kontenerze:  
```bash
echo "To jest przyk\305\202adowy plik tekstowy." > /tmp/example.txt
```

```bash
exit
```  

skopiowanie z kontenera na hosta:  
```bash
docker cp zad3:/tmp/example.txt ./example.txt
```

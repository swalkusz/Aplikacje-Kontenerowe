# 4. Pokaż działanie komend ENTRYPOINT i CMD w wybranym projekcie.  

```bash
mkdir entrypoint-cmd-example
cd entrypoint-cmd-example
echo. > Dockerfile  
```  

`Dockerfile`:  
```Dockerfile
FROM ubuntu:22.04
ENTRYPOINT ["echo", "ENTRYPOINT:"]
CMD ["Default CMD argument"]
```

budowanie obrazu:  
```bash
docker build -t entrypoint-cmd-demo .
```

uruchomienie z domyślnymi argumentami:  
```bash
docker run --rm entrypoint-cmd-demo
```

Uruchomienie z własnymi argumentami:  
```bash
docker run --rm entrypoint-cmd-demo "Custom argument"
```

* `ENTRYPOINT` definiuje stałą część polecenia, która zawsze zostanie wykonana.  
* `CMD` dostarcza domyślne argumenty dla `ENTRYPOINT`. Jeśli podasz własne argumenty przy uruchomieniu, nadpiszą one wartości ustawione w `CMD`.
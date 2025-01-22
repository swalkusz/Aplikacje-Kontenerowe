# 10. Jaka jest różnica między obrazem i kontenerem? Pokaż przykład budowania obrazu (Dockerfile) i uruchamiania na jego podstawie kontenera.

Dockerfile
```sh
# Użycie obrazu bazowego z Pythonem
FROM python:3.9-slim

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie lokalnego pliku Python do obrazu
COPY hello.py .

# Ustawienie komendy startowej
CMD ["python", "hello.py"]
```

Budowanie obrazu:  
```sh
docker build -t hello-docker .
```

>`-t hello-docker`: Ustawia nazwę i tag obrazu (`hello-docker:latest`).  
`.`: Wskazuje na bieżący katalog jako kontekst budowania.  

Uruchamianie kontenera:  
```sh
docker run --rm hello-docker
```
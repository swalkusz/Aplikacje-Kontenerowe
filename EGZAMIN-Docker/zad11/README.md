# Pokaż jak "wejść" do wybranego kontenera. Utwórz w nim plik tekstowy z dowolnymi danymi. Co zrobić, żeby po zamknięciu kontenera dane z pliku były dostępne po ponownym uruchomieniu kontenera?
Zademonstruj dowolny sposób.

## Metoda 1: Docker Volume
Utwórz volume:
```sh
docker volume create mydata
```

Uruchom kontener z podpiętym volume:
```sh
docker run -dit --name mycontainer -v mydata:/data ubuntu
```

Wejdź do kontenera i utwórz plik:
```sh
docker exec -it mycontainer /bin/bash
echo "Treść pliku z volume" > /data/example.txt
exit
```

Zatrzymaj i uruchom ponownie kontener:
```sh
docker stop mycontainer
```

```sh
docker start mycontainer
```

Sprawdź plik w kontenerze:
```sh
docker exec -it mycontainer cat /data/example.txt
```

## Metoda 2: Bind Mount

```sh
docker run -dit --name mycontainer -v <full-path>:/data ubuntu
```

```sh
docker exec -it mycontainer /bin/bash
echo "Treść pliku w bind mount" > /data/example.txt
exit
```

```sh
docker rm -f mycontainer
```

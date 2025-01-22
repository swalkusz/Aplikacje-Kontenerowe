# 9. Czym są sieci w Dockerze? Zaprezentuj przykład na bazie swojego projektu.

Sieci w Dockerze umożliwiają kontenerom komunikację między sobą oraz z hostem. Docker domyślnie udostępnia kilka typów sieci:

* Bridge (domyślna dla większości kontenerów):

        Tworzy prywatną sieć wirtualną, gdzie kontenery mogą się komunikować.
        Używana głównie w konfiguracjach lokalnych.  
* Host:

        Udostępnia kontenerowi ten sam stos sieciowy, co host.
        Używana, gdy chcesz uniknąć izolacji sieciowej.  
* None:

        Całkowicie odłącza kontener od sieci.  
* Custom:

        ręcznie definiowana sieć, 

Uruchomienie sieci i kontenerów:  
```sh
docker compose up
```

Sprawdzenie dostępnych sieci:
```sh
docker network ls
```

Sprawdzenie komunikacji między kontenerami: Po wejściu do kontenera backend:
```sh
docker exec -it <backend_container_id> bash
ping db
```
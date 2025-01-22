# 5. Pokaż działanie usługi bazodanowej z wykorzystaniem docker-compose.  

`docker-compose.yml`:  
```yml
version: '3.8'

services:
  db:
    image: postgres:15
    container_name: postgres-db
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: exampledb
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```  

```bash
docker-compose up -d
```
wejście do terminala postgres:  
```bash
docker exec -it postgres-db psql -U user -d exampledb
```  

przykładowe polecenia które można wykonać wewnątrz terminala postgres:  
```sql
CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(50));
INSERT INTO test_table (name) VALUES ('Alice'), ('Bob');
SELECT * FROM test_table;
```

```bash
docker-compose down
```

usunięcie voluminów:  
```bash
docker-compose down -v
```
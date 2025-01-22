FROM ubuntu:22.04

# katalog roboczy
WORKDIR /app

# Dodanie pliku za pomocą COPY
COPY example.txt /app/example_copy.txt

# Dodanie i rozpakowanie archiwum za pomocą ADD
ADD folder.zip /app/extracted/

# Komenda uruchamiająca kontener
CMD ["ls", "-la", "/app"]
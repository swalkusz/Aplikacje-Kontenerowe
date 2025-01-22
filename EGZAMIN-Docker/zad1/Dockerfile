# Użycie obrazu bazowego z Pythonem
FROM python:3.9-slim

# Ustawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

# Skopiowanie folderu code z hosta do kontenera
COPY code /app/code

# Ustawienie folderu code jako domyślnego miejsca pracy
WORKDIR /app/code

# Domyślna komenda uruchamiająca kontener
CMD ["python", "script.py"]
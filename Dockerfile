# Usa un'immagine Python leggera
FROM python:3.11-slim

# Imposta la cartella di lavoro
WORKDIR /app

# Copia l'intero progetto (inclusa la cartella Class)
COPY . .

# Non servono librerie esterne, ma creiamo un requirements.txt vuoto per standard
RUN touch requirements.txt

# Comando per avviare il programma. 
# Usiamo -u per evitare che Python metta l'output in cache (vedrai i print in tempo reale)
CMD ["python", "-u", "main.py"]
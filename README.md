# 🏛️ Python Enigma Machine Simulator

> Un simulatore fedele e interattivo della celebre macchina crittografica **Enigma (Modello M3)**, l'apparecchio utilizzato per cifrare le comunicazioni durante la Seconda Guerra Mondiale.

Questo progetto dimostra l'implementazione di logiche crittografiche complesse, l'uso della **programmazione a oggetti (OOP)** e la distribuzione del software tramite **containerizzazione Docker**.

---

## 🚀 Caratteristiche Tecniche

Il simulatore riproduce accuratamente i componenti principali della macchina Enigma:

| Componente | Descrizione |
|---|---|
| **Rotori (I, II, III)** | Implementazione delle permutazioni degli alfabeti originali |
| **Meccanismo di Stepping** | Simulazione del "double step": il rotore centrale avanza se lui stesso o il destro si trovano sulla tacca |
| **Riflettore (Reflector B)** | Garantisce la cifratura simmetrica — cifrare due volte con la stessa chiave restituisce il testo originale |
| **Plugboard** | Supporto per lo scambio di coppie di lettere per aumentare la complessità crittografica |

---

## 🛠️ Tecnologie Utilizzate

- **Linguaggio:** Python 3.10+ (con utilizzo del pattern matching `match-case`)
- **Containerizzazione:** Docker — per la portabilità totale dell'ambiente di esecuzione

---

## 🐳 Esecuzione con Docker (Consigliato)

Usare Docker permette di testare il simulatore **senza installare Python** o configurare l'ambiente localmente.

### 1. Build dell'immagine

Dalla cartella principale del progetto, esegui:

```bash
docker build -t enigma-app .
```

### 2. Avvio del simulatore

Dato che il programma è interattivo, avviarlo con i flag `-it` e `--rm` (per pulire il container alla chiusura):

```bash
docker run -it --rm enigma-app
```

---

## 💻 Esecuzione Locale

Se preferisci avviarlo direttamente con Python:

1. Assicurati di avere **Python 3.10 o superiore** installato
2. Esegui il comando:

```bash
python main.py
```

---

## 📂 Struttura del Progetto

```
.
├── Class/
│   └── Enigma.py      # Logica interna e algoritmi dei rotori
├── main.py            # Interfaccia utente e ciclo principale
├── Dockerfile         # Configurazione per il container Docker
├── .gitignore         # File esclusi da Git (es. __pycache__)
└── README.md          # Documentazione del progetto
```

---

## 👤 Autore

**Davide Barbieri** — Sviluppo logica crittografica e containerizzazione

# 🏛️ Python Enigma Machine Simulator
 
> Un simulatore fedele e interattivo della celebre macchina crittografica **Enigma (Modello M3)**, l'apparecchio utilizzato per cifrare le comunicazioni durante la Seconda Guerra Mondiale.
 
Questo progetto dimostra l'implementazione di logiche crittografiche complesse, l'uso della **programmazione a oggetti (OOP)** e la distribuzione del software tramite **containerizzazione Docker**.
 
---
 
## 📌 Versioni
 
| Versione | Descrizione | Stato |
|---|---|---|
| **v1.0.0** | Replica autentica — comportamento asimmetrico originale (una lettera non cifra mai sé stessa) | ✅ Stabile |
| **v2.0.0** | Riflettore custom — punto debole rimosso, una lettera può cifrare sé stessa | ✅ Stabile |
 
> Puoi consultare tutte le versioni nella sezione [**Releases**](../../releases) del repository.
 
---
 
## 🔐 Evoluzione Crittografica
 
### v1.0.0 — Replica Autentica
La prima versione riproduce il comportamento **autentico** della macchina Enigma, incluso il suo celebre punto debole:
 
> **Una lettera non può mai cifrare sé stessa.**
 
Questo vincolo, imposto dal Riflettore B originale, fu uno dei principali punti di attacco sfruttati da Alan Turing e dai crittografi di Bletchley Park per violare il codice Enigma durante la Seconda Guerra Mondiale. Escludere questa possibilità eliminava milioni di combinazioni, rendendo l'attacco statistico molto più efficace.
 
### v2.0.0 — Riflettore Custom
Questa versione introduce un **riflettore custom (Riflettore C)**, costruito per ammettere **punti fissi** — ovvero lettere che possono cifrare sé stesse. Il punto debole originale è rimosso:
 
> **Una lettera può cifrare sé stessa**, rendendo impossibile l'esclusione statistica sfruttata da Turing.
 
Il riflettore custom mantiene la **simmetria delle coppie** — cifrare due volte con la stessa configurazione restituisce il testo originale — ma aggiunge un grado di libertà crittografica assente nella macchina originale.
 
---
 
## 🚀 Caratteristiche Tecniche
 
| Componente | Descrizione |
|---|---|
| **Rotori (I, II, III)** | Permutazioni degli alfabeti originali della macchina M3 |
| **Meccanismo di Stepping** | Simulazione accurata del *double step*: il rotore centrale avanza se lui stesso o il destro si trovano sulla tacca |
| **Riflettore B** | Riflettore originale — garantisce la cifratura simmetrica ma introduce il punto debole autentico |
| **Riflettore C** | Riflettore custom — ammette punti fissi, punto debole rimosso *(attivo dalla v2.0.0)* |
| **Plugboard** | Scambio di coppie di lettere configurabile per aumentare la complessità crittografica |
 
---
 
## 🛠️ Tecnologie Utilizzate
 
- **Linguaggio:** Python 3.11+ (con pattern matching `match-case`)
- **Containerizzazione:** Docker — per la portabilità totale dell'ambiente di esecuzione
---
 
## 🐳 Esecuzione con Docker (Consigliato)
 
Usare Docker permette di testare il simulatore **senza installare Python** o configurare l'ambiente localmente.
 
### 1. Build dell'immagine
 
Dalla cartella principale del progetto:
 
```bash
docker build -t enigma-app .
```
 
### 2. Avvio del simulatore
 
Il flag `-it` è necessario perché il programma è interattivo; `--rm` rimuove il container alla chiusura:
 
```bash
docker run -it --rm enigma-app
```
 
---
 
## 💻 Esecuzione Locale
 
Se preferisci avviarlo direttamente con Python (3.11 o superiore):
 
```bash
python main.py
```
 
---
 
## 🖥️ Utilizzo
 
All'avvio, il simulatore mostra la configurazione attiva e presenta un menu interattivo:
 
```
========================================
       MACCHINA ENIGMA
  Rotori: ['I', 'II', 'III']
  Chiave: MCG | Plugboard: AV BS DT
========================================
 
Cosa vuoi fare?
  [1] Cifrare un messaggio
  [2] Decifrare un messaggio
  [3] Esci
```
 
Per decifrare un messaggio è sufficiente inserirlo nella voce **[2]**: la macchina applica la stessa trasformazione restituendo il testo originale — a patto di usare la stessa configurazione di rotori, chiave e plugboard.
 
---
 
## 📂 Struttura del Progetto
 
```
ENIGMA/
├── Class/
│   └── Enigma.py      # Logica crittografica: rotori, plugboard, riflettori, stepping
├── main.py            # Interfaccia utente e ciclo principale
├── Dockerfile         # Configurazione per il container Docker
├── .dockerignore      # File esclusi dal contesto Docker
├── .gitignore         # File esclusi da Git
├── LICENSE            # Licenza del progetto
└── README.md          # Documentazione del progetto
```
 
---
 
## 👤 Autore
 
**Davide Barbieri** — Sviluppo logica crittografica e containerizzazione
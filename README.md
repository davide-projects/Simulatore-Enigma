# 🏛️ Python Enigma Machine Simulator
 
> Un simulatore fedele e interattivo della celebre macchina crittografica **Enigma (Modello M3)**, l'apparecchio utilizzato per cifrare le comunicazioni durante la Seconda Guerra Mondiale.
 
Questo progetto dimostra l'implementazione di logiche crittografiche complesse, l'uso della **programmazione a oggetti (OOP)** e la distribuzione del software tramite **containerizzazione Docker**.
 
---
 
## 📌 Versioni
 
| Versione | Descrizione | Stato |
|---|---|---|
| **v1.1** | Replica autentica — comportamento asimmetrico originale (una lettera non cifra mai sé stessa) | ✅ Stabile |
| **v1.2** | Crittografia simmetrica rinforzata — maggiore robustezza e difficoltà di decifrazione | 🔧 In sviluppo |
 
> Puoi consultare tutte le versioni nella sezione [**Releases**](../../releases) del repository.
 
---
 
## 🔐 Fedeltà Crittografica (v1.1)
 
Questa versione riproduce il comportamento **autentico** della macchina Enigma, incluso il suo celebre punto debole:
 
> **Una lettera non può mai cifrare sé stessa.**
 
Questo vincolo, imposto dal riflettore, fu uno dei principali punti di attacco sfruttati da Alan Turing e dai crittografi di Bletchley Park per violare il codice Enigma durante la Seconda Guerra Mondiale.
 
La cifratura è **simmetrica nell'uso**: cifrare un testo e poi cifrare il risultato con la stessa configurazione iniziale restituisce il testo originale.
 
---
 
## 🚀 Caratteristiche Tecniche
 
| Componente | Descrizione |
|---|---|
| **Rotori (I, II, III)** | Permutazioni degli alfabeti originali della macchina M3 |
| **Meccanismo di Stepping** | Simulazione accurata del *double step*: il rotore centrale avanza se lui stesso o il destro si trovano sulla tacca |
| **Riflettore B** | Garantisce la cifratura simmetrica — cifrare due volte con la stessa chiave restituisce il testo originale |
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
 
Per decifrare un messaggio, è sufficiente inserirlo nella voce **[2]**: la macchina applica la stessa trasformazione in senso inverso, restituendo il testo originale — a patto di usare la stessa configurazione di rotori, chiave e plugboard.
 
---
 
## 📂 Struttura del Progetto
 
```
ENIGMA/
├── Class/
│   └── Enigma.py      # Logica crittografica: rotori, plugboard, riflettore, stepping
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
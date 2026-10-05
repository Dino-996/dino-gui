# Deinosuchus Grab Calculator

Calcolatore desktop per **The Isle • Evrima** che determina il peso massimo afferrabile da un Deinosuchus (DINO) in base al peso corrente e alla posizione.

## A cosa serve

Nel gioco, il DINO può afferrare altri dinosauri solo se il loro peso è inferiore a una certa percentuale del peso del DINO stesso:
- **Terra**: 50% del peso del DINO
- **Acqua**: 75% del peso del DINO

Questo tool calcola istantaneamente il limite massimo inserendo il peso attuale e la posizione.

## Come funziona

1. Inserisci il **peso attuale** del tuo DINO (0–14.000 kg)
2. Seleziona la **posizione**: `terra` o `acqua`
3. Clicca **CALCOLA**
4. Il risultato mostra il **peso massimo afferrabile** in kg

Formula: `peso_DINO × percentuale_posizione / 100`

## Installazione

```bash
# Clona il repository
cd dino-gui

# Crea un ambiente virtuale (opzionale ma consigliato)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Installa le dipendenze
pip install -r requirements.txt
```

## Avvio

```bash
python dino_gui.py
```

## Requisiti

- Python 3.10+
- PyQt6 ≥ 6.7

## Struttura del progetto

```
dino-gui/
├── dino_gui.py      # Interfaccia grafica (PyQt6)
├── service.py       # Logica di calcolo (riutilizzabile)
├── requirements.txt # Dipendenze
└── README.md
```

## Licenza

Progetto personale per uso didattico/gioco.

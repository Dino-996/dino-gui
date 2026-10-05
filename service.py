"""Calcolatore del peso supportato dal DINO in base alla posizione."""

POSIZIONI = {"terra": 50, "acqua": 75}

def convalida_numero(messaggio: str, minimo: float, massimo: float) -> float:
    """Chiede un numero all'utente finché non è compreso in [minimo, massimo]."""

    valore = float(input(messaggio).strip())

    while valore < minimo or valore > massimo:
        print(f"***Errore: Il valore deve essere compreso tra {minimo} e {massimo}.\n")
        valore = float(input("Riprova: ").strip())

    return valore

def convalida_dizionario(messaggio: str, dizionario: dict) -> str:
    """Chiede una stringa, tra le varie opzioni, all'utente finché non è tra i valori ammessi."""

    valore = input(messaggio).strip().lower()

    while valore not in dizionario:
        opzioni = ", ".join(dizionario)
        print(f"***Errore: '{valore}' non è valido. Valori possibili: {opzioni}\n")
        valore = input("Riprova: ").strip().lower()

    return valore

def calcola_peso_supportato(peso: float, posizione:str) -> float:
    """Calcola il peso supportato in base alla posizione del DINO."""
    return peso * POSIZIONI[posizione] / 100

def verifica_posizione() -> float:
    """Raccoglie gli input dell'utente e restituisce il peso supportato."""

    peso = convalida_numero("Inserisci il peso attuale del tuo crocodilo in kg (0-14000): ", 0, 14000)
    chiave = convalida_dizionario(f"Inserisci la posizione attuale del DINO ({", ".join(POSIZIONI)}): ", POSIZIONI)

    return calcola_peso_supportato(peso, chiave)

if __name__ == '__main__':
    risultato = verifica_posizione()
    print(f"\nPuoi prendere il DINO se pesa meno di {risultato:.2f} kg")
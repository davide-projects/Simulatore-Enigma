from Class.Enigma import Enigma

def esegui():
    rotori_scelti = ["I", "II", "III"]
    chiave_iniziale = "MCG"
    prese = "AV BS DT"

    print("=" * 40)
    print("       MACCHINA ENIGMA")
    print(f"  Rotori: {rotori_scelti}")
    print(f"  Chiave: {chiave_iniziale} | Plugboard: {prese}")
    print("=" * 40)

    while True:
        print("\nCosa vuoi fare?")
        print("  [1] Cifrare un messaggio")
        print("  [2] Decifrare un messaggio")
        print("  [3] Esci")

        scelta = input("\nScelta: ").strip()

        try:
            match scelta:
                case "1":
                    messaggio = input("Inserisci il messaggio da cifrare: ").upper()
                    enigma = Enigma(rotori_scelti, chiave_iniziale, prese)
                    risultato = enigma.elabora_testo(messaggio)
                    print(f"\nOriginale: {messaggio}")
                    print(f"Cifrato:   {risultato}")

                case "2":
                    messaggio = input("Inserisci il messaggio da decifrare: ").upper()
                    enigma = Enigma(rotori_scelti, chiave_iniziale, prese)
                    risultato = enigma.elabora_testo(messaggio)
                    print(f"\nCifrato:   {messaggio}")
                    print(f"Decifrato: {risultato}")

                case "3":
                    print("\nArrivederci!")
                    break

                case _:
                    print("Scelta non valida, riprova.")

        except ValueError:
            print("Errore: Carattere Non consentito!")

if __name__ == "__main__":
    esegui()
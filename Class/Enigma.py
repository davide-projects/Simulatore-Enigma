class Enigma:
    def __init__(self, id_rotori, posizioni_iniziali, collegamenti_plugboard=""):
        self.alfabeti_rotori = {
            "I":   "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "II":  "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "III": "BDFHJLCPTXVZNYEIWGAKMUSQOR",
            "RIFLETTORE_B": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        }
        self.tacche = {"I": "Q", "II": "E", "III": "V"}

        # Carichiamo i rotori (0=Sinistra, 1=Centro, 2=Destra)
        self.rotori = [self.alfabeti_rotori[id] for id in id_rotori]
        self.offset = [ord(p) - ord('A') for p in posizioni_iniziali.upper()]
        self.pos_tacche = [ord(self.tacche[id]) - ord('A') for id in id_rotori]
        self.tabella_scambi = self.configura_plugboard(collegamenti_plugboard)

    def configura_plugboard(self, collegamenti):
        mappa = list(range(26))
        if collegamenti:
            coppie = collegamenti.upper().split()
            for coppia in coppie:
                if len(coppia) == 2:
                    a, b = ord(coppia[0]) - ord('A'), ord(coppia[1]) - ord('A')
                    mappa[a], mappa[b] = b, a
        return mappa
    
    def fai_scattare_rotori(self):
        # Salva lo stato PRIMA di qualsiasi modifica
        tacca_destra  = (self.offset[2] == self.pos_tacche[2])
        tacca_centro  = (self.offset[1] == self.pos_tacche[1])

        # Double step: il centro avanza se lui stesso o il destro sono sulla tacca
        if tacca_centro:
            self.offset[0] = (self.offset[0] + 1) % 26
            self.offset[1] = (self.offset[1] + 1) % 26
        elif tacca_destra:
            self.offset[1] = (self.offset[1] + 1) % 26

        # Il destro avanza sempre
        self.offset[2] = (self.offset[2] + 1) % 26

    def passaggio_rotore(self, n, stringa_rotore, spostamento, inverso=False):
        if not inverso:
            c = (n + spostamento) % 26
            segnale_interno = ord(stringa_rotore[c]) - ord('A')
            return (segnale_interno - spostamento + 26) % 26
        else:
            c = (n + spostamento) % 26
            # Trova l'indice i dove il VALORE di output della permutazione == c
            pos_interna = next(i for i in range(26) if ord(stringa_rotore[i]) - ord('A') == c)
            return (pos_interna - spostamento + 26) % 26

    def cifra_carattere(self, c):
        if not c.isalpha(): return c
        
        self.fai_scattare_rotori()

        # # DEBUG TEMPORANEO
        # print(f"Char: {c.upper()} | Offset: {self.offset}")

        n = ord(c.upper()) - ord('A')
        
        n = self.tabella_scambi[n]
        
        # Andata: Destra -> Centro -> Sinistra
        n = self.passaggio_rotore(n, self.rotori[2], self.offset[2])
        n = self.passaggio_rotore(n, self.rotori[1], self.offset[1])
        n = self.passaggio_rotore(n, self.rotori[0], self.offset[0])
        
        # Riflettore
        n = (ord(self.alfabeti_rotori["RIFLETTORE_B"][n]) - ord('A')) % 26
        
        # Ritorno: Sinistra -> Centro -> Destra
        n = self.passaggio_rotore(n, self.rotori[0], self.offset[0], inverso=True)
        n = self.passaggio_rotore(n, self.rotori[1], self.offset[1], inverso=True)
        n = self.passaggio_rotore(n, self.rotori[2], self.offset[2], inverso=True)
        
        n = self.tabella_scambi[n]
        return chr(n + ord('A'))

    def elabora_testo(self, testo):
        return "".join([self.cifra_carattere(c) for c in testo])
    
    def test_simmetria_rotore(self):
        print("\n--- TEST SIMMETRIA ROTORI ---")
        for idx, (rotore, offset) in enumerate(zip(self.rotori, self.offset)):
            errori = 0
            for n in range(26):
                andata = self.passaggio_rotore(n, rotore, offset, inverso=False)
                ritorno = self.passaggio_rotore(andata, rotore, offset, inverso=True)
                if ritorno != n:
                    print(f"Rotore {idx} offset {offset}: {n} -> {andata} -> {ritorno} ❌")
                    errori += 1
            if errori == 0:
                print(f"Rotore {idx} offset {offset}: simmetria OK ✅")
        print()
class Asmuo:
    def __init__(self, vardas, pavarde, asmens_kodas, telefonas, el_pastas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.asmens_kodas = asmens_kodas
        self.telefonas = telefonas
        self.el_pastas = el_pastas

    def gauti_bendra_info(self):
        return f"{self.vardas} {self.pavarde}, tel. {self.telefonas}, el. paštas: {self.el_pastas}"

from asmuo import Asmuo

class Darbuotojas(Asmuo):
    def __init__(self, vardas, pavarde, asmens_kodas, telefonas, el_pastas, darbuotojo_pareigos, darbuotojo_atlyginimas):
        super().__init__(vardas, pavarde, asmens_kodas, telefonas, el_pastas)
        self.darbuotojo_pareigos = darbuotojo_pareigos
        self.darbuotojo_atlyginimas = darbuotojo_atlyginimas

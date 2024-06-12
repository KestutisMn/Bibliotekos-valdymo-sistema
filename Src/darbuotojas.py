from asmuo import Asmuo
class Darbuotojas(Asmuo):
    def __init__(self, vardas, pavarde, asmens_kodas, telefonas, el_pastas, darbuotojo_pareigos, darbuotojo_atlyginimas):
        super().__init__(vardas, pavarde, asmens_kodas, telefonas, el_pastas)
        self.darbuotojo_pareigos = darbuotojo_pareigos
        self.darbuotojo_atlyginimas = darbuotojo_atlyginimas

    def gauti_viso_info(self):
        bendra_info = self.gauti_bendra_info()
        return f"{bendra_info}, pareigos: {self.darbuotojo_pareigos}, atlyginimas: {self.darbuotojo_atlyginimas} EUR"

    def ivesti_nauja_knyga(self, knygu_sarasas, knyga):
        knygu_sarasas.append(knyga)
        print(f"Nauja knyga '{knyga.pavadinimas}' sėkmingai pridėta į biblioteką.")

    def pasalinti_knyga(self, knygu_sarasas, knyga_id):
        for knyga in knygu_sarasas:
            if knyga.id == knyga_id:
                knygu_sarasas.remove(knyga)
                print(f"Knyga '{knyga.pavadinimas}' sėkmingai pašalinta iš bibliotekos.")
                return
        print(f"Knyga su ID '{knyga_id}' nerasta bibliotekoje.")
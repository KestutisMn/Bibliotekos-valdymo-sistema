from datetime import datetime, timedelta

class Lankytojas:
    def __init__(self, lankytojo_id, knygu_sarasas):
        self.lankytojo_id = lankytojo_id
        self.knygu_sarasas = knygu_sarasas

    def registruoti_lankytoja(self):
        pass

    def patikrinti_paimtas_knygas(self):
        return self.knygu_sarasas

    def skaiciuoti_delspinigius(self, paskolintos_knygos):
        dabartine_data = datetime.now()
        delspinigiai = 0
        for knyga in paskolintos_knygos:
            grazinimo_data = knyga.paemimo_data + timedelta(days=30)
            if dabartine_data > grazinimo_data:
                delspinigiai += (dabartine_data - grazinimo_data).days * 0.01
        return delspinigiai

    def apmoketi(self, suma):
        return True

    def pasirinkti_knyga(self):
        pass

    def patikrinti_knygu_limita(self):
        return len(self.knygu_sarasas) < 5

    def patikrinti_veluojancio_lankytojo_knygu_pasiemima(self, paskolintos_knygos):
        grazinimo_data = paskolintos_knygos.paemimo_data + timedelta(days=30)
        dabartine_data = datetime.now()
        return dabartine_data <= grazinimo_data

    def patikrinti_delspinigius_ir_galimybe_paimti(self, delspinigiai):
        return delspinigiai <= 0.05

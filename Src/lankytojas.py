from datetime import datetime, timedelta
class Lankytojas:
    def __init__(self, lankytojo_id, paimtos_knygos=None):
        self.lankytojo_id = lankytojo_id
        if paimtos_knygos is None:
            paimtos_knygos = []
        self.knygu_sarasas = paimtos_knygos

    def registruoti_lankytoja(self):
        pass

    def patikrinti_paimtas_knygas(self):
        return self.knygu_sarasas

    def prideti_paimta_knyga(self, knyga):
        self.knygu_sarasas.append(knyga)
        knyga.paemimo_data = datetime.now()

    def skaiciuoti_delspinigius(self):
        dabartine_data = datetime.now()
        delspinigiai = 0
        for knyga in self.knygu_sarasas:
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

    def patikrinti_veluojancio_lankytojo_knygu_pasiemima(self):
        dabartine_data = datetime.now()
        for knyga in self.knygu_sarasas:
            grazinimo_data = knyga.paemimo_data + timedelta(days=30)
            if dabartine_data > grazinimo_data:
                return False
        return True

    def patikrinti_delspinigius_ir_galimybe_paimti(self):
        delspinigiai = self.skaiciuoti_delspinigius()
        return delspinigiai <= 0.05

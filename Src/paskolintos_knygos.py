from datetime import datetime

class PaskolintosKnygos:
    def __init__(self, knyga, data=None, grazinta=None):
        self.knyga = knyga
        self.data = data if data else datetime.now()
        self.grazinta = grazinta

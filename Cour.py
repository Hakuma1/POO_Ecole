from datetime import datetime
from datetime import time


class Cour:
    def __init__(self, nom, date_heure, duree):
        self.nom = nom
        self.date_heure = date_heure
        self.duree = duree

    def __str__(self):
        return f"Il s'agit du cours de {self.nom}.\
 Il a lieu le {self.date_heure.strftime('%d/%m/%Y')} à {self.date_heure.strftime('%H:%M:%S')} pendant {self.duree.hour}H:\
{self.duree.minute}Min"

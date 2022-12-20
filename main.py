from Cour import Cour
from datetime import datetime
from datetime import time
from Professeur import Professeur
from Etudiant import Etudiant
from Classe import Classe

dh = datetime(2022, 12, 2, 17, 30, 30)
d = time(4, 45)

ob_cour = Cour("Informatique", dh, d)
print(ob_cour)
ob_prof = Professeur("Lionel Messi", "Homme", "200000")
print(ob_prof)
ob_et = Etudiant("Kylian MBappé", "Homme", "Licence")
print(ob_et)
ob_cl = Classe("Classe 1", "Licence")
print(ob_cl)

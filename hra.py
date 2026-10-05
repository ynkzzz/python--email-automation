príkazy = ["start", "stop", "restart", "status",]
for p in príkazy:
    print(f"Spracovávam príkaz: {p}") 
def spracuj_prikazy(zoznam):
    for p in zoznam:
        print(f"Spracovávam príkaz: {p}")

prikazy = ["start", "stop", "restart", "status"]

nove_prikazy = ["update", "upgrade", "install", "backup"]
spracuj_prikazy(nove_prikazy)

def spocitaj_sumu(ceny):
    spolu = 0
    for cena in ceny:
        spolu = spolu + cena
    return spolu

def spocitaj_drahsie(ceny):
    spolu = 0
    for cena in ceny:
        if cena > 10:
            spolu = spolu + cena
    return spolu

kosik = [10, 20, 11, 5, 7]
suma = spocitaj_drahsie(kosik)
print(f"Suma v kosiku je: {suma} €") 

from abc import ABC, abstractmethod


def najdi_chyby(zoznam_sprav):
    vysledky = []
    for sprava in zoznam_sprav:
        if "CHYBA" in sprava:
            vysledky.append(sprava)
    return vysledky


logy = [" Server startuje", " CHYBA: Nedá sa pripojiť k databáze", " Server beží", " CHYBA: Neznáma chyba", " Server sa vypína"]
najdene_chyby = najdi_chyby(logy)
print("Nájdené chyby:")
for chyba in najdene_chyby:
    print(chyba)


class Print(ABC):
    @abstractmethod
    def write(self, text):
        """Zapíše text do výstupu."""
        raise NotImplementedError

    @abstractmethod
    def flush(self):
        """Uvoľní výstup a zabezpečí dokončenie zápisu."""
        raise NotImplementedError


class ConsolePrint(Print):
    def write(self, text):
        print(text, end="")
        return text

    def flush(self):
        print()
        return None
print(najdi_chyby(logy))

import smtplib
from email.mime.text import MIMEText 

sprava_text = "ahoj toto je automaticka sprava"

msg = MIMEText("python je super")
msg["subject"] = "pozdrav z pythonu" 
msg["from"] = "blazegamer0400@gmail.com"
msg["to"] = "rikkaexe4@gmail.com"

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("blazegamer0400@gmail.com", "heslo" 
        server.send_message(msg)
    print("email bol uspesne odoslany")
except Exception as e:
    print(f"Chyba pri odosielani emailu: {e}")
   
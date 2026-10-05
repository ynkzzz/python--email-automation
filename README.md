# python-log-email-automation
# Python Log Email Automation

Tento skript slúži na automatické spracovanie logov a odosielanie e-mailových upozornení.

## Funkcionalita
- **Filtrovanie logov:** Prehľadáva správy a identifikuje chybové hlásenia (`CHYBA:`).
- **E-mailové notifikácie:** Pri nájdení chyby automaticky odosiela e-mail cez SMTP server (Gmail) s využitím modulu `smtplib` a `email.mime`.
- **Spracovanie dát:** Obsahuje logiku pre prácu so zoznamami a podmienkami.

## Požiadavky a spustenie
1. Python 3.x
2. Pre odosielanie e-mailov je potrebné nastaviť App Password v Google účte.
3. Spustenie skriptu:
   ```bash
   python hra.py

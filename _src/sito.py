"""Dati dello studio e impostazioni del sito.

Tutto ciò che compare su più pagine si cambia qui, una volta sola,
poi si rigenera il sito con:  python _src/build.py
"""

DOMINIO = "https://sozzisound.it"
NOME = "SozziSound"
SLOGAN = ("Tecnici competenti in acustica in Puglia e in Italia: misure, valutazioni "
          "e relazioni per la conformità acustica.")

EMAIL = "info@sozzisound.it"
WHATSAPP = "393348748771"

TELEFONI = [
    {"nome": "Ing. Emanuele Sozzi", "numero": "+393348748771", "mostra": "+39 334 874 8771"},
    {"nome": "Prof. Vincenzo Sozzi", "numero": "+393356688997", "mostra": "+39 335 668 8997"},
]

INDIRIZZO = {"via": "Via Tenente Antonio Specchia, 30", "cap": "72017", "citta": "Ostuni", "provincia": "BR"}
SEDE_LAT, SEDE_LON = 40.7297, 17.5777

# Partita IVA: lasciare vuoto finché non c'è. Appena inserita compare nel piè di pagina di tutto il sito.
PARTITA_IVA = ""

# Profili social. Una voce vuota non viene mostrata.
SOCIAL = {
    "instagram": "https://www.instagram.com/sozzisound/",
    "linkedin": "https://www.linkedin.com/company/sozzisound/",
    "facebook": "",
    "tiktok": "",
    "youtube": "",
}
LINKEDIN_EMANUELE = "https://www.linkedin.com/in/emanuele-sozzi-a1758920a/"

# Modulo contatti: indirizzo dell'app web di Google Apps Script (vedi _src/modulo-contatti/ISTRUZIONI.md).
# Finché resta vuoto, il modulo invia tramite l'app di posta o WhatsApp del visitatore.
MODULO_ENDPOINT = "https://script.google.com/macros/s/AKfycbzOGQRPA1nKQwZz5fbfAWcTnR7GlFsUHScDrLXnoaR1r9VcH4D5_bP6X2nncx6zBnJJ0w/exec"

# Google Analytics e Google Ads
GA4 = "G-8PBHZKBKSM"
ADS = "AW-18331963974"

# Data mostrata come "ultimo aggiornamento" nelle pagine che non ne hanno una propria (AAAA-MM-GG)
AGGIORNATO = "2026-11-10"

PROFESSIONISTI = [
    {
        "id": "emanuele-sozzi",
        "nome": "Ing. Emanuele Sozzi",
        "nome_semplice": "Emanuele Sozzi",
        "prefisso": "Ing.",
        "enteca": "12994",
        "foto": "assets/emanuele-sozzi.jpg",
        "iniziali": "ES",
        "breve": "Ingegnere aerospaziale, con un interesse specifico per acustica e vibrazioni.",
        "linkedin": LINKEDIN_EMANUELE,
    },
    {
        "id": "vincenzo-sozzi",
        "nome": "Prof. Vincenzo Sozzi",
        "nome_semplice": "Vincenzo Sozzi",
        "prefisso": "Prof.",
        "enteca": "12993",
        "foto": "assets/vincenzo-sozzi.jpg",
        "iniziali": "VS",
        "breve": "Fisico, con oltre 30 anni di esperienza nel settore acustico.",
        "linkedin": "",
    },
]

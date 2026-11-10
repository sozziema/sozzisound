"""Elenco completo dei servizi e delle aree in cui sono raggruppati."""

from .servizi_a import SERVIZI_A
from .servizi_b import SERVIZI_B

# chiave, nome, voce del modulo contatti, descrizione dell'area
AREE = [
    ("pratiche", "Autorizzazioni e pratiche", "Impatto o clima acustico per una pratica",
     "La documentazione acustica che serve per aprire, costruire, ampliare o modificare un'attività."),
    ("locali", "Locali, musica, eventi e sport", "Locale con musica, evento o impianto sportivo",
     "Per chi lavora con la musica o con lo sport vicino alle case: pratiche, limiti, deroghe."),
    ("edilizia", "Edilizia e ambienti", "Edificio: requisiti passivi, collaudo, progetto",
     "L'acustica degli edifici, dal progetto al collaudo, e quella degli ambienti interni."),
    ("disturbo", "Rumore, disturbo e controversie", "Rumore che disturba, esposto o perizia",
     "Quando un rumore è già un problema: misurarlo, attribuirlo, ridurlo."),
    ("lavoro", "Luoghi di lavoro", "Rumore nei luoghi di lavoro",
     "L'esposizione dei lavoratori al rumore secondo il D.Lgs 81/2008."),
    ("enti", "Enti pubblici", "Richiesta di un ente pubblico",
     "Il supporto tecnico agli uffici comunali per pianificare, regolare e controllare."),
]

SERVIZI = sorted(SERVIZI_A + SERVIZI_B, key=lambda s: s["n"])
PER_SLUG = {s["slug"]: s for s in SERVIZI}

for _s in SERVIZI:
    _s["url"] = f"servizi/{_s['slug']}.html"

# Servizi mostrati nella griglia della home (i nove storici) e nel piè di pagina
IN_HOME = [1, 2, 3, 4, 5, 6, 7, 8, 9]
NEL_PIEDE = [1, 2, 5, 8, 10, 7, 6]

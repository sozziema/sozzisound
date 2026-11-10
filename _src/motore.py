"""Motore di impaginazione: funzioni e componenti comuni a tutte le pagine."""

import hashlib
import html
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote

import sito as S

QUI = Path(__file__).resolve().parent
RADICE = QUI.parent

MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
        "agosto", "settembre", "ottobre", "novembre", "dicembre"]

# Riempiti da build.py prima di impaginare (servono a menu e piè di pagina).
PIEDE_SERVIZI = []   # [(nome, url)]
PIEDE_PERCHI = []    # [(nome, url)]
AREE_MODULO = []     # [(chiave, etichetta)]


# ---------------------------------------------------------------- testo

_TAG = re.compile(r"(<script\b.*?</script>|<style\b.*?</style>|<[^>]+>)", re.S | re.I)
_NBSP = " "


def tipo(testo):
    """Tipografia del testo visibile: apostrofi curvi, puntini, spazi non separabili.
    Agisce solo fuori dai tag, quindi non tocca attributi, script e stili."""
    parti = _TAG.split(testo)
    for i in range(0, len(parti), 2):
        t = parti[i]
        t = t.replace("'", "’").replace("...", "…")
        t = re.sub(r"(\d) (dB|km|m/s|Hz|ore|euro|anni|m\b)", r"\1" + _NBSP + r"\2", t)
        t = re.sub(r"\b(artt?|n|c|lett|D\.Lgs|L|L\.R|p)\. (?=[\dA-Za-z])", lambda m: m.group(1) + "." + _NBSP, t)
        parti[i] = t
    return "".join(parti)


def q(testo):
    """Tipografia per stringhe semplici (titoli, descrizioni, attributi)."""
    return testo.replace("'", "’").replace("...", "…")


def piano(testo):
    """Toglie i tag e restituisce testo semplice su una riga."""
    t = re.sub(r"<br\s*/?>", " ", testo)
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    return re.sub(r"\s+", " ", t).strip()


def schema_testo(testo):
    return piano(tipo(testo)).replace(_NBSP, " ")


def esc(testo):
    return html.escape(testo, quote=True)


def data_it(iso):
    a, m, g = iso.split("-")
    return f"{int(g)} {MESI[int(m) - 1]} {a}"


def slug(testo):
    t = piano(testo).lower()
    for a, b in (("à", "a"), ("è", "e"), ("é", "e"), ("ì", "i"), ("ò", "o"), ("ù", "u"), ("’", ""), ("'", "")):
        t = t.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


_versioni = {}


def versione(nome):
    """Impronta del file, per evitare che il browser usi una copia vecchia."""
    if nome not in _versioni:
        percorso = RADICE / nome
        _versioni[nome] = hashlib.sha1(percorso.read_bytes()).hexdigest()[:8] if percorso.exists() else "0"
    return _versioni[nome]


# ---------------------------------------------------------------- pagina

@dataclass
class Pagina:
    url: str                    # "", "servizi/", "servizi/nome.html"
    title: str
    descrizione: str
    corpo: str = ""
    sezione: str = ""           # voce di menu attiva
    briciole: list = field(default_factory=list)   # [(nome, url)] senza la home
    schema: list = field(default_factory=list)
    indicizza: bool = True
    og_occhiello: str = ""
    og_titolo: str = ""         # può contenere <em>
    og_tipo: str = "website"
    lettura: bool = False       # barra di avanzamento della lettura
    assoluta: bool = False      # percorsi dalla radice (pagina 404)
    aggiornato: str = S.AGGIORNATO
    studio_completo: bool = False

    @property
    def file(self):
        if self.url == "":
            return "index.html"
        return self.url + "index.html" if self.url.endswith("/") else self.url

    @property
    def radice(self):
        return "/" if self.assoluta else "../" * self.url.count("/")

    def a(self, url):
        """Indirizzo, relativo a questa pagina, di un'altra pagina o risorsa del sito."""
        if re.match(r"^(https?:|mailto:|tel:|#)", url):
            return url
        return (self.radice + url) or "./"

    @property
    def canonico(self):
        return S.DOMINIO + "/" + self.url

    @property
    def chiave_og(self):
        if self.url == "":
            return "home"
        return self.url.replace(".html", "").strip("/").replace("/", "--")


def contatti_url(area="", rif=""):
    parti = []
    if area:
        parti.append("tipo=" + quote(area))
    if rif:
        parti.append("rif=" + quote(piano(rif)))
    return "contatti.html" + ("?" + "&".join(parti) if parti else "") + "#richiesta"


# ---------------------------------------------------------------- icone

ICONE = {
    "telefono": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
    "whatsapp": '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16.004 3C9.383 3 4 8.373 4 15c0 2.393.7 4.623 1.902 6.5L4 29l7.71-1.863A11.9 11.9 0 0 0 16.004 27C22.625 27 28 21.627 28 15S22.625 3 16.004 3zm0 21.6c-1.98 0-3.822-.55-5.395-1.5l-.386-.23-4.57 1.104 1.14-4.457-.25-.398A9.55 9.55 0 0 1 5.4 15c0-5.302 4.31-9.6 9.604-9.6 5.293 0 9.6 4.298 9.6 9.6 0 5.302-4.307 9.6-9.6 9.6zm5.29-7.19c-.29-.146-1.716-.847-1.982-.943-.266-.097-.46-.146-.654.146-.194.291-.75.943-.92 1.137-.17.194-.34.218-.63.073-.29-.146-1.224-.451-2.332-1.44-.862-.769-1.444-1.72-1.613-2.01-.17-.29-.018-.447.128-.592.13-.13.29-.34.435-.51.146-.17.194-.291.29-.485.097-.194.049-.364-.024-.51-.073-.146-.654-1.576-.897-2.158-.236-.567-.477-.49-.654-.5l-.557-.01c-.194 0-.51.073-.777.364-.267.291-1.02.996-1.02 2.428 0 1.432 1.044 2.816 1.19 3.01.146.194 2.055 3.14 4.98 4.404.696.3 1.24.48 1.663.615.699.222 1.334.19 1.837.115.56-.084 1.716-.702 1.958-1.38.243-.68.243-1.262.17-1.38-.072-.12-.266-.194-.556-.34z"/></svg>',
    "email": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor" stroke="none"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.6h.06c.53-.95 1.83-1.95 3.76-1.95 4.02 0 4.76 2.5 4.76 5.75V21h-4v-5.2c0-1.24-.02-2.84-1.83-2.84-1.83 0-2.11 1.36-2.11 2.75V21h-4z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-8h2.7l.4-3.1h-3.1V7.9c0-.9.3-1.5 1.6-1.5h1.6V3.6c-.3 0-1.300-.1-2.400-.1-2.400 0-4 1.400-4 4.100v2.300H7.600V13h2.700v8z"/></svg>',
    "tiktok": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 3c.3 2.100 1.500 3.600 3.700 3.800v3c-1.300.1-2.500-.3-3.700-1v5.700c0 6.300-6.900 8.300-9.700 3.800-1.800-2.900-.7-8 5-8.200v3.200c-.4.100-.900.200-1.300.3-1.300.4-2 1.200-1.800 2.600.4 2.600 5.100 3.400 4.700-1.700V3z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.600 7.200a2.500 2.500 0 0 0-1.800-1.800C18.300 5 12 5 12 5s-6.300 0-7.800.4A2.500 2.500 0 0 0 2.400 7.200C2 8.800 2 12 2 12s0 3.200.4 4.800a2.500 2.500 0 0 0 1.800 1.800C5.700 19 12 19 12 19s6.300 0 7.800-.4a2.500 2.500 0 0 0 1.800-1.800c.4-1.600.4-4.800.4-4.800s0-3.200-.4-4.800zM10 15V9l5.200 3z"/></svg>',
    "onde": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 10v4M7.500 6v12M12 3v18M16.500 7v10M21 10v4"/></svg>',
}

NOMI_SOCIAL = {"instagram": "Instagram", "linkedin": "LinkedIn", "facebook": "Facebook",
               "tiktok": "TikTok", "youtube": "YouTube"}


def social_html():
    voci = []
    for chiave, indirizzo in S.SOCIAL.items():
        if indirizzo:
            voci.append(f'<li><a href="{esc(indirizzo)}" target="_blank" rel="noopener" '
                        f'aria-label="SozziSound su {NOMI_SOCIAL[chiave]}">{ICONE[chiave]}</a></li>')
    return '<ul class="social">' + "".join(voci) + "</ul>"


def whatsapp_url(testo="Buongiorno, vorrei richiedere una consulenza acustica."):
    return f"https://wa.me/{S.WHATSAPP}?text={quote(testo)}"


# ---------------------------------------------------------------- grafiche

BANDE = ["50", "63", "80", "100", "125", "160", "200", "250", "315", "400", "500", "630",
         "800", "1k", "1.25k", "1.6k", "2k", "2.5k", "3.15k", "4k", "5k", "6.3k", "8k", "10k"]


def _valori_spettro(seme, n=24):
    impronta = hashlib.sha256(seme.encode("utf-8")).digest()
    valori = []
    for i in range(n):
        base = 0.55 + 0.38 * math.sin(math.pi * (i + 3) / (n + 2))
        pendenza = 1 - 0.016 * i
        valori.append(base * pendenza * (0.6 + 0.4 * impronta[i % 32] / 255))
    lisci = [(valori[max(i - 1, 0)] + 2 * valori[i] + valori[min(i + 1, n - 1)]) / 4 for i in range(n)]
    massimo = max(lisci)
    return [v / massimo for v in lisci]


def spettro(seme):
    """Piccolo spettro decorativo in terzi d'ottava, diverso per ogni pagina."""
    barre, etichette = [], []
    for i, v in enumerate(_valori_spettro(seme)):
        h = round(16 + 104 * v, 1)
        x = round(i * 13.6, 1)
        barre.append(f'<rect x="{x}" y="{round(122 - h, 1)}" width="9.6" height="{h}" style="animation-delay:{i * 26}ms"/>')
        if i % 3 == 1:
            etichette.append(f'<text x="{round(x + 4.8, 1)}" y="134" text-anchor="middle">{BANDE[i]}</text>')
    return ('<div class="spettro" aria-hidden="true"><svg viewBox="0 0 326 138" width="326" height="138">'
            + "".join(barre) + "".join(etichette) + "</svg></div>")


def bande_svg():
    """Fascia decorativa del piè di pagina (file assets/bande.svg)."""
    n = 120
    valori = _valori_spettro("sozzisound", 32)
    barre = []
    for i in range(n):
        v = valori[i % 32] * (0.55 + 0.45 * math.sin(math.pi * (i % 40) / 40))
        h = round(4 + 28 * v, 1)
        barre.append(f'<rect x="{i * 8}" y="{round(34 - h, 1)}" width="4" height="{h}"/>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="960" height="34" viewBox="0 0 960 34">'
            '<g fill="#70b7ff" opacity=".32">' + "".join(barre) + "</g></svg>\n")


# Contorno schematico della Puglia (lat, lon), tracciato a mano per punti: serve da sfondo, non da carta.
_CONTORNO = [
    (41.925, 15.135), (41.917, 15.250), (41.908, 15.450), (41.928, 15.620), (41.920, 15.760), (41.932, 15.885),
    (41.940, 15.960), (41.950, 16.015), (41.935, 16.100), (41.890, 16.180), (41.800, 16.195), (41.740, 16.120),
    (41.705, 16.060), (41.640, 15.935), (41.600, 15.895), (41.520, 15.905), (41.455, 15.965), (41.405, 16.060),
    (41.375, 16.150), (41.325, 16.285), (41.282, 16.418), (41.243, 16.505), (41.207, 16.598), (41.190, 16.672),
    (41.140, 16.850), (41.085, 17.000), (41.062, 17.090), (40.997, 17.222), (40.953, 17.303), (40.872, 17.410),
    (40.838, 17.470), (40.790, 17.585), (40.765, 17.700), (40.717, 17.800), (40.690, 17.935), (40.650, 18.015),
    (40.565, 18.035), (40.497, 18.120), (40.450, 18.210), (40.385, 18.300), (40.300, 18.400), (40.272, 18.432),
    (40.147, 18.492), (40.107, 18.520), (40.080, 18.485), (40.035, 18.460), (40.000, 18.425), (39.930, 18.390),
    (39.870, 18.390), (39.795, 18.365), (39.790, 18.345), (39.830, 18.275), (39.840, 18.210), (39.887, 18.110),
    (39.970, 18.020), (40.055, 17.975), (40.127, 17.995), (40.215, 17.925), (40.260, 17.895), (40.288, 17.845),
    (40.297, 17.760), (40.307, 17.680), (40.300, 17.570), (40.300, 17.500), (40.330, 17.440), (40.345, 17.360),
    (40.400, 17.215), (40.445, 17.190), (40.480, 17.190), (40.505, 17.120), (40.512, 17.040), (40.490, 16.970),
    (40.468, 16.935), (40.425, 16.885), (40.400, 16.862),
    (40.470, 16.835), (40.560, 16.700), (40.650, 16.715), (40.700, 16.720), (40.745, 16.660), (40.740, 16.550),
    (40.750, 16.400), (40.790, 16.270), (40.870, 16.190), (40.920, 16.120), (40.955, 16.030), (41.030, 16.020),
    (41.100, 15.990), (41.130, 15.930), (41.110, 15.800), (41.080, 15.650), (41.055, 15.560), (41.040, 15.500),
    (41.075, 15.420), (41.100, 15.330), (41.115, 15.240), (41.190, 15.210), (41.250, 15.210), (41.310, 15.120),
    (41.370, 15.040), (41.450, 15.000), (41.530, 14.960), (41.600, 14.940), (41.660, 15.000), (41.710, 15.040),
    (41.760, 15.080), (41.840, 15.120),
]

_LON0, _LAT0, _KX, _KY = 14.85, 42.02, 168.6, 222.4


def _xy(lat, lon):
    return round((lon - _LON0) * _KX, 1), round((_LAT0 - lat) * _KY, 1)


def distanza_km(lat, lon):
    """Distanza in linea d'aria dalla sede, in chilometri."""
    r = 6371.0
    f1, f2 = math.radians(S.SEDE_LAT), math.radians(lat)
    df, dl = f2 - f1, math.radians(lon - S.SEDE_LON)
    a = math.sin(df / 2) ** 2 + math.cos(f1) * math.cos(f2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def mappa(p, province, comuni, didascalia="Schema delle distanze in linea d'aria dalla sede di Ostuni."):
    """Schema della Puglia con anelli di distanza dalla sede e punti cliccabili."""
    contorno = "M" + " L".join(f"{x},{y}" for x, y in (_xy(a, b) for a, b in _CONTORNO)) + " Z"
    cx, cy = _xy(S.SEDE_LAT, S.SEDE_LON)
    parti = [f'<path class="mappa-terra" d="{contorno}"/>']
    for km in (25, 50, 100, 150, 200):
        parti.append(f'<circle class="mappa-anello" cx="{cx}" cy="{cy}" r="{km * 2}"/>')
    for km in (25, 50, 100):
        r = km * 2
        x, y = round(cx + r * math.cos(math.radians(100)), 1), round(cy - r * math.sin(math.radians(100)) + 3, 1)
        parti.append(f'<text class="mappa-km" x="{x}" y="{y}" text-anchor="middle">{km} km</text>')
    for km in (150, 200):
        parti.append(f'<text class="mappa-km" x="{round(cx - km * 2 + 6, 1)}" y="{round(cy - 5, 1)}">{km} km</text>')
    for c in comuni:
        x, y = _xy(c["lat"], c["lon"])
        parti.append(f'<a href="{p.a(c["url"])}"><title>{esc(c["nome"])}</title>'
                     f'<circle class="mappa-comune" cx="{x}" cy="{y}" r="3.2"/></a>')
    for c in province:
        x, y = _xy(c["lat"], c["lon"])
        dx, dy, ancora = c.get("etichetta", (9, 4, "start"))
        parti.append(f'<a href="{p.a(c["url"])}"><circle class="mappa-punto" cx="{x}" cy="{y}" r="5"/>'
                     f'<text class="mappa-nome" x="{x + dx}" y="{y + dy}" text-anchor="{ancora}">{esc(c["nome_mappa"])}</text></a>')
    parti.append(f'<circle class="mappa-sede-onda" cx="{cx}" cy="{cy}" r="7"/>'
                 f'<circle class="mappa-sede" cx="{cx}" cy="{cy}" r="5.5"/>'
                 f'<text class="mappa-sede-nome" x="{cx + 10}" y="{cy - 9}">Ostuni · sede</text>')
    return ('<figure class="mappa"><svg viewBox="0 0 640 512" role="img" '
            'aria-label="Schema della Puglia con le distanze dalla sede di Ostuni e i collegamenti alle pagine delle province">'
            + "".join(parti) + f"</svg><figcaption>{didascalia}</figcaption></figure>")


# ---------------------------------------------------------------- componenti

def briciole_html(p):
    voci = [f'<li><a href="{p.a("")}">Home</a></li>']
    for nome, url in p.briciole[:-1]:
        voci.append(f'<li><a href="{p.a(url)}">{nome}</a></li>')
    voci.append(f'<li aria-current="page">{p.briciole[-1][0]}</li>')
    return '<nav class="briciole" aria-label="Percorso"><ol>' + "".join(voci) + "</ol></nav>"


def briciole_schema(p):
    elementi = [{"@type": "ListItem", "position": 1, "name": "Home", "item": S.DOMINIO + "/"}]
    for i, (nome, url) in enumerate(p.briciole, start=2):
        elementi.append({"@type": "ListItem", "position": i, "name": schema_testo(nome), "item": S.DOMINIO + "/" + url})
    return {"@type": "BreadcrumbList", "itemListElement": elementi}


def testata(p, occhiello, h1, sommario, azioni="", extra="", seme=None):
    return f"""<section class="testata">
<div class="container">
{briciole_html(p)}
<p class="eyebrow">{occhiello}</p>
<h1>{h1}</h1>
<p class="sommario">{sommario}</p>
{f'<div class="testata-azioni">{azioni}</div>' if azioni else ''}{extra}
</div>
{spettro(seme or p.url)}
</section>"""


def domande_html(lista, due_colonne=False):
    def voce(d, r):
        corpo = r if r.lstrip().startswith("<") else f"<p>{r}</p>"
        return f'<details class="domanda"><summary>{d}</summary><div class="risposta">{corpo}</div></details>'
    if due_colonne:
        meta = (len(lista) + 1) // 2
        return ('<div class="domande due-colonne"><div>' + "".join(voce(*x) for x in lista[:meta])
                + "</div><div>" + "".join(voce(*x) for x in lista[meta:]) + "</div></div>")
    return '<div class="domande">' + "".join(voce(*x) for x in lista) + "</div>"


def domande_schema(lista):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": schema_testo(d),
         "acceptedAnswer": {"@type": "Answer", "text": schema_testo(r)}} for d, r in lista]}


def schede_link(p, voci, due=False):
    """voci: [{"piccolo", "titolo", "testo", "url", "etichetta"}]"""
    pezzi = []
    for v in voci:
        pezzi.append(f"""<article class="scheda-link"><small>{v.get("piccolo", "")}</small>
<h3>{v["titolo"]}</h3><p>{v.get("testo", "")}</p>
<a href="{p.a(v["url"])}">{v.get("etichetta", "Apri")} <span aria-hidden="true">→</span></a></article>""")
    return f'<div class="schede{" due" if due else ""}">' + "".join(pezzi) + "</div>"


def linee_contatto(p, classe="scheda-linee"):
    t = S.TELEFONI[0]
    return f"""<div class="{classe}">
<a href="tel:{t["numero"]}">{ICONE["telefono"]}{t["mostra"]}</a>
<a href="{whatsapp_url()}" target="_blank" rel="noopener">{ICONE["whatsapp"]}Scrivici su WhatsApp</a>
<a href="mailto:{S.EMAIL}">{ICONE["email"]}{S.EMAIL}</a>
</div>"""


def scheda_cta(p, titolo, testo, area="", rif="", etichetta="Richiedi un preventivo"):
    return f"""<div class="scheda-cta">
<p class="eyebrow">Preventivo gratuito</p>
<h2>{titolo}</h2>
<p>{testo}</p>
<a class="button button-primary" href="{p.a(contatti_url(area, rif))}">{etichetta} <span aria-hidden="true">→</span></a>
{linee_contatto(p)}
</div>"""


def cta_band(p, area="", rif="", titolo="Hai un caso <em>da valutare?</em>",
             testo="Raccontaci in breve la situazione. Ti diciamo quale documentazione serve davvero e prepariamo un preventivo gratuito."):
    t1, t2 = S.TELEFONI
    return f"""<section class="cta-band">
<div class="container cta-grid">
<div><p class="eyebrow">Parliamone</p><h2>{titolo}</h2><p>{testo}</p></div>
<div class="cta-actions">
<a class="button button-primary" href="{p.a(contatti_url(area, rif))}">Scrivi la tua richiesta <span aria-hidden="true">→</span></a>
<a class="cta-linea" href="tel:{t1["numero"]}">{ICONE["telefono"]}{t1["mostra"]}<small>{t1["nome"]}</small></a>
<a class="cta-linea" href="tel:{t2["numero"]}">{ICONE["telefono"]}{t2["mostra"]}<small>{t2["nome"]}</small></a>
<a class="cta-linea" href="{whatsapp_url()}" target="_blank" rel="noopener">{ICONE["whatsapp"]}Scrivici su WhatsApp</a>
</div>
</div>
</section>"""


def modulo_html(p, titolo="Scrivi la tua richiesta", sotto="Bastano poche righe: ti ricontattiamo per un primo confronto e per il preventivo, che è gratuito."):
    opzioni = "".join(f'<option value="{esc(etichetta)}" data-area="{chiave}">{etichetta}</option>'
                      for chiave, etichetta in AREE_MODULO)
    if S.MODULO_ENDPOINT:
        nota = "I dati servono solo per risponderti. Puoi anche inviare la stessa richiesta su WhatsApp."
    else:
        nota = ("«Invia richiesta» apre la tua app di posta con il messaggio già scritto; "
                "«Invia su WhatsApp» lo apre in chat. I dati servono solo per risponderti.")
    return f"""<form class="modulo" id="modulo-contatti" data-endpoint="{esc(S.MODULO_ENDPOINT)}" method="post" action="mailto:{S.EMAIL}">
<p class="modulo-titolo" id="richiesta">{titolo}</p>
<p class="modulo-sotto">{sotto}</p>
<p class="form-note" data-riferimento hidden>Richiesta su: <strong><span></span></strong></p>
<input type="hidden" name="riferimento" value="">
<div class="campo"><label for="f-nome">Nome e cognome</label><input type="text" id="f-nome" name="nome" autocomplete="name" required></div>
<div class="campo-coppia">
<div class="campo"><label for="f-email">Email</label><input type="email" id="f-email" name="email" autocomplete="email" placeholder="nome@email.it" required></div>
<div class="campo"><label for="f-telefono">Telefono <span class="facoltativo">(facoltativo)</span></label><input type="tel" id="f-telefono" name="telefono" autocomplete="tel"></div>
</div>
<div class="campo-coppia">
<div class="campo"><label for="f-tipo">Tipo di richiesta</label><select id="f-tipo" name="tipo" required><option value="">Scegli una voce</option>{opzioni}</select></div>
<div class="campo"><label for="f-comune">Comune dell'intervento</label><input type="text" id="f-comune" name="comune" autocomplete="address-level2" required></div>
</div>
<div class="campo"><label for="f-messaggio">Messaggio</label><textarea id="f-messaggio" name="messaggio" rows="4" placeholder="Che attività o immobile riguarda, che cosa ti è stato richiesto e da chi." required></textarea></div>
<div class="trappola" aria-hidden="true"><label for="f-sito">Non compilare questo campo</label><input type="text" id="f-sito" name="sito_web" tabindex="-1" autocomplete="off"></div>
<label class="consenso"><input type="checkbox" name="privacy" value="sì" required><span>Ho letto l'<a href="{p.a("privacy.html")}">informativa sulla privacy</a> e acconsento al trattamento dei dati per ricevere risposta.</span></label>
<div class="modulo-azioni">
<button class="button button-primary" type="submit">Invia richiesta <span aria-hidden="true">→</span></button>
<button class="button button-wa" type="button" data-invia-whatsapp>{ICONE["whatsapp"]}Invia su WhatsApp</button>
</div>
<p class="form-note">{nota}</p>
<div class="modulo-esito" role="status" aria-live="polite" hidden></div>
</form>"""


# ---------------------------------------------------------------- dati strutturati

def nodo_studio(completo=False):
    n = {
        "@type": ["ProfessionalService", "LocalBusiness"],
        "@id": S.DOMINIO + "/#studio",
        "name": S.NOME,
        "url": S.DOMINIO + "/",
        "image": S.DOMINIO + "/assets/og/home.png",
        "logo": S.DOMINIO + "/favicon.png",
        "email": S.EMAIL,
        "telephone": S.TELEFONI[0]["numero"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": S.INDIRIZZO["via"],
            "addressLocality": S.INDIRIZZO["citta"],
            "addressRegion": S.INDIRIZZO["provincia"],
            "postalCode": S.INDIRIZZO["cap"],
            "addressCountry": "IT",
        },
    }
    if completo:
        n.update({
            "description": q("Studio di tecnici competenti in acustica: valutazioni di impatto e clima acustico, "
                             "requisiti acustici passivi, collaudi, perizie fonometriche e misure del rumore "
                             "nei luoghi di lavoro."),
            "slogan": S.SLOGAN,
            "geo": {"@type": "GeoCoordinates", "latitude": S.SEDE_LAT, "longitude": S.SEDE_LON},
            "areaServed": [
                {"@type": "AdministrativeArea", "name": "Città metropolitana di Bari"},
                {"@type": "AdministrativeArea", "name": "Provincia di Barletta-Andria-Trani"},
                {"@type": "AdministrativeArea", "name": "Provincia di Brindisi"},
                {"@type": "AdministrativeArea", "name": "Provincia di Foggia"},
                {"@type": "AdministrativeArea", "name": "Provincia di Lecce"},
                {"@type": "AdministrativeArea", "name": "Provincia di Taranto"},
                {"@type": "Country", "name": "Italia"},
            ],
            "contactPoint": [
                {"@type": "ContactPoint", "telephone": t["numero"], "name": t["nome"],
                 "contactType": "customer service", "areaServed": "IT", "availableLanguage": "Italian"}
                for t in S.TELEFONI],
            "sameAs": [u for u in S.SOCIAL.values() if u],
            "knowsAbout": ["acustica ambientale", "impatto acustico", "clima acustico", "requisiti acustici passivi",
                           "collaudo acustico", "perizie fonometriche", "rumore nei luoghi di lavoro",
                           "bonifica acustica", "acustica previsionale"],
            "employee": [{"@id": f"{S.DOMINIO}/#{x['id']}"} for x in S.PROFESSIONISTI],
        })
        if S.PARTITA_IVA:
            n["vatID"] = "IT" + S.PARTITA_IVA
    return n


def nodi_persone():
    nodi = []
    for x in S.PROFESSIONISTI:
        n = {
            "@type": "Person",
            "@id": f"{S.DOMINIO}/#{x['id']}",
            "name": x["nome_semplice"],
            "honorificPrefix": x["prefisso"],
            "jobTitle": "Tecnico competente in acustica",
            "worksFor": {"@id": S.DOMINIO + "/#studio"},
            "hasCredential": {
                "@type": "EducationalOccupationalCredential",
                "credentialCategory": "Iscrizione all’elenco nazionale dei tecnici competenti in acustica (ENTECA)",
                "name": f"ENTECA n. {x['enteca']}",
            },
        }
        if x["foto"]:
            n["image"] = f"{S.DOMINIO}/{x['foto']}"
        if x["linkedin"]:
            n["sameAs"] = [x["linkedin"]]
        if x["id"] == "emanuele-sozzi":
            n["alumniOf"] = {"@type": "CollegeOrUniversity", "name": "Università del Salento"}
            n["memberOf"] = {"@type": "Organization", "name": "Ordine degli Ingegneri della Provincia di Brindisi"}
            n["knowsAbout"] = ["acustica", "vibrazioni"]
        nodi.append(n)
    return nodi


# ---------------------------------------------------------------- impaginazione

MENU = [("servizi", "Servizi", "servizi/"), ("per", "Per chi", "per/"), ("guide", "Guide", "guide/"),
        ("chi-siamo", "Chi siamo", "chi-siamo.html"), ("contatti", "Contatti", "contatti.html")]


def _analitica():
    return f"""<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('consent', 'default', {{ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'denied'}});
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={S.GA4}"></script>
<script>
gtag('js', new Date());
gtag('config', '{S.GA4}');
gtag('config', '{S.ADS}');
</script>"""


def _immagine_og(p):
    nome = f"assets/og/{p.chiave_og}.png"
    if not (RADICE / nome).exists():
        nome = "assets/og/home.png"
    return S.DOMINIO + "/" + nome


def _testa(p):
    titolo, descr = esc(q(p.title)), esc(q(p.descrizione))
    grafo = [nodo_studio(p.studio_completo)] + p.schema
    if p.briciole:
        grafo.append(briciole_schema(p))
    dati = json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, separators=(",", ":"))
    dati = dati.replace("</", "<\\/")
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titolo}</title>
<meta name="description" content="{descr}">
<meta name="robots" content="{'index, follow' if p.indicizza else 'noindex, follow'}">
<link rel="canonical" href="{p.canonico}">
<meta name="theme-color" content="#071b36">
<meta property="og:type" content="{p.og_tipo}">
<meta property="og:site_name" content="{S.NOME}">
<meta property="og:locale" content="it_IT">
<meta property="og:title" content="{titolo}">
<meta property="og:description" content="{descr}">
<meta property="og:url" content="{p.canonico}">
<meta property="og:image" content="{_immagine_og(p)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="627">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{titolo}">
<meta name="twitter:description" content="{descr}">
<meta name="twitter:image" content="{_immagine_og(p)}">
<link rel="icon" type="image/png" href="{p.a('favicon.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p.a('style.css')}?v={versione('style.css')}">
{_analitica()}
<script type="application/ld+json">{dati}</script>"""


def _intestazione(p):
    voci = []
    for chiave, nome, url in MENU:
        corrente = ' aria-current="page"' if chiave == p.sezione else ""
        voci.append(f'<a href="{p.a(url)}"{corrente}>{nome}</a>')
    barra = '<div class="lettura" aria-hidden="true"><i></i></div>' if p.lettura else ""
    consulenza = "#contatti" if p.url == "" else p.a(contatti_url())
    return f"""<a class="skip-link" href="#contenuto">Vai al contenuto</a>
<header class="site-header">
<div class="container nav">
<a class="logo" href="{p.a('')}" aria-label="SozziSound, pagina iniziale"><span>Sozzi</span>Sound</a>
<button class="menu-button" type="button" aria-label="Apri il menu" aria-expanded="false" aria-controls="menu-principale"><span></span></button>
<nav class="menu" id="menu-principale" aria-label="Menu principale">
{"".join(voci)}
<a class="nav-cta" href="{consulenza}">Richiedi una consulenza</a>
</nav>
</div>
{barra}
</header>"""


def _pie(p):
    i = S.INDIRIZZO
    servizi = "".join(f'<li><a href="{p.a(u)}">{n}</a></li>' for n, u in PIEDE_SERVIZI)
    perchi = "".join(f'<li><a href="{p.a(u)}">{n}</a></li>' for n, u in PIEDE_PERCHI)
    telefoni = "".join(f'<li><a href="tel:{t["numero"]}">{t["mostra"]}</a><small>{t["nome"]}</small></li>' for t in S.TELEFONI)
    piva = f" · P. IVA {S.PARTITA_IVA}" if S.PARTITA_IVA else ""
    return f"""<footer class="site-footer">
<div class="bande" aria-hidden="true"></div>
<div class="container footer-grid">
<div class="footer-brand">
<a class="logo" href="{p.a('')}" aria-label="SozziSound, pagina iniziale"><span>Sozzi</span>Sound</a>
<p>{S.SLOGAN}</p>
{social_html()}
</div>
<nav aria-label="Servizi"><p class="footer-titolo">Servizi</p><ul>{servizi}<li><a href="{p.a('servizi/')}">Tutti i servizi →</a></li></ul></nav>
<nav aria-label="Per chi lavoriamo"><p class="footer-titolo">Per chi</p><ul>{perchi}</ul></nav>
<nav aria-label="Lo studio"><p class="footer-titolo">Studio</p><ul>
<li><a href="{p.a('chi-siamo.html')}">Chi siamo</a></li>
<li><a href="{p.a('guide/')}">Guide</a></li>
<li><a href="{p.a('quale-pratica-acustica.html')}">Che pratica mi serve?</a></li>
<li><a href="{p.a('faq.html')}">Domande frequenti</a></li>
<li><a href="{p.a('citta/')}">Dove operiamo</a></li>
<li><a href="{p.a('contatti.html')}">Contatti</a></li>
</ul></nav>
<div class="footer-contatti"><p class="footer-titolo">Contatti</p>
<address>{i["via"]}<br>{i["cap"]} {i["citta"]} ({i["provincia"]})</address>
<ul>{telefoni}<li><a href="mailto:{S.EMAIL}">{S.EMAIL}</a></li></ul>
</div>
</div>
<div class="container footer-bottom">
<p>© <span id="year">{S.AGGIORNATO[:4]}</span> {S.NOME}{piva} · Tecnici competenti in acustica</p>
<div><a href="{p.a('privacy.html')}">Privacy</a><a href="{p.a('cookie-policy.html')}">Cookie policy</a><a href="#" id="cookie-manage">Gestisci cookie</a></div>
</div>
</footer>"""


def _servizi_fissi(p):
    t = S.TELEFONI[0]
    return f"""<nav class="dock" aria-label="Contatti rapidi">
<a href="tel:{t["numero"]}">{ICONE["telefono"]}Chiama</a>
<a class="dock-wa" href="{whatsapp_url()}" target="_blank" rel="noopener">{ICONE["whatsapp"]}WhatsApp</a>
<button type="button" data-apri-risposte aria-expanded="false" aria-controls="risposte">{ICONE["onde"]}Cosa mi serve?</button>
</nav>
<div class="rapidi">
<button class="rapidi-domande" type="button" data-apri-risposte aria-expanded="false" aria-controls="risposte" aria-label="Che pratica mi serve? Apri il percorso guidato">{ICONE["onde"]}<span>Che pratica mi serve?</span></button>
<a class="rapidi-wa" href="{whatsapp_url()}" target="_blank" rel="noopener" aria-label="Scrivici su WhatsApp">{ICONE["whatsapp"]}</a>
</div>
<section class="risposte" id="risposte" aria-label="Percorso guidato e risposte rapide" hidden>
<div class="risposte-testa">
<h2>Che cosa ti serve?</h2>
<p>Rispondi a due o tre domande, oppure scrivi la tua. Sono risposte automatiche: niente di ciò che scegli o scrivi viene inviato.</p>
<button class="risposte-chiudi" type="button" aria-label="Chiudi il pannello">×</button>
</div>
<div class="risposte-flusso">
<div class="percorso percorso-compatto"><div class="percorso-testa"><span>Percorso guidato</span><span class="percorso-tappa">Domanda 1</span></div><div class="percorso-corpo" aria-live="polite"></div></div>
<div class="risposte-libere" aria-live="polite"></div>
</div>
<form class="risposte-form" autocomplete="off">
<label class="visually-hidden" for="r-domanda">La tua domanda</label>
<input type="text" id="r-domanda" placeholder="Oppure scrivi una domanda" maxlength="300">
<button type="submit">Chiedi</button>
</form>
</section>
<div id="cookie-banner" role="region" aria-label="Preferenze sui cookie" hidden>
<p>Usiamo cookie tecnici e, solo con il tuo consenso, cookie di analisi e marketing (Google Analytics, Google Ads). Dettagli nella <a href="{p.a('cookie-policy.html')}">cookie policy</a>.</p>
<div class="cookie-actions">
<button id="cookie-accept" type="button">Accetta</button>
<button id="cookie-reject" type="button">Rifiuta</button>
</div>
</div>"""


def impagina(p):
    attributi = f' data-radice="{p.radice}" data-dati="{versione("assets/dati.js")}"'
    corpo = tipo(f"""{_intestazione(p)}
<main id="contenuto"{' data-lettura' if p.lettura else ''}>
{p.corpo}
</main>
{_pie(p)}
{_servizi_fissi(p)}""")
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
<!-- Pagina generata da _src/build.py: le modifiche vanno fatte nei sorgenti in _src/ -->
{_testa(p)}
</head>
<body{attributi}>
{corpo}
<script src="{p.a('script.js')}?v={versione('script.js')}" defer></script>
</body>
</html>
"""

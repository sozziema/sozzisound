"""Genera il sito statico di SozziSound nella cartella principale del progetto.

Uso:  python _src/build.py

Non servono librerie esterne. I testi stanno in _src/contenuti/, i dati dello studio
in _src/sito.py, l'impaginazione in _src/motore.py.
"""

import json
import math
import re
import sys
import unicodedata
from pathlib import Path

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))

import sito as S                                    # noqa: E402
import motore as M                                  # noqa: E402
from motore import Pagina, ICONE, esc, piano, q, data_it   # noqa: E402
from contenuti import servizi as CS                 # noqa: E402
from contenuti import perchi as CP                  # noqa: E402
from contenuti import guide as CG                   # noqa: E402
from contenuti import citta as CC                   # noqa: E402
from contenuti import faq as CF                     # noqa: E402
from contenuti import percorso as CX                # noqa: E402

RADICE = M.RADICE
FRECCIA = '<span aria-hidden="true">→</span>'
STUDIO = {"@id": S.DOMINIO + "/#studio"}
AREA = {a[0]: a for a in CS.AREE}
ENTECA = " e ".join(f"n. {x['enteca']}" for x in S.PROFESSIONISTI)

PAGINE = []
AVVISI = []

M.PIEDE_SERVIZI = [(CS.SERVIZI[n - 1]["nome"], CS.SERVIZI[n - 1]["url"]) for n in CS.NEL_PIEDE]
M.PIEDE_PERCHI = [(x["nome"], x["url"]) for x in CP.PERCHI]
M.AREE_MODULO = [(a[0], a[2]) for a in CS.AREE] + [("altro", "Altro, o non so ancora")]


# ---------------------------------------------------------------- utilità

def bottone(p, testo, url, classe="button-primary"):
    return f'<a class="button {classe}" href="{p.a(url)}">{testo} {FRECCIA}</a>'


def prima_frase(testo, massimo=150):
    """Prima frase di un testo; ne aggiunge una seconda se resta spazio."""
    frasi = re.split(r"(?<=[.!?])\s+", piano(testo))
    scelta = frasi[0]
    if len(frasi) > 1 and len(scelta) + len(frasi[1]) + 1 <= massimo:
        scelta += " " + frasi[1]
    return scelta


def km(luogo):
    return int(round(M.distanza_km(luogo["lat"], luogo["lon"])))


def parole_chiave(*testi):
    """Parole normalizzate (minuscole, senza accenti) per il pannello Risposte rapide."""
    t = unicodedata.normalize("NFD", " ".join(testi).lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    viste, elenco = set(), []
    for parola in re.sub(r"[^a-z0-9]+", " ", t).split():
        if len(parola) > 2 and parola not in viste:
            viste.add(parola)
            elenco.append(parola)
    return elenco


def minuti_lettura(*testi):
    parole = sum(len(piano(t).split()) for t in testi)
    return max(2, int(math.ceil(parole / 210)))


def risposta_faq(p, v):
    collegamento = f'<p><a href="{p.a(v["u"])}">{v["e"]} {FRECCIA}</a></p>' if v.get("u") else ""
    return v["a"] + collegamento


def faq_pagina(p, voci):
    return [(v["q"], risposta_faq(p, v)) for v in voci]


def faq_schema(voci):
    return M.domande_schema([(v["q"], v["a"]) for v in voci])


def scheda_servizio(s, etichetta="Vai al servizio"):
    return {"piccolo": f"Servizio {s['n']:02d}", "titolo": s["nome"], "testo": s["breve"],
            "url": s["url"], "etichetta": etichetta}


def scheda_guida(g):
    return {"piccolo": f"Guida · {g['minuti']} min", "titolo": g["titolo"], "testo": prima_frase(g["sommario"]),
            "url": g["url"], "etichetta": "Leggi la guida"}


def scheda_perchi(x):
    return {"piccolo": "Per chi", "titolo": x["nome"], "testo": x["breve"], "url": x["url"], "etichetta": "Apri la pagina"}


def cartiglio(testa, numero, righe):
    corpo = "".join(f"<div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in righe)
    return (f'<div class="cartiglio"><div class="cartiglio-testa"><span>{testa}</span><span>{numero}</span></div>'
            f"<dl>{corpo}</dl></div>")


def fascia(titolo, contenuto, sotto="", pale=False, ident=""):
    return f"""<section class="fascia{' fascia-pale' if pale else ''}"{f' id="{ident}"' if ident else ''}>
<div class="container">
<div class="fascia-titolo"><h2>{titolo}</h2>{f'<p>{sotto}</p>' if sotto else ''}</div>
{contenuto}
</div>
</section>"""


def aggiungi(p):
    PAGINE.append(p)
    return p


def servizio(slug_servizio, da):
    if slug_servizio not in CS.PER_SLUG:
        AVVISI.append(f"servizio inesistente «{slug_servizio}» citato in {da}")
        return None
    return CS.PER_SLUG[slug_servizio]


def guida(slug_guida, da):
    if slug_guida not in CG.PER_SLUG:
        AVVISI.append(f"guida inesistente «{slug_guida}» citata in {da}")
        return None
    return CG.PER_SLUG[slug_guida]


def perchi(slug_perchi, da):
    if slug_perchi not in CP.PER_SLUG:
        AVVISI.append(f"pagina «per chi» inesistente «{slug_perchi}» citata in {da}")
        return None
    return CP.PER_SLUG[slug_perchi]


for _g in CG.GUIDE:
    _g["minuti"] = minuti_lettura(_g["corpo"], " ".join(_g["sintesi"]))


# ---------------------------------------------------------------- percorso guidato

PAGINA_PERCORSO = "quale-pratica-acustica.html"


def percorso_html(p):
    """Primo passo del percorso, già scritto nella pagina: funziona come elenco di collegamenti
    anche senza JavaScript. I passi successivi li disegna script.js con gli stessi elementi."""
    primo = CX.DOMANDE[CX.INIZIO]
    opzioni = "".join(
        f'<li><a href="{p.a(PAGINA_PERCORSO)}#{dopo}" data-vai="{dopo}" data-breve="{esc(breve)}">{testo}</a></li>'
        for testo, dopo, breve in primo["opzioni"])
    return f"""<div class="percorso" data-percorso>
<div class="percorso-testa"><span>Percorso guidato</span><span class="percorso-tappa">Domanda 1</span></div>
<div class="percorso-corpo" aria-live="polite">
<p class="percorso-domanda" tabindex="-1">{primo["domanda"]}</p>
<ul class="percorso-opzioni">{opzioni}</ul>
</div>
</div>"""


def esito_percorso(ident):
    """Dati di un esito, con la pratica collegata già risolta."""
    e = CX.ESITI[ident]
    if e.get("servizio"):
        s = servizio(e["servizio"], f"percorso «{ident}»")
        destinazione = ({"nome": s["nome"], "url": s["url"], "area": s["area"], "etichetta": "Scheda del servizio"}
                        if s else None)
    else:
        x = perchi(e.get("pagina", ""), f"percorso «{ident}»")
        destinazione = ({"nome": x["nome"], "url": x["url"], "area": x["area"], "etichetta": "Apri la pagina"}
                        if x else None)
    if not destinazione:
        return None
    g = guida(e["guida"], f"percorso «{ident}»") if e.get("guida") else None
    return {"titolo": e.get("titolo") or destinazione["nome"], "testo": e["testo"], "norme": e.get("norme", []),
            "guida": g, "cta": e.get("cta", "Richiedi il preventivo"), **destinazione}


def percorsi_possibili(passo, cammino=()):
    """Tutte le strade che da un passo portano a un esito: [(etichette scelte, esito)]."""
    if passo in CX.ESITI:
        return [(cammino, passo)]
    strade = []
    for testo, dopo, _breve in CX.DOMANDE[passo]["opzioni"]:
        strade += percorsi_possibili(dopo, cammino + (testo,))
    return strade


def dati_percorso():
    domande = {}
    for ident, d in CX.DOMANDE.items():
        voce = {"d": M.tipo(d["domanda"]), "o": [[M.tipo(t), dopo, q(breve)] for t, dopo, breve in d["opzioni"]]}
        if d.get("nota"):
            voce["n"] = M.tipo(d["nota"])
        domande[ident] = voce
    esiti = {}
    for ident in CX.ESITI:
        e = esito_percorso(ident)
        if not e:
            continue
        voce = {"t": M.tipo(e["titolo"]), "h": M.tipo(e["testo"]), "u": e["url"], "e": e["etichetta"],
                "a": e["area"], "r": q(e["nome"]), "c": e["cta"]}
        if e["norme"]:
            voce["n"] = [M.tipo(n) for n in e["norme"]]
        if e["guida"]:
            voce["g"] = {"t": q(e["guida"]["titolo"]), "u": e["guida"]["url"]}
        esiti[ident] = voce
    return {"inizio": CX.INIZIO, "domande": domande, "esiti": esiti}


def controlla_percorso():
    raggiunti = set()

    def visita(passo):
        if passo in raggiunti:
            return
        raggiunti.add(passo)
        if passo in CX.DOMANDE:
            for _t, dopo, _b in CX.DOMANDE[passo]["opzioni"]:
                if dopo not in CX.DOMANDE and dopo not in CX.ESITI:
                    AVVISI.append(f"percorso: «{passo}» rimanda a un passo inesistente «{dopo}»")
                else:
                    visita(dopo)

    visita(CX.INIZIO)
    for ident in list(CX.DOMANDE) + list(CX.ESITI):
        if ident not in raggiunti:
            AVVISI.append(f"percorso: «{ident}» non è raggiungibile da nessuna risposta")
    for ident in set(CX.DOMANDE) & set(CX.ESITI):
        AVVISI.append(f"percorso: «{ident}» è sia una domanda sia un esito")


def pagina_percorso():
    p = Pagina(
        url=PAGINA_PERCORSO,
        title="Quale pratica acustica ti serve? Tre domande | SozziSound",
        descrizione="Rispondi a due o tre domande a scelta multipla e scopri quale documentazione acustica riguarda "
                    "il tuo caso, che cosa dice la norma e come chiedere il preventivo.",
        briciole=[("Che pratica mi serve?", PAGINA_PERCORSO)],
        og_occhiello="Percorso guidato", og_titolo="Che pratica <em>ti serve?</em>",
    )
    gruppi = []
    for testo, dopo, _breve in CX.DOMANDE[CX.INIZIO]["opzioni"]:
        righe = []
        for cammino, ident in percorsi_possibili(dopo):
            e = esito_percorso(ident)
            if e:
                se = " › ".join(cammino)
                righe.append(f'<li>{se}: <a href="{p.a(e["url"])}">{e["titolo"]}</a></li>')
        gruppi.append(f'<details class="domanda" id="{dopo}"><summary>{testo}</summary>'
                      f'<div class="risposta"><ul class="percorso-elenco">{"".join(righe)}</ul></div></details>')
    p.corpo = f"""{M.testata(p, "Percorso guidato", "Che pratica<br><em>ti serve?</em>",
        "Due o tre domande a scelta multipla. Alla fine trovi la pratica che riguarda il tuo caso, che cosa dice la norma in breve e il modo per chiedere il preventivo.")}
<section class="corpo">
<div class="container stretto">
{percorso_html(p)}
<p class="nota-guida">Le indicazioni sono generali e non sostituiscono la valutazione del caso specifico: quali documenti servano davvero dipende dall'attività, dal procedimento e dal regolamento del Comune. Niente di ciò che scegli viene inviato.</p>
</div>
</section>
<section class="fascia fascia-pale">
<div class="container stretto">
<div class="fascia-titolo"><h2>Tutti i percorsi, in chiaro</h2><p>Le stesse strade, da leggere invece che da percorrere.</p></div>
<div class="domande">{"".join(gruppi)}</div>
</div>
</section>
{M.cta_band(p, titolo="Preferisci <em>parlarne?</em>", testo="Raccontaci il caso con parole tue: ti diciamo noi quale pratica serve e prepariamo un preventivo gratuito.")}"""
    p.schema = [{"@type": "WebPage", "@id": p.canonico + "#pagina", "url": p.canonico, "name": q(p.title),
                 "description": q(p.descrizione), "about": STUDIO, "inLanguage": "it-IT"}]
    return aggiungi(p)


# ---------------------------------------------------------------- home

def professionisti_home():
    pezzi = []
    for x in S.PROFESSIONISTI:
        if x["foto"]:
            volto = (f'<img class="profile-photo" src="{x["foto"]}" width="128" height="128" loading="lazy" '
                     f'alt="{esc(x["nome"])}">')
        else:
            volto = f'<div class="initials" aria-hidden="true">{x["iniziali"]}</div>'
        linkedin = (f'<a class="linkedin-link" href="{x["linkedin"]}" target="_blank" rel="noopener">Profilo LinkedIn ↗</a>'
                    if x["linkedin"] else "")
        pezzi.append(f"""<article class="professional">{volto}<div><h3>{x["nome"]}</h3><p>{x["breve"]}</p>
<p class="registration-note">Tecnico competente in acustica · ENTECA n. {x["enteca"]}</p>{linkedin}</div></article>""")
    return '<div class="professionals">' + "".join(pezzi) + "</div>"


def dettagli_contatto(p):
    i = S.INDIRIZZO
    telefoni = "".join(f'<a href="tel:{t["numero"]}"><small>{t["nome"]}</small>{t["mostra"]}</a>' for t in S.TELEFONI)
    return f"""<div class="contact-details">
{telefoni}
<a href="mailto:{S.EMAIL}"><small>Email</small>{S.EMAIL}</a>
<a href="{M.whatsapp_url()}" target="_blank" rel="noopener"><small>WhatsApp</small>Scrivici su WhatsApp</a>
<span>{i["via"]} · {i["cap"]} {i["citta"]} ({i["provincia"]})</span>
<span>Puglia · Incarichi in tutta Italia</span>
</div>
<div class="seguici"><span>Seguici</span>{M.social_html()}</div>"""


def pagina_home():
    p = Pagina(
        url="",
        title="SozziSound | Tecnici competenti in acustica in Puglia e in Italia",
        descrizione="Tecnici competenti in acustica a Ostuni, in Puglia e in Italia: impatto e clima acustico, "
                    "requisiti passivi, collaudi, perizie fonometriche. Preventivo gratuito.",
        studio_completo=True,
        og_occhiello="Tecnici competenti in acustica",
        og_titolo="Misurazioni e valutazioni <em>per la conformità acustica.</em>",
    )
    comuni_mappa = [c for c in CC.COMUNI if c["nome"] != "Ostuni"]
    province = "".join(f'<a href="{x["url"]}">{x["nome"]}</a>' for x in CC.PROVINCE)

    schede = "".join(
        f'<article class="service-card"><span class="number">{s["n"]:02d}</span><h3>{s["nome"]}</h3><p>{s["breve"]}</p>'
        f'<a class="service-link" href="{s["url"]}">Approfondisci {FRECCIA}</a></article>'
        for s in (CS.SERVIZI[n - 1] for n in CS.IN_HOME))

    interlocutori = "".join(
        f'<li><a href="{x["url"]}"><strong>{x["nome"]}</strong><small>{x["breve"]}</small><i aria-hidden="true">→</i></a></li>'
        for x in CP.PERCHI)

    guide_home = "".join(
        f'<article class="guide-card"><small>Guida · {g["minuti"]} min</small><h3>{g["titolo"]}</h3>'
        f'<p>{prima_frase(g["sommario"])}</p><a href="{g["url"]}">Leggi la guida {FRECCIA}</a></article>'
        for g in (CG.PER_SLUG[s] for s in CG.IN_HOME))

    domande = [CF.PER_ID[i] for i in CF.IN_HOME]

    p.corpo = f"""<section class="hero">
<div class="container hero-grid">
<div class="hero-copy">
<p class="eyebrow">Tecnici competenti in acustica</p>
<h1>Misurazioni e valutazioni<br><em>per la conformità acustica.</em></h1>
<p class="hero-text">Consulenze, valutazioni e relazioni tecniche per imprese, professionisti e privati. Rilievi affidabili e soluzioni documentate in base alla normativa applicabile.</p>
<p class="location-note">Ostuni · Puglia · Incarichi in tutta Italia</p>
<div class="hero-actions">
<a class="button button-primary" href="#contatti">Richiedi un preventivo gratuito {FRECCIA}</a>
<a class="text-link" href="#orientati">Che pratica mi serve?</a>
</div>
<div class="hero-numbers">
<div><strong>ENTECA {ENTECA}</strong><span>iscritti all'elenco nazionale</span></div>
<div><strong>Fonometro di classe 1</strong><span>tarato e certificato</span></div>
<div><strong>Relazioni</strong><span>tecniche e documentate</span></div>
</div>
</div>
<div class="hero-image">
<img src="assets/hero-fonometro.jpg" width="1200" height="800" alt="Fonometro di classe 1 durante una rilevazione acustica in ambiente urbano" fetchpriority="high">
<p class="image-caption"><span></span> Rilevazione strumentale del rumore</p>
</div>
</div>
</section>

<section class="intro section">
<div class="container intro-grid">
<p class="eyebrow">Ascoltare, analizzare, intervenire</p>
<h2>Conformità normativa,<br><em>rigore strumentale.</em></h2>
<p>Ogni incarico viene inquadrato rispetto alle norme applicabili e supportato da dati misurati. L'obiettivo è fornire una base tecnica solida per autorizzazioni, progettazione e gestione delle criticità acustiche.</p>
</div>
</section>

<section class="orienta section" id="orientati">
<div class="container orienta-grid">
<div>
<p class="eyebrow">Orientati</p>
<h2>Che pratica<br><em>ti serve?</em></h2>
<p>Rispondi a due o tre domande a scelta multipla. Ti diciamo quale documentazione riguarda il tuo caso e che cosa dice la norma, in breve. Poi, se vuoi, chiedi il preventivo.</p>
<p class="orienta-nota">Sono indicazioni generali: il caso concreto lo verifichiamo insieme.</p>
</div>
{percorso_html(p)}
</div>
</section>

<section class="local-area section" id="dove-operiamo">
<div class="container local-grid">
<div>
<p class="eyebrow">Dove operiamo</p>
<h2>Consulenza acustica<br><em>in Puglia e nel resto d'Italia.</em></h2>
<p>SozziSound ha sede a Ostuni e lavora in tutte e sei le province pugliesi. Su incarico affianchiamo aziende, professionisti e privati nel resto d'Italia.</p>
<p>Per valutazioni di impatto e clima acustico, bonifiche, requisiti acustici passivi, perizie e rumore nei luoghi di lavoro definiamo un percorso tecnico coerente con il contesto e con la normativa applicabile.</p>
<p class="city-links">{province}</p>
<a class="text-link" href="citta/">Tutte le zone e i comuni</a>
</div>
<div>
{M.mappa(p, CC.PROVINCE, comuni_mappa)}
</div>
</div>
</section>

<section class="services section" id="servizi">
<div class="container">
<div class="section-heading"><div><p class="eyebrow">Competenze</p><h2>Servizi di acustica<br><em>specialistica.</em></h2></div><p>Supporto tecnico dalla valutazione iniziale alla definizione dell'intervento, con un approccio chiaro e documentato.</p></div>
<div class="service-grid">{schede}</div>
<div class="services-more"><p>E poi locali con musica, deroghe per eventi, impianti sportivi, pratiche edilizie, impianti tecnici, energie rinnovabili, supporto agli enti pubblici.</p><a class="text-link" href="servizi/">Tutti i {len(CS.SERVIZI)} servizi</a></div>
</div>
</section>

<section class="perchi section" id="per-chi">
<div class="container perchi-grid">
<div>
<p class="eyebrow">Per chi lavoriamo</p>
<h2>Ogni interlocutore<br><em>ha la sua domanda.</em></h2>
<p>Un progettista, un gestore di locale e un condomino non chiedono la stessa cosa, anche quando il rumore è lo stesso. Per ciascuno abbiamo raccolto le situazioni più frequenti e i servizi che le risolvono.</p>
</div>
<ul class="perchi-lista">{interlocutori}</ul>
</div>
</section>

<section class="method section" id="metodo">
<div class="container method-grid">
<div><p class="eyebrow">Il metodo SozziSound</p><h2>Analisi del problema,<br><em>rilevazione fonometrica e relazione tecnica.</em></h2></div>
<ol class="steps">
<li><span>01</span><div><h3>Inquadramento dell'incarico</h3><p>Definiamo obiettivi, contesto e riferimenti normativi applicabili al servizio richiesto.</p></div></li>
<li><span>02</span><div><h3>Rilievi strumentali</h3><p>Effettuiamo le rilevazioni con fonometro di classe 1, tarato e certificato, secondo le procedure tecniche pertinenti.</p></div></li>
<li><span>03</span><div><h3>Relazione tecnica</h3><p>Elaboriamo i risultati e predisponiamo la relazione tecnica, con le eventuali indicazioni di intervento.</p></div></li>
<li><span>04</span><div><h3>Dopo la consegna</h3><p>Se l'ente chiede chiarimenti sui contenuti tecnici della relazione, rispondiamo noi.</p></div></li>
</ol>
</div>
</section>

<section class="about section" id="chi-siamo">
<div class="container about-grid">
<div class="about-panel" aria-hidden="true"><p>COMPETENZA<br>TECNICA</p><div class="panel-line"></div><span>SOZZISOUND<br>ACUSTICA</span></div>
<div>
<p class="eyebrow">I professionisti</p>
<h2>Competenze complementari<br>per una consulenza <em>completa.</em></h2>
<p>SozziSound riunisce esperienza scientifica, tecnica e progettuale per affrontare con precisione le esigenze di valutazione e controllo del rumore.</p>
{professionisti_home()}
<div class="about-actions"><a class="button button-dark" href="chi-siamo.html">Chi siamo {FRECCIA}</a><a class="text-link" href="#contatti">Contattaci</a></div>
</div>
</div>
</section>

<section class="guide-home section" id="guide">
<div class="container">
<div class="section-heading"><div><p class="eyebrow">Guide</p><h2>Le norme,<br><em>spiegate con calma.</em></h2></div><p>Articoli brevi su obblighi, limiti e procedure, con i riferimenti di legge citati per esteso.</p></div>
<div class="guide-cards">{guide_home}</div>
<p class="guide-home-more"><a class="text-link" href="guide/">Tutte le guide</a></p>
</div>
</section>

<section class="faq section" id="faq">
<div class="container">
<div class="faq-head"><div><p class="eyebrow">Domande frequenti</p><h2>Acustica: alcuni chiarimenti<br><em>prima di iniziare.</em></h2></div><p>Risposte generali alle domande che arrivano più spesso. Per il tuo caso specifico ci sentiamo: il primo confronto serve a questo.</p></div>
{M.domande_html(faq_pagina(p, domande), due_colonne=True)}
<p class="faq-more"><a class="text-link" href="faq.html">Tutte le domande frequenti</a></p>
</div>
</section>

<section class="contact section" id="contatti">
<div class="container contact-grid">
<div>
<p class="eyebrow">Contatti</p>
<h2>Parliamo del tuo <em>progetto.</em></h2>
<p>Descrivi in breve la tua necessità. Ti diciamo quale documentazione serve davvero e prepariamo un preventivo gratuito.</p>
{dettagli_contatto(p)}
</div>
{M.modulo_html(p)}
</div>
</section>"""

    p.schema = [
        {"@type": "WebSite", "@id": S.DOMINIO + "/#sito", "url": S.DOMINIO + "/", "name": S.NOME,
         "inLanguage": "it-IT", "publisher": STUDIO},
        *M.nodi_persone(),
        faq_schema(domande),
    ]
    return aggiungi(p)


# ---------------------------------------------------------------- servizi

def pagina_servizio(s):
    area = AREA[s["area"]]
    p = Pagina(
        url=s["url"], title=s["title"], descrizione=s["descrizione"], sezione="servizi",
        briciole=[("Servizi", "servizi/"), (s["nome"], s["url"])],
        og_occhiello=f"Servizio {s['n']:02d} · {area[1]}", og_titolo=s["h1"],
    )
    azioni = (bottone(p, "Richiedi un preventivo", M.contatti_url(s["area"], s["nome"]))
              + '<a class="text-link" href="#come-si-svolge">Come si svolge</a>')
    consegne = "".join(f"<li>{x}</li>" for x in s["consegniamo"])
    passi = "".join(f"<li><strong>{t}</strong><span>{d}</span></li>" for t, d in s["passi"])
    norme = "".join(f'<li class="rif">{n}</li>' for n in s["norme"])
    scheda = cartiglio("Scheda servizio", f"N. {s['n']:02d} / {len(CS.SERVIZI)}", [
        ("Servizio", s["nome"]),
        ("Area", f'<a href="{p.a("servizi/")}#{s["area"]}">{area[1]}</a>'),
        ("Norme", f"<ul>{norme}</ul>"),
        ("Consegna", s["consegna"]),
        ("Dove", "Puglia e, su incarico, resto d'Italia"),
        ("Preventivo", "Gratuito"),
    ])

    correlati = [x for x in (servizio(c, s["url"]) for c in s["correlati"]) if x]
    utili = [scheda_guida(g) for g in (guida(c, s["url"]) for c in s["guide"]) if g][:2]
    utili += [scheda_perchi(x) for x in (perchi(c, s["url"]) for c in s["perchi"]) if x]
    utili = utili[:3]

    p.corpo = f"""{M.testata(p, f"Servizio {s['n']:02d} · {area[1]}", s["h1"], s["sommario"], azioni)}
<section class="corpo">
<div class="container colonne">
<article class="prosa">
<h2 id="a-chi-serve">A chi serve</h2>
{s["a_chi"]}
<h2 id="quando">Quando è richiesta</h2>
{s["quando"]}
<h2 id="cosa-consegniamo">Che cosa consegniamo</h2>
<ul class="consegne">{consegne}</ul>
<h2 id="come-si-svolge">Come si svolge</h2>
<ol class="passi">{passi}</ol>
</article>
<aside>
{scheda}
{M.scheda_cta(p, "Parliamone prima di iniziare", "Raccontaci il caso: ti diciamo che cosa serve davvero e quanto lavoro richiede.", s["area"], s["nome"])}
</aside>
</div>
</section>
{fascia("Domande frequenti", M.domande_html(s["faq"], due_colonne=len(s["faq"]) > 3), pale=True, ident="domande")}
{fascia("Servizi collegati", M.schede_link(p, [scheda_servizio(x) for x in correlati]))}
{fascia("Per approfondire", M.schede_link(p, utili), pale=True) if utili else ""}
{M.cta_band(p, s["area"], s["nome"])}"""

    p.schema = [
        {"@type": "Service", "@id": p.canonico + "#servizio", "name": M.schema_testo(s["h1"]).rstrip("."),
         "serviceType": s["nome"], "description": q(s["descrizione"]), "url": p.canonico, "provider": STUDIO,
         "areaServed": [{"@type": "AdministrativeArea", "name": "Puglia"}, {"@type": "Country", "name": "Italia"}]},
        M.domande_schema(s["faq"]),
    ]
    return aggiungi(p)


def voce_indice(p, numero, titolo, url, nota="", descrizione=""):
    sotto = f'<span class="indice-desc">{descrizione}</span>' if descrizione else ""
    return (f'<li><a href="{p.a(url)}"><span class="indice-num">{numero}</span><span class="indice-titolo">{titolo}</span>'
            f'<span class="indice-punti"></span><span class="indice-nota">{nota}</span>{sotto}</a></li>')


def pagina_indice_servizi():
    p = Pagina(
        url="servizi/",
        title="Servizi di acustica in Puglia: tutti i 20 servizi | SozziSound",
        descrizione="Tutti i servizi di SozziSound: impatto e clima acustico, locali ed eventi, edilizia, "
                    "rumore di impianti e attività, perizie, luoghi di lavoro, enti pubblici.",
        sezione="servizi", briciole=[("Servizi", "servizi/")],
        og_occhiello="Servizi", og_titolo="Venti servizi, <em>sei aree di lavoro.</em>",
    )
    gruppi = []
    for chiave, nome, _voce, descrizione in CS.AREE:
        voci = "".join(voce_indice(p, f"{s['n']:02d}", s["nome"], s["url"], s["norme"][0], s["breve"])
                       for s in CS.SERVIZI if s["area"] == chiave)
        gruppi.append(f'<div class="gruppo-indice" id="{chiave}"><h2>{nome}</h2><p>{descrizione}</p>'
                      f'<ul class="indice">{voci}</ul></div>')
    salti = "".join(f'<a href="#{a[0]}">{a[1]}</a>' for a in CS.AREE)
    p.corpo = f"""{M.testata(p, "Servizi", "Venti servizi,<br><em>sei aree di lavoro.</em>",
        "Dalla pratica per aprire un'attività alla perizia per una causa: ogni servizio ha la sua pagina, con le norme di riferimento, che cosa consegniamo e come si svolge.",
        extra=f'<p class="city-links">{salti}</p>')}
<section class="corpo">
<div class="container">
{"".join(gruppi)}
</div>
</section>
{M.cta_band(p, titolo="Non sai quale <em>ti serve?</em>", testo="Capita spesso: l'ente chiede «una relazione acustica» senza altre indicazioni. Mandaci la richiesta così com'è, ti diciamo noi di che cosa si tratta.")}"""
    p.schema = [{"@type": "ItemList", "name": "Servizi di acustica", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": s["nome"], "url": S.DOMINIO + "/" + s["url"]}
        for i, s in enumerate(CS.SERVIZI, start=1)]}]
    return aggiungi(p)


# ---------------------------------------------------------------- per chi

def pagina_perchi(x):
    p = Pagina(
        url=x["url"], title=x["title"], descrizione=x["descrizione"], sezione="per",
        briciole=[("Per chi", "per/"), (x["nome"], x["url"])],
        og_occhiello="Per chi lavoriamo", og_titolo=x["h1"],
    )
    azioni = (bottone(p, "Richiedi un preventivo", M.contatti_url(x["area"], x["nome"]))
              + '<a class="text-link" href="#servizi">I servizi di riferimento</a>')
    situazioni = "".join(f"<li><strong>{t}</strong><span>{d}</span></li>" for t, d in x["situazioni"])
    schede = []
    for slug_servizio, frase in x["servizi"]:
        s = servizio(slug_servizio, x["url"])
        if s:
            schede.append({"piccolo": f"Servizio {s['n']:02d}", "titolo": s["nome"], "testo": frase,
                           "url": s["url"], "etichetta": "Vai al servizio"})
    altri = "".join(f'<li><a href="{p.a(y["url"])}">{y["nome"]}</a></li>' for y in CP.PERCHI if y is not x)
    guide_utili = [scheda_guida(g) for g in (guida(c, x["url"]) for c in x["guide"]) if g][:3]

    p.corpo = f"""{M.testata(p, "Per chi lavoriamo", x["h1"], x["sommario"], azioni)}
<section class="corpo">
<div class="container colonne">
<article class="prosa">
<h2 id="situazioni">Le situazioni più frequenti</h2>
<ol class="passi">{situazioni}</ol>
<h2 id="metodo">{x["metodo_titolo"]}</h2>
{x["metodo"]}
</article>
<aside>
{M.scheda_cta(p, "Parliamone", "Bastano poche righe o una telefonata per capire che cosa serve davvero.", x["area"], x["nome"])}
<nav class="indice-guida" aria-label="Altri interlocutori"><p>Lavoriamo anche con</p><ol>{altri}</ol></nav>
</aside>
</div>
</section>
{fascia("I servizi di riferimento", M.schede_link(p, schede, due=len(schede) in (1, 2, 4)), pale=True, ident="servizi")}
{fascia("Domande frequenti", M.domande_html(x["faq"], due_colonne=len(x["faq"]) > 3), ident="domande")}
{fascia("Guide utili", M.schede_link(p, guide_utili, due=len(guide_utili) == 2), pale=True) if guide_utili else ""}
{M.cta_band(p, x["area"], x["nome"])}"""
    p.schema = [
        {"@type": "WebPage", "@id": p.canonico + "#pagina", "url": p.canonico, "name": q(x["title"]),
         "description": q(x["descrizione"]), "about": STUDIO, "inLanguage": "it-IT"},
        M.domande_schema(x["faq"]),
    ]
    return aggiungi(p)


def pagina_indice_perchi():
    p = Pagina(
        url="per/",
        title="Per chi lavoriamo: la consulenza acustica su misura | SozziSound",
        descrizione="Consulenza acustica per progettisti, locali ed eventi, aziende, RSPP, studi legali, privati "
                    "e condomìni, impianti sportivi, enti pubblici. Trova la tua pagina.",
        sezione="per", briciole=[("Per chi", "per/")],
        og_occhiello="Per chi lavoriamo", og_titolo="Lo stesso rumore, <em>domande diverse.</em>",
    )
    voci = "".join(voce_indice(p, f"{i:02d}", x["nome"], x["url"], "", x["breve"])
                   for i, x in enumerate(CP.PERCHI, start=1))
    p.corpo = f"""{M.testata(p, "Per chi lavoriamo", "Lo stesso rumore,<br><em>domande diverse.</em>",
        "Chi progetta vuole una relazione da allegare, chi gestisce un locale vuole lavorare tranquillo, chi abita accanto vuole dormire. Scegli la pagina che parla la tua lingua.")}
<section class="corpo">
<div class="container">
<ul class="indice">{voci}</ul>
</div>
</section>
{M.cta_band(p)}"""
    p.schema = [{"@type": "ItemList", "name": "Per chi lavoriamo", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": x["nome"], "url": S.DOMINIO + "/" + x["url"]}
        for i, x in enumerate(CP.PERCHI, start=1)]}]
    return aggiungi(p)


# ---------------------------------------------------------------- guide

def pagina_guida(g):
    p = Pagina(
        url=g["url"], title=g["title"], descrizione=g["descrizione"], sezione="guide",
        briciole=[("Guide", "guide/"), (g["titolo"], g["url"])],
        og_occhiello="Guida", og_titolo=g["h1"], og_tipo="article", lettura=True, aggiornato=g["data"],
    )
    indice = []

    def con_ancora(m):
        ancora = M.slug(m.group(1))
        indice.append((ancora, m.group(1)))
        return f'<h2 id="{ancora}">{m.group(1)}</h2>'

    corpo = re.sub(r"<h2>(.*?)</h2>", con_ancora, g["corpo"])
    sommario = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in indice)
    sintesi = "".join(f"<li>{x}</li>" for x in g["sintesi"])
    norme = "".join(f'<li><span class="norma">{n}</span></li>' for n in g["norme"])
    meta = (f'<p class="guida-meta"><span>Aggiornata il {data_it(g["data"])}</span>'
            f'<span>Lettura: {g["minuti"]} minuti</span><span>A cura di SozziSound</span></p>')
    servizi_utili = [scheda_servizio(s) for s in (servizio(c, g["url"]) for c in g["servizi"]) if s][:3]
    altre = [scheda_guida(x) for x in (guida(c, g["url"]) for c in g["guide"]) if x][:2]

    p.corpo = f"""{M.testata(p, "Guida", g["h1"], g["sommario"], extra=meta)}
<section class="corpo">
<div class="container colonne guida">
<article class="prosa">
<div class="sintesi"><p class="etichetta">In sintesi</p><ul>{sintesi}</ul></div>
{corpo}
<div class="riferimenti"><h2>Riferimenti normativi</h2><ul>{norme}</ul></div>
<p class="nota-guida">Contenuto informativo: non sostituisce una valutazione del caso specifico. Le norme vanno sempre lette nel testo vigente e insieme ai regolamenti del Comune interessato. Ultimo aggiornamento: {data_it(g["data"])}.</p>
<p class="segui-guida"><a href="{S.SOCIAL["linkedin"]}" target="_blank" rel="noopener">Segui SozziSound su LinkedIn</a> per i prossimi approfondimenti.</p>
</article>
<aside>
<nav class="indice-guida" aria-label="Indice della guida"><p>In questa guida</p><ol>{sommario}</ol></nav>
{M.scheda_cta(p, "Hai un caso concreto?", "La guida spiega la regola. Per applicarla alla tua situazione ci sentiamo.", "", g["titolo"], "Scrivi la tua richiesta")}
</aside>
</div>
</section>
{fascia("Servizi collegati", M.schede_link(p, servizi_utili), pale=True)}
{fascia("Continua a leggere", M.schede_link(p, altre, due=True), sotto=f'<a class="text-link" href="{p.a("guide/")}">Tutte le guide</a>')}
{M.cta_band(p, "", g["titolo"])}"""
    p.schema = [{
        "@type": "Article", "@id": p.canonico + "#articolo", "headline": q(g["titolo"]),
        "description": q(g["descrizione"]), "datePublished": g["data"], "dateModified": g["data"],
        "inLanguage": "it-IT", "author": STUDIO, "publisher": STUDIO,
        "mainEntityOfPage": p.canonico, "image": M._immagine_og(p),
    }]
    return aggiungi(p)


def pagina_indice_guide():
    p = Pagina(
        url="guide/",
        title="Guide di acustica: norme, limiti e procedure | SozziSound",
        descrizione="Guide pratiche di acustica: impatto e clima acustico, ENTECA, L.R. Puglia 3/2002, requisiti "
                    "passivi, musica nei locali, rumore del vicino, luoghi di lavoro.",
        sezione="guide", briciole=[("Guide", "guide/")],
        og_occhiello="Guide", og_titolo="Le norme, <em>spiegate con calma.</em>",
    )
    voci = "".join(voce_indice(p, f"{i:02d}", g["titolo"], g["url"], f"{g['minuti']} min", prima_frase(g["sommario"], 170))
                   for i, g in enumerate(CG.GUIDE, start=1))
    p.corpo = f"""{M.testata(p, "Guide", "Le norme,<br><em>spiegate con calma.</em>",
        "Articoli brevi su obblighi, limiti e procedure dell'acustica, scritti per chi deve prendere una decisione. Ogni guida cita le norme per esteso e riporta la data dell'ultimo aggiornamento.")}
<section class="corpo">
<div class="container">
<ul class="indice">{voci}</ul>
<p class="nota-guida">Le guide hanno scopo informativo e non sostituiscono la valutazione del caso specifico. <a class="text-link" href="{S.SOCIAL["linkedin"]}" target="_blank" rel="noopener">Segui SozziSound su LinkedIn</a> per i prossimi approfondimenti.</p>
</div>
</section>
{M.cta_band(p)}"""
    p.schema = [{"@type": "ItemList", "name": "Guide di acustica", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": q(g["titolo"]), "url": S.DOMINIO + "/" + g["url"]}
        for i, g in enumerate(CG.GUIDE, start=1)]}]
    return aggiungi(p)


# ---------------------------------------------------------------- città

def casi_html(p, casi, da):
    righe = []
    for titolo, testo, slug_servizio in casi:
        s = servizio(slug_servizio, da)
        coll = f' <a href="{p.a(s["url"])}">{s["nome"]}</a>' if s else ""
        righe.append(f"<li><strong>{titolo}</strong><span>{testo}{coll}</span></li>")
    return '<ol class="passi">' + "".join(righe) + "</ol>"


def elenco_comuni(p, comuni, classe="elenco-comuni"):
    voci = "".join(
        f'<li><a href="{p.a(c["url"])}">{c["nome"]}<small>{"sede" if c["nome"] == "Ostuni" else f"{km(c)} km"}</small></a></li>'
        for c in comuni)
    return f'<ul class="{classe}">{voci}</ul>'


def elenco_servizi(p):
    voci = "".join(f'<li><a href="{p.a(s["url"])}">{s["nome"]}<small>{s["n"]:02d}</small></a></li>' for s in CS.SERVIZI)
    return f'<ul class="elenco-comuni">{voci}</ul>'


LIMITI = """<p>Dipende dalla zona e dagli atti del Comune. Prima di ogni incarico verifichiamo se esiste un piano di classificazione acustica, che cosa prevede per l'area interessata e che cosa dicono i regolamenti comunali su orari, attività temporanee e deroghe. Dove il piano manca si applicano i limiti transitori previsti dalla normativa nazionale.</p>
<p>La classe del sito e la fonte da cui l'abbiamo ricavata sono indicate all'inizio di ogni nostra relazione.</p>"""


def pagina_comune(c):
    prov = CC.PROVINCIA[c["prov"]]
    sede = c["nome"] == "Ostuni"
    p = Pagina(
        url=c["url"], title=c["title"], descrizione=c["descrizione"],
        briciole=[("Dove operiamo", "citta/"), (prov["nome"], prov["url"]), (c["nome"], c["url"])],
        og_occhiello=f"Dove operiamo · {CC.NOME_PROVINCIA[c['prov']]}",
        og_titolo=f"Tecnico competente in acustica <em>{c['dove']}</em>",
    )
    azioni = (bottone(p, "Richiedi un preventivo", M.contatti_url("", f"Intervento {c['dove']}"))
              + '<a class="text-link" href="#richieste">Le richieste più tipiche</a>')
    distanza = "" if sede else f" {c['nome']} dista circa {km(c)} km in linea d'aria dalla sede di Ostuni."
    vicini = sorted((x for x in CC.COMUNI if x is not c),
                    key=lambda x: (x["lat"] - c["lat"]) ** 2 + ((x["lon"] - c["lon"]) * 0.76) ** 2)[:6]
    scheda = cartiglio("Scheda territorio", f"{CC.COMUNI.index(c) + 1:02d} / {len(CC.COMUNI)}", [
        ("Comune", c["nome"]),
        ("Provincia", f'<a href="{p.a(prov["url"])}">{CC.NOME_PROVINCIA[c["prov"]]}</a>'),
        ("Distanza", "Sede dello studio" if sede else f"circa {km(c)} km dalla sede, in linea d'aria"),
        ("Firma", f"Tecnici competenti in acustica, ENTECA {ENTECA}"),
        ("Preventivo", "Gratuito"),
    ])
    p.corpo = f"""{M.testata(p, f"Dove operiamo · {CC.NOME_PROVINCIA[c['prov']]}", f"Tecnico competente in acustica <em>{c['dove']}</em>", c["sommario"], azioni)}
<section class="corpo">
<div class="container colonne">
<article class="prosa">
<h2 id="contesto">Il contesto</h2>
{c["contesto"]}
<h2 id="richieste">Le richieste più tipiche</h2>
{casi_html(p, c["casi"], c["url"])}
<h2 id="limiti">Quali limiti valgono {c["dove"]}</h2>
{LIMITI}
<h2 id="come">Come ci muoviamo</h2>
<p>{c["arrivo"]}{distanza} Le misure si fanno quando il rumore c'è: di giorno, di sera o di notte, nei feriali e nei festivi.</p>
<p>Il preventivo è gratuito. Per prepararlo bastano l'indirizzo, due righe sull'attività o sull'immobile e, se c'è, la richiesta dell'ente.</p>
</article>
<aside>
{scheda}
{M.scheda_cta(p, f"Un caso {c['dove']}?", "Raccontacelo in breve: ti diciamo che cosa serve davvero.", "", f"Intervento {c['dove']}")}
</aside>
</div>
</section>
{fascia("Comuni vicini", elenco_comuni(p, vicini), sotto=f'<a class="text-link" href="{p.a("citta/")}">Tutte le zone</a>', pale=True)}
{fascia("Tutti i servizi", elenco_servizi(p), sotto=f"Disponibili {c['dove']} e in tutta la provincia.")}
{M.cta_band(p, "", f"Intervento {c['dove']}")}"""
    p.schema = [{
        "@type": "Service", "@id": p.canonico + "#servizio", "name": f"Consulenza acustica {c['dove']}",
        "serviceType": "Tecnico competente in acustica", "description": q(c["descrizione"]), "url": p.canonico,
        "provider": STUDIO,
        "areaServed": {"@type": "City", "name": c["nome"],
                       "containedInPlace": {"@type": "AdministrativeArea", "name": CC.NOME_PROVINCIA[c["prov"]]}},
    }]
    return aggiungi(p)


def pagina_provincia(x):
    p = Pagina(
        url=x["url"], title=x["title"], descrizione=x["descrizione"],
        briciole=[("Dove operiamo", "citta/"), (x["nome"], x["url"])],
        og_occhiello="Dove operiamo", og_titolo=f"Tecnico competente in acustica <em>{x['dove']}</em>",
    )
    comuni = [c for c in CC.COMUNI if c["prov"] == x["chiave"]]
    azioni = (bottone(p, "Richiedi un preventivo", M.contatti_url("", f"Intervento {x['dove']}"))
              + '<a class="text-link" href="#richieste">Le richieste più tipiche</a>')
    altre = "".join(f'<a href="{p.a(y["url"])}">{y["nome"]}</a>' for y in CC.PROVINCE if y is not x)
    righe = [
        ("Territorio", CC.NOME_PROVINCIA[x["chiave"]]),
        ("Distanza", f"{x['nome'] if x['chiave'] != 'bat' else 'Il centro della provincia'} dista circa {km(x)} km dalla sede di Ostuni, in linea d'aria"),
    ]
    if comuni:
        righe.append(("Comuni", "<ul>" + "".join(f'<li><a href="{p.a(c["url"])}">{c["nome"]}</a></li>' for c in comuni) + "</ul>"))
    righe += [("Firma", f"Tecnici competenti in acustica, ENTECA {ENTECA}"), ("Preventivo", "Gratuito")]
    blocco_comuni = (fascia(f"I comuni che seguiamo più da vicino", elenco_comuni(p, comuni),
                            sotto="Ogni comune ha una pagina con il suo contesto e le richieste più tipiche.", pale=True)
                     if comuni else "")
    p.corpo = f"""{M.testata(p, "Dove operiamo", f"Tecnico competente in acustica <em>{x['dove']}</em>", x["sommario"], azioni)}
<section class="corpo">
<div class="container colonne">
<article class="prosa">
<h2 id="contesto">Acustica: {x["area"]}</h2>
{x["contesto"]}
<h2 id="richieste">Le richieste più tipiche</h2>
{casi_html(p, x["casi"], x["url"])}
<h2 id="limiti">Quali limiti valgono</h2>
{LIMITI}
<h2 id="come">Come ci muoviamo</h2>
<p>{x["arrivo"]} Le misure si fanno quando il rumore c'è: di giorno, di sera o di notte, nei feriali e nei festivi.</p>
<p>Il preventivo è gratuito. Per prepararlo bastano l'indirizzo, due righe sull'attività o sull'immobile e, se c'è, la richiesta dell'ente.</p>
</article>
<aside>
{cartiglio("Scheda territorio", x["nome_mappa"], righe)}
{M.scheda_cta(p, f"Un caso {x['dove']}?", "Raccontacelo in breve: ti diciamo che cosa serve davvero.", "", f"Intervento {x['dove']}")}
</aside>
</div>
</section>
{blocco_comuni}
{fascia("Tutti i servizi", elenco_servizi(p), sotto=f"Disponibili {x['dove']} e in tutta la provincia.", pale=not comuni)}
<section class="fascia{' fascia-pale' if comuni else ''}"><div class="container"><div class="fascia-titolo"><h2>Le altre province</h2><a class="text-link" href="{p.a("citta/")}">Tutte le zone</a></div><p class="city-links">{altre}</p></div></section>
{M.cta_band(p, "", f"Intervento {x['dove']}")}"""
    p.schema = [{
        "@type": "Service", "@id": p.canonico + "#servizio", "name": f"Consulenza acustica {x['dove']}",
        "serviceType": "Tecnico competente in acustica", "description": q(x["descrizione"]), "url": p.canonico,
        "provider": STUDIO, "areaServed": {"@type": "AdministrativeArea", "name": CC.NOME_PROVINCIA[x["chiave"]]},
    }]
    return aggiungi(p)


def pagina_indice_citta():
    p = Pagina(
        url="citta/",
        title="Dove operiamo: tecnici in acustica in Puglia | SozziSound",
        descrizione="Sede a Ostuni, incarichi in tutta la Puglia e in Italia. Le pagine delle sei province e dei "
                    "comuni più vicini: Fasano, Monopoli, Martina Franca, Gallipoli e altri.",
        briciole=[("Dove operiamo", "citta/")],
        og_occhiello="Dove operiamo", og_titolo="Da Ostuni, <em>in tutta la Puglia.</em>",
    )
    comuni_mappa = [c for c in CC.COMUNI if c["nome"] != "Ostuni"]
    province = "".join(voce_indice(p, f"{i:02d}", x["nome"], x["url"], f"{km(x)} km")
                       for i, x in enumerate(CC.PROVINCE, start=1))
    per_distanza = sorted(CC.COMUNI, key=km)
    p.corpo = f"""{M.testata(p, "Dove operiamo", "Da Ostuni,<br><em>in tutta la Puglia.</em>",
        "La sede è a Ostuni, in provincia di Brindisi. Lavoriamo in tutte e sei le province pugliesi e, su incarico, nel resto d'Italia: l'iscrizione all'elenco dei tecnici competenti in acustica è nazionale.")}
<section class="corpo">
<div class="container citta-indice">
<div>
{M.mappa(p, CC.PROVINCE, comuni_mappa, "Schema delle distanze in linea d'aria dalla sede di Ostuni. I punti piccoli sono i comuni con una pagina dedicata.")}
</div>
<div>
<div class="gruppo-indice"><h2>Le sei province</h2><p>Distanza del capoluogo dalla sede, in linea d'aria.</p><ul class="indice">{province}</ul></div>
<div class="gruppo-indice"><h2>I comuni più vicini</h2><p>Per ciascuno, il contesto e le richieste più tipiche.</p>{elenco_comuni(p, per_distanza, "elenco-comuni due")}</div>
</div>
</div>
</section>
{M.cta_band(p, titolo="Il tuo comune <em>non è in elenco?</em>", testo="Non cambia nulla: lavoriamo in tutta la regione e, su incarico, nel resto d'Italia. Scrivici dove si trova l'intervento.")}"""
    p.schema = [{"@type": "ItemList", "name": "Zone in cui operiamo", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": x["nome"], "url": S.DOMINIO + "/" + x["url"]}
        for i, x in enumerate(CC.PROVINCE + CC.COMUNI, start=1)]}]
    return aggiungi(p)


# ---------------------------------------------------------------- pagine singole

def pagina_faq():
    p = Pagina(
        url="faq.html",
        title="Domande frequenti sull'acustica | SozziSound",
        descrizione="Le risposte alle domande più comuni: quando serve l'impatto acustico, chi può firmare, quanto "
                    "costa, quanto tempo serve, che cosa fornire per un preventivo.",
        briciole=[("Domande frequenti", "faq.html")],
        og_occhiello="Domande frequenti", og_titolo="Le domande <em>che arrivano più spesso.</em>",
    )
    gruppi = []
    tutte = []
    for chiave, nome, descrizione in CF.GRUPPI:
        voci = [v for v in CF.FAQ if v["gruppo"] == chiave]
        tutte += voci
        gruppi.append(f'<div class="gruppo-indice" id="{chiave}"><h2>{nome}</h2><p>{descrizione}</p>'
                      f'{M.domande_html(faq_pagina(p, voci))}</div>')
    salti = "".join(f'<a href="#{g[0]}">{g[1]}</a>' for g in CF.GRUPPI)
    p.corpo = f"""{M.testata(p, "Domande frequenti", "Le domande<br><em>che arrivano più spesso.</em>",
        "Risposte generali, scritte per orientarsi. Ogni caso ha i suoi dettagli: per il tuo ci sentiamo, e il preventivo è gratuito.",
        extra=f'<p class="city-links">{salti}</p>')}
<section class="corpo">
<div class="container stretto">
{"".join(gruppi)}
</div>
</section>
{M.cta_band(p, titolo="La tua domanda <em>non c'è?</em>", testo="Scrivila così com'è, anche in due righe. Rispondiamo di persona.")}"""
    p.schema = [faq_schema(tutte)]
    return aggiungi(p)


def pagina_chi_siamo():
    p = Pagina(
        url="chi-siamo.html",
        title="Chi siamo: i tecnici competenti in acustica | SozziSound",
        descrizione="Lo studio di due tecnici competenti in acustica iscritti a ENTECA: l'Ing. Emanuele Sozzi "
                    "e il Prof. Vincenzo Sozzi. Sede a Ostuni, incarichi in tutta Italia.",
        sezione="chi-siamo", briciole=[("Chi siamo", "chi-siamo.html")],
        og_occhiello="Lo studio", og_titolo="Un fisico e un ingegnere, <em>lo stesso metodo.</em>",
    )
    e, v = S.PROFESSIONISTI
    te, tv = S.TELEFONI

    def volto(x):
        if x["foto"]:
            return f'<img src="{x["foto"]}" width="184" height="184" loading="lazy" alt="{esc(x["nome"])}">'
        return f'<div class="initials" aria-hidden="true">{x["iniziali"]}</div>'

    p.corpo = f"""{M.testata(p, "Lo studio", "Un fisico e un ingegnere,<br><em>lo stesso metodo.</em>",
        "SozziSound è uno studio di consulenza acustica con sede a Ostuni. Ci lavorano due tecnici competenti in acustica, con una formazione in fisica e in ingegneria: misuriamo il rumore, lo confrontiamo con le norme e mettiamo per iscritto che cosa fare.")}
<section class="corpo">
<div class="container">
<div class="chi-griglia">
<article class="persona">
<div class="persona-testa">{volto(e)}<div><h2>{e["nome"]}</h2><p class="persona-ruolo">Tecnico competente in acustica</p></div></div>
<p>Ingegnere aerospaziale, con laurea magistrale all'Università del Salento e un interesse specifico per acustica e vibrazioni.</p>
<dl>
<div><dt>Elenco nazionale</dt><dd>ENTECA n. {e["enteca"]}</dd></div>
<div><dt>Formazione</dt><dd>Laurea magistrale in ingegneria aerospaziale, Università del Salento</dd></div>
<div><dt>Albo</dt><dd>Ordine degli Ingegneri della Provincia di Brindisi, sezione A, settore industriale</dd></div>
<div><dt>Telefono</dt><dd><a href="tel:{te["numero"]}">{te["mostra"]}</a></dd></div>
<div><dt>LinkedIn</dt><dd><a href="{e["linkedin"]}" target="_blank" rel="noopener">Profilo personale ↗</a></dd></div>
</dl>
</article>
<article class="persona">
<div class="persona-testa">{volto(v)}<div><h2>{v["nome"]}</h2><p class="persona-ruolo">Tecnico competente in acustica</p></div></div>
<p>Fisico, con oltre 30 anni di esperienza nel settore acustico.</p>
<dl>
<div><dt>Elenco nazionale</dt><dd>ENTECA n. {v["enteca"]}</dd></div>
<div><dt>Professione</dt><dd>Fisico</dd></div>
<div><dt>Esperienza</dt><dd>Oltre 30 anni nel settore acustico</dd></div>
<div><dt>Telefono</dt><dd><a href="tel:{tv["numero"]}">{tv["mostra"]}</a></dd></div>
</dl>
</article>
</div>
</div>
</section>
<section class="fascia fascia-pale">
<div class="container">
<div class="fascia-titolo"><h2>Abilitazioni, strumenti, territorio</h2><p>Quello che puoi verificare prima di affidarci un incarico.</p></div>
<div class="tre-blocchi">
<div><h3>Abilitazioni</h3><ul>
<li>Iscrizione all'elenco nazionale dei tecnici competenti in acustica (ENTECA): {ENTECA}.</li>
<li>Iscrizione all'Ordine degli Ingegneri della Provincia di Brindisi (Ing. Emanuele Sozzi).</li>
</ul><p><a class="text-link" href="{p.a("guide/tecnico-competente-in-acustica-enteca.html")}">Che cos'è l'elenco ENTECA</a></p></div>
<div><h3>Strumentazione</h3><ul>
<li>Fonometro di classe 1, tarato e certificato.</li>
<li>Software di modellazione previsionale.</li>
</ul><p>Gli estremi dei certificati di taratura sono riportati in ogni rapporto di misura.</p></div>
<div><h3>Dove lavoriamo</h3><ul>
<li>Sede a Ostuni, in provincia di Brindisi.</li>
<li>Tutte e sei le province pugliesi.</li>
<li>Su incarico, il resto d'Italia.</li>
</ul><p><a class="text-link" href="{p.a("citta/")}">Le zone in cui operiamo</a></p></div>
</div>
</div>
</section>
<section class="corpo">
<div class="container colonne">
<article class="prosa">
<h2 id="come-lavoriamo">Come lavoriamo</h2>
<p>Ogni incarico segue gli stessi cinque passaggi, che si tratti di una pratica per un bar o di una perizia per una causa.</p>
<ol class="passi">
<li><strong>Primo confronto</strong><span>Ci racconti il caso, per telefono o per iscritto. Capiamo che cosa ti è stato chiesto, da chi, e quale documentazione serve davvero. Poi prepariamo il preventivo, che è gratuito.</span></li>
<li><strong>Sopralluogo preliminare</strong><span>Vediamo il luogo, le sorgenti e chi ci abita o lavora intorno. Da qui dipendono i punti e gli orari di misura.</span></li>
<li><strong>Rilievi strumentali</strong><span>Misuriamo con fonometro di classe 1, tarato e certificato, secondo le tecniche del DM 16/03/1998 o delle norme pertinenti al caso.</span></li>
<li><strong>Elaborazione e relazione</strong><span>Confrontiamo i dati con i limiti applicabili e scriviamo la relazione: metodo, risultati, conclusioni e, se servono, gli interventi da prevedere.</span></li>
<li><strong>Consegna e assistenza</strong><span>Ti spieghiamo i risultati in parole semplici. Se l'ente chiede chiarimenti sui contenuti tecnici, rispondiamo noi.</span></li>
</ol>
<h2 id="seguici">Dove seguirci</h2>
<p>Pubblichiamo aggiornamenti normativi e nuove guide sulla <a href="{S.SOCIAL["linkedin"]}" target="_blank" rel="noopener">pagina LinkedIn di SozziSound</a> e su <a href="{S.SOCIAL["instagram"]}" target="_blank" rel="noopener">Instagram</a>.</p>
</article>
<aside>
{M.scheda_cta(p, "Vuoi parlarne con noi?", "Una telefonata basta per capire se e come possiamo esserti utili.")}
</aside>
</div>
</section>
{M.cta_band(p)}"""
    p.schema = [
        {"@type": "AboutPage", "@id": p.canonico + "#pagina", "url": p.canonico, "name": q(p.title),
         "about": STUDIO, "inLanguage": "it-IT"},
        *M.nodi_persone(),
    ]
    p.studio_completo = True
    return aggiungi(p)


def pagina_contatti():
    p = Pagina(
        url="contatti.html",
        title="Contatti e preventivo gratuito | SozziSound",
        descrizione="Contatta SozziSound: telefono, WhatsApp, email o modulo. Raccontaci il caso, ti diciamo quale "
                    "documentazione acustica serve e prepariamo un preventivo gratuito.",
        sezione="contatti", briciole=[("Contatti", "contatti.html")],
        og_occhiello="Contatti", og_titolo="Parliamo del tuo <em>caso.</em>",
    )
    p.corpo = f"""{M.testata(p, "Contatti", "Parliamo del tuo <em>caso.</em>",
        "Scrivici, chiamaci o mandaci un messaggio su WhatsApp. Ti diciamo quale documentazione serve davvero e prepariamo un preventivo gratuito.")}
<section class="contatti-pagina">
<div class="container contact-grid">
<div>
<p class="eyebrow">Contatti diretti</p>
{dettagli_contatto(p)}
<div class="elenco-serve"><p>Per un preventivo ci aiuta sapere</p><ul>
<li>Indirizzo e Comune dell'intervento.</li>
<li>Che attività o immobile riguarda.</li>
<li>Che cosa ti è stato richiesto, e da chi.</li>
<li>Se c'è, una planimetria: va bene anche una bozza.</li>
<li>Orari dell'attività ed elenco degli impianti.</li>
</ul></div>
</div>
{M.modulo_html(p)}
</div>
</section>"""
    p.schema = [{"@type": "ContactPage", "@id": p.canonico + "#pagina", "url": p.canonico, "name": q(p.title),
                 "about": STUDIO, "inLanguage": "it-IT"}]
    p.studio_completo = True
    return aggiungi(p)


def traccia_404():
    punti = []
    for i in range(0, 146):
        x = i * 8
        ampiezza = 30 * max(0.0, 1 - x / 660) ** 1.6
        y = 40 - ampiezza * math.sin(x / 9.5) * math.cos(x / 31)
        punti.append(f"{x},{round(y, 1)}")
    return "M" + " L".join(punti)


def pagina_404():
    p = Pagina(
        url="404.html", title="Pagina non trovata | SozziSound",
        descrizione="La pagina che cerchi non esiste o è stata spostata.",
        indicizza=False, assoluta=True,
    )
    p.corpo = f"""<section class="errore-pagina">
<div class="container">
<p class="eyebrow">Errore 404</p>
<svg class="errore-traccia" viewBox="0 0 1160 80" preserveAspectRatio="none" aria-hidden="true"><path d="{traccia_404()}"/></svg>
<h1>Qui non arriva<br><em>nessun segnale.</em></h1>
<p>La pagina che cerchi non esiste o è stata spostata. Da qui puoi ripartire dai servizi, dalle guide o scriverci direttamente.</p>
<div class="errore-link">
<a class="button button-primary" href="{p.a("")}">Torna alla home {FRECCIA}</a>
<a class="button button-line" href="{p.a("servizi/")}">Servizi</a>
<a class="button button-line" href="{p.a("guide/")}">Guide</a>
<a class="button button-line" href="{p.a("contatti.html")}">Contatti</a>
</div>
</div>
</section>"""
    return aggiungi(p)


def pagina_privacy():
    p = Pagina(
        url="privacy.html", title="Informativa sulla privacy | SozziSound",
        descrizione="Informativa sul trattamento dei dati personali di chi visita il sito sozzisound.it e di chi ci contatta.",
        briciole=[("Privacy", "privacy.html")], indicizza=False,
    )
    i = S.INDIRIZZO
    if S.MODULO_ENDPOINT:
        modulo = """<p>I dati che inserisci nel modulo (nome, email, telefono se indicato, tipo di richiesta, Comune e messaggio) vengono trasmessi a un servizio ospitato sull'account Google Workspace dello studio, che li recapita alla casella di posta del titolare. Google Ireland Limited tratta questi dati come responsabile del trattamento, nell'ambito dei servizi Google Workspace.</p>
<p>In alternativa puoi inviare la stessa richiesta dalla tua app di posta o su WhatsApp: in quel caso i dati viaggiano attraverso il servizio che scegli.</p>"""
    else:
        modulo = """<p>Il modulo non invia dati a un server del sito. Con «Invia richiesta» si apre la tua app di posta con il messaggio già compilato, e sei tu a spedirlo alla casella del titolare; con «Invia su WhatsApp» lo stesso testo si apre in una chat. I dati (nome, email, telefono se indicato, tipo di richiesta, Comune e messaggio) arrivano quindi direttamente al titolare attraverso il servizio che scegli.</p>"""
    p.corpo = f"""{M.testata(p, "Informativa", "Informativa sulla <em>privacy</em>",
        "Informativa resa ai sensi degli articoli 13 e 14 del Regolamento (UE) 2016/679 (GDPR) a chi visita il sito sozzisound.it e a chi ci contatta.")}
<section class="corpo">
<div class="container">
<article class="prosa">
<h2>Titolare del trattamento</h2>
<p>Il titolare del trattamento è SozziSound, {i["via"]}, {i["cap"]} {i["citta"]} ({i["provincia"]}), contattabile all'indirizzo <a href="mailto:{S.EMAIL}">{S.EMAIL}</a>.</p>
<h2>Dati che ci invii con il modulo di contatto</h2>
{modulo}
<p>Usiamo questi dati solo per rispondere alla tua richiesta e preparare il preventivo.</p>
<h2>Telefono, email e WhatsApp</h2>
<p>Se ci chiami, ci scrivi un'email o un messaggio su WhatsApp, trattiamo i dati che ci comunichi per risponderti. Le conversazioni su WhatsApp avvengono sulla piattaforma di WhatsApp Ireland Limited, secondo le sue condizioni.</p>
<h2>Percorso guidato e risposte rapide</h2>
<p>Il percorso guidato «Che pratica mi serve?» e le risposte rapide funzionano interamente nel tuo browser: le scelte che fai e le domande che scrivi non vengono inviate né conservate. Se hai dato il consenso ai cookie di analisi, registriamo soltanto a quale risultato sei arrivato o quale risposta è stata aperta, mai il testo che hai digitato.</p>
<p>Se alla fine del percorso scegli di chiedere il preventivo, il riepilogo delle tue scelte viene riportato nel modulo di contatto, dove puoi leggerlo prima di inviare.</p>
<h2>Dati di navigazione e cookie</h2>
<p>Il sito usa Google Analytics e Google Ads per raccogliere dati statistici e di conversione in forma aggregata. Si attivano solo con il tuo consenso, espresso dall'avviso sui cookie, secondo le impostazioni di Google Consent Mode. Il dettaglio è nella <a href="{p.a("cookie-policy.html")}">cookie policy</a>.</p>
<p>I caratteri tipografici sono caricati dai server di Google Fonts: per scaricarli il tuo browser comunica a Google l'indirizzo IP.</p>
<h2>Finalità e base giuridica</h2>
<p>Trattiamo i dati per rispondere alle richieste ricevute (misure precontrattuali e contrattuali, art. 6, par. 1, lett. b del GDPR) e, solo con il tuo consenso, per finalità statistiche e di marketing (art. 6, par. 1, lett. a).</p>
<h2>Conservazione</h2>
<p>Conserviamo i dati delle richieste per il tempo necessario a gestirle e ad adempiere agli obblighi contrattuali o di legge che ne derivano. I dati di analisi e pubblicità sono conservati secondo i periodi previsti dagli strumenti di Google; il consenso si può revocare in ogni momento.</p>
<h2>I tuoi diritti</h2>
<p>Puoi chiedere in qualsiasi momento l'accesso ai tuoi dati, la rettifica, la cancellazione, la limitazione del trattamento, oppure opporti, scrivendo a <a href="mailto:{S.EMAIL}">{S.EMAIL}</a>. Puoi inoltre proporre reclamo al Garante per la protezione dei dati personali.</p>
<p class="nota-guida">Ultimo aggiornamento: {data_it(S.AGGIORNATO)}.</p>
</article>
</div>
</section>"""
    return aggiungi(p)


def pagina_cookie():
    p = Pagina(
        url="cookie-policy.html", title="Cookie policy | SozziSound",
        descrizione="Quali cookie usa il sito sozzisound.it e come cambiare le proprie preferenze.",
        briciole=[("Cookie policy", "cookie-policy.html")], indicizza=False,
    )
    p.corpo = f"""{M.testata(p, "Informativa", "Cookie <em>policy</em>",
        "Quali cookie usa sozzisound.it e come cambiare le tue preferenze in qualsiasi momento.")}
<section class="corpo">
<div class="container">
<article class="prosa">
<h2>Che cosa sono i cookie</h2>
<p>I cookie sono piccoli file di testo che i siti visitati inviano al dispositivo dell'utente, dove vengono memorizzati per essere ritrasmessi agli stessi siti alla visita successiva.</p>
<h2>Strumenti tecnici</h2>
<p>Il sito ricorda la scelta che esprimi nell'avviso sui cookie salvandola nella memoria locale del browser. È un dato tecnico, necessario al funzionamento: non richiede consenso e non viene comunicato a terzi.</p>
<h2>Cookie di analisi e marketing</h2>
<p>Con il tuo consenso il sito attiva:</p>
<ul>
<li><strong>Google Analytics (GA4)</strong>: raccoglie dati statistici aggregati sulla navigazione, per capire come viene usato il sito e migliorarlo.</li>
<li><strong>Google Ads</strong>: misura l'efficacia delle campagne pubblicitarie e i contatti generati dal sito.</li>
</ul>
<p>Entrambi i servizi sono forniti da Google Ireland Limited e gestiti tramite Google Consent Mode: restano disattivati finché non esprimi il consenso.</p>
<h2>Come cambiare le preferenze</h2>
<p>Puoi modificare la tua scelta in qualsiasi momento con il collegamento «Gestisci cookie» in fondo a ogni pagina, oppure dalle impostazioni del browser, dove puoi bloccare o eliminare i cookie già salvati.</p>
<p>Per tutto il resto vale l'<a href="{p.a("privacy.html")}">informativa sulla privacy</a>.</p>
<p class="nota-guida">Ultimo aggiornamento: {data_it(S.AGGIORNATO)}.</p>
</article>
</div>
</section>"""
    return aggiungi(p)


# ---------------------------------------------------------------- file di servizio

def scrivi(percorso, testo):
    file = RADICE / percorso
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(testo, encoding="utf-8", newline="\n")


def sitemap():
    righe = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in PAGINE:
        if p.indicizza:
            righe.append(f"  <url><loc>{p.canonico}</loc><lastmod>{p.aggiornato}</lastmod></url>")
    righe.append("</urlset>")
    return "\n".join(righe) + "\n"


def risposte_rapide():
    voci = []
    for v in CF.FAQ:
        voce = {"id": v["id"], "q": q(v["q"]), "a": M.tipo(v["a"]), "k": parole_chiave(v["k"])}
        if v.get("f"):
            voce["f"] = parole_chiave(v["f"])
        for campo in ("u", "e", "c"):
            if v.get(campo):
                voce[campo] = q(v[campo]) if campo != "u" else v[campo]
        voci.append(voce)
    pagine = []
    for s in CS.SERVIZI:
        pagine.append({"t": s["nome"], "u": s["url"], "k": parole_chiave(s["nome"], s["chiavi"])})
    for g in CG.GUIDE:
        pagine.append({"t": "Guida: " + q(g["titolo"]), "u": g["url"], "k": parole_chiave(g["chiavi"])})
    for x in CP.PERCHI:
        pagine.append({"t": "Per " + x["nome"][0].lower() + x["nome"][1:], "u": x["url"],
                       "k": parole_chiave(x["nome"], x["chiavi"])})
    for c in CC.PROVINCE + CC.COMUNI:
        pagine.append({"t": f"Tecnico in acustica {c['dove']}", "u": c["url"], "k": parole_chiave(c["nome"])})
    pagine.append({"t": "Che pratica mi serve?", "u": PAGINA_PERCORSO,
                   "k": parole_chiave("percorso guidato pratica quale orientarsi scegliere capire")})
    oggetto = {"suggerite": CF.SUGGERITE, "voci": voci, "pagine": pagine, "percorso": dati_percorso()}
    testo = json.dumps(oggetto, ensure_ascii=False, separators=(",", ":"))
    return "window.SOZZI_DATI=" + testo.replace("</", "<\\/") + ";\n"


def manifest_og():
    voci = []
    for p in PAGINE:
        if p.og_titolo:
            voci.append({"chiave": p.chiave_og, "occhiello": p.og_occhiello,
                         "titolo": M.tipo(re.sub(r"<br\s*/?>", " ", p.og_titolo)), "seme": p.url})
    return json.dumps(voci, ensure_ascii=False, indent=1)


# ---------------------------------------------------------------- controlli

def controlla_testi():
    titoli, descrizioni = {}, {}
    for p in PAGINE:
        if len(p.title) > 65:
            AVVISI.append(f"titolo lungo ({len(p.title)}): {p.url or 'home'}")
        if p.indicizza and not 110 <= len(p.descrizione) <= 165:
            AVVISI.append(f"descrizione di {len(p.descrizione)} caratteri: {p.url or 'home'}")
        if p.title in titoli:
            AVVISI.append(f"titolo ripetuto: {p.url} e {titoli[p.title]}")
        if p.descrizione in descrizioni:
            AVVISI.append(f"descrizione ripetuta: {p.url} e {descrizioni[p.descrizione]}")
        titoli[p.title] = p.url
        descrizioni[p.descrizione] = p.url
        if len(re.findall(r"<h1[ >]", p.corpo)) != 1:
            AVVISI.append(f"la pagina deve avere un solo h1: {p.url or 'home'}")
    for v in CF.FAQ:
        if v.get("u"):
            destinazione = v["u"].split("#")[0]
            if destinazione.endswith("/"):
                destinazione += "index.html"
            if destinazione not in {p.file for p in PAGINE}:
                AVVISI.append(f"la risposta «{v['id']}» rimanda a una pagina inesistente: {v['u']}")
    for ident in CF.FORTI:
        if ident not in CF.PER_ID:
            AVVISI.append(f"faq.FORTI: voce inesistente «{ident}»")
    for elenco, nome in ((CF.IN_HOME, "IN_HOME"), (CF.SUGGERITE, "SUGGERITE")):
        for ident in elenco:
            if ident not in CF.PER_ID:
                AVVISI.append(f"faq.{nome}: voce inesistente «{ident}»")


def controlla_collegamenti():
    """Ogni collegamento interno delle pagine generate deve portare a un file esistente."""
    rotti = 0
    for p in PAGINE:
        testo = (RADICE / p.file).read_text(encoding="utf-8")
        base = (RADICE / p.file).parent
        for url in set(re.findall(r'(?:href|src)="([^"]+)"', testo)):
            if re.match(r"^(https?:|mailto:|tel:|#|data:)", url):
                continue
            percorso = url.split("#")[0].split("?")[0]
            if percorso in ("", "./"):
                continue
            destinazione = (RADICE / percorso.lstrip("/")) if percorso.startswith("/") else (base / percorso)
            if percorso.endswith("/"):
                destinazione = destinazione / "index.html"
            if not destinazione.resolve().exists():
                rotti += 1
                AVVISI.append(f"collegamento rotto in {p.file}: {url}")
            ancora = url.split("#")[1] if "#" in url else ""
            if ancora and destinazione.resolve().exists() and destinazione.suffix == ".html":
                if f'id="{ancora}"' not in destinazione.read_text(encoding="utf-8"):
                    AVVISI.append(f"ancora inesistente in {p.file}: {url}")
        for ancora in set(re.findall(r'href="#([^"]+)"', testo)):
            if f'id="{ancora}"' not in testo:
                AVVISI.append(f"ancora inesistente in {p.file}: #{ancora}")
    return rotti


# ---------------------------------------------------------------- esecuzione

def main():
    pagina_home()
    pagina_indice_servizi()
    for s in CS.SERVIZI:
        pagina_servizio(s)
    pagina_indice_perchi()
    for x in CP.PERCHI:
        pagina_perchi(x)
    pagina_indice_guide()
    for g in CG.GUIDE:
        pagina_guida(g)
    pagina_indice_citta()
    for x in CC.PROVINCE:
        pagina_provincia(x)
    for c in CC.COMUNI:
        pagina_comune(c)
    pagina_percorso()
    pagina_faq()
    pagina_chi_siamo()
    pagina_contatti()
    pagina_privacy()
    pagina_cookie()
    pagina_404()

    scrivi("assets/bande.svg", M.bande_svg())
    scrivi("assets/dati.js", risposte_rapide())
    for p in PAGINE:
        scrivi(p.file, M.impagina(p))
    scrivi("sitemap.xml", sitemap())
    scrivi("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {S.DOMINIO}/sitemap.xml\n")
    (QUI / "og").mkdir(exist_ok=True)
    (QUI / "og" / "manifest.json").write_text(manifest_og(), encoding="utf-8", newline="\n")

    controlla_testi()
    controlla_percorso()
    controlla_collegamenti()
    senza_anteprima = [p.chiave_og for p in PAGINE if p.og_titolo and not (RADICE / f"assets/og/{p.chiave_og}.png").exists()]

    print(f"Pagine generate: {len(PAGINE)} ({sum(1 for p in PAGINE if p.indicizza)} nella sitemap)")
    if senza_anteprima:
        print(f"Anteprime social mancanti: {len(senza_anteprima)}. Esegui  python _src/og.py  e poi di nuovo questo script.")
    if AVVISI:
        print(f"\nAvvisi ({len(AVVISI)}):")
        for a in AVVISI:
            print("  - " + a)
        return 1
    print("Nessun avviso.")
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    sys.exit(main())

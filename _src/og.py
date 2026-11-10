"""Genera le anteprime per i social (1200x627) in assets/og/.

Uso:  python _src/og.py           solo le anteprime mancanti o cambiate
      python _src/og.py --tutte   le rigenera tutte

Serve Google Chrome (o Edge) installato e la libreria Pillow. L'elenco delle anteprime
viene scritto da build.py in _src/og/manifest.json: eseguire prima build.py, poi questo
script, poi di nuovo build.py perché le pagine puntino alle nuove immagini.
"""

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI))

import motore as M  # noqa: E402

try:
    from PIL import Image
except ImportError:
    sys.exit("Manca la libreria Pillow: installarla con  pip install pillow")

DEST = M.RADICE / "assets" / "og"
MANIFEST = QUI / "og" / "manifest.json"
FATTE = QUI / "og" / "fatte.json"

BROWSER = [
    os.environ.get("CHROME", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]

MODELLO = """<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; }}
html, body {{ width: 1200px; height: 627px; overflow: hidden; }}
body {{ position: relative; padding: 64px 72px; color: #fff; font-family: "DM Sans", system-ui, sans-serif;
  background: radial-gradient(circle at 88% 12%, #12386b 0, #0b2a52 30%, #071b36 62%); }}
.logo {{ font: 700 44px "Playfair Display", Georgia, serif; letter-spacing: -.09em; }}
.logo span {{ color: #70b7ff; }}
.occhiello {{ margin-top: 78px; color: #70b7ff; font-size: 19px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }}
h1 {{ margin-top: 20px; max-width: 980px; font: 600 {corpo}px/1.08 "Playfair Display", Georgia, serif; letter-spacing: -.04em; }}
h1 em {{ font-style: italic; color: #5ba0ff; }}
.piede {{ position: absolute; left: 72px; bottom: 54px; display: flex; gap: 22px; align-items: center; font-size: 21px; font-weight: 500; color: #b5c9e4; }}
.piede b {{ color: #fff; font-weight: 700; }}
.piede i {{ width: 34px; height: 1px; background: #70b7ff; }}
svg {{ position: absolute; right: 60px; bottom: 0; }}
svg rect {{ fill: #70b7ff; opacity: .22; }}
</style></head><body>
<div class="logo"><span>Sozzi</span>Sound</div>
<p class="occhiello">{occhiello}</p>
<h1>{titolo}</h1>
<div class="piede"><b>sozzisound.it</b><i></i>Tecnici competenti in acustica</div>
<svg width="408" height="170" viewBox="0 0 408 170">{barre}</svg>
</body></html>
"""


def browser():
    for percorso in BROWSER:
        if percorso and Path(percorso).exists():
            return percorso
    sys.exit("Non trovo Chrome né Edge. Indicarne il percorso nella variabile d'ambiente CHROME.")


def pagina(voce):
    lunghezza = len(M.piano(voce["titolo"]))
    corpo = 78 if lunghezza <= 42 else 64 if lunghezza <= 70 else 54
    barre = []
    for i, v in enumerate(M._valori_spettro(voce["seme"] or "home")):
        h = round(20 + 140 * v, 1)
        barre.append(f'<rect x="{i * 17}" y="{round(170 - h, 1)}" width="12" height="{h}"/>')
    return MODELLO.format(corpo=corpo, occhiello=voce["occhiello"], titolo=voce["titolo"], barre="".join(barre))


def main():
    if not MANIFEST.exists():
        sys.exit("Manca _src/og/manifest.json: eseguire prima  python _src/build.py")
    voci = json.loads(MANIFEST.read_text(encoding="utf-8"))
    fatte = json.loads(FATTE.read_text(encoding="utf-8")) if FATTE.exists() else {}
    tutte = "--tutte" in sys.argv
    DEST.mkdir(parents=True, exist_ok=True)
    chrome = browser()
    create = 0
    with tempfile.TemporaryDirectory() as cartella:
        cartella = Path(cartella)
        for voce in voci:
            html = pagina(voce)
            impronta = hashlib.sha1(html.encode("utf-8")).hexdigest()[:12]
            destinazione = DEST / f"{voce['chiave']}.png"
            if not tutte and destinazione.exists() and fatte.get(voce["chiave"]) == impronta:
                continue
            sorgente = cartella / "anteprima.html"
            sorgente.write_text(html, encoding="utf-8")
            grezza = cartella / "anteprima.png"
            subprocess.run(
                [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                 f"--user-data-dir={cartella / 'profilo'}", "--window-size=1200,627",
                 "--virtual-time-budget=6000", f"--screenshot={grezza}", sorgente.as_uri()],
                check=True, capture_output=True, timeout=120)
            immagine = Image.open(grezza).convert("RGB").crop((0, 0, 1200, 627))
            immagine.quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(
                destinazione, optimize=True)
            fatte[voce["chiave"]] = impronta
            create += 1
            print(f"  {voce['chiave']}.png")
            FATTE.write_text(json.dumps(fatte, indent=1, sort_keys=True), encoding="utf-8", newline="\n")
    print(f"Anteprime create: {create} su {len(voci)}.")


if __name__ == "__main__":
    main()

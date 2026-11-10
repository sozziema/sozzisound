"""Elenco completo delle guide."""

from .guide_a import GUIDE_A
from .guide_b import GUIDE_B

GUIDE = GUIDE_A + GUIDE_B
PER_SLUG = {g["slug"]: g for g in GUIDE}

for _g in GUIDE:
    _g["url"] = f"guide/{_g['slug']}.html"

# Guide mostrate nella home
IN_HOME = [
    "bar-ristoranti-alberghi-impatto-acustico",
    "rumore-del-vicino-normale-tollerabilita",
    "legge-regionale-puglia-3-2002-acustica",
]

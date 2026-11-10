# Sorgenti del sito sozzisound.it

Il sito pubblicato è fatto di pagine HTML statiche. Queste pagine non si modificano a mano:
si generano da questa cartella con uno script Python che non richiede librerie.

```
python _src/build.py
```

Lo script riscrive tutte le pagine nella cartella principale, più `sitemap.xml`,
`robots.txt` e `assets/dati.js` (percorso guidato e risposte rapide), e alla fine controlla
titoli, descrizioni, collegamenti interni e coerenza del percorso guidato. Se segnala avvisi, vanno risolti prima di pubblicare.

La cartella `_src/` non viene pubblicata: GitHub Pages ignora le cartelle che iniziano con
il trattino basso.

## Dove si cambia che cosa

| Che cosa | Dove |
|---|---|
| Telefoni, email, indirizzo, social, Partita IVA, indirizzo del modulo | `sito.py` |
| Testi dei servizi | `contenuti/servizi_a.py`, `contenuti/servizi_b.py` |
| Pagine «Per chi» | `contenuti/perchi.py` |
| Guide | `contenuti/guide_a.py`, `contenuti/guide_b.py` |
| Province e comuni | `contenuti/citta.py` |
| Percorso guidato «Che pratica mi serve?» (domande ed esiti) | `contenuti/percorso.py` |
| Domande frequenti e risposte rapide | `contenuti/faq.py` |
| Home, chi siamo, contatti, privacy, cookie, 404 | `build.py` |
| Intestazione, piè di pagina, modulo, dati strutturati | `motore.py` |
| Aspetto | `../style.css` |
| Comportamenti (menu, modulo, cookie, risposte rapide) | `../script.js` |

## Operazioni frequenti

**Aggiungere la Partita IVA.** Scriverla in `sito.py` alla voce `PARTITA_IVA` e rigenerare:
compare nel piè di pagina di tutte le pagine e nei dati strutturati.

**Aggiungere un profilo social.** Incollare l'indirizzo nella voce corrispondente di `SOCIAL`
in `sito.py`. Le voci vuote non vengono mostrate.

**Aggiungere la foto di un professionista.** Salvarla in `assets/` (quadrata, almeno 400 px) e
scriverne il percorso nel campo `foto` di `PROFESSIONISTI` in `sito.py`.

**Attivare l'invio del modulo contatti.** Seguire `modulo-contatti/ISTRUZIONI.md`.

**Cambiare il percorso guidato.** In `contenuti/percorso.py` ogni domanda elenca le risposte e
il passo a cui portano; ogni esito indica la pratica collegata e una risposta breve. Lo script
avvisa se una risposta porta a un passo che non esiste o se un esito resta irraggiungibile.

**Aggiungere una guida.** Copiare una voce in `contenuti/guide_b.py`, cambiare `slug`, testi e
data. Per mostrarla in home, aggiungere lo slug a `IN_HOME` in `contenuti/guide.py`.

**Aggiungere un comune.** Copiare una voce di `COMUNI` in `contenuti/citta.py`. Il testo deve
essere scritto per quel comune: niente copie con il nome cambiato.

**Anteprime per i social.** Dopo aver aggiunto pagine: `python _src/og.py` (serve Google
Chrome), poi di nuovo `python _src/build.py`.

## Regole per i testi

- Ogni affermazione normativa deve trovarsi in `norme-verificate.md`. Una cifra nuova va
  prima controllata sul testo della norma e annotata lì.
- Mai scrivere che un documento è obbligatorio in assoluto: dipende da attività, procedimento
  e regolamento comunale.
- La valutazione del rischio rumore nei luoghi di lavoro richiede «personale qualificato»:
  non è riservata al tecnico competente in acustica.
- Niente nomi di clienti o cantieri, niente prezzi, niente numeri non verificabili.
- Titoli: solo «Ing. Emanuele Sozzi» e «Prof. Vincenzo Sozzi».
- Nessuna affermazione sulla classificazione acustica di un Comune senza una fonte.

## Vedere il sito in locale

```
python -m http.server 8811
```

dalla cartella principale, poi aprire <http://localhost:8811>.

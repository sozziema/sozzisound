# Attivare l'invio del modulo contatti

Il modulo del sito è già pronto. Finché non viene collegato a questo script funziona in
modalità di ripiego: «Invia richiesta» apre l'app di posta del visitatore, «Invia su WhatsApp»
apre la chat. Collegandolo, la richiesta parte direttamente dalla pagina e arriva a
`info@sozzisound.it`, da qualunque dispositivo.

Servono circa cinque minuti e l'account Google Workspace dello studio.

## 1. Creare lo script

1. Accedi con `info@sozzisound.it` e apri <https://script.google.com>.
2. **Nuovo progetto**. In alto a sinistra rinominalo, per esempio «Modulo contatti sito».
3. Cancella il contenuto dell'editor e incolla tutto il file `Codice.gs` di questa cartella.
4. Salva (icona del dischetto).

## 2. Pubblicarlo come app web

1. In alto a destra: **Esegui il deployment → Nuovo deployment**.
2. Accanto a «Seleziona tipo» scegli l'ingranaggio e poi **App web**.
3. Imposta:
   - *Esegui come*: **Me**
   - *Utenti autorizzati ad accedere*: **Chiunque**
4. **Esegui il deployment**. Google chiede di autorizzare lo script a inviare email a tuo nome:
   conferma. È l'unico permesso richiesto.
5. Copia l'**URL dell'app web**: finisce con `/exec`.

Se la voce «Chiunque» non compare, nell'account Workspace è attiva una restrizione sulla
condivisione verso l'esterno: va allentata dalla console di amministrazione.

## 3. Collegare il sito

1. Apri `_src/sito.py` e incolla l'indirizzo tra le virgolette di `MODULO_ENDPOINT`.
2. Rigenera il sito: `python _src/build.py`.
3. Pubblica le modifiche (commit e push).

L'informativa sulla privacy si aggiorna da sola: descrive l'invio tramite Google Workspace
solo quando `MODULO_ENDPOINT` è compilato.

## 4. Provare

Invia una richiesta dal sito pubblicato e controlla che arrivi nella casella. Rispondendo
all'email, la risposta va direttamente a chi ha scritto.

## Se in futuro modifichi lo script

**Esegui il deployment → Gestisci deployment → matita → Versione: Nuova versione → Esegui il
deployment.** L'indirizzo resta lo stesso e il sito non va toccato.

## Che cosa fa, in breve

- Accetta solo i campi del modulo, con una lunghezza massima ciascuno.
- Scarta in silenzio i messaggi in cui è compilato il campo nascosto anti-spam.
- Si ferma dopo 30 invii in un'ora, per evitare abusi.
- Non salva nulla: i dati esistono solo nell'email che ricevi.

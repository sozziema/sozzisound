"""Percorso guidato: domande a scelta multipla che portano alla pratica giusta.

DOMANDE   passo -> domanda, nota facoltativa, opzioni
          ogni opzione: (testo del pulsante, passo o esito successivo, etichetta breve per il riepilogo)
ESITI     esito -> risposta breve e pratica collegata
          servizio  slug di un servizio          (oppure)
          pagina    slug di una pagina "Per chi"
          titolo    facoltativo: sostituisce il nome del servizio
          testo     due o tre frasi, in HTML semplice e senza collegamenti
          norme     riferimenti mostrati come etichette (facoltativo)
          guida     slug di una guida da proporre (facoltativo)
          cta       testo del pulsante principale (facoltativo)

Le risposte restano generali e prudenti: le cifre citate sono quelle di _src/norme-verificate.md.
"""

INIZIO = "inizio"

DOMANDE = {
    "inizio": {
        "domanda": "Da dove partiamo?",
        "opzioni": [
            ("Apro, amplio o modifico un'attività", "attivita", "Attività"),
            ("Faccio musica o organizzo un evento", "musica", "Musica ed eventi"),
            ("Costruisco o ristrutturo un edificio", "edilizia", "Edilizia"),
            ("Un rumore mi disturba", "disturbo", "Un rumore mi disturba"),
            ("Ho ricevuto un esposto o una richiesta dal Comune", "esposto", "Esposto o richiesta"),
            ("Devo valutare il rumore per i lavoratori", "lavoro", "Luoghi di lavoro"),
            ("Sono un tecnico, un avvocato o un ente", "professionisti", "Professionisti ed enti"),
        ],
    },
    "attivita": {
        "domanda": "Che attività è?",
        "opzioni": [
            ("Bar, ristorante, albergo, negozio, palestra, lido", "attivita-pubblico", "Pubblico esercizio"),
            ("Produzione o artigianato: capannone, laboratorio, officina", "esito-produttive", "Produzione"),
            ("Impianto sportivo: padel, piscina, centro sportivo", "esito-sport", "Impianto sportivo"),
            ("Impianto energetico o ambientale: eolico, fotovoltaico, biogas", "esito-energia", "Impianto energetico"),
            ("Un'altra attività, o non lo so", "esito-impatto", "Altra attività"),
        ],
    },
    "attivita-pubblico": {
        "nota": "Per le piccole e medie imprese molte di queste attività sono considerate a bassa rumorosità (DPR 227/2011). C'è però un'eccezione che cambia tutto: la musica.",
        "domanda": "Ci sarà musica? Impianto audio, dj, musica dal vivo, serate.",
        "opzioni": [
            ("Sì", "esito-locali-musica", "Con musica"),
            ("No, nessuna musica", "esito-esonero", "Senza musica"),
            ("Solo un sottofondo", "esito-sottofondo", "Sottofondo"),
        ],
    },
    "musica": {
        "domanda": "Di che cosa si tratta?",
        "opzioni": [
            ("Un locale che fa musica con regolarità", "musica-locale", "Locale"),
            ("Ricevimenti con musica: masseria, sala, lido", "esito-locali-musica", "Ricevimenti"),
            ("Un evento occasionale: concerto, festa, sagra, serata", "esito-deroga", "Evento occasionale"),
        ],
    },
    "musica-locale": {
        "domanda": "Che cosa ti serve?",
        "opzioni": [
            ("La pratica per aprire, o per aggiungere la musica", "esito-locali-musica", "Pratica"),
            ("La verifica dell'impianto audio e del limitatore", "esito-verifica", "Verifica impianto"),
            ("I vicini si lamentano", "esito-bonifica", "Vicini che si lamentano"),
        ],
    },
    "edilizia": {
        "domanda": "A che punto sei?",
        "opzioni": [
            ("Sto chiedendo il permesso di costruire", "esito-permesso", "Permesso di costruire"),
            ("Sto progettando e voglio un buon isolamento", "esito-passivi", "Progetto"),
            ("L'edificio è finito: serve una verifica", "esito-collaudo", "Edificio finito"),
            ("Costruisco vicino a una strada, una ferrovia o un locale", "esito-clima", "Vicino a sorgenti rumorose"),
            ("Una scuola, un asilo o una struttura sanitaria", "esito-clima", "Scuola o struttura sanitaria"),
            ("Una sala, un'aula o un ufficio in cui non ci si capisce", "esito-sale", "Sala rumorosa"),
            ("Devo insonorizzare un locale o una sala prove", "esito-progettazione", "Insonorizzazione"),
        ],
    },
    "disturbo": {
        "domanda": "Da dove arriva il rumore?",
        "opzioni": [
            ("Da un locale, un negozio o un'azienda", "esito-disturbo-attivita", "Da un'attività"),
            ("Da un campo sportivo o da padel", "esito-disturbo-attivita", "Da un impianto sportivo"),
            ("Da un vicino di casa", "esito-disturbo-vicino", "Da un vicino"),
            ("Da un impianto: pompa di calore, condizionatore, ascensore", "esito-impianti", "Da un impianto"),
            ("Sento troppo chi abita accanto o sopra", "esito-isolamento", "Isolamento scarso"),
        ],
    },
    "esposto": {
        "domanda": "Che cosa è successo?",
        "opzioni": [
            ("I vicini si lamentano della mia attività", "esito-bonifica", "Lamentele dei vicini"),
            ("Il Comune o l'ARPA contestano un superamento", "esito-bonifica", "Contestazione"),
            ("Il Comune mi chiede una documentazione acustica", "esito-impatto", "Richiesta di documentazione"),
            ("Sono in causa, o sto per andarci", "esito-causa", "Causa"),
        ],
    },
    "lavoro": {
        "domanda": "Che cosa ti serve?",
        "opzioni": [
            ("Le misure per la valutazione del rischio rumore", "esito-lavoro", "Valutazione del rischio"),
            ("Ridurre il rumore in un reparto", "esito-riduzione", "Ridurre il rumore"),
            ("Sono un RSPP o un consulente: cerco chi faccia le misure", "esito-rspp", "RSPP o consulente"),
        ],
    },
    "professionisti": {
        "domanda": "Chi sei?",
        "opzioni": [
            ("Architetto, ingegnere o geometra", "esito-progettisti", "Progettista"),
            ("Avvocato", "esito-legali", "Avvocato"),
            ("RSPP o consulente per la sicurezza", "esito-rspp", "RSPP o consulente"),
            ("Comune o ente pubblico", "esito-enti", "Ente pubblico"),
        ],
    },
}

ESITI = {
    "esito-locali-musica": {
        "servizio": "impatto-acustico-locali-musica-puglia",
        "titolo": "Impatto acustico per locali con musica",
        "testo": "<p>Con un impianto di diffusione sonora o con eventi con musica, l'esclusione prevista per le attività a bassa rumorosità non vale: la norma chiede la documentazione di previsione di impatto acustico.</p><p>Di solito si aggiunge la verifica dell'impianto audio prevista dal DPCM 215/1999.</p>",
        "norme": ["DPR 227/2011, art. 4", "DPCM 215/1999"],
        "guida": "musica-nei-locali-limiti-deroghe",
    },
    "esito-esonero": {
        "servizio": "rumore-attivita-commerciali-artigianali-puglia",
        "titolo": "Probabilmente nessuna pratica",
        "testo": "<p>Se l'impresa è piccola o media e l'attività è tra quelle a bassa rumorosità dell'Allegato B del DPR 227/2011, di norma la documentazione di impatto acustico non è dovuta. Conviene comunque leggere il regolamento del Comune.</p><p>I limiti di rumore però restano. Se hai cappe, gruppi frigo o unità esterne vicino a delle abitazioni, una verifica prima di installarli evita un esposto dopo.</p>",
        "norme": ["DPR 227/2011, art. 4 e Allegato B"],
        "guida": "bar-ristoranti-alberghi-impatto-acustico",
        "cta": "Chiedi una verifica",
    },
    "esito-sottofondo": {
        "servizio": "impatto-acustico-locali-musica-puglia",
        "titolo": "Dipende dal tuo Comune",
        "testo": "<p>La norma parla di impianti di diffusione sonora senza distinguere per volume, e i Comuni la applicano in modi diversi. Prima di decidere va letto il regolamento comunale, o sentito lo sportello unico.</p><p>Lo verifichiamo noi e ti diciamo se la documentazione di impatto acustico serve.</p>",
        "norme": ["DPR 227/2011, art. 4"],
        "guida": "bar-ristoranti-alberghi-impatto-acustico",
        "cta": "Chiedi una verifica",
    },
    "esito-produttive": {
        "servizio": "relazione-acustica-attivita-produttive-puglia",
        "titolo": "Relazione acustica per attività produttive",
        "testo": "<p>Per i nuovi impianti destinati ad attività produttive la legge quadro prevede una documentazione di previsione di impatto acustico, da allegare alla domanda di titolo edilizio o di autorizzazione.</p><p>In Puglia la L.R. 3/2002 chiede inoltre una relazione asseverata per le attività che superano le soglie di rumore indicate. Per le piccole e medie imprese esistono forme semplificate: quale si applica lo verifichiamo insieme.</p>",
        "norme": ["L. 447/1995, art. 8", "L.R. Puglia 3/2002, art. 12", "DPR 227/2011, art. 4"],
    },
    "esito-sport": {
        "servizio": "impatto-acustico-impianti-sportivi-puglia",
        "titolo": "Impatto acustico per impianti sportivi",
        "testo": "<p>Gli impianti sportivi e ricreativi sono tra le opere per cui la legge quadro prevede la documentazione di impatto acustico. In Puglia la L.R. 3/2002 fissa orari e livelli in facciata per le attività all'aperto.</p><p>Per il padel conviene valutare distanza dalle case, orientamento dei campi e orari prima di costruire.</p>",
        "norme": ["L. 447/1995, art. 8", "L.R. Puglia 3/2002, art. 16"],
        "guida": "campi-da-padel-rumore",
    },
    "esito-energia": {
        "servizio": "impatto-acustico-impianti-energetici-puglia",
        "titolo": "Impatto acustico per impianti energetici",
        "testo": "<p>Nei procedimenti autorizzativi di impianti eolici, fotovoltaici con cabine e inverter, biogas e impianti di trattamento, la valutazione previsionale del rumore è tra i documenti richiesti.</p><p>Dopo l'avvio possono servire misure di monitoraggio, per confrontare i livelli reali con quelli previsti.</p>",
        "norme": ["L. 447/1995, art. 8"],
    },
    "esito-impatto": {
        "servizio": "valutazione-impatto-acustico-puglia",
        "titolo": "Valutazione di impatto acustico",
        "testo": "<p>La documentazione di impatto acustico è prevista in molti procedimenti per attività, impianti e opere che producono rumore verso l'esterno. Che cosa serva nel tuo caso dipende dall'attività, dal procedimento e dal regolamento del Comune.</p><p>Se hai una richiesta scritta dell'ente, mandacela così com'è: ti diciamo di che cosa si tratta.</p>",
        "norme": ["L. 447/1995, art. 8", "DPR 227/2011, art. 4"],
        "guida": "impatto-acustico-e-clima-acustico-differenze",
    },
    "esito-deroga": {
        "servizio": "deroga-acustica-eventi-puglia",
        "titolo": "Autorizzazione in deroga per eventi",
        "testo": "<p>Le manifestazioni temporanee le autorizza il Comune, anche in deroga ai limiti di rumore. In Puglia la L.R. 3/2002 consente le manifestazioni musicali nella fascia 9-24, con livelli massimi in facciata; per andare oltre serve la deroga, da chiedere con domanda scritta e motivata.</p><p>Tempi e moduli cambiano da Comune a Comune: conviene muoversi per tempo.</p>",
        "norme": ["L. 447/1995, art. 6", "L.R. Puglia 3/2002, art. 17"],
        "guida": "musica-nei-locali-limiti-deroghe",
    },
    "esito-verifica": {
        "servizio": "verifica-livelli-sonori-locali-puglia",
        "titolo": "Verifica dell'impianto audio",
        "testo": "<p>Il DPCM 215/1999 fissa i livelli massimi all'interno dei locali con impianti di amplificazione: 102 dB(A) di livello massimo e 95 dB(A) di livello equivalente. Il gestore deve far verificare l'impianto da un tecnico competente, e rifarlo dopo ogni modifica.</p><p>Se l'impianto può superare i limiti, si interviene con un limitatore protetto contro le manomissioni.</p>",
        "norme": ["DPCM 215/1999"],
        "guida": "musica-nei-locali-limiti-deroghe",
    },
    "esito-bonifica": {
        "servizio": "bonifica-acustica-puglia",
        "titolo": "Misure e bonifica acustica",
        "testo": "<p>Si parte da misure nelle abitazioni e al confine, negli orari in cui l'attività lavora: dicono se un superamento c'è, e di quanto. Poi si individua la sorgente, si progetta l'intervento e una nuova misura conferma il risultato.</p><p>È il modo per rispondere con i dati a una contestazione, dei vicini o dell'ente.</p>",
        "norme": ["DPCM 14/11/1997"],
    },
    "esito-permesso": {
        "servizio": "relazione-acustica-permesso-costruire-puglia",
        "titolo": "Relazione acustica per il permesso di costruire",
        "testo": "<p>In Puglia la L.R. 3/2002 chiede che il progetto dei nuovi edifici industriali e residenziali, e delle ristrutturazioni di edifici industriali, sia corredato da una relazione asseverata da un tecnico competente, da presentare con la domanda di permesso di costruire.</p><p>Per la ristrutturazione di un'abitazione conta il regolamento del Comune.</p>",
        "norme": ["L.R. Puglia 3/2002, art. 15", "DPCM 5/12/1997"],
        "guida": "legge-regionale-puglia-3-2002-acustica",
    },
    "esito-passivi": {
        "servizio": "requisiti-acustici-passivi-puglia",
        "titolo": "Requisiti acustici passivi",
        "testo": "<p>Il DPCM 5/12/1997 fissa le prestazioni minime di facciate, pareti tra alloggi e solai, e i livelli massimi del rumore degli impianti. Contano i valori dell'edificio finito, non quelli di laboratorio.</p><p>Con un calcolo sul progetto si scelgono stratigrafie e dettagli prima del cantiere, quando cambiare è ancora semplice.</p>",
        "norme": ["DPCM 5/12/1997"],
        "guida": "requisiti-acustici-passivi-dpcm-5-12-1997",
    },
    "esito-collaudo": {
        "servizio": "collaudo-acustico-edifici-puglia",
        "titolo": "Collaudo acustico dell'edificio",
        "testo": "<p>Il collaudo misura in opera l'isolamento di facciate, pareti e solai e il rumore degli impianti, e lo confronta con i valori del DPCM 5/12/1997.</p><p>In Puglia la conformità acustica delle opere viene verificata al rilascio dell'agibilità.</p>",
        "norme": ["DPCM 5/12/1997", "L.R. Puglia 3/2002, art. 15"],
        "guida": "requisiti-acustici-passivi-dpcm-5-12-1997",
    },
    "esito-clima": {
        "servizio": "clima-acustico-puglia",
        "titolo": "Valutazione di clima acustico",
        "testo": "<p>Per scuole e asili nido, ospedali, case di cura e di riposo, parchi e nuove residenze vicine a strade, ferrovie, locali o impianti sportivi, la legge prevede una valutazione previsionale del clima acustico.</p><p>Si misura il rumore che c'è oggi, di giorno e di notte, e lo si traduce in richieste per il progetto.</p>",
        "norme": ["L. 447/1995, art. 8, c. 3"],
        "guida": "impatto-acustico-e-clima-acustico-differenze",
    },
    "esito-sale": {
        "servizio": "acustica-aule-uffici-sale-puglia",
        "titolo": "Correzione acustica di sale, aule e uffici",
        "testo": "<p>Quando in una sala non ci si capisce, il problema è quasi sempre il riverbero. Si misura il tempo di riverberazione, si calcola quanta superficie fonoassorbente serve e dove metterla, e a lavori fatti si verifica il risultato.</p>",
    },
    "esito-progettazione": {
        "servizio": "progettazione-acustica-ambienti-puglia",
        "titolo": "Progettazione acustica dell'ambiente",
        "testo": "<p>Insonorizzare vuol dire due cose diverse: non far uscire il suono, e farlo suonare bene dentro. Si parte dalle misure dello stato di fatto e dal risultato che vuoi ottenere, poi si progettano pareti, solai, porte e trattamenti interni.</p>",
    },
    "esito-disturbo-attivita": {
        "servizio": "perizie-acustiche-controversie-puglia",
        "titolo": "Misure in casa e perizia fonometrica",
        "testo": "<p>Per le attività valgono i limiti della zona e, dentro casa tua, il criterio differenziale: il rumore non deve superare di oltre 5 dB di giorno e 3 dB di notte quello che c'è quando l'attività è ferma.</p><p>Una misura in casa, negli orari giusti, dice se il limite è superato. Con la relazione puoi fare un esposto al Comune, trattare o agire in giudizio.</p>",
        "norme": ["DPCM 14/11/1997, art. 4"],
        "guida": "rumore-del-vicino-normale-tollerabilita",
    },
    "esito-disturbo-vicino": {
        "servizio": "perizie-acustiche-controversie-puglia",
        "titolo": "Misure in casa e perizia fonometrica",
        "testo": "<p>Tra privati non c'è un limite numerico fissato dalle norme amministrative: vale la «normale tollerabilità» del codice civile, che il giudice valuta caso per caso.</p><p>La misura serve a capire se il problema è oggettivo, prima di spendere in avvocati, e a sostenere una trattativa o una causa.</p>",
        "norme": ["Codice civile, art. 844"],
        "guida": "rumore-del-vicino-normale-tollerabilita",
    },
    "esito-impianti": {
        "servizio": "rumore-impianti-tecnici-puglia",
        "titolo": "Misura del rumore dell'impianto",
        "testo": "<p>Si misura nella stanza disturbata, con l'impianto acceso e spento. Se l'impianto è di un'attività vale il criterio differenziale; se è dell'edificio, i livelli del DPCM 5/12/1997; se è di un vicino, la normale tollerabilità.</p><p>Dal confronto si capisce di quanto ridurre e come: antivibranti, spostamento, schermi.</p>",
        "norme": ["DPCM 14/11/1997, art. 4", "DPCM 5/12/1997", "Codice civile, art. 844"],
        "guida": "pompe-di-calore-unita-esterne-rumore",
    },
    "esito-isolamento": {
        "servizio": "collaudo-acustico-edifici-puglia",
        "titolo": "Verifica dell'isolamento acustico",
        "testo": "<p>Negli edifici più recenti si può misurare in opera quanto isolano pareti e solai, e confrontare il risultato con i valori del DPCM 5/12/1997.</p><p>È una verifica utile anche prima di contestare un difetto a chi ha costruito o venduto.</p>",
        "norme": ["DPCM 5/12/1997"],
        "guida": "requisiti-acustici-passivi-dpcm-5-12-1997",
    },
    "esito-causa": {
        "servizio": "perizie-acustiche-controversie-puglia",
        "titolo": "Consulenza tecnica di parte",
        "testo": "<p>Una relazione firmata da un tecnico competente, con misure eseguite secondo il DM 16/03/1998, è un documento che il tuo avvocato può produrre in giudizio come consulenza di parte.</p><p>Se il giudice nomina un proprio consulente, possiamo assisterti durante le operazioni.</p>",
        "norme": ["DM 16/03/1998", "Codice civile, art. 844"],
    },
    "esito-lavoro": {
        "servizio": "sicurezza-rumore-lavoro-puglia",
        "titolo": "Misure del rumore nei luoghi di lavoro",
        "testo": "<p>Il D.Lgs 81/2008 chiede al datore di lavoro di valutare l'esposizione dei lavoratori al rumore, e di aggiornare la valutazione almeno ogni quattro anni o quando cambiano macchine e lavorazioni. Le soglie di riferimento sono 80, 85 e 87 dB(A).</p><p>Noi eseguiamo le misure e calcoliamo l'esposizione per mansione; la valutazione del rischio resta in capo al datore di lavoro e al suo servizio di prevenzione.</p>",
        "norme": ["D.Lgs 81/2008, artt. 181, 189 e 190"],
        "guida": "rumore-luoghi-di-lavoro-valori-azione-limite",
    },
    "esito-riduzione": {
        "servizio": "bonifica-acustica-puglia",
        "titolo": "Riduzione del rumore in reparto",
        "testo": "<p>Il D.Lgs 81/2008 mette in ordine le cose da fare: prima ridurre il rumore alla fonte, con macchine, schermature, involucri e organizzazione del lavoro; i dispositivi di protezione vengono dopo.</p><p>Si parte dalle misure, per capire quali sorgenti pesano davvero sull'esposizione.</p>",
        "norme": ["D.Lgs 81/2008, art. 192"],
    },
    "esito-rspp": {
        "pagina": "rspp-consulenti-sicurezza",
        "titolo": "Misure fonometriche per i vostri clienti",
        "testo": "<p>Eseguiamo le misure e vi consegniamo i dati di esposizione per mansione, pronti da riportare nel documento di valutazione dei vostri clienti.</p>",
        "norme": ["D.Lgs 81/2008, Titolo VIII, Capo II"],
    },
    "esito-progettisti": {
        "pagina": "progettisti",
        "titolo": "La parte acustica delle vostre pratiche",
        "testo": "<p>Relazione asseverata per il permesso di costruire, requisiti acustici passivi in progetto, clima acustico del sito, collaudo a fine lavori: seguiamo la parte acustica e rispondiamo alle richieste dell'ufficio tecnico sui contenuti della relazione.</p>",
    },
    "esito-legali": {
        "pagina": "studi-legali",
        "titolo": "Consulenza tecnica di parte",
        "testo": "<p>Nelle cause per immissioni di rumore eseguiamo le misure, redigiamo la relazione di parte e assistiamo alle operazioni del consulente nominato dal giudice.</p>",
        "norme": ["Codice civile, art. 844"],
    },
    "esito-enti": {
        "servizio": "acustica-enti-pubblici-puglia",
        "titolo": "Supporto tecnico agli enti pubblici",
        "testo": "<p>Affianchiamo gli uffici nella classificazione acustica del territorio, nei piani di risanamento, nei regolamenti per le attività temporanee e nelle misure di verifica.</p>",
        "norme": ["L. 447/1995, artt. 6 e 7", "L.R. Puglia 3/2002"],
    },
}

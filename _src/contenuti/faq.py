"""Domande frequenti e voci del pannello "Risposte rapide".

Ogni voce:
  id      identificativo
  gruppo  chiave del gruppo nella pagina faq.html ("" = solo pannello Risposte rapide)
  q       domanda
  a       risposta, in HTML semplice e senza collegamenti (il collegamento va in "u")
  k       parole chiave per il pannello: scriverle come le scriverebbe chi cerca
  f       parole "forti" (vedi FORTI in fondo): ne basta una per far scegliere la voce
  u, e    pagina di approfondimento ed etichetta del collegamento (facoltativi)
  c       etichetta breve per i pulsanti del pannello (facoltativa)

Le risposte restano generali e prudenti: le cifre citate sono quelle di _src/norme-verificate.md.
"""

GRUPPI = [
    ("generali", "In generale", "Chi siamo, che cosa facciamo, dove."),
    ("pratiche", "Pratiche e autorizzazioni", "Quando un documento acustico è richiesto, e quale."),
    ("misure", "Misure e risultati", "Come si misura il rumore e che cosa succede dopo."),
    ("costi", "Tempi, costi e preventivo", "Che cosa aspettarsi prima di iniziare."),
]

FAQ = [
    # ------------------------------------------------------------ generali
    {
        "id": "chi-firma", "gruppo": "generali",
        "q": "Chi può firmare una relazione acustica?",
        "a": "<p>Le misure del rumore ambientale e le valutazioni che ne dipendono sono affidate dalla legge al tecnico competente in acustica (L. 447/1995, art. 2), iscritto nell'elenco nazionale noto come ENTECA. L'elenco è pubblico: nome e numero di iscrizione si possono verificare.</p><p>I nostri numeri: Ing. Emanuele Sozzi, n. 12994; Prof. Vincenzo Sozzi, n. 12993.</p>",
        "k": "firma firmare chi puo abilitato abilitazione tecnico competente enteca elenco iscrizione albo titolo",
        "u": "guide/tecnico-competente-in-acustica-enteca.html", "e": "Leggi la guida su ENTECA",
        "c": "Chi può firmare?",
    },
    {
        "id": "differenza-impatto-clima", "gruppo": "generali",
        "q": "Che differenza c'è tra impatto acustico e clima acustico?",
        "a": "<p>L'impatto acustico riguarda il rumore che un'attività o un'opera porterà verso chi le sta intorno. Il clima acustico riguarda il rumore già presente in un'area dove si vuole costruire qualcosa di sensibile: una scuola, una struttura sanitaria, delle abitazioni.</p><p>Uno stesso intervento può richiederle entrambe.</p>",
        "k": "differenza clima acustico impatto cos e cosa significa",
        "u": "guide/impatto-acustico-e-clima-acustico-differenze.html", "e": "Leggi la guida",
    },
    {
        "id": "previsionale-collaudo", "gruppo": "generali",
        "q": "Che differenza c'è tra valutazione previsionale e collaudo?",
        "a": "<p>La valutazione previsionale si fa prima: stima con il calcolo che cosa succederà una volta realizzata l'opera o avviata l'attività, quando correggere il progetto è ancora semplice. Il collaudo si fa dopo: misura in opera il risultato e lo confronta con i limiti o con le prestazioni di progetto.</p>",
        "k": "previsionale collaudo differenza prima dopo calcolo progetto fine lavori",
        "u": "servizi/collaudo-acustico-edifici-puglia.html", "e": "Il collaudo acustico",
    },
    {
        "id": "fuori-puglia", "gruppo": "generali",
        "q": "Lavorate anche fuori dalla Puglia?",
        "a": "<p>Sì. La sede è a Ostuni e lavoriamo in tutte e sei le province pugliesi; su incarico seguiamo pratiche nel resto d'Italia. L'iscrizione all'elenco dei tecnici competenti in acustica è nazionale.</p>",
        "k": "fuori puglia italia regione basilicata zona zone dove operate trasferta lontano citta provincia",
        "u": "citta/", "e": "Dove operiamo",
        "c": "Dove lavorate?",
    },
    {
        "id": "privati", "gruppo": "generali",
        "q": "Seguite anche i privati?",
        "a": "<p>Sì. Rumore di un vicino, di un locale, di un impianto condominiale; la verifica dell'isolamento di una casa appena acquistata; una pompa di calore da collocare bene. Spieghiamo che cosa si può misurare e a che cosa serve, in concreto, la relazione.</p>",
        "k": "privato privati condominio casa appartamento cittadino famiglia amministratore",
        "u": "per/privati-condomini.html", "e": "Per privati e condomìni",
    },
    {
        "id": "tribunale", "gruppo": "generali",
        "q": "Una perizia fonometrica vale in tribunale?",
        "a": "<p>Una relazione firmata da un tecnico competente, con misure eseguite secondo il DM 16/03/1998 e strumenti con taratura valida, è un documento tecnico che il tuo avvocato può produrre in giudizio come consulenza di parte. Il peso che avrà lo decide il giudice, che può nominare un proprio consulente.</p><p>In quel caso possiamo assisterti come consulenti tecnici di parte durante le operazioni.</p>",
        "k": "tribunale giudice causa perizia avvocato legale giudizio ctu ctp prova valore denuncia",
        "u": "servizi/perizie-acustiche-controversie-puglia.html", "e": "Perizie e controversie",
        "c": "Vale in tribunale?",
    },
    # ------------------------------------------------------------ pratiche
    {
        "id": "quando-impatto", "gruppo": "pratiche",
        "q": "Quando serve una valutazione di impatto acustico?",
        "a": "<p>La legge quadro (L. 447/1995, art. 8) la prevede in molti procedimenti: titoli edilizi e autorizzazioni per attività produttive, sportive e ricreative, discoteche, pubblici esercizi con impianti rumorosi. In Puglia la L.R. 3/2002 aggiunge regole proprie per imprese ed edifici.</p><p>Che cosa serva nel caso concreto dipende dall'attività, dal procedimento e dal regolamento del Comune: lo verifichiamo insieme prima di iniziare.</p>",
        "k": "quando serve impatto acustico obbligatorio obbligo richiesta richiesto chiesto comune suap apertura aprire nuova attivita pratica",
        "u": "servizi/valutazione-impatto-acustico-puglia.html", "e": "Impatto acustico",
        "c": "Quando serve l'impatto acustico?",
    },
    {
        "id": "esonero", "gruppo": "pratiche",
        "q": "Il mio locale è esonerato dalla documentazione di impatto acustico?",
        "a": "<p>Per le piccole e medie imprese il DPR 227/2011 esclude dall'obbligo molte attività a bassa rumorosità: tra le altre alberghi, bar, ristoranti, palestre, stabilimenti balneari, negozi.</p><p>L'esclusione però non vale per bar, ristoranti, stabilimenti balneari e simili che usano impianti di diffusione sonora o organizzano eventi con musica. E in ogni caso riguarda il documento, non i limiti di rumore, che restano da rispettare.</p>",
        "k": "esonero esonerato esente esenzione escluso bar ristorante albergo pizzeria negozio aprire apertura 227 bassa rumorosita dichiarazione sostitutiva",
        "u": "guide/bar-ristoranti-alberghi-impatto-acustico.html", "e": "Leggi la guida",
        "c": "Il mio locale è esonerato?",
    },
    {
        "id": "musica-locale", "gruppo": "pratiche",
        "q": "Voglio fare musica nel mio locale: che cosa serve?",
        "a": "<p>Di norma tre cose. La documentazione di impatto acustico, perché con la diffusione sonora l'esonero delle attività a bassa rumorosità non vale più. La verifica dell'impianto audio prevista dal DPCM 215/1999, che fissa i livelli massimi all'interno del locale. E, per le serate fuori dall'ordinario, l'autorizzazione del Comune, anche in deroga.</p>",
        "k": "musica locale bar ristorante pub dj live karaoke serata impianto audio casse volume limitatore discoteca lido stabilimento 215",
        "u": "guide/musica-nei-locali-limiti-deroghe.html", "e": "Leggi la guida",
        "c": "Musica nel locale",
    },
    {
        "id": "deroga-evento", "gruppo": "pratiche",
        "q": "Come si chiede la deroga per un evento?",
        "a": "<p>L'autorizzazione per attività temporanee e manifestazioni, anche in deroga ai limiti, la rilascia il Comune (L. 447/1995, art. 6). In Puglia la L.R. 3/2002 (art. 17) indica fasce orarie e livelli per le manifestazioni musicali, e prevede che la deroga sia chiesta con domanda scritta e motivata.</p><p>Tempi e documenti cambiano da Comune a Comune: conviene muoversi per tempo. Noi prepariamo la parte tecnica.</p>",
        "k": "deroga evento concerto festa sagra festival manifestazione temporanea matrimonio piazza autorizzazione comune",
        "u": "servizi/deroga-acustica-eventi-puglia.html", "e": "Deroghe per eventi",
    },
    {
        "id": "ristrutturare-casa", "gruppo": "pratiche",
        "q": "Mi serve la relazione acustica per ristrutturare casa?",
        "a": "<p>Dipende dall'intervento e dal Comune. In Puglia la L.R. 3/2002 (art. 15) chiede la relazione asseverata per i nuovi edifici industriali e residenziali e per le ristrutturazioni di quelli industriali. Per la ristrutturazione di un'abitazione conta che cosa prevede il regolamento comunale e quanto l'intervento tocca pareti, solai, facciate e impianti.</p><p>Anche quando il documento non è richiesto, verificare l'isolamento in progetto è più semplice che rimediare a lavori finiti.</p>",
        "k": "ristrutturare ristrutturazione casa permesso costruire edilizia relazione asseverata progetto nuova costruzione scia villa",
        "u": "servizi/relazione-acustica-permesso-costruire-puglia.html", "e": "Relazione per il permesso di costruire",
    },
    {
        "id": "classificazione", "gruppo": "pratiche",
        "q": "Che cos'è la classificazione acustica del mio Comune?",
        "a": "<p>È il piano con cui il Comune divide il territorio in sei classi, dalle aree particolarmente protette a quelle esclusivamente industriali, e assegna a ciascuna i limiti di rumore diurni e notturni. Dove il piano manca si applicano limiti transitori.</p><p>Per conoscere la classe di un immobile si consultano le tavole del piano, sul sito del Comune o all'ufficio tecnico.</p>",
        "k": "classificazione acustica zonizzazione classe zona piano comunale limiti comune mio",
        "u": "guide/classificazione-acustica-comunale.html", "e": "Leggi la guida",
    },
    # ------------------------------------------------------------ misure
    {
        "id": "come-rilievi", "gruppo": "misure",
        "q": "Come vengono eseguiti i rilievi fonometrici?",
        "a": "<p>Con un fonometro di classe 1, tarato e certificato, secondo le tecniche del DM 16/03/1998: controllo con il calibratore prima e dopo, condizioni meteorologiche adatte, posizioni e tempi di misura scelti in base alla sorgente. Tutto è riportato nel rapporto di misura allegato alla relazione.</p>",
        "k": "rilievo rilievi fonometrico fonometro misura misurazione come si svolge strumento strumenti taratura classe",
        "u": "guide/rilievo-fonometrico-come-si-svolge.html", "e": "Leggi la guida",
        "c": "Come si misura il rumore?",
    },
    {
        "id": "notte-weekend", "gruppo": "misure",
        "q": "Fate misure di notte o nel fine settimana?",
        "a": "<p>Sì. Il rumore si misura quando c'è: se il problema è la musica del sabato sera o un impianto che parte di notte, la misura si fa in quel momento. Per la legge il periodo notturno va dalle 22 alle 6.</p>",
        "k": "notte notturno notturne sera sabato domenica weekend fine settimana festivo orario orari",
    },
    {
        "id": "superamento", "gruppo": "misure",
        "q": "Che cosa succede se le misure superano i limiti?",
        "a": "<p>Lo diciamo con chiarezza, e insieme al dato indichiamo che cosa si può fare: spostare o schermare un impianto, cambiare orari, isolare, regolare un impianto audio. Se la misura riguarda una pratica, la relazione riporta gli interventi previsti per rientrare nei limiti. A lavori eseguiti, una nuova misura conferma il risultato.</p>",
        "k": "supera superano superamento limiti oltre fuori norma sforamento multa sanzione cosa succede rimedio soluzione bonifica",
        "u": "servizi/bonifica-acustica-puglia.html", "e": "Bonifica acustica",
    },
    {
        "id": "rumore-vicino", "gruppo": "misure",
        "q": "Un rumore mi disturba in casa: che cosa posso fare?",
        "a": "<p>Il primo passo è misurarlo, in casa tua, nelle ore in cui c'è. Se la sorgente è un'attività, come un locale, un negozio o un laboratorio, si verificano i limiti di zona e il criterio differenziale: non più di 5 dB di giorno e 3 dB di notte sopra il rumore residuo. Se è un privato, il riferimento è la normale tollerabilità dell'art. 844 del codice civile.</p><p>Con la relazione in mano si può trattare, fare un esposto o rivolgersi a un avvocato.</p>",
        "k": "vicino vicini disturbo disturba rumore casa sopra condominio esposto denuncia tollerabilita cane tacchi locale sotto",
        "u": "guide/rumore-del-vicino-normale-tollerabilita.html", "e": "Leggi la guida",
        "c": "Un rumore mi disturba",
    },
    {
        "id": "app-telefono", "gruppo": "misure",
        "q": "Posso misurare da solo con un'app del telefono?",
        "a": "<p>Un'app dà un'idea dell'ordine di grandezza, non una misura: il microfono di un telefono non è uno strumento di classe 1 e non ha un certificato di taratura. Davanti a un ente o a un giudice quel numero non regge.</p><p>È invece utile tenere un diario: giorni, orari e durata del rumore. Ci aiuta a scegliere quando misurare.</p>",
        "k": "app telefono cellulare smartphone applicazione misurare solo decibel fai da te",
    },
    # ------------------------------------------------------------ tempi e costi
    {
        "id": "costo", "gruppo": "costi",
        "q": "Quanto costa una valutazione acustica?",
        "a": "<p>Dipende dal tipo di attività, dal numero di misure, dagli orari in cui vanno eseguite e dal contesto. Per questo non pubblichiamo un listino: dopo un primo confronto prepariamo un preventivo scritto, gratuito, con le attività previste voce per voce.</p>",
        "k": "costo costa costi prezzo prezzi tariffa tariffe quanto spesa spendere pagare listino euro",
        "u": "contatti.html#richiesta", "e": "Chiedi un preventivo",
        "c": "Quanto costa?",
    },
    {
        "id": "tempi", "gruppo": "costi",
        "q": "Quanto tempo serve per ricevere la relazione?",
        "a": "<p>Dipende dalla pratica: dal numero di misure, dalla necessità di misurare in giorni o orari precisi, dalle condizioni meteorologiche. I tempi li concordiamo prima di iniziare e li scriviamo nel preventivo.</p><p>Se hai una scadenza, per esempio un'apertura o un termine dell'ente, diccelo subito.</p>",
        "k": "tempo tempi tempistiche vuole giorni settimane urgente urgenza scadenza consegna pronta attesa",
    },
    {
        "id": "preventivo", "gruppo": "costi",
        "q": "Che cosa devo fornire per un preventivo?",
        "a": "<p>Bastano poche informazioni: l'indirizzo e il Comune; che attività o immobile riguarda; che cosa ti è stato richiesto e da chi, meglio se con la copia della richiesta; una planimetria, anche in bozza; orari di attività ed elenco degli impianti, se ci sono.</p><p>Il preventivo è gratuito.</p>",
        "k": "preventivo gratis gratuito documenti fornire servono planimetria informazioni richiedere offerta sopralluogo",
        "u": "contatti.html#richiesta", "e": "Scrivi la tua richiesta",
        "c": "Che cosa serve per un preventivo?",
    },
    {
        "id": "integrazioni", "gruppo": "costi",
        "q": "E se l'ente chiede integrazioni dopo la consegna?",
        "a": "<p>Sui contenuti tecnici della nostra relazione rispondiamo noi, direttamente o tramite il tuo tecnico: chi ha fatto le misure è la persona giusta per spiegarle.</p>",
        "k": "integrazioni integrazione ente comune arpa chiarimenti osservazioni dopo consegna rigetto",
    },
    # ------------------------------------------------------------ solo pannello
    {
        "id": "contatti", "gruppo": "",
        "q": "Come posso contattarvi?",
        "a": "<p>Per telefono al +39 334 874 8771 (Ing. Emanuele Sozzi) o al +39 335 668 8997 (Prof. Vincenzo Sozzi), su WhatsApp al primo numero, per email a info@sozzisound.it, oppure con il modulo del sito.</p>",
        "k": "contatto contatti contattare telefono numero chiamare email mail scrivere whatsapp parlare appuntamento",
        "u": "contatti.html", "e": "Vai ai contatti",
    },
    {
        "id": "sede", "gruppo": "",
        "q": "Dove si trova lo studio?",
        "a": "<p>A Ostuni, in provincia di Brindisi: Via Tenente Antonio Specchia, 30. Sopralluoghi e misure li facciamo dove serve, in tutta la Puglia e, su incarico, nel resto d'Italia.</p>",
        "k": "sede studio ufficio indirizzo ostuni dove siete trovate venire",
        "u": "chi-siamo.html", "e": "Chi siamo",
    },
    {
        "id": "servizi", "gruppo": "",
        "q": "Di che cosa vi occupate?",
        "a": "<p>Di acustica, in tutte le sue applicazioni pratiche: impatto e clima acustico, locali con musica ed eventi, impianti sportivi, requisiti acustici passivi e collaudi degli edifici, rumore di impianti e attività, perizie fonometriche, rumore nei luoghi di lavoro, supporto agli enti pubblici.</p>",
        "k": "servizi servizio occupate fate offrite attivita elenco cosa fate consulenza",
        "u": "servizi/", "e": "Tutti i servizi",
    },
    {
        "id": "chi-siete", "gruppo": "",
        "q": "Chi siete?",
        "a": "<p>Due tecnici competenti in acustica iscritti all'elenco nazionale: l'Ing. Emanuele Sozzi, ingegnere aerospaziale, e il Prof. Vincenzo Sozzi, fisico. Lo studio ha sede a Ostuni.</p>",
        "k": "chi siete siamo professionisti ingegnere fisico emanuele vincenzo sozzi sozzisound curriculum esperienza",
        "u": "chi-siamo.html", "e": "Chi siamo",
    },
]

# Parole che da sole identificano la domanda. Usare solo termini specifici:
# una parola generica qui fa rispondere il pannello a sproposito.
FORTI = {
    "chi-firma": "firma firmare firmata enteca abilitato abilitazione",
    "differenza-impatto-clima": "clima",
    "previsionale-collaudo": "collaudo previsionale",
    "fuori-puglia": "fuori basilicata trasferta",
    "privati": "privato privati condominio",
    "tribunale": "tribunale giudice causa giudizio ctu ctp",
    "quando-impatto": "obbligatorio obbligo suap",
    "esonero": "esonero esonerato esente esenzione",
    "musica-locale": "musica karaoke discoteca",
    "deroga-evento": "deroga evento concerto sagra festival manifestazione",
    "ristrutturare-casa": "ristrutturare ristrutturazione permesso",
    "classificazione": "classificazione zonizzazione classe",
    "come-rilievi": "rilievo rilievi fonometro fonometrico",
    "notte-weekend": "notte notturno notturne sabato domenica weekend festivo",
    "superamento": "supera superano superamento sforamento",
    "rumore-vicino": "vicino vicini disturba disturbo esposto",
    "app-telefono": "app applicazione smartphone cellulare",
    "costo": "costo costa costi prezzo prezzi tariffa tariffe listino",
    "tempi": "tempistiche giorni settimane urgente urgenza scadenza",
    "preventivo": "preventivo",
    "integrazioni": "integrazioni chiarimenti",
    "contatti": "contatto contatti contattare telefono numero chiamare email mail whatsapp",
    "sede": "sede indirizzo ufficio",
    "servizi": "servizi servizio",
    "chi-siete": "curriculum",
}

for _v in FAQ:
    _v["f"] = FORTI.get(_v["id"], "")

PER_ID = {v["id"]: v for v in FAQ}

# Domande mostrate nella home, nell'ordine
IN_HOME = ["quando-impatto", "esonero", "chi-firma", "differenza-impatto-clima", "come-rilievi",
           "costo", "tempi", "preventivo", "fuori-puglia", "tribunale"]

# Pulsanti proposti all'apertura del pannello "Risposte rapide"
SUGGERITE = ["quando-impatto", "esonero", "costo", "preventivo", "rumore-vicino", "fuori-puglia"]

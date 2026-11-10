"""Pagine territoriali: le sei province e i comuni più vicini alla sede.

Regole: il contesto descrive solo caratteri noti e generali di ciascun luogo.
Nessuna affermazione sulla classificazione acustica di un Comune, nessun nome di
attività, evento o committente.
"""

# casi: (titolo, testo, slug del servizio collegato)

PROVINCE = [
    {
        "chiave": "bari",
        "nome": "Bari",
        "dove": "a Bari",
        "area": "Bari e provincia",
        "nome_mappa": "Bari",
        "lat": 41.117, "lon": 16.871, "etichetta": (8, -9, "start"),
        "title": "Tecnico competente in acustica a Bari | SozziSound",
        "descrizione": "Tecnico competente in acustica a Bari e provincia: impatto e clima acustico, requisiti acustici passivi, perizie fonometriche, rumore nei luoghi di lavoro.",
        "sommario": "Misure, valutazioni e relazioni tecniche per imprese, professionisti e privati a Bari e in tutta la città metropolitana.",
        "contesto": """<p>Bari e il suo hinterland concentrano attività commerciali, locali di intrattenimento e cantieri in ambito urbano. I casi più frequenti riguardano l'impatto acustico di nuove attività, il clima acustico per gli interventi edilizi e le perizie per le contestazioni di vicinato in condominio.</p>
<p>La città metropolitana è anche la più varia della regione. La costa tra Polignano e Monopoli vive di turismo e ricevimenti, la Valle d'Itria di ospitalità diffusa, la Murgia di produzione e artigianato: cambiano le sorgenti, e con loro le valutazioni da fare.</p>""",
        "casi": [
            ("Un locale al piano terra di un condominio", "Impianti, cucina e musica passano attraverso solai e facciate. Verifichiamo prima dell'apertura che cosa arriverà agli appartamenti.", "rumore-attivita-commerciali-artigianali-puglia"),
            ("Un edificio residenziale lungo una strada trafficata", "Misuriamo il rumore del sito e lo traduciamo in prestazioni per le facciate.", "clima-acustico-puglia"),
            ("Una lite per il rumore di un impianto", "Misure nell'abitazione disturbata e relazione utilizzabile nella trattativa o in giudizio.", "perizie-acustiche-controversie-puglia"),
            ("Un capannone in zona industriale", "La relazione acustica per nuove attività, ampliamenti e modifiche.", "relazione-acustica-attivita-produttive-puglia"),
        ],
        "arrivo": "Raggiungiamo Bari e i comuni della provincia dalla sede di Ostuni lungo la statale adriatica.",
    },
    {
        "chiave": "bat",
        "nome": "Barletta-Andria-Trani",
        "dove": "nella provincia di Barletta-Andria-Trani",
        "area": "Barletta, Andria, Trani e provincia",
        "nome_mappa": "Barletta-Andria-Trani",
        "lat": 41.27, "lon": 16.33, "etichetta": (-6, 17, "middle"),
        "title": "Tecnico competente in acustica a Barletta, Andria e Trani",
        "descrizione": "Tecnico competente in acustica nella provincia di Barletta-Andria-Trani: impatto acustico, requisiti acustici passivi, collaudi, rumore nei luoghi di lavoro.",
        "sommario": "Misure, valutazioni e relazioni tecniche per imprese, professionisti e privati a Barletta, Andria, Trani e negli altri comuni della provincia.",
        "contesto": """<p>Nella provincia di Barletta-Andria-Trani, tra cantieri, attività artigianali e commerciali, i casi più comuni riguardano l'impatto acustico delle nuove aperture, i requisiti acustici passivi negli interventi edilizi e i collaudi a fine lavori.</p>
<p>Sono città vicine tra loro, con zone produttive attive: laboratori di lavorazione della pietra, opifici, frantoi, caseifici. Lavorazioni rumorose per chi le svolge e, a volte, per chi abita accanto. Sul mare, d'estate, tornano i temi dei lungomare: locali, musica, serate.</p>""",
        "casi": [
            ("Un laboratorio o un opificio", "Misure dell'esposizione dei lavoratori e indicazioni per ridurla alla fonte.", "sicurezza-rumore-lavoro-puglia"),
            ("Un nuovo edificio residenziale", "La relazione acustica da allegare alla domanda di permesso di costruire.", "relazione-acustica-permesso-costruire-puglia"),
            ("La fine di un cantiere", "Le misure in opera degli isolamenti, prima della consegna.", "collaudo-acustico-edifici-puglia"),
            ("Un locale sul lungomare", "La documentazione di impatto acustico per chi lavora con la musica.", "impatto-acustico-locali-musica-puglia"),
        ],
        "arrivo": "Dalla sede di Ostuni organizziamo sopralluogo e misure in un'unica uscita, concordata per tempo.",
    },
    {
        "chiave": "brindisi",
        "nome": "Brindisi",
        "dove": "a Brindisi",
        "area": "Brindisi e provincia",
        "nome_mappa": "Brindisi",
        "lat": 40.632, "lon": 17.936, "etichetta": (9, 4, "start"),
        "title": "Tecnico competente in acustica a Brindisi | SozziSound",
        "descrizione": "Tecnico competente in acustica a Brindisi e provincia, con sede a Ostuni: impatto e clima acustico, locali ed eventi, rumore nei luoghi di lavoro, perizie.",
        "sommario": "È la nostra provincia: la sede è a Ostuni. Misure, valutazioni e relazioni tecniche per imprese, professionisti e privati a Brindisi e in tutti i comuni del territorio.",
        "contesto": """<p>Tra area industriale, porto e aeroporto, a Brindisi le richieste più frequenti riguardano l'impatto acustico di impianti e infrastrutture, il clima acustico per i nuovi insediamenti e l'esposizione al rumore nei contesti produttivi.</p>
<p>Il resto della provincia ha un altro passo. A nord, tra Ostuni, Fasano, Cisternino e Carovigno, prevalgono turismo, masserie, ricevimenti e locali estivi. Nell'entroterra, tra Francavilla Fontana, Ceglie Messapica e Mesagne, commercio, artigianato e centri storici tornati a vivere di sera.</p>""",
        "casi": [
            ("Un'azienda dell'area industriale", "Relazione acustica per nuove attività e misure dell'esposizione dei lavoratori.", "relazione-acustica-attivita-produttive-puglia"),
            ("Una masseria o una sala ricevimenti", "La documentazione di impatto acustico per chi ospita eventi con musica.", "impatto-acustico-locali-musica-puglia"),
            ("Una rassegna o una festa in piazza", "La parte tecnica della richiesta di autorizzazione in deroga.", "deroga-acustica-eventi-puglia"),
            ("Nuove residenze vicino a strade e ferrovia", "La valutazione del clima acustico dell'area.", "clima-acustico-puglia"),
        ],
        "arrivo": "Per sopralluoghi e misure, anche serali e notturne, siamo già sul posto.",
    },
    {
        "chiave": "foggia",
        "nome": "Foggia",
        "dove": "a Foggia",
        "area": "Foggia e provincia",
        "nome_mappa": "Foggia",
        "lat": 41.462, "lon": 15.544, "etichetta": (9, 4, "start"),
        "title": "Tecnico competente in acustica a Foggia | SozziSound",
        "descrizione": "Tecnico competente in acustica a Foggia e provincia: impatto acustico di attività e impianti, clima acustico, rumore nei luoghi di lavoro, bonifica acustica.",
        "sommario": "Misure, valutazioni e relazioni tecniche per imprese, professionisti e privati a Foggia, nel Tavoliere, sui Monti Dauni e sul Gargano.",
        "contesto": """<p>Nella provincia di Foggia, tra attività agricole, industriali e artigianali, i servizi più richiesti sono l'impatto acustico delle nuove attività, il clima acustico e le misure dell'esposizione al rumore nei siti produttivi.</p>
<p>La Capitanata è anche terra di impianti eolici e fotovoltaici: nei procedimenti autorizzativi la valutazione previsionale del rumore è tra i documenti richiesti. Sul Gargano, d'estate, tornano i temi delle località turistiche: musica, strutture ricettive, campeggi.</p>""",
        "casi": [
            ("Un impianto da fonti rinnovabili", "La valutazione previsionale del rumore nel procedimento autorizzativo e i monitoraggi successivi.", "impatto-acustico-impianti-energetici-puglia"),
            ("Uno stabilimento di trasformazione", "La relazione acustica per nuove attività, ampliamenti e modifiche.", "relazione-acustica-attivita-produttive-puglia"),
            ("Reparti e linee di lavorazione", "Misure dell'esposizione dei lavoratori secondo il D.Lgs 81/2008.", "sicurezza-rumore-lavoro-puglia"),
            ("Una struttura turistica con animazione", "La documentazione di impatto acustico per chi lavora con la musica.", "impatto-acustico-locali-musica-puglia"),
        ],
        "arrivo": "È la provincia più lontana dalla nostra sede: organizziamo sopralluogo e misure in un'unica trasferta, concordata per tempo.",
    },
    {
        "chiave": "lecce",
        "nome": "Lecce",
        "dove": "a Lecce",
        "area": "Lecce e il Salento",
        "nome_mappa": "Lecce",
        "lat": 40.352, "lon": 18.169, "etichetta": (9, 4, "start"),
        "title": "Tecnico competente in acustica a Lecce | SozziSound",
        "descrizione": "Tecnico competente in acustica a Lecce e nel Salento: impatto acustico di locali, lidi ed eventi, deroghe, bonifica acustica, perizie, requisiti passivi.",
        "sommario": "Misure, valutazioni e relazioni tecniche per imprese, professionisti e privati a Lecce e in tutto il Salento.",
        "contesto": """<p>Nel Salento la stagione turistica porta con sé molte richieste di valutazione di impatto acustico per locali, eventi e strutture ricettive, e interventi di bonifica per le attività che disturbano nei centri storici e sulla costa.</p>
<p>Da giugno a settembre cambia tutto: i lidi diventano locali, le masserie ospitano ricevimenti, i centri storici restano pieni fino a notte. È il periodo in cui arrivano gli esposti, ed è prima di allora che conviene avere i documenti in ordine.</p>""",
        "casi": [
            ("Un lido con musica", "La documentazione di impatto acustico e la verifica dell'impianto audio, prima della stagione.", "impatto-acustico-locali-musica-puglia"),
            ("Un evento estivo in piazza", "La parte tecnica della richiesta di autorizzazione in deroga al Comune.", "deroga-acustica-eventi-puglia"),
            ("Un locale del centro storico con un esposto", "Misure nelle abitazioni e progetto degli interventi per rientrare nei limiti.", "bonifica-acustica-puglia"),
            ("Gli impianti di una struttura ricettiva", "Misura del rumore di pompe di calore e gruppi frigo, e indicazioni per ridurlo.", "rumore-impianti-tecnici-puglia"),
        ],
        "arrivo": "Dalla sede di Ostuni raggiungiamo Lecce lungo la superstrada; per il basso Salento concordiamo le uscite per tempo.",
    },
    {
        "chiave": "taranto",
        "nome": "Taranto",
        "dove": "a Taranto",
        "area": "Taranto e provincia",
        "nome_mappa": "Taranto",
        "lat": 40.476, "lon": 17.230, "etichetta": (-9, 16, "end"),
        "title": "Tecnico competente in acustica a Taranto | SozziSound",
        "descrizione": "Tecnico competente in acustica a Taranto e provincia: impatto acustico di attività produttive, clima acustico, bonifica acustica, rumore nei luoghi di lavoro.",
        "sommario": "Misure, valutazioni e relazioni tecniche per imprese, professionisti e privati a Taranto e in tutta la provincia.",
        "contesto": """<p>Il tessuto industriale e portuale di Taranto richiede spesso valutazioni di impatto e di clima acustico per gli impianti produttivi, piani di bonifica acustica e misure dell'esposizione al rumore dei lavoratori.</p>
<p>Accanto alla grande industria c'è la provincia: la Valle d'Itria con Martina Franca, la costa ionica con le sue strutture balneari, i centri dell'entroterra con laboratori e piccole imprese. Scale diverse, stesse regole.</p>""",
        "casi": [
            ("Reparti con macchine e impianti rumorosi", "Misure dell'esposizione dei lavoratori e programma di riduzione.", "sicurezza-rumore-lavoro-puglia"),
            ("Una nuova attività produttiva", "La relazione acustica da allegare alla pratica.", "relazione-acustica-attivita-produttive-puglia"),
            ("Un superamento dei limiti da risolvere", "Individuazione delle sorgenti e progetto degli interventi.", "bonifica-acustica-puglia"),
            ("Uno stabilimento balneare con musica", "La documentazione di impatto acustico per la stagione.", "impatto-acustico-locali-musica-puglia"),
        ],
        "arrivo": "Dalla sede di Ostuni raggiungiamo Taranto attraverso la Valle d'Itria.",
    },
]

_ORDINE = ["bari", "lecce", "taranto", "brindisi", "foggia", "bat"]
PROVINCE.sort(key=lambda p: _ORDINE.index(p["chiave"]))

for _p in PROVINCE:
    _p["slug"] = f"tecnico-acustica-{_p['chiave']}"
    _p["url"] = f"citta/{_p['slug']}.html"


COMUNI = [
    {
        "nome": "Ostuni", "prov": "brindisi", "lat": 40.729, "lon": 17.577,
        "descrizione": "Tecnici competenti in acustica con sede a Ostuni: impatto acustico per masserie, locali ed eventi, pratiche edilizie, perizie fonometriche. Preventivo gratuito.",
        "sommario": "Ostuni è la nostra sede. Qui il rumore ha un calendario: d'inverno un paese tranquillo, d'estate una delle mete più frequentate della Puglia.",
        "contesto": """<p>Il centro storico è fatto di vicoli stretti, case una sopra l'altra e locali al piano terra: basta poco perché una serata arrivi nelle camere da letto di qualcuno. Nell'agro, masserie e ville ospitano ricevimenti con musica all'aperto, spesso in zone dove di notte il rumore di fondo è molto basso. Lungo la costa lavorano lidi, villaggi e campeggi.</p>
<p>Accanto al turismo c'è la città di tutti i giorni: la zona artigianale, le attività commerciali lungo le strade di accesso, i cantieri di ristrutturazione e le nuove costruzioni.</p>""",
        "casi": [
            ("Una masseria che ospita ricevimenti", "Con la musica all'aperto serve capire fin dove arriva il suono, e a che ora. Lo misuriamo e lo mettiamo nella documentazione di impatto acustico.", "impatto-acustico-locali-musica-puglia"),
            ("Un locale nel centro storico", "Tra vicoli e volte il suono si comporta in modo particolare. Verifichiamo i livelli nelle case vicine e, se serve, progettiamo i rimedi.", "bonifica-acustica-puglia"),
            ("Una serata o una rassegna estiva", "Prepariamo la parte tecnica della richiesta di autorizzazione in deroga da presentare al Comune.", "deroga-acustica-eventi-puglia"),
            ("Una casa da costruire", "Seguiamo la relazione acustica del progetto e le verifiche a fine lavori.", "relazione-acustica-permesso-costruire-puglia"),
        ],
        "arrivo": "Siamo di casa: sopralluoghi e misure, anche serali e notturne, si organizzano senza trasferte.",
    },
    {
        "nome": "Fasano", "prov": "brindisi", "lat": 40.836, "lon": 17.358,
        "descrizione": "Tecnico competente in acustica a Fasano: impatto acustico per masserie, resort e sale ricevimenti, aziende della zona industriale, impianti. Preventivo gratuito.",
        "sommario": "Tra la collina della Selva e il mare di Savelletri e Torre Canne, Fasano mette insieme ospitalità, ricevimenti e una zona industriale attiva.",
        "contesto": """<p>Lungo la costa e nella piana degli ulivi lavorano masserie, resort e sale ricevimenti. La musica all'aperto è parte del mestiere, e gli ospiti delle strutture vicine sono i primi a sentirla. Qui il tema acustico ha due facce: non disturbare e non essere disturbati.</p>
<p>Sul versante opposto c'è la Fasano produttiva, con la zona industriale e le attività lungo la statale, dove contano il rumore verso l'esterno e l'esposizione dei lavoratori. E c'è la collina, con le frazioni residenziali dove d'estate basta un impianto mal posizionato per accendere una lite.</p>""",
        "casi": [
            ("Una struttura ricettiva con eventi", "Valutiamo l'impatto della musica verso le case e verso le altre strutture, e indichiamo orari e livelli sostenibili.", "impatto-acustico-locali-musica-puglia"),
            ("Un'azienda della zona industriale", "Relazione acustica per nuove attività e ampliamenti.", "relazione-acustica-attivita-produttive-puglia"),
            ("Pompe di calore e gruppi frigo", "Negli alberghi e nei ristoranti gli impianti lavorano giorno e notte: ne misuriamo il rumore e indichiamo come ridurlo.", "rumore-impianti-tecnici-puglia"),
            ("Un lido con dj set", "Verifica dell'impianto audio secondo il DPCM 215/1999.", "verifica-livelli-sonori-locali-puglia"),
        ],
        "arrivo": "È tra i comuni più vicini alla nostra sede.",
    },
    {
        "nome": "Monopoli", "prov": "bari", "lat": 40.950, "lon": 17.300,
        "descrizione": "Tecnico competente in acustica a Monopoli: rumore nei luoghi di lavoro, impatto acustico di locali e attività produttive, clima acustico. Preventivo gratuito.",
        "sommario": "Un porto, un centro storico affacciato sul mare, una zona industriale importante e decine di contrade: a Monopoli le sorgenti di rumore non mancano.",
        "contesto": """<p>Il centro storico e il porto concentrano ristoranti e locali serali a pochi metri dalle abitazioni. A sud, la costa ospita lidi e locali che d'estate lavorano fino a tardi. Nelle contrade dell'agro, masserie e ville per ricevimenti convivono con chi in campagna abita tutto l'anno.</p>
<p>Poi c'è la Monopoli che produce: stabilimenti, officine, logistica. Per chi costruisce o amplia un capannone la relazione acustica entra nella pratica; per chi ci lavora dentro conta l'esposizione al rumore.</p>""",
        "casi": [
            ("Uno stabilimento con reparti rumorosi", "Misuriamo l'esposizione dei lavoratori, mansione per mansione.", "sicurezza-rumore-lavoro-puglia"),
            ("Un locale affacciato sul porto", "Che cosa serve per lavorare con la musica, e come restare nei limiti verso le case.", "impatto-acustico-locali-musica-puglia"),
            ("Una villa per ricevimenti in contrada", "Per gli eventi oltre l'ordinario prepariamo la richiesta di deroga.", "deroga-acustica-eventi-puglia"),
            ("Residenze vicino alla ferrovia o alla statale", "La valutazione del clima acustico, prima di progettare le facciate.", "clima-acustico-puglia"),
        ],
        "arrivo": "La statale adriatica la collega direttamente a Ostuni.",
    },
    {
        "nome": "Martina Franca", "prov": "taranto", "lat": 40.705, "lon": 17.336,
        "descrizione": "Tecnico competente in acustica a Martina Franca: deroghe per spettacoli ed eventi, rumore nei laboratori e nelle aziende, impatto acustico. Preventivo gratuito.",
        "sommario": "La città più grande della Valle d'Itria: un centro storico barocco che d'estate diventa palcoscenico, e un tessuto produttivo che lavora tutto l'anno.",
        "contesto": """<p>D'estate piazze, chiostri e cortili ospitano concerti e spettacoli all'aperto, in mezzo alle case. Per chi organizza la domanda è sempre la stessa: fino a che ora, e a quale livello. La risposta sta nell'autorizzazione del Comune e nella documentazione tecnica che la accompagna.</p>
<p>Tutto l'anno lavorano invece i laboratori di confezioni e le aziende della zona industriale, dove macchine e impianti pongono il tema dell'esposizione dei lavoratori e, verso l'esterno, quello del rumore ai confini. Nelle contrade, tra trulli e masserie, crescono le strutture ricettive e i ricevimenti in campagna.</p>""",
        "casi": [
            ("Uno spettacolo in piazza o in un chiostro", "La relazione tecnica per l'autorizzazione in deroga, con orari e livelli sostenibili.", "deroga-acustica-eventi-puglia"),
            ("Un laboratorio di confezioni", "Misure dell'esposizione al rumore di chi lavora alle macchine.", "sicurezza-rumore-lavoro-puglia"),
            ("Una nuova attività in zona industriale", "La relazione acustica da allegare alla pratica.", "relazione-acustica-attivita-produttive-puglia"),
            ("Un ristorante con tavoli all'aperto", "Impianti, cucina e avventori: che cosa arriva alle finestre vicine, e come ridurlo.", "rumore-attivita-commerciali-artigianali-puglia"),
        ],
        "arrivo": "Dalla sede di Ostuni ci si arriva attraverso la Valle d'Itria.",
    },
    {
        "nome": "Cisternino", "prov": "brindisi", "lat": 40.741, "lon": 17.426,
        "descrizione": "Tecnico competente in acustica a Cisternino: rumore di ristoranti e impianti nel centro storico, eventi, strutture ricettive in Valle d'Itria. Preventivo gratuito.",
        "sommario": "Un borgo piccolo e molto frequentato, dove d'estate si cena all'aperto fino a tardi e le case sono a un passo dai tavoli.",
        "contesto": """<p>Il centro storico di Cisternino è compatto: vicoli, piazzette, abitazioni sopra e accanto ai locali. La ristorazione serale all'aperto è la sua identità, e con lei arrivano le voci, la musica di sottofondo, gli impianti di aspirazione e i gruppi frigo che lavorano a ridosso delle finestre.</p>
<p>Fuori dal borgo, le contrade della Valle d'Itria sono punteggiate di trulli e casali trasformati in strutture ricettive. Sono luoghi scelti per il silenzio: un impianto rumoroso o una festa in una proprietà vicina si notano subito.</p>""",
        "casi": [
            ("Cappe, aspirazioni e gruppi frigo", "Misuriamo il rumore degli impianti dove dà fastidio e indichiamo l'intervento più semplice che lo risolve.", "rumore-impianti-tecnici-puglia"),
            ("Musica dal vivo in piazzetta", "La documentazione tecnica per l'autorizzazione del Comune.", "deroga-acustica-eventi-puglia"),
            ("Una struttura ricettiva in contrada", "Piscina, climatizzazione, eventi: stimiamo prima che cosa sentiranno i vicini.", "acustica-previsionale-puglia"),
            ("Una contestazione tra confinanti", "Misure in casa e relazione tecnica, per trattare con dati alla mano.", "perizie-acustiche-controversie-puglia"),
        ],
        "arrivo": "Pochi chilometri di strada dalla nostra sede.",
    },
    {
        "nome": "Ceglie Messapica", "prov": "brindisi", "lat": 40.646, "lon": 17.517,
        "descrizione": "Tecnico competente in acustica a Ceglie Messapica: rumore di ristoranti e laboratori, sale ricevimenti, comfort acustico delle sale. Preventivo gratuito.",
        "sommario": "Una città conosciuta per la sua cucina, con un centro storico vivo di sera e una campagna fitta di masserie.",
        "contesto": """<p>A Ceglie la ristorazione è una cosa seria, e buona parte si concentra nel centro storico, tra case abitate. Cucine, cappe e unità esterne lavorano a lungo; d'estate si aggiungono i tavoli all'aperto e qualche serata con musica.</p>
<p>Nell'agro, masserie e sale ricevimenti ospitano matrimoni ed eventi. In paese e nella zona artigianale lavorano laboratori, officine e piccole imprese, per le quali il tema è doppio: il rumore verso i vicini e quello a cui sono esposti i dipendenti.</p>""",
        "casi": [
            ("Un ristorante tra le case", "Impianti e orari sono la prima fonte di esposti: li verifichiamo prima che lo diventino.", "rumore-attivita-commerciali-artigianali-puglia"),
            ("Una sala troppo rumorosa", "Quando in sala non ci si sente parlare il problema è il riverbero: lo misuriamo e progettiamo la correzione.", "acustica-aule-uffici-sale-puglia"),
            ("Una sala ricevimenti in campagna", "La documentazione di impatto acustico per gli eventi con musica.", "impatto-acustico-locali-musica-puglia"),
            ("Un'officina o un laboratorio", "Misure dell'esposizione dei lavoratori al rumore.", "sicurezza-rumore-lavoro-puglia"),
        ],
        "arrivo": "È a pochi chilometri dalla nostra sede, verso l'interno.",
    },
    {
        "nome": "Carovigno", "prov": "brindisi", "lat": 40.707, "lon": 17.657,
        "descrizione": "Tecnico competente in acustica a Carovigno, Torre Santa Sabina e Specchiolla: villaggi, lidi, campeggi, eventi estivi, case vacanza. Preventivo gratuito.",
        "sommario": "Un paese d'entroterra con una lunga costa: Torre Santa Sabina, Specchiolla e, poco oltre, la riserva di Torre Guaceto.",
        "contesto": """<p>D'estate la vita si sposta verso il mare. Lungo la costa lavorano lidi, villaggi turistici e campeggi, con animazione e musica serale; nelle marine, seconde case e locali stanno fianco a fianco. La vicinanza di un'area naturale protetta rende il contesto più delicato: è un elemento da considerare quando si progetta un'attività o un evento.</p>
<p>In paese, il centro storico attorno al castello ospita serate ed eventi. Lungo le strade verso Ostuni, San Vito dei Normanni e Brindisi si trovano attività commerciali, artigianali e sale ricevimenti.</p>""",
        "casi": [
            ("Un villaggio o un campeggio con animazione", "La documentazione di impatto acustico per le attività con diffusione sonora.", "impatto-acustico-locali-musica-puglia"),
            ("Un lido che fa musica", "Verifica dell'impianto e taratura del limitatore.", "verifica-livelli-sonori-locali-puglia"),
            ("Una serata nel centro storico", "La parte tecnica della richiesta di deroga.", "deroga-acustica-eventi-puglia"),
            ("Case vacanza vicino a un locale", "Misuriamo il rumore esistente prima di costruire o di comprare.", "clima-acustico-puglia"),
        ],
        "arrivo": "Pochi chilometri separano Carovigno dalla nostra sede.",
    },
    {
        "nome": "Francavilla Fontana", "prov": "brindisi", "lat": 40.531, "lon": 17.585,
        "title": "Tecnico competente in acustica a Francavilla Fontana",
        "descrizione": "Tecnico competente in acustica a Francavilla Fontana: rumore di attività commerciali e artigianali, capannoni, pratiche edilizie, collaudi. Preventivo gratuito.",
        "sommario": "Uno dei centri più grandi dell'entroterra brindisino: commercio, artigianato, una zona industriale e un tessuto residenziale che si rinnova.",
        "contesto": """<p>Francavilla è una città di servizi e di lavoro. Attorno al centro si distribuiscono supermercati, officine, carrozzerie, autolavaggi, laboratori: attività utili e rumorose, spesso inserite tra le case. Gruppi frigo, compressori, aspirazioni e operazioni di carico e scarico sono le sorgenti che più spesso finiscono in un esposto.</p>
<p>Nella zona industriale il tema è quello delle nuove attività e degli ampliamenti, con la relazione acustica da allegare alla pratica, e quello dell'esposizione dei lavoratori. In città si costruisce e si ristruttura: per i nuovi edifici entra in gioco la relazione acustica di progetto.</p>""",
        "casi": [
            ("Un supermercato o un'attività con gruppi frigo", "Misure al confine e nelle case vicine, e soluzioni per impianti e orari.", "rumore-attivita-commerciali-artigianali-puglia"),
            ("Un capannone da costruire o ampliare", "La relazione acustica per la pratica.", "relazione-acustica-attivita-produttive-puglia"),
            ("Una palazzina in progetto", "La relazione asseverata per il permesso di costruire.", "relazione-acustica-permesso-costruire-puglia"),
            ("Un edificio appena finito", "Il collaudo in opera degli isolamenti.", "collaudo-acustico-edifici-puglia"),
        ],
        "arrivo": "È nell'entroterra, a sud della nostra sede.",
    },
    {
        "nome": "Mesagne", "prov": "brindisi", "lat": 40.559, "lon": 17.808,
        "descrizione": "Tecnico competente in acustica a Mesagne: locali ed eventi nel centro storico, requisiti acustici dei nuovi edifici, attività artigianali. Preventivo gratuito.",
        "sommario": "Un centro storico recuperato e tornato a vivere di sera, a pochi chilometri da Brindisi.",
        "contesto": """<p>Negli ultimi anni il cuore antico di Mesagne si è riempito di ristoranti, locali e iniziative culturali. Le serate si svolgono tra case abitate, in strade strette dove il suono rimbalza. È il caso tipico in cui conviene sapere prima quanto rumore arriverà alle finestre, e non dopo il primo esposto.</p>
<p>Fuori dal centro, lungo la statale tra Brindisi e Taranto, si trovano la zona artigianale e commerciale e le attività di lavorazione dei prodotti agricoli. La vicinanza al capoluogo porta anche nuove residenze, per le quali contano i requisiti acustici dell'edificio.</p>""",
        "casi": [
            ("Un locale con musica dal vivo", "La documentazione di impatto acustico e i livelli a cui si può lavorare.", "impatto-acustico-locali-musica-puglia"),
            ("Una rassegna nelle piazze del centro", "La relazione per l'autorizzazione in deroga.", "deroga-acustica-eventi-puglia"),
            ("Un nuovo edificio residenziale", "Il calcolo dei requisiti acustici passivi, prima del cantiere.", "requisiti-acustici-passivi-puglia"),
            ("Un'attività artigianale con macchinari", "Impatto verso l'esterno e relazione per la pratica.", "valutazione-impatto-acustico-puglia"),
        ],
        "arrivo": "Si raggiunge dalla nostra sede attraverso l'entroterra brindisino.",
    },
    {
        "nome": "Locorotondo", "prov": "bari", "lat": 40.755, "lon": 17.326,
        "descrizione": "Tecnico competente in acustica a Locorotondo: impianti e locali nel centro storico, cantine e aziende, strutture ricettive in contrada. Preventivo gratuito.",
        "sommario": "Un borgo raccolto su un'altura, circondato da contrade abitate e vigneti: qui il silenzio fa parte del paesaggio, e si nota quando manca.",
        "contesto": """<p>Il centro storico è piccolo e densamente abitato. Ristoranti, enoteche e locali lavorano a contatto diretto con le case, e d'estate le serate si allungano all'aperto. Bastano un impianto di aspirazione mal posizionato o una diffusione sonora non regolata per creare un problema.</p>
<p>Tutt'intorno, le contrade della Valle d'Itria uniscono residenze, trulli destinati all'ospitalità, cantine e aziende agricole. In campagna il rumore di fondo notturno è molto basso: anche sorgenti modeste, come una pompa di calore, l'impianto di una piscina o una festa privata, si sentono a distanza.</p>""",
        "casi": [
            ("Una cantina o un'azienda con impianti", "Celle, compressori, linee di lavorazione: il rumore verso l'esterno e la relazione per la pratica.", "relazione-acustica-attivita-produttive-puglia"),
            ("Pompe di calore e impianti di piscina", "Misura, verifica dei limiti e indicazioni per collocarli e schermarli.", "rumore-impianti-tecnici-puglia"),
            ("Un locale del centro storico", "Impianti, orari e musica di sottofondo, verificati nelle abitazioni vicine.", "rumore-attivita-commerciali-artigianali-puglia"),
            ("Ricevimenti in contrada", "La documentazione di impatto acustico per chi ospita eventi con musica.", "impatto-acustico-locali-musica-puglia"),
        ],
        "arrivo": "Dalla nostra sede ci si arriva passando per Cisternino.",
    },
    {
        "nome": "Alberobello", "prov": "bari", "lat": 40.784, "lon": 17.237,
        "descrizione": "Tecnico competente in acustica ad Alberobello: impianti e attività nei trulli, ristoranti, strutture ricettive, eventi, sale ricevimenti. Preventivo gratuito.",
        "dove": "ad Alberobello",
        "sommario": "Un sito UNESCO visitato tutto l'anno, dove botteghe, ristoranti e strutture ricettive occupano gli stessi trulli in cui si abita.",
        "contesto": """<p>Ad Alberobello il turismo non ha una vera bassa stagione. Nei rioni dei trulli le attività sono una accanto all'altra e i muri, per quanto spessi, separano spazi piccoli: un impianto di climatizzazione, una cucina o la musica di un locale riguardano subito i vicini e gli ospiti delle strutture accanto.</p>
<p>Chi apre o trasforma un'attività in un contesto tutelato ha poco margine per interventi visibili. Gli impianti vanno scelti e collocati bene fin dall'inizio, perché schermarli dopo non è sempre possibile. Fuori dal centro, lungo le strade verso Locorotondo, Noci e Putignano, si trovano sale ricevimenti, strutture più grandi e attività artigianali.</p>""",
        "casi": [
            ("Gli impianti di una struttura nei trulli", "Stimiamo il rumore prima dell'installazione, quando cambiare modello o posizione è ancora facile.", "acustica-previsionale-puglia"),
            ("Un'unità esterna che disturba", "Misura nelle stanze vicine e indicazione del rimedio.", "rumore-impianti-tecnici-puglia"),
            ("Un ristorante tra le abitazioni", "Cucina, aspirazione, tavoli all'aperto: che cosa verificare.", "rumore-attivita-commerciali-artigianali-puglia"),
            ("Un evento in piazza", "La parte tecnica della richiesta di autorizzazione in deroga.", "deroga-acustica-eventi-puglia"),
        ],
        "arrivo": "Dalla nostra sede ci si arriva attraverso la Valle d'Itria.",
    },
    {
        "nome": "Polignano a Mare", "prov": "bari", "lat": 40.996, "lon": 17.220,
        "descrizione": "Tecnico competente in acustica a Polignano a Mare: locali e terrazze con musica, ricevimenti, deroghe per eventi, clima acustico. Preventivo gratuito.",
        "sommario": "Un centro storico a picco sul mare, tra le mete più visitate della regione: terrazze, locali e ricevimenti con vista, e case tutt'intorno.",
        "contesto": """<p>A Polignano si viene per il mare e si resta fino a sera. Le terrazze e le piazzette del centro ospitano ristoranti, locali e ricevimenti; la musica, anche quando è di sottofondo, si propaga bene sull'acqua e tra le facciate. La stagione è lunga, le presenze alte, e gli esposti seguono.</p>
<p>Fuori dal centro storico il territorio cambia. La statale e la ferrovia adriatica corrono vicine all'abitato, e per le nuove residenze il rumore del traffico è un dato di progetto. Nell'entroterra, ville e masserie per eventi lavorano in mezzo a una campagna abitata.</p>""",
        "casi": [
            ("Una terrazza con musica", "La documentazione di impatto acustico e i livelli sostenibili verso le case.", "impatto-acustico-locali-musica-puglia"),
            ("L'impianto audio di un locale", "La verifica prevista dal DPCM 215/1999 e la taratura del limitatore.", "verifica-livelli-sonori-locali-puglia"),
            ("Un ricevimento o un evento all'aperto", "La richiesta di autorizzazione in deroga, con la sua relazione tecnica.", "deroga-acustica-eventi-puglia"),
            ("Residenze vicino a strada e ferrovia", "La valutazione del clima acustico dell'area.", "clima-acustico-puglia"),
        ],
        "arrivo": "La statale adriatica la collega direttamente a Ostuni.",
    },
    {
        "nome": "Gallipoli", "prov": "lecce", "lat": 40.055, "lon": 17.992,
        "descrizione": "Tecnico competente in acustica a Gallipoli: lidi e locali all'aperto, verifica degli impianti audio, deroghe per eventi, bonifica acustica. Preventivo gratuito.",
        "sommario": "D'inverno una città di mare tranquilla, d'estate una delle mete più frequentate del Salento, anche di notte. L'acustica, qui, è un tema stagionale e molto concreto.",
        "contesto": """<p>Lungo i litorali a nord e a sud della città, lidi e locali all'aperto lavorano con impianti audio importanti, dal pomeriggio a notte fonda. Tutt'intorno ci sono alberghi, campeggi, case vacanza e residenze. È il contesto in cui le regole sulla musica contano di più: i livelli all'interno del locale, i limiti verso l'esterno, le autorizzazioni per gli eventi.</p>
<p>Nel centro storico, sull'isola, ristoranti e locali occupano i piani terra di palazzi abitati, e il porto aggiunge le sue attività. Fuori stagione restano i temi di ogni città: impianti, attività commerciali, cantieri, nuove costruzioni.</p>""",
        "casi": [
            ("Un lido o un locale all'aperto", "Verifica dell'impianto, limitatore e documentazione di impatto acustico, prima dell'apertura.", "verifica-livelli-sonori-locali-puglia"),
            ("Una serata o un festival", "La relazione tecnica per l'autorizzazione in deroga.", "deroga-acustica-eventi-puglia"),
            ("Un locale con esposti a carico", "Misure nelle abitazioni e piano di interventi che l'ente possa accettare.", "bonifica-acustica-puglia"),
            ("Una struttura ricettiva disturbata", "Misure e relazione tecnica per far valere le proprie ragioni.", "perizie-acustiche-controversie-puglia"),
        ],
        "arrivo": "È tra i comuni più lontani dalla nostra sede: sopralluogo e misure, comprese quelle notturne, si concordano per tempo.",
    },
    {
        "nome": "Otranto", "prov": "lecce", "lat": 40.144, "lon": 18.491,
        "dove": "a Otranto",
        "descrizione": "Tecnico competente in acustica a Otranto: villaggi turistici e campeggi, locali nel centro storico, spettacoli estivi, impianti. Preventivo gratuito.",
        "sommario": "La città più orientale d'Italia: un centro storico cinto da mura, un porto e una costa di baie, villaggi e campeggi.",
        "contesto": """<p>Dentro le mura, il centro storico concentra in poco spazio ristoranti, locali, botteghe e strutture ricettive, sotto e accanto alle abitazioni. D'estate i bastioni e il lungomare ospitano spettacoli e concerti: eventi temporanei, per i quali orari e livelli si definiscono con il Comune.</p>
<p>Lungo la costa, a nord verso i laghi Alimini e a sud verso le baie, lavorano villaggi turistici, campeggi e lidi con animazione e musica. Sono strutture grandi, in aree di pregio naturalistico, dove il rumore si valuta sia verso gli ospiti sia verso le abitazioni e le strutture vicine.</p>""",
        "casi": [
            ("Un villaggio turistico con animazione", "La documentazione di impatto acustico per le attività con diffusione sonora.", "impatto-acustico-locali-musica-puglia"),
            ("Uno spettacolo estivo", "La parte tecnica della richiesta di autorizzazione in deroga.", "deroga-acustica-eventi-puglia"),
            ("Un locale dentro le mura", "Impianti, orari e musica verificati nelle abitazioni vicine.", "rumore-attivita-commerciali-artigianali-puglia"),
            ("Gli impianti di una struttura ricettiva", "Misura del rumore e indicazioni per ridurlo.", "rumore-impianti-tecnici-puglia"),
        ],
        "arrivo": "È il comune più lontano dalla nostra sede tra quelli di questo elenco: organizziamo sopralluogo e misure in un'unica uscita.",
    },
    {
        "nome": "Altamura", "prov": "bari", "lat": 40.827, "lon": 16.553,
        "dove": "ad Altamura",
        "descrizione": "Tecnico competente in acustica ad Altamura: rumore di forni e laboratori, esposizione dei lavoratori, capannoni, pratiche edilizie. Preventivo gratuito.",
        "sommario": "La città più grande della Murgia: forni, laboratori, le aziende del mobile imbottito e un abitato che continua a crescere.",
        "contesto": """<p>Ad Altamura il pane è un'industria diffusa. Forni e laboratori lavorano di notte, spesso al piano terra di edifici abitati, con impastatrici, celle e impianti di aspirazione. I laboratori per la produzione di pane sono tra le attività che il DPR 227/2011 considera a bassa rumorosità; di notte, in una strada silenziosa, possono comunque creare un problema, e i limiti restano da rispettare.</p>
<p>Nella zona industriale e lungo le strade verso Gravina e Matera si concentrano le aziende del mobile imbottito e la loro filiera, con reparti di taglio, cucitura e assemblaggio. Qui il tema è l'esposizione dei lavoratori, insieme alla relazione acustica per nuovi capannoni e ampliamenti. E la città continua a costruire: per i nuovi edifici residenziali la relazione acustica fa parte del progetto.</p>""",
        "casi": [
            ("Un forno con laboratorio notturno", "Misure nelle abitazioni vicine e soluzioni per impianti e orari.", "rumore-attivita-commerciali-artigianali-puglia"),
            ("Reparti di taglio e assemblaggio", "Misure dell'esposizione dei lavoratori al rumore.", "sicurezza-rumore-lavoro-puglia"),
            ("Un nuovo capannone", "La relazione acustica da allegare alla pratica.", "relazione-acustica-attivita-produttive-puglia"),
            ("Una palazzina in progetto", "La relazione asseverata per il permesso di costruire.", "relazione-acustica-permesso-costruire-puglia"),
        ],
        "arrivo": "È sul versante opposto della regione rispetto alla nostra sede: organizziamo sopralluogo e misure in un'unica uscita.",
    },
]


def _slug(nome):
    return nome.lower().replace(" ", "-")


for _c in COMUNI:
    _c["slug"] = f"tecnico-acustica-{_slug(_c['nome'])}"
    _c["url"] = f"citta/{_c['slug']}.html"
    _c.setdefault("dove", f"a {_c['nome']}")
    _c.setdefault("title", f"Tecnico competente in acustica {_c['dove']} | SozziSound")

PROVINCIA = {p["chiave"]: p for p in PROVINCE}
NOME_PROVINCIA = {"bari": "Città metropolitana di Bari", "bat": "Provincia di Barletta-Andria-Trani",
                  "brindisi": "Provincia di Brindisi", "foggia": "Provincia di Foggia",
                  "lecce": "Provincia di Lecce", "taranto": "Provincia di Taranto"}

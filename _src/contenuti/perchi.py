"""Pagine "Per chi": una per ciascun tipo di interlocutore."""

PERCHI = [
    {
        "slug": "progettisti",
        "nome": "Architetti, ingegneri e geometri",
        "breve": "Relazioni per le pratiche edilizie, requisiti passivi, collaudi.",
        "area": "edilizia",
        "h1": "Per <em>architetti, ingegneri e geometri</em>",
        "title": "Acustica per architetti, ingegneri e geometri | SozziSound",
        "descrizione": "Un riferimento per la parte acustica delle pratiche edilizie in Puglia: relazione asseverata, requisiti acustici passivi in progetto, collaudo a fine lavori.",
        "sommario": "La parte acustica delle vostre pratiche, seguita da tecnici competenti: relazione per il permesso di costruire, requisiti passivi in progetto, collaudo a fine lavori. Un solo interlocutore, tempi concordati pratica per pratica.",
        "chiavi": "architetto ingegnere geometra progettista studio tecnico pratica edilizia collaborazione",
        "situazioni": [
            ("La pratica è quasi pronta e manca la relazione acustica",
             "Ci mandate gli elaborati e verifichiamo che cosa chiede quel Comune. La relazione arriva nel formato che usate per il deposito."),
            ("Il committente chiede garanzie sull'isolamento",
             "Calcoliamo le prestazioni di pareti, solai e facciate prima del cantiere e indichiamo i dettagli da curare."),
            ("Il lotto è vicino a una strada o a una ferrovia",
             "Misuriamo il clima acustico e traduciamo il dato in richieste per le facciate e per la distribuzione degli ambienti."),
            ("A fine lavori serve il collaudo",
             "Eseguiamo le misure in opera e consegniamo la relazione con l'esito per ciascun elemento provato."),
        ],
        "servizi": [
            ("relazione-acustica-permesso-costruire-puglia", "La relazione asseverata prevista dalla L.R. Puglia 3/2002 per il permesso di costruire."),
            ("requisiti-acustici-passivi-puglia", "Il calcolo previsionale di isolamenti e impianti secondo il DPCM 5/12/1997."),
            ("collaudo-acustico-edifici-puglia", "Le misure in opera a edificio finito."),
            ("clima-acustico-puglia", "Il rumore esistente sul sito, per scuole, strutture sanitarie e residenze."),
            ("acustica-previsionale-puglia", "Modelli di calcolo per confrontare alternative di progetto."),
        ],
        "metodo_titolo": "Come lavoriamo con uno studio",
        "metodo": """<p>Lavoriamo sugli elaborati che avete, senza chiedervi di rifarli.</p>
<ul>
<li>Un referente unico per tutte le pratiche dello studio.</li>
<li>Tempi concordati all'inizio di ogni incarico e scritti nel preventivo.</li>
<li>Osservazioni in forma di dettagli e prescrizioni, pronte da riportare nelle tavole.</li>
<li>Risposta diretta alle richieste di integrazione dell'ufficio tecnico.</li>
</ul>""",
        "faq": [
            ("Lavorate anche su progetti piccoli?",
             "Sì. Una villetta o un cambio di destinazione d'uso meritano la stessa cura di un condominio: cambia la quantità di lavoro, non il metodo."),
            ("Possiamo indicarvi come consulenti nel nostro preventivo al cliente?",
             "Certo. Possiamo formulare l'offerta a voi oppure direttamente al committente, come preferite."),
            ("Che cosa vi serve per un preventivo?",
             "Piante, sezioni e prospetti anche in bozza, la destinazione d'uso, il Comune e una riga su che cosa vi è stato chiesto."),
        ],
        "guide": ["legge-regionale-puglia-3-2002-acustica", "requisiti-acustici-passivi-dpcm-5-12-1997", "impatto-acustico-e-clima-acustico-differenze"],
    },
    {
        "slug": "locali-eventi",
        "nome": "Locali, lidi e organizzatori di eventi",
        "breve": "Musica senza esposti: pratiche, limiti, deroghe, verifica degli impianti.",
        "area": "locali",
        "h1": "Per <em>locali, lidi e organizzatori di eventi</em>",
        "title": "Acustica per locali, lidi, ricevimenti ed eventi | SozziSound",
        "descrizione": "Per locali con musica, lidi, masserie, sale ricevimenti e organizzatori di eventi in Puglia: impatto acustico, deroghe, verifica dell'impianto, soluzioni.",
        "sommario": "Lavorare con la musica senza rischiare esposti e sospensioni. Vi diciamo quali documenti servono al vostro locale, a che volume potete arrivare e come restarci.",
        "chiavi": "gestore locale lido organizzatore eventi sala ricevimenti masseria discoteca matrimoni serate",
        "situazioni": [
            ("State per aprire, o per aggiungere la musica",
             "Con un impianto di diffusione sonora la documentazione di impatto acustico torna necessaria anche per bar, ristoranti e stabilimenti balneari."),
            ("È arrivato un esposto dei vicini",
             "Misuriamo nelle abitazioni e al confine, negli orari di attività, e costruiamo un piano di interventi che l'ente possa accettare."),
            ("Organizzate una serata o un festival",
             "Prepariamo la relazione tecnica per l'autorizzazione in deroga del Comune, con orari e livelli sostenibili."),
            ("Vi hanno chiesto la verifica dell'impianto",
             "È la relazione prevista dal DPCM 215/1999 sui livelli sonori all'interno del locale."),
        ],
        "servizi": [
            ("impatto-acustico-locali-musica-puglia", "La documentazione di impatto acustico per chi usa impianti di diffusione sonora."),
            ("deroga-acustica-eventi-puglia", "La relazione tecnica per l'autorizzazione in deroga di eventi temporanei."),
            ("verifica-livelli-sonori-locali-puglia", "La verifica dell'impianto audio secondo il DPCM 215/1999."),
            ("bonifica-acustica-puglia", "Misure e interventi quando i limiti sono superati."),
            ("progettazione-acustica-ambienti-puglia", "Isolamento e acustica interna, per chi sta costruendo o ristrutturando."),
        ],
        "metodo_titolo": "Come lavoriamo con un locale",
        "metodo": """<p>Conosciamo i tempi di una stagione: le pratiche vanno chiuse prima dell'apertura, non a luglio.</p>
<ul>
<li>Sopralluogo negli orari in cui il locale lavora davvero.</li>
<li>Indicazioni operative: dove puntare le casse, a quanto tarare il limitatore, fino a che ora.</li>
<li>Un documento che gestore, tecnico audio e dj possano leggere.</li>
</ul>""",
        "faq": [
            ("Il limitatore risolve tutto?",
             "Risolve il livello dentro il locale e lo rende costante. Verso i vicini contano anche la direzione dei diffusori, le basse frequenze e le aperture: per questo il valore a cui tararlo va calcolato."),
            ("Abbiamo solo musica di sottofondo: serve comunque qualcosa?",
             "La norma parla di impianti di diffusione sonora senza soglie di volume, e i Comuni la applicano in modi diversi. Verifichiamo il regolamento del vostro Comune prima di proporvi qualsiasi cosa."),
            ("Lavoriamo solo d'estate: cambia qualcosa?",
             "Cambia il calendario, non le regole. Conviene fare misure e pratica nei mesi di chiusura, così l'apertura trova tutto in ordine."),
        ],
        "guide": ["musica-nei-locali-limiti-deroghe", "bar-ristoranti-alberghi-impatto-acustico"],
    },
    {
        "slug": "aziende",
        "nome": "Aziende e stabilimenti",
        "breve": "Rumore verso l'esterno ed esposizione dei lavoratori, in due documenti distinti.",
        "area": "pratiche",
        "h1": "Per <em>aziende e stabilimenti</em>",
        "title": "Acustica per aziende e stabilimenti in Puglia | SozziSound",
        "descrizione": "Per le aziende pugliesi: impatto acustico di nuovi insediamenti, misure del rumore per i lavoratori secondo il D.Lgs 81/2008, bonifica di impianti rumorosi.",
        "sommario": "Il rumore di un'azienda ha due fronti, con regole diverse: quello che esce dal perimetro e quello a cui sono esposti i lavoratori. Li seguiamo entrambi, con documenti distinti.",
        "chiavi": "azienda impresa stabilimento fabbrica industria datore di lavoro produzione reparto",
        "situazioni": [
            ("Nuovo insediamento, ampliamento, nuova linea",
             "Serve la documentazione di previsione di impatto acustico per il titolo edilizio e per l'esercizio."),
            ("La valutazione del rischio rumore è da fare o da aggiornare",
             "Eseguiamo le misure e calcoliamo i livelli di esposizione previsti dal D.Lgs 81/2008."),
            ("Un vicino o il Comune segnalano un disturbo",
             "Misure al confine e presso i ricettori, poi un piano di interventi mirato alla sorgente che pesa."),
            ("State scegliendo un impianto",
             "Dai dati dichiarati dal costruttore stimiamo il rumore al confine prima dell'acquisto."),
        ],
        "servizi": [
            ("relazione-acustica-attivita-produttive-puglia", "La documentazione per nuovi insediamenti e ampliamenti."),
            ("sicurezza-rumore-lavoro-puglia", "Le misure dell'esposizione dei lavoratori al rumore."),
            ("bonifica-acustica-puglia", "Gli interventi per rientrare nei limiti."),
            ("valutazione-impatto-acustico-puglia", "La valutazione del rumore prodotto verso l'esterno."),
            ("rumore-attivita-commerciali-artigianali-puglia", "Impianti e orari delle attività vicine alle abitazioni."),
        ],
        "metodo_titolo": "Come lavoriamo in azienda",
        "metodo": """<p>Entriamo in stabilimento per misurare, non per fermare il lavoro.</p>
<ul>
<li>Misure a impianti in marcia, nelle condizioni reali.</li>
<li>Relazioni separate per ambiente esterno e sicurezza dei lavoratori.</li>
<li>Un referente unico per RSPP, ufficio tecnico e direzione.</li>
<li>Interventi indicati in ordine di efficacia, a partire dalla sorgente che conta di più.</li>
</ul>""",
        "faq": [
            ("Le misure fermano la produzione?",
             "No. Si misura a impianti in marcia. Per isolare il contributo di una singola sorgente può servire fermarla per pochi minuti, e lo concordiamo con il reparto."),
            ("Potete lavorare insieme al nostro RSPP?",
             "È il modo normale di lavorare: l'RSPP conosce mansioni e tempi di esposizione, noi portiamo misure e calcoli."),
            ("Siamo in zona industriale: i limiti ci riguardano?",
             "Sì. Anche le aree industriali hanno limiti, e spesso il vincolo arriva da un'abitazione o da un ufficio al margine della zona."),
        ],
        "guide": ["rumore-luoghi-di-lavoro-valori-azione-limite", "impatto-acustico-e-clima-acustico-differenze"],
    },
    {
        "slug": "rspp-consulenti-sicurezza",
        "nome": "RSPP e consulenti della sicurezza",
        "breve": "Un partner per le misure fonometriche e il capitolo rumore dei vostri clienti.",
        "area": "lavoro",
        "h1": "Per <em>RSPP e consulenti della sicurezza</em>",
        "title": "Misure fonometriche per RSPP e consulenti sicurezza | SozziSound",
        "descrizione": "Partner tecnico per RSPP e consulenti della sicurezza in Puglia: misure fonometriche e relazione sul rumore per la valutazione dei rischi del D.Lgs 81/2008.",
        "sommario": "Un partner per le misure fonometriche e per il capitolo rumore dei vostri clienti. Voi tenete la regia della valutazione dei rischi, noi portiamo strumenti, misure e calcoli.",
        "chiavi": "rspp consulente sicurezza hse medico competente dvr valutazione rischi partner misure fonometriche",
        "situazioni": [
            ("Un cliente ha reparti rumorosi e servono misure",
             "Misuriamo per postazione e per mansione, e calcoliamo i livelli di esposizione da confrontare con i valori di legge."),
            ("La valutazione ha più di quattro anni, o sono cambiate le macchine",
             "È il momento del riesame previsto dall'art. 181 del D.Lgs 81/2008."),
            ("Dovete scegliere i dispositivi di protezione dell'udito",
             "I livelli misurati sono il dato di partenza per sceglierli e per verificarne l'adeguatezza."),
            ("L'organo di vigilanza chiede chiarimenti",
             "Vi affianchiamo sulla parte strumentale e di calcolo."),
        ],
        "servizi": [
            ("sicurezza-rumore-lavoro-puglia", "Misure e calcolo dei livelli di esposizione."),
            ("bonifica-acustica-puglia", "Interventi sulle sorgenti quando i valori di azione sono superati."),
            ("relazione-acustica-attivita-produttive-puglia", "Se il cliente deve anche documentare il rumore verso l'esterno."),
        ],
        "metodo_titolo": "Come lavoriamo con un consulente",
        "metodo": """<p>Il rapporto con il cliente resta vostro.</p>
<ul>
<li>Programma delle misure costruito sulle mansioni e sui tempi che ci indicate.</li>
<li>Relazione tecnica firmata da noi, da inserire nel documento di valutazione che curate voi.</li>
<li>Dati in forma tabellare, per gruppi omogenei, pronti da riportare.</li>
<li>Disponibilità a tornare quando cambiano macchine o lavorazioni.</li>
</ul>""",
        "faq": [
            ("La valutazione del rischio rumore deve farla un tecnico competente in acustica?",
             "No. Il D.Lgs 81/2008 la affida a personale qualificato con specifiche conoscenze in materia, nell'ambito del servizio di prevenzione e protezione. Il tecnico competente in acustica è la figura prevista per l'acustica ambientale; nelle aziende portiamo la stessa cura strumentale."),
            ("Che strumentazione usate?",
             "Un fonometro di classe 1, tarato e certificato, con verifica della calibrazione prima e dopo ogni ciclo di misura."),
            ("Potete seguire più aziende dello stesso consulente?",
             "Sì, ed è il caso più frequente: stesso formato dei dati e stesso modo di lavorare su tutti i clienti."),
        ],
        "guide": ["rumore-luoghi-di-lavoro-valori-azione-limite", "rilievo-fonometrico-come-si-svolge"],
    },
    {
        "slug": "studi-legali",
        "nome": "Studi legali",
        "breve": "Consulenza tecnica di parte nelle cause per immissioni di rumore.",
        "area": "disturbo",
        "h1": "Per <em>studi legali</em>",
        "title": "Consulenza tecnica di parte per immissioni di rumore | SozziSound",
        "descrizione": "Consulenza tecnica di parte nelle controversie per immissioni di rumore (art. 844 c.c.): misure fonometriche, relazione utilizzabile in giudizio, assistenza al CTU.",
        "sommario": "Consulenza tecnica di parte nelle controversie per immissioni di rumore. Misure eseguite secondo le tecniche di legge e una relazione scritta per essere prodotta in giudizio.",
        "chiavi": "avvocato studio legale ctp consulente tecnico di parte causa giudizio immissioni 844 ctu accertamento tecnico preventivo",
        "situazioni": [
            ("Prima di agire volete sapere se il caso regge",
             "Una campagna di misure preliminare dice se e di quanto il rumore supera il fondo, prima di affrontare i costi di una causa."),
            ("Il giudice ha nominato un consulente d'ufficio",
             "Assistiamo la parte nelle operazioni peritali e formuliamo osservazioni alla bozza di relazione."),
            ("Assistete l'attività accusata del disturbo",
             "Verifichiamo le misure avversarie e documentiamo lo stato reale, compresi gli interventi già attuati."),
            ("Serve un parere su una relazione altrui",
             "Esaminiamo metodo, strumentazione, tempi di misura e conclusioni."),
        ],
        "servizi": [
            ("perizie-acustiche-controversie-puglia", "Misure in abitazione e relazione tecnica di parte."),
            ("rumore-impianti-tecnici-puglia", "Quando la sorgente è un impianto: pompe di calore, ascensori, gruppi frigo."),
            ("bonifica-acustica-puglia", "Per definire e verificare gli interventi in una transazione."),
        ],
        "metodo_titolo": "Come lavoriamo con un avvocato",
        "metodo": """<p>Una misura vale quanto la sua tenuta al contraddittorio.</p>
<ul>
<li>Strumentazione di classe 1 con certificato di taratura in corso di validità.</li>
<li>Rapporto di misura con i dati previsti dal DM 16/03/1998: condizioni, tempi, catena di misura, livelli.</li>
<li>Distinzione netta tra dato misurato e valutazione.</li>
<li>Un linguaggio leggibile anche da chi non è tecnico.</li>
</ul>""",
        "faq": [
            ("Normale tollerabilità e limiti amministrativi coincidono?",
             "No. La giurisprudenza tiene distinti i due piani: i limiti del DPCM 14/11/1997 tutelano l'interesse pubblico, mentre l'art. 844 del codice civile regola i rapporti tra privati e chiede una valutazione in concreto, avuto riguardo alla condizione dei luoghi. La relazione li tratta separatamente."),
            ("Fate misure anche in assenza della controparte?",
             "Sì, per una relazione di parte. In un accertamento disposto dal giudice le operazioni si svolgono in contraddittorio, e vi partecipiamo come consulenti."),
            ("Seguite cause fuori dalla Puglia?",
             "Sì. La sede è a Ostuni, ma assumiamo incarichi in tutta Italia."),
        ],
        "guide": ["rumore-del-vicino-normale-tollerabilita", "rilievo-fonometrico-come-si-svolge"],
    },
    {
        "slug": "privati-condomini",
        "nome": "Privati e condomìni",
        "breve": "Rumori del vicino, di un locale, di un impianto: che cosa si può misurare.",
        "area": "disturbo",
        "h1": "Per <em>privati e condomìni</em>",
        "title": "Rumore in casa e in condominio: misure e perizie | SozziSound",
        "descrizione": "Per privati e condomìni in Puglia: misure del rumore di vicini, locali e impianti, verifica dell'isolamento, relazione per amministratore, Comune o avvocato.",
        "sommario": "Il locale sotto casa, l'impianto del vicino, l'ascensore, i passi dal piano di sopra. Ti spieghiamo che cosa si può misurare, quanto vale quella misura e a che cosa serve la relazione.",
        "chiavi": "privato condominio casa appartamento vicino amministratore famiglia abitazione rumore notte dormire",
        "situazioni": [
            ("Un locale o un'attività ti disturba",
             "Si misura dentro casa tua, negli orari del disturbo. Se i limiti sono superati, la relazione sostiene l'esposto al Comune o la richiesta dell'avvocato."),
            ("Il rumore viene da un impianto",
             "Pompe di calore, condizionatori, autoclavi, ascensori: si misura dove si sente e si capisce come ridurlo."),
            ("Senti tutto quello che fa il vicino",
             "Può essere un difetto di isolamento dell'edificio. Le misure in opera dicono se pareti e solai rispettano i requisiti di legge."),
            ("Stai comprando o ristrutturando casa",
             "Una verifica prima dell'acquisto, o un consiglio prima dei lavori, evita di scoprire il problema dopo."),
        ],
        "servizi": [
            ("perizie-acustiche-controversie-puglia", "Le misure in abitazione e la relazione di parte."),
            ("rumore-impianti-tecnici-puglia", "Il rumore di pompe di calore, ascensori, autoclavi."),
            ("collaudo-acustico-edifici-puglia", "La verifica dell'isolamento di pareti, solai e facciate."),
            ("requisiti-acustici-passivi-puglia", "Che cosa deve garantire un edificio per legge."),
        ],
        "metodo_titolo": "Come lavoriamo con un privato",
        "metodo": """<p>Niente gergo. Prima di proporti una misura ti diciamo se, secondo noi, ha senso farla.</p>
<ul>
<li>Un primo confronto al telefono per capire il problema.</li>
<li>Preventivo gratuito e scritto, con che cosa misuriamo e perché.</li>
<li>Misure negli orari in cui il rumore c'è, anche di sera, di notte o nel fine settimana.</li>
<li>Una relazione che puoi consegnare all'amministratore, al Comune o al tuo avvocato.</li>
</ul>""",
        "faq": [
            ("Posso usare un'app del telefono per misurare?",
             "Per farti un'idea, sì. Per un esposto o una causa, no: servono un fonometro di classe 1 tarato e una misura eseguita secondo le tecniche previste dalla legge, firmata da un tecnico competente."),
            ("Quanto costa una perizia?",
             "Dipende da quante misure servono e in quali orari. Dopo un primo confronto ti mandiamo un preventivo gratuito, senza impegno."),
            ("Il rumore c'è solo ogni tanto: come si fa?",
             "Si programma la misura quando è più probabile e, se serve, si ripete in più momenti. Ne parliamo prima, per non fare misure inutili."),
        ],
        "guide": ["rumore-del-vicino-normale-tollerabilita", "pompe-di-calore-unita-esterne-rumore"],
    },
    {
        "slug": "impianti-sportivi",
        "nome": "Impianti sportivi",
        "breve": "Padel, palestre, piscine: costruire e gestire senza avere i vicini contro.",
        "area": "locali",
        "h1": "Per <em>impianti sportivi</em>",
        "title": "Acustica per padel, palestre e centri sportivi | SozziSound",
        "descrizione": "Per gestori e progettisti di campi da padel, palestre, piscine e centri sportivi in Puglia: previsione del rumore, pratiche, soluzioni e misure dopo un esposto.",
        "sommario": "Padel, tennis, calcetto, palestre, piscine, scuole di danza. Vi aiutiamo a costruire o ampliare senza trovarvi i vicini contro, e a rimediare se è già successo.",
        "chiavi": "gestore centro sportivo societa sportiva circolo padel tennis palestra piscina danza",
        "situazioni": [
            ("State progettando nuovi campi",
             "Una previsione fatta sul progetto dice dove metterli, come orientarli e se servono barriere o coperture."),
            ("I campi ci sono, e sono arrivate le proteste",
             "Misuriamo nelle abitazioni e al confine durante il gioco, poi definiamo interventi e orari."),
            ("La palestra ha musica e corsi serali",
             "Basse frequenze e pesi che cadono passano dai solai: si misura sotto e accanto, e si interviene su pavimento e impianto audio."),
            ("Il Comune chiede la documentazione acustica",
             "Prepariamo la previsione di impatto acustico per il titolo edilizio o per lo sportello unico."),
        ],
        "servizi": [
            ("impatto-acustico-impianti-sportivi-puglia", "La previsione e le misure per campi, palestre e piscine."),
            ("bonifica-acustica-puglia", "Gli interventi su un impianto esistente."),
            ("progettazione-acustica-ambienti-puglia", "L'isolamento di sale e palestre con musica."),
            ("valutazione-impatto-acustico-puglia", "La documentazione generale di impatto acustico."),
        ],
        "metodo_titolo": "Come lavoriamo con un centro sportivo",
        "metodo": """<p>Il nostro obiettivo è che l'impianto resti aperto negli orari in cui rende.</p>
<ul>
<li>Misure negli orari di punta, quando i campi sono tutti occupati.</li>
<li>Soluzioni valutate anche per l'effetto sul gioco e sulla gestione.</li>
<li>Indicazioni chiare su orari e prenotazioni compatibili con i limiti.</li>
</ul>""",
        "faq": [
            ("Coprire i campi risolve?",
             "Aiuta molto verso l'alto e verso i lati chiusi. Una copertura aperta sui fianchi, però, lascia uscire il rumore proprio in orizzontale, verso le case. Forma e chiusure vanno valutate con un calcolo."),
            ("Quali orari sono ammessi?",
             "In Puglia la L.R. 3/2002 colloca le attività sportive rumorose all'aperto nella fascia 8.00-24.00, con livelli in facciata più bassi nelle ore centrali e serali. Il regolamento comunale può aggiungere prescrizioni."),
            ("Le voci dei giocatori contano?",
             "Sì. Nella valutazione entrano i colpi, i rimbalzi e anche le voci, che di sera possono pesare quanto il gioco."),
        ],
        "guide": ["campi-da-padel-rumore", "legge-regionale-puglia-3-2002-acustica"],
    },
    {
        "slug": "enti-pubblici",
        "nome": "Comuni ed enti pubblici",
        "breve": "Classificazione acustica, regolamenti, deroghe, misure a supporto degli uffici.",
        "area": "enti",
        "h1": "Per <em>Comuni ed enti pubblici</em>",
        "title": "Acustica per Comuni ed enti pubblici in Puglia | SozziSound",
        "descrizione": "Supporto tecnico agli uffici comunali pugliesi: classificazione acustica, regolamenti per attività temporanee, esame delle pratiche, misure, edifici pubblici.",
        "sommario": "Agli uffici tecnici e ambiente servono risposte solide su classificazione acustica, regolamenti, deroghe e pratiche dei privati. Ci presentiamo: siamo due tecnici competenti in acustica con sede a Ostuni.",
        "chiavi": "comune sindaco assessore ufficio tecnico ufficio ambiente suap polizia locale ente pubblico amministrazione",
        "situazioni": [
            ("Il territorio non è classificato, o la classificazione è datata",
             "Affianchiamo l'ufficio nella redazione e nell'aggiornamento, con le misure che servono a fondarla."),
            ("Ogni estate tornano le richieste di deroga per gli eventi",
             "Un regolamento chiaro su orari, livelli e documenti da presentare riduce il lavoro dell'ufficio e il contenzioso."),
            ("Arrivano esposti e servono misure",
             "Eseguiamo rilievi e relazioni a supporto dei procedimenti."),
            ("C'è un nuovo edificio pubblico da progettare",
             "Scuole, asili, strutture sanitarie: clima acustico del sito, requisiti passivi, acustica delle aule."),
        ],
        "servizi": [
            ("acustica-enti-pubblici-puglia", "Classificazione, piani di risanamento, regolamenti."),
            ("deroga-acustica-eventi-puglia", "La parte tecnica delle autorizzazioni per gli eventi."),
            ("clima-acustico-puglia", "Le valutazioni per scuole e strutture sanitarie."),
            ("acustica-aule-uffici-sale-puglia", "Il comfort acustico di aule e sale pubbliche."),
        ],
        "metodo_titolo": "Come lavoriamo con un ente",
        "metodo": """<p>Il nostro lavoro è dare all'ufficio elementi tecnici che reggano, in una forma utile agli atti.</p>
<ul>
<li>Un primo incontro tecnico per capire priorità e risorse.</li>
<li>Elaborati pensati per essere adottati, non solo consegnati.</li>
<li>Rispetto della separazione che la legge chiede tra chi redige e chi controlla.</li>
</ul>""",
        "faq": [
            ("Come possiamo affidarvi un incarico?",
             "Con le procedure previste per i servizi tecnici. Su richiesta inviamo la documentazione dello studio e gli estremi delle iscrizioni all'elenco nazionale dei tecnici competenti in acustica."),
            ("Operate solo in provincia di Brindisi?",
             "No. La sede è a Ostuni, ma lavoriamo in tutta la Puglia e, su incarico, nel resto d'Italia."),
            ("Potete formare il personale dell'ufficio?",
             "Possiamo affiancare i tecnici dell'ente nella lettura delle relazioni acustiche e nell'applicazione del regolamento, durante lo svolgimento dell'incarico."),
        ],
        "guide": ["classificazione-acustica-comunale", "legge-regionale-puglia-3-2002-acustica"],
    },
]

PER_SLUG = {x["slug"]: x for x in PERCHI}
for _x in PERCHI:
    _x["url"] = f"per/{_x['slug']}.html"

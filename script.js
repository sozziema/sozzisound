/* SozziSound — script condiviso da tutte le pagine. */
(function () {
  'use strict';

  var radice = document.body.dataset.radice || '';
  var WHATSAPP = '393348748771';
  var TELEFONO = '+393348748771';
  var EMAIL = 'info@sozzisound.it';

  function evento(nome, parametri) {
    if (typeof window.gtag === 'function') window.gtag('event', nome, parametri || {});
  }

  function linkWhatsapp(testo) {
    return 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(testo);
  }

  /* ---------- Intestazione e menu ---------- */
  var intestazione = document.querySelector('.site-header');
  var pulsanteMenu = document.querySelector('.menu-button');
  var menu = document.querySelector('.menu');

  function chiudiMenu() {
    if (!menu || !pulsanteMenu) return;
    menu.classList.remove('open');
    pulsanteMenu.setAttribute('aria-expanded', 'false');
    pulsanteMenu.setAttribute('aria-label', 'Apri il menu');
  }

  if (pulsanteMenu && menu) {
    pulsanteMenu.addEventListener('click', function () {
      var aperto = menu.classList.toggle('open');
      pulsanteMenu.setAttribute('aria-expanded', String(aperto));
      pulsanteMenu.setAttribute('aria-label', aperto ? 'Chiudi il menu' : 'Apri il menu');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) chiudiMenu();
    });
    document.addEventListener('click', function (e) {
      if (menu.classList.contains('open') && !e.target.closest('.site-header')) chiudiMenu();
    });
  }

  /* Ombra sotto l'intestazione e barra di lettura */
  var barra = document.querySelector('.lettura i');
  var articolo = document.querySelector('[data-lettura]');
  var inAttesa = false;

  function aggiornaScorrimento() {
    inAttesa = false;
    var y = window.scrollY || window.pageYOffset;
    if (intestazione) intestazione.classList.toggle('is-scrolled', y > 8);
    document.body.classList.toggle('pagina-scorsa', y > 600);
    if (barra && articolo) {
      var r = articolo.getBoundingClientRect();
      var totale = r.height - window.innerHeight * 0.6;
      var fatto = Math.min(1, Math.max(0, (-r.top + 120) / (totale > 0 ? totale : 1)));
      barra.style.setProperty('--p', fatto.toFixed(3));
    }
  }

  window.addEventListener('scroll', function () {
    if (!inAttesa) { inAttesa = true; window.requestAnimationFrame(aggiornaScorrimento); }
  }, { passive: true });
  aggiornaScorrimento();

  var anno = document.querySelector('#year');
  if (anno) anno.textContent = new Date().getFullYear();

  /* ---------- Tracciamento dei contatti (solo se Analytics è attivo) ---------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    var metodo = href.indexOf('tel:') === 0 ? 'telefono'
      : href.indexOf('wa.me') > -1 ? 'whatsapp'
      : href.indexOf('mailto:') === 0 ? 'email' : '';
    if (metodo) evento('contatto', { metodo: metodo, pagina: location.pathname });

    /* Pagine aperte dal disco: una cartella non mostra da sola la sua pagina indice */
    if (location.protocol === 'file:' && a.protocol === 'file:' && a.pathname.slice(-1) === '/' && !a.target) {
      e.preventDefault();
      location.href = a.href.replace(/\/(?=[?#]|$)/, '/index.html');
    }
  });

  /* ---------- Modulo contatti ---------- */
  var modulo = document.querySelector('#modulo-contatti');

  /* Sceglie il tipo di richiesta e annota da quale pagina o percorso arriva chi scrive */
  var precompila = function (area, rif) {
    if (!modulo) return false;
    var tipo = modulo.querySelector('[name="tipo"]');
    var riferimento = modulo.querySelector('[name="riferimento"]');
    var notaRif = modulo.querySelector('[data-riferimento]');
    if (tipo && area) {
      Array.prototype.forEach.call(tipo.options, function (o) {
        if (o.dataset.area === area) tipo.value = o.value;
      });
    }
    if (riferimento && rif) {
      riferimento.value = String(rif).slice(0, 220);
      if (notaRif) {
        notaRif.hidden = false;
        notaRif.querySelector('span').textContent = riferimento.value;
      }
    }
    return true;
  };

  if (modulo) {
    var esito = modulo.querySelector('.modulo-esito');
    var parametri = new URLSearchParams(location.search);
    precompila(parametri.get('tipo'), parametri.get('rif'));

    var leggi = function () {
      var d = {};
      new FormData(modulo).forEach(function (v, k) { d[k] = String(v).trim(); });
      return d;
    };

    var componi = function (d) {
      var righe = ['Nome: ' + d.nome, 'Email: ' + d.email];
      if (d.telefono) righe.push('Telefono: ' + d.telefono);
      righe.push('Tipo di richiesta: ' + d.tipo);
      if (d.riferimento) righe.push('Riferimento: ' + d.riferimento);
      righe.push('Comune: ' + d.comune, '', d.messaggio);
      return righe.join('\n');
    };

    var mostra = function (html, errore) {
      esito.innerHTML = html;
      esito.classList.toggle('errore', !!errore);
      esito.hidden = false;
      esito.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    };

    var valido = function () {
      Array.prototype.forEach.call(modulo.elements, function (c) {
        if (c.willValidate) c.classList.toggle('non-valido', !c.checkValidity());
      });
      return modulo.reportValidity();
    };

    var conferma = function () {
      modulo.classList.add('inviato');
      mostra('<strong>Richiesta inviata.</strong>Grazie. Ti ricontattiamo per un primo confronto e per il preventivo, che è gratuito.');
      evento('generate_lead', { metodo: 'modulo' });
    };

    var alternative = function (d) {
      var testo = 'Richiesta dal sito\n' + componi(d);
      return '<a href="' + linkWhatsapp(testo) + '" target="_blank" rel="noopener">WhatsApp</a> oppure <a href="mailto:' + EMAIL
        + '?subject=' + encodeURIComponent('Richiesta dal sito - ' + d.nome) + '&body=' + encodeURIComponent(componi(d)) + '">email</a>';
    };

    modulo.addEventListener('input', function (e) {
      if (e.target.classList) e.target.classList.remove('non-valido');
    });

    modulo.addEventListener('invalid', function (e) {
      if (e.target.classList) e.target.classList.add('non-valido');
    }, true);

    modulo.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!valido()) return;
      var d = leggi();
      if (d.sito_web) { conferma(); return; }
      var endpoint = modulo.dataset.endpoint || '';

      if (!endpoint) {
        location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent('Richiesta dal sito - ' + d.nome)
          + '&body=' + encodeURIComponent(componi(d));
        mostra('<strong>Controlla la tua app di posta.</strong>La richiesta è pronta nel messaggio: premi Invia per spedirla. Se non si è aperto nulla, mandala con ' + alternative(d) + '.');
        evento('generate_lead', { metodo: 'email' });
        return;
      }

      var pulsante = modulo.querySelector('[type="submit"]');
      var etichetta = pulsante.innerHTML;
      pulsante.disabled = true;
      pulsante.textContent = 'Invio in corso…';
      var corpo = new URLSearchParams(d);
      corpo.set('pagina', location.href);
      var controllo = new AbortController();
      var timer = setTimeout(function () { controllo.abort(); }, 20000);

      fetch(endpoint, { method: 'POST', body: corpo, signal: controllo.signal })
        .then(function (r) { return r.json(); })
        .then(function (j) { if (j && j.ok) conferma(); else throw new Error('risposta'); })
        .catch(function () {
          mostra('<strong>Invio non riuscito.</strong>Puoi riprovare tra poco, oppure mandarci la stessa richiesta con ' + alternative(d) + '.', true);
        })
        .then(function () {
          clearTimeout(timer);
          pulsante.disabled = false;
          pulsante.innerHTML = etichetta;
        });
    });

    var viaWhatsapp = modulo.querySelector('[data-invia-whatsapp]');
    if (viaWhatsapp) {
      viaWhatsapp.addEventListener('click', function () {
        if (!valido()) return;
        var d = leggi();
        if (d.sito_web) { conferma(); return; }
        window.open(linkWhatsapp('Richiesta dal sito\n' + componi(d)), '_blank', 'noopener');
        mostra('<strong>Si è aperto WhatsApp.</strong>La richiesta è già scritta: premi Invia nella chat per spedirla.');
        evento('generate_lead', { metodo: 'whatsapp' });
      });
    }
  }

  /* ---------- Consenso cookie (Google Consent Mode v2) ---------- */
  var CHIAVE = 'sozzisound-cookie-consent';
  var avviso = document.querySelector('#cookie-banner');

  function applicaConsenso(concesso) {
    if (typeof window.gtag !== 'function') return;
    var stato = concesso ? 'granted' : 'denied';
    window.gtag('consent', 'update', {
      ad_storage: stato,
      ad_user_data: stato,
      ad_personalization: stato,
      analytics_storage: stato
    });
  }

  function memoria(azione, valore) {
    try {
      if (azione === 'leggi') return localStorage.getItem(CHIAVE);
      if (azione === 'scrivi') localStorage.setItem(CHIAVE, valore);
      if (azione === 'togli') localStorage.removeItem(CHIAVE);
    } catch (err) { /* archiviazione non disponibile */ }
    return null;
  }

  var scelta = memoria('leggi');
  if (scelta) applicaConsenso(scelta === 'granted');
  else if (avviso) avviso.hidden = false;

  function decidi(concesso) {
    memoria('scrivi', concesso ? 'granted' : 'denied');
    applicaConsenso(concesso);
    if (avviso) avviso.hidden = true;
  }

  var accetta = document.querySelector('#cookie-accept');
  var rifiuta = document.querySelector('#cookie-reject');
  var gestisci = document.querySelector('#cookie-manage');
  if (accetta) accetta.addEventListener('click', function () { decidi(true); });
  if (rifiuta) rifiuta.addEventListener('click', function () { decidi(false); });
  if (gestisci) gestisci.addEventListener('click', function (e) {
    e.preventDefault();
    memoria('togli');
    if (avviso) { avviso.hidden = false; avviso.querySelector('button').focus(); }
  });

  /* ---------- Dati del percorso guidato e delle risposte rapide ----------
     Si caricano con un tag script, così funzionano anche aprendo le pagine dal disco. */
  var dati = null;
  var codaDati = [];

  var conDati = function (riuscito, fallito) {
    if (dati) { riuscito(); return; }
    codaDati.push([riuscito, fallito]);
    if (codaDati.length > 1) return;
    var s = document.createElement('script');
    s.src = radice + 'assets/dati.js?v=' + (document.body.dataset.dati || '');
    s.onload = function () {
      dati = window.SOZZI_DATI || null;
      var coda = codaDati;
      codaDati = [];
      coda.forEach(function (c) { if (dati) c[0](); else if (c[1]) c[1](); });
    };
    s.onerror = function () {
      var coda = codaDati;
      codaDati = [];
      coda.forEach(function (c) { if (c[1]) c[1](); });
    };
    document.head.appendChild(s);
  };

  var protetto = function (s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  };

  var chiudiPannello = function () {};

  /* ---------- Percorso guidato ---------- */
  var montaPercorso = function (el) {
    var corpo = el.querySelector('.percorso-corpo');
    var tappa = el.querySelector('.percorso-tappa');
    var storia = [];
    var corrente = null;

    var disegna = function (conFuoco) {
      var P = dati.percorso;
      if (!corrente) corrente = P.inizio;
      var html = '';
      var scelte = storia.map(function (s) { return s.breve; });

      if (storia.length) {
        html += '<p class="percorso-scelte"><button type="button" data-indietro>← Indietro</button><span>'
          + protetto(scelte.join(' › ')) + '</span></p>';
      }

      var d = P.domande[corrente];
      if (d) {
        if (tappa) tappa.textContent = 'Domanda ' + (storia.length + 1);
        if (d.n) html += '<p class="percorso-nota">' + d.n + '</p>';
        html += '<p class="percorso-domanda" tabindex="-1">' + d.d + '</p><ul class="percorso-opzioni">'
          + d.o.map(function (o) {
            return '<li><button type="button" data-vai="' + o[1] + '" data-breve="' + protetto(o[2]) + '">' + o[0] + '</button></li>';
          }).join('') + '</ul>';
      } else {
        var e = P.esiti[corrente];
        var cammino = scelte.join(' › ');
        var rif = e.r + ' (percorso: ' + cammino + ')';
        if (tappa) tappa.textContent = 'Risultato';
        html += '<p class="percorso-etichetta">Fa al caso tuo</p>'
          + '<h3 class="percorso-titolo" tabindex="-1">' + e.t + '</h3>'
          + '<div class="percorso-testo">' + e.h + '</div>';
        if (e.n && e.n.length) {
          html += '<ul class="percorso-norme">' + e.n.map(function (n) { return '<li><span class="norma">' + n + '</span></li>'; }).join('') + '</ul>';
        }
        html += '<div class="percorso-azioni">'
          + '<a class="button button-primary" data-preventivo data-area="' + e.a + '" data-rif="' + protetto(rif) + '" href="'
          + radice + 'contatti.html?tipo=' + encodeURIComponent(e.a) + '&rif=' + encodeURIComponent(rif) + '#richiesta">'
          + e.c + ' <span aria-hidden="true">→</span></a>'
          + '<a class="button button-line" href="' + radice + e.u + '">' + e.e + '</a></div>'
          + '<p class="percorso-altro"><a href="' + linkWhatsapp('Buongiorno, dal percorso guidato del sito: ' + cammino + '. Vorrei un preventivo per: ' + e.r + '.')
          + '" target="_blank" rel="noopener">Scrivici su WhatsApp</a>'
          + (e.g ? '<a href="' + radice + e.g.u + '">Leggi la guida</a>' : '')
          + '<button type="button" data-ricomincia>Ricomincia</button></p>';
      }

      corpo.innerHTML = html;
      if (!conFuoco) return;
      var titolo = corpo.querySelector('[tabindex="-1"]');
      if (titolo) titolo.focus({ preventScroll: true });
      var contenitore = el.closest('.risposte-flusso');
      if (contenitore) contenitore.scrollTop = 0;
      else if (el.getBoundingClientRect().top < 0) el.scrollIntoView();
    };

    el.addEventListener('click', function (e) {
      var b = e.target.closest('[data-vai], [data-indietro], [data-ricomincia], [data-preventivo]');
      if (!b || !el.contains(b)) return;

      if (b.hasAttribute('data-preventivo')) {
        evento('percorso_preventivo', { esito: corrente });
        if (precompila(b.getAttribute('data-area'), b.getAttribute('data-rif'))) {
          e.preventDefault();
          chiudiPannello();
          modulo.scrollIntoView();
          var primo = modulo.querySelector('[name="nome"]');
          if (primo) primo.focus({ preventScroll: true });
        }
        return;
      }

      e.preventDefault();
      conDati(function () {
        if (b.hasAttribute('data-vai')) {
          storia.push({ nodo: corrente || dati.percorso.inizio, breve: b.getAttribute('data-breve') || b.textContent });
          corrente = b.getAttribute('data-vai');
          if (dati.percorso.esiti[corrente]) evento('percorso_esito', { esito: corrente });
        } else if (b.hasAttribute('data-indietro') && storia.length) {
          corrente = storia.pop().nodo;
        } else {
          storia = [];
          corrente = dati.percorso.inizio;
        }
        disegna(true);
      }, function () {
        if (b.tagName === 'A') location.href = b.href;
      });
    });

    return {
      avvia: function () {
        if (corpo.firstChild) return;
        conDati(function () { disegna(false); }, function () {
          corpo.innerHTML = '<p class="percorso-nota">Il percorso non è disponibile in questo momento. Scrivici su WhatsApp o chiamaci: rispondiamo di persona.</p>';
        });
      }
    };
  };

  Array.prototype.forEach.call(document.querySelectorAll('[data-percorso]'), function (el) { montaPercorso(el); });

  /* ---------- Pannello: percorso guidato e risposte rapide ---------- */
  var pannello = document.querySelector('#risposte');
  var apritori = document.querySelectorAll('[data-apri-risposte]');

  if (pannello && apritori.length) {
    var flusso = pannello.querySelector('.risposte-flusso');
    var libere = pannello.querySelector('.risposte-libere');
    var formRisposte = pannello.querySelector('.risposte-form');
    var campo = formRisposte.querySelector('input');
    var percorsoPannello = montaPercorso(pannello.querySelector('.percorso'));
    var pronto = false;
    var origine = null;
    var VUOTE = ' il lo la i gli le un uno una di a da in con su per tra fra e o ma che chi cui non mi ti si ci vi ne del dello della dei degli delle al allo alla ai agli alle dal dallo dalla dai dagli dalle nel nello nella nei negli nelle sul sullo sulla sui sugli sulle come cosa quando quanto quale quali dove sono sei ho hai ha abbiamo avete hanno essere avere fare devo deve posso puo serve servono mio mia miei mie tuo tua suo sua questo questa quello quella anche piu vorrei voglio lavorate lavorare lavoriamo operate qualcosa sapere buongiorno salve ciao grazie relazione relazioni acustica acustico acustici acustiche valutazione valutazioni ';

    var normalizza = function (s) {
      return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, ' ').trim();
    };

    var parole = function (s) {
      return normalizza(s).split(' ').filter(function (p) { return p.length > 2 && VUOTE.indexOf(' ' + p + ' ') < 0; });
    };

    /* 2 = stessa parola, 1 = stessa radice (campo/campi, costa/costo), 0 = parole diverse */
    var simili = function (a, b) {
      if (a === b) return 2;
      var n = Math.min(a.length, b.length);
      var i = 0;
      while (i < n && a.charAt(i) === b.charAt(i)) i++;
      return i >= 4 && i >= n - 2 && i >= Math.max(a.length, b.length) - 3 ? 1 : 0;
    };

    /* Le parole rare contano di più di quelle che compaiono in molte voci */
    var frequenze = {};
    var peso = function (k) {
      var f = frequenze[k] || 1;
      return f <= 2 ? 2 : f <= 5 ? 1.5 : 1;
    };

    var valuta = function (richieste, chiavi) {
      var esito = { punti: 0, trovate: 0 };
      richieste.forEach(function (r) {
        var migliore = 0;
        chiavi.forEach(function (k) { migliore = Math.max(migliore, simili(r, k) * peso(k)); });
        if (migliore > 0) esito.trovate++;
        esito.punti += migliore;
      });
      return esito;
    };

    var prepara = function () {
      if (pronto) return;
      pronto = true;
      dati.voci.forEach(function (v) {
        v.tutte = v.k.concat(parole(v.q));
        v.f = v.f || [];
      });
      dati.voci.map(function (v) { return v.tutte; })
        .concat(dati.pagine.map(function (pg) { return pg.k; }))
        .forEach(function (elenco) {
          var viste = {};
          elenco.forEach(function (k) {
            if (!viste[k]) { viste[k] = true; frequenze[k] = (frequenze[k] || 0) + 1; }
          });
        });
    };

    var aggiungi = function (nodo) {
      libere.appendChild(nodo);
      flusso.scrollTop = flusso.scrollHeight;
      return nodo;
    };

    var crea = function (tag, classe, html) {
      var n = document.createElement(tag);
      if (classe) n.className = classe;
      if (html) n.innerHTML = html;
      return n;
    };

    var azioni = function (elenco) {
      var riga = crea('div', 'r-azioni');
      elenco.forEach(function (a) {
        var link = crea('a', a.principale ? 'principale' : '');
        link.href = a.href;
        link.textContent = a.testo;
        if (/^https?:\/\/wa\.me/.test(a.href)) { link.target = '_blank'; link.rel = 'noopener'; }
        riga.appendChild(link);
      });
      return riga;
    };

    var rispondi = function (voce) {
      var m = crea('div', 'r-msg');
      var titolo = crea('strong');
      titolo.textContent = voce.q;
      m.appendChild(titolo);
      m.appendChild(crea('div', '', voce.a));
      var elenco = [];
      if (voce.u) elenco.push({ href: radice + voce.u, testo: voce.e || 'Approfondisci', principale: true });
      elenco.push({ href: linkWhatsapp('Buongiorno, ho una domanda: ' + voce.q), testo: 'Parlane con noi su WhatsApp' });
      m.appendChild(azioni(elenco));
      aggiungi(m);
      evento('risposta_rapida', { domanda: voce.id });
    };

    var suggerimenti = function (ids) {
      var riga = crea('div', 'r-chips');
      ids.forEach(function (id) {
        var voce = dati.voci.filter(function (v) { return v.id === id; })[0];
        if (!voce) return;
        var b = crea('button', 'r-chip');
        b.type = 'button';
        b.textContent = voce.c || voce.q;
        b.addEventListener('click', function () {
          var io = crea('div', 'r-me');
          io.textContent = voce.q;
          aggiungi(io);
          rispondi(voce);
        });
        riga.appendChild(b);
      });
      aggiungi(riga);
    };

    var pagineAffini = function (richieste, esclusa) {
      return dati.pagine.map(function (pg) {
        return { p: pg, punti: valuta(richieste, pg.k).punti };
      }).filter(function (x) { return x.punti >= 2 && x.p.u !== esclusa; })
        .sort(function (x, y) { return y.punti - x.punti; });
    };

    var cerca = function (testo) {
      var richieste = parole(testo);
      var io = crea('div', 'r-me');
      io.textContent = testo;
      aggiungi(io);

      if (!richieste.length) {
        aggiungi(crea('div', 'r-msg', '<p>Dimmi qualcosa in più: che attività o immobile riguarda, oppure che cosa ti è stato chiesto. Intanto, le domande più comuni:</p>'));
        suggerimenti(dati.suggerite);
        return;
      }

      var migliore = null;
      var massimo = 0;
      dati.voci.forEach(function (v) {
        var forti = valuta(richieste, v.f).trovate;
        var deboli = valuta(richieste, v.tutte);
        var basta = forti > 0 || (deboli.trovate >= 2 && deboli.punti >= 3)
          || (richieste.length === 1 && deboli.trovate === 1);
        var punti = forti * 6 + deboli.punti;
        if (basta && punti > massimo) { massimo = punti; migliore = v; }
      });

      if (migliore) {
        rispondi(migliore);
        var affini = richieste.length < 2 ? [] : pagineAffini(richieste, migliore.u).filter(function (x) { return x.punti >= 3; }).slice(0, 2);
        if (affini.length) {
          var altro = crea('div', 'r-msg');
          altro.appendChild(crea('p', '', 'Sul sito ne parliamo anche qui:'));
          altro.appendChild(azioni(affini.map(function (x) { return { href: radice + x.p.u, testo: x.p.t }; })));
          aggiungi(altro);
        }
        return;
      }

      var trovate = pagineAffini(richieste, '').slice(0, 3);
      var m = crea('div', 'r-msg');
      if (trovate.length) {
        m.appendChild(crea('p', '', 'Non ho una risposta pronta, ma queste pagine trattano l’argomento:'));
        m.appendChild(azioni(trovate.map(function (x) { return { href: radice + x.p.u, testo: x.p.t }; })));
        m.appendChild(crea('p', '', 'Se preferisci, giraci la domanda così com’è.'));
      } else {
        m.appendChild(crea('p', '', 'Per questa domanda serve una persona. Mandacela così com’è: ti rispondiamo noi.'));
      }
      m.appendChild(azioni([
        { href: linkWhatsapp('Buongiorno, ho una domanda: ' + testo), testo: 'Invia su WhatsApp', principale: true },
        { href: 'tel:' + TELEFONO, testo: 'Chiama' },
        { href: radice + 'contatti.html', testo: 'Modulo' }
      ]));
      aggiungi(m);
      evento('risposta_rapida', { domanda: 'senza_risposta' });
    };

    var apri = function (da) {
      origine = da || null;
      pannello.hidden = false;
      apritori.forEach(function (b) { b.setAttribute('aria-expanded', 'true'); });
      percorsoPannello.avvia();
      evento('percorso_aperto', { pagina: location.pathname });
    };

    chiudiPannello = function () {
      if (pannello.hidden) return;
      pannello.hidden = true;
      apritori.forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
      if (origine) origine.focus();
    };

    apritori.forEach(function (b) {
      b.addEventListener('click', function () { if (pannello.hidden) apri(b); else chiudiPannello(); });
    });
    pannello.querySelector('.risposte-chiudi').addEventListener('click', chiudiPannello);

    formRisposte.addEventListener('submit', function (e) {
      e.preventDefault();
      var testo = campo.value.trim().slice(0, 300);
      if (!testo) return;
      campo.value = '';
      conDati(function () { prepara(); cerca(testo); }, function () {
        aggiungi(crea('div', 'r-msg', '<p>Le risposte non sono disponibili in questo momento. Scrivici su WhatsApp o chiamaci: rispondiamo di persona.</p>'));
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      if (!pannello.hidden) chiudiPannello();
      else chiudiMenu();
    });
  } else {
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') chiudiMenu(); });
  }
})();

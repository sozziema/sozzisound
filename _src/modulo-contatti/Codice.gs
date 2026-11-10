/**
 * SozziSound - ricezione del modulo contatti del sito.
 *
 * Riceve i dati inviati dal modulo di sozzisound.it e li inoltra per email
 * alla casella dello studio. Non salva nulla: i dati restano solo nella posta.
 *
 * Come attivarlo: vedi ISTRUZIONI.md nella stessa cartella.
 */

var DESTINATARIO = 'info@sozzisound.it';
var INVII_MASSIMI_PER_ORA = 30;

// Lunghezza massima accettata per ogni campo
var CAMPI = {
  nome: 120,
  email: 160,
  telefono: 40,
  tipo: 120,
  comune: 120,
  riferimento: 240,
  pagina: 300,
  messaggio: 4000
};

function doPost(e) {
  try {
    var p = (e && e.parameter) || {};

    // Campo trappola: le persone non lo vedono, i programmi automatici lo compilano.
    if (p.sito_web) return risposta({ ok: true });

    var d = {};
    Object.keys(CAMPI).forEach(function (campo) {
      var valore = String(p[campo] || '').trim().slice(0, CAMPI[campo]);
      if (campo !== 'messaggio') valore = valore.replace(/[\r\n]+/g, ' ');
      d[campo] = valore;
    });

    var emailValida = /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email);
    if (!d.nome || !d.messaggio || !emailValida) return risposta({ ok: false, errore: 'dati' });
    if (!p.privacy) return risposta({ ok: false, errore: 'consenso' });

    // Freno contro gli invii a raffica
    var memoria = CacheService.getScriptCache();
    var invii = Number(memoria.get('invii') || 0);
    if (invii >= INVII_MASSIMI_PER_ORA) return risposta({ ok: false, errore: 'limite' });
    memoria.put('invii', String(invii + 1), 3600);

    var righe = [
      'Nome: ' + d.nome,
      'Email: ' + d.email
    ];
    if (d.telefono) righe.push('Telefono: ' + d.telefono);
    righe.push('Tipo di richiesta: ' + (d.tipo || 'non indicato'));
    if (d.riferimento) righe.push('Riferimento: ' + d.riferimento);
    righe.push('Comune: ' + (d.comune || 'non indicato'));
    righe.push('', d.messaggio, '', '--', 'Inviato dal modulo del sito' + (d.pagina ? ' (' + d.pagina + ')' : ''));

    MailApp.sendEmail({
      to: DESTINATARIO,
      replyTo: d.email,
      name: 'Sito SozziSound',
      subject: 'Richiesta dal sito - ' + d.nome + (d.comune ? ' (' + d.comune + ')' : ''),
      body: righe.join('\n')
    });

    return risposta({ ok: true });
  } catch (errore) {
    return risposta({ ok: false, errore: 'invio' });
  }
}

// Aprendo l'indirizzo nel browser si vede solo che il servizio è attivo.
function doGet() {
  return risposta({ ok: true, servizio: 'Modulo contatti SozziSound' });
}

function risposta(oggetto) {
  return ContentService
    .createTextOutput(JSON.stringify(oggetto))
    .setMimeType(ContentService.MimeType.JSON);
}

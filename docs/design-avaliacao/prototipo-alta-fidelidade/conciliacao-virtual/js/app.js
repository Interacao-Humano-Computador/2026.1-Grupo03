var screens = [
  { id: 'notificacao', label: '1 · Notificação WhatsApp', file: 'telas/01-notificacao.html' },
  { id: 'espera', label: '2 · Sala de Espera', file: 'telas/02-espera.html' },
  { id: 'teste', label: '3 · Teste Periféricos', file: 'telas/03-teste.html' },
  { id: 'sala', label: '4 · Videoconferência', file: 'telas/04-sala.html' },
  { id: 'evidencias', label: '5 · Chat de Evidências', file: 'telas/05-evidencias.html' },
  { id: 'termo', label: '6 · Termo de Acordo', file: 'telas/06-termo.html' },
  { id: 'assinatura', label: '7 · Assinatura Digital', file: 'telas/07-assinatura.html' },
  { id: 'encerramento', label: '8 · Encerramento', file: 'telas/08-encerramento.html' }
];

var currentIndex = 0;

function init() {
  var jump = document.getElementById('jump');
  screens.forEach(function (s, i) {
    var opt = document.createElement('option');
    opt.value = i;
    opt.textContent = s.label;
    jump.appendChild(opt);
  });
  goTo(0);
}

function goTo(index) {
  if (index < 0 || index >= screens.length) return;
  currentIndex = index;
  var iframe = document.getElementById('screen-frame');
  iframe.src = screens[index].file;
  document.getElementById('jump').value = index;
  document.getElementById('screen-index').textContent = (index + 1) + ' / ' + screens.length;
  updateNavButtons();
}

function next() { goTo(currentIndex + 1); }
function prev() { goTo(currentIndex - 1); }

function jumpTo() {
  var val = parseInt(document.getElementById('jump').value);
  if (!isNaN(val)) goTo(val);
}

function updateNavButtons() {
  document.getElementById('btn-prev').style.visibility = currentIndex > 0 ? 'visible' : 'hidden';
  document.getElementById('btn-next').style.visibility = currentIndex < screens.length - 1 ? 'visible' : 'hidden';
}

document.addEventListener('DOMContentLoaded', init);

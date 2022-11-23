function pesquisarAdministrador() {
  const entrada = document.getElementsByTagName('input')[0];
  const filtro = entrada.value.toUpperCase();
  const tabela = document.getElementsByTagName('table')[0];
  var linha, coluna, texto;

  linha = tabela.getElementsByTagName('tr');

  for (var i = 0; i < linha.length; i++) {
    coluna = linha[i].getElementsByTagName('td')[1];

    if (coluna) {
      texto = coluna.textContent || coluna.innerText;

      if (texto.toUpperCase().indexOf(filtro) > -1) {
        linha[i].style.display = '';
      } else {
        linha[i].style.display = 'none';
      }
    }
  }
}

function pesquisarEmpresa() {
  const entrada = document.getElementsByTagName('input')[0];
  const filtro = entrada.value.toUpperCase();
  const tabela = document.getElementsByTagName('table')[0];
  var linha, coluna, texto;

  linha = tabela.getElementsByTagName('tr');

  for (var i = 0; i < linha.length; i++) {
    coluna = linha[i].getElementsByTagName('td')[1];

    if (coluna) {
      texto = coluna.textContent || coluna.innerText;

      if (texto.toUpperCase().indexOf(filtro) > -1) {
        linha[i].style.display = '';
      } else {
        linha[i].style.display = 'none';
      }
    }
  }
}

function pesquisarAssociado() {
  const entrada = document.getElementsByTagName('input')[0];
  const filtro = entrada.value.toUpperCase();
  const tabela = document.getElementsByTagName('table')[0];
  var linha, coluna, texto;

  linha = tabela.getElementsByTagName('tr');

  for (var i = 0; i < linha.length; i++) {
    coluna = linha[i].getElementsByTagName('td')[1];

    if (coluna) {
      texto = coluna.textContent || coluna.innerText;

      if (texto.toUpperCase().indexOf(filtro) > -1) {
        linha[i].style.display = '';
      } else {
        linha[i].style.display = 'none';
      }
    }
  }
}

function pesquisarCurso() {
  const entrada = document.getElementsByTagName('input')[0];
  const filtro = entrada.value.toUpperCase();
  const tabela = document.getElementsByTagName('table')[0];
  var linha, coluna, texto;

  linha = tabela.getElementsByTagName('tr');

  for (var i = 0; i < linha.length; i++) {
    coluna = linha[i].getElementsByTagName('td')[0];

    if (coluna) {
      texto = coluna.textContent || coluna.innerText;

      if (texto.toUpperCase().indexOf(filtro) > -1) {
        linha[i].style.display = '';
      } else {
        linha[i].style.display = 'none';
      }
    }
  }
}

function pesquisarEvento() {
  const entrada = document.getElementsByTagName('input')[0];
  const filtro = entrada.value.toUpperCase();
  const tabela = document.getElementsByTagName('table')[0];
  var linha, coluna, texto;

  linha = tabela.getElementsByTagName('tr');

  for (var i = 0; i < linha.length; i++) {
    coluna = linha[i].getElementsByTagName('td')[0];

    if (coluna) {
      texto = coluna.textContent || coluna.innerText;

      if (texto.toUpperCase().indexOf(filtro) > -1) {
        linha[i].style.display = '';
      } else {
        linha[i].style.display = 'none';
      }
    }
  }
}

function pesquisarJogo() {
  const entrada = document.getElementsByTagName('input')[0];
  const filtro = entrada.value.toUpperCase();
  const tabela = document.getElementsByTagName('table')[0];
  var linha, coluna, texto;

  linha = tabela.getElementsByTagName('tr');

  for (var i = 0; i < linha.length; i++) {
    coluna = linha[i].getElementsByTagName('td')[0];

    if (coluna) {
      texto = coluna.textContent || coluna.innerText;

      if (texto.toUpperCase().indexOf(filtro) > -1) {
        linha[i].style.display = '';
      } else {
        linha[i].style.display = 'none';
      }
    }
  }
}

function pesquisarVideoaula() {
  const entrada = document.getElementsByTagName('input')[0];
  const filtro = entrada.value.toUpperCase();
  const tabela = document.getElementsByTagName('table')[0];
  var linha, coluna, texto;

  linha = tabela.getElementsByTagName('tr');

  for (var i = 0; i < linha.length; i++) {
    coluna = linha[i].getElementsByTagName('td')[0];

    if (coluna) {
      texto = coluna.textContent || coluna.innerText;

      if (texto.toUpperCase().indexOf(filtro) > -1) {
        linha[i].style.display = '';
      } else {
        linha[i].style.display = 'none';
      }
    }
  }
}

function pesquisarVaga() {
  const entrada = document.getElementsByTagName('input')[0];
  const filtro = entrada.value.toUpperCase();
  const tabela = document.getElementsByTagName('table')[0];
  var linha, coluna, texto;

  linha = tabela.getElementsByTagName('tr');

  for (var i = 0; i < linha.length; i++) {
    coluna = linha[i].getElementsByTagName('td')[1];

    if (coluna) {
      texto = coluna.textContent || coluna.innerText;

      if (texto.toUpperCase().indexOf(filtro) > -1) {
        linha[i].style.display = '';
      } else {
        linha[i].style.display = 'none';
      }
    }
  }
}

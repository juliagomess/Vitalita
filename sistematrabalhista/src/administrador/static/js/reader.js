var elementos = [];
var indice = 0;

const mapeamento = {
	a: 'link', 
	button: 'button',
	h1: 'heading',
	h2: 'heading',
	h3: 'heading', 
	h4: 'heading', 
	h5: 'heading', 
	h6: 'heading', 
	strong: 'heading',
	p: 'paragraph',
	small: 'paragraph',
	html: 'page',
	img: 'image',
	aside: 'aside',
	nav: 'nav',
	ul: 'ul',
	table: 'table',
	tbody: 'tbody',
	th: 'th',
	td: 'td',
	tr: 'tr',
	label: 'label',
	input: 'input',
	textarea: 'textarea',
};

const narrador = {
	page(elemento) {
		const titulo = elemento.querySelector('title').textContent;
		audio(`Página ${titulo}`);
	},

	link(elemento) {
		audio(`Link, ${acessibilidade(elemento)}. Para acessar o link, pressione ENTER`);
	},

	button(elemento) {
		audio(`Botão, ${acessibilidade(elemento)}. Para clicar no botão, pressione ENTER`);
	},

	heading(elemento) {
		audio(`${acessibilidade(elemento)}`);
	},

	paragraph(elemento) {
		audio(elemento.textContent);
	},

	image(elemento) {
		audio(`Imagem, ${acessibilidade(elemento)}`);
	},

	nav(elemento) {
		audio(`Barra de navegação`);
	},

	aside(elemento) {
		audio(`Barra lateral`);
	},

	ul(elemento) {
		const quantidade = $(elemento).children('li').length;
		var plural;

		if (quantidade > 1) {
			plural = 'itens';
		} else {
			plural = 'item;'
		}

		audio(`Lista com ${quantidade} ${plural}`);
	},

	table(elemento) {
		audio(`Tabela`);
	},

	tbody(elemento) {
		const quantidade = $(elemento).children('tr').length;
		let plural;

		if (quantidade > 1) {
			plural = 'itens';
		} else {
			plural = 'item';
		}

		audio(`Tabela possui ${quantidade} ${plural}`);
	},

	th(elemento) {
		audio(`Coluna da tabela, ${acessibilidade(elemento)}`);
	},

	td(elemento) {
		audio(`Conteúdo da coluna, ${acessibilidade(elemento)}`);
	},

	tr(elemento) {
		audio(`Linha da tabela`);
	},

	label(elemento) {
		audio(`${acessibilidade(elemento)}`);
	},

	input(elemento) {
		const valor = $(elemento)[0].value;
		const formulario = $(elemento)[0].placeholder;

		if (valor !== '') {
			audio(`Texto de entrada, ${valor}`);
		} else {
			audio(`Texto de entrada, ${formulario}`);
		}
	},

	textarea(elemento) {
		const valor = $(elemento)[0].value;
		const formulario = $(elemento)[0].placeholder;

		if (valor !== '') {
			audio(`Caixa de texto, ${valor}`);
		} else {
			audio(`Caixa de texto, ${formulario}`);
		}
	},

	default(elemento) {
		audio(`${elemento.tagName}, ${acessibilidade(elemento)}`);
	}
};

$(document).ready(function() {
	const todos = $('*');
	var atual;

	elementos = [];
	indice = 0;

	for (var i = 0; i < todos.length; i += 1) {
		atual = todos[i];

		if (existeAudio(atual)) {
			elementos.push(atual);
		}
	}

	for (var i = 0; i < elementos.length; i += 1) {
		atual = elementos[i];
		atual.setAttribute('tabindex', i);
		elementos[i] = atual;
	}
});

function existeAudio(elemento) {
	const tags = [
		'html', 
		'h1', 
		'h2', 
		'h3', 
		'h4', 
		'h5', 
		'h6', 
		'p', 
		'button',
		'img',
		'table',
		'th',
		'td',
		'tr',
		'tbody',
		'aside',
		'nav',
		'a',
		'ul',
		'strong',
		'small',
		'input',
		'textarea',
		'select',
		'option',
		'label',
	];

	for (var i = 0; i < tags.length; i += 1) {
		if ($(elemento)[0].tagName.toLowerCase() === tags[i]) {
			if ($(elemento)[0].ariaHidden !== 'true' && 
				$(elemento)[0].style.display !== 'none' && $(elemento)[0].type !== 'hidden') {
					return true;
			}
		}
	}

	return false;
}

function moverFoco(offset) {
	const ultimo = document.querySelector('.screen-reader-effect');

	if (ultimo) {
		ultimo.classList.remove('screen-reader-effect');
	}

	if (offset instanceof HTMLElement) {
		indice = elementos.findIndex(function(elemento) {
			return elemento === offset;
		});

		return focarElemento(offset);
	}

	indice = indice + offset;

	if (indice < 0) {
		indice = elementos.length - 1;

	} else {
		if (indice > elementos.length - 1) {
			indice = 0;
		}
	}

	focarElemento(elementos[indice]);
}

function obterElementoAtivo() {
	if (document.activeElement && document.activeElement !== document.body) {
		return document.activeElement;
	}

	return elementos[0];
}

function focarElemento(elemento) {
	if (elemento === document.body) {
		elemento = document.documentElement;
	}

	elemento.classList.add('screen-reader-effect');
	elemento.focus();

	anunciarElemento(elemento);
}

function anunciarElemento(elemento) {
	const funcionalidade = verificaFuncionalidade(elemento);

	if (narrador[funcionalidade]) {
		narrador[funcionalidade](elemento);
	} else {
		narrador.default(elemento);
	}
}

function verificaFuncionalidade(elemento) {
	const nome = elemento.tagName.toLowerCase();

	if (elemento.getAttribute('role')) {
		return elemento.getAttribute('role');
	}

	return mapeamento[nome] || 'default';
}

function acessibilidade(elemento) {
	const conteudo = elemento.textContent.trim();

	if (elemento.getAttribute('aria-label')) {
		return elemento.getAttribute('aria-label');
	} else {
		if (elemento.getAttribute('alt')) {
			return elemento.getAttribute('alt');
		}
	}

	return conteudo;
}

function audio(texto, retorno=null) {
	const sintetizador = new SpeechSynthesisUtterance(texto);	
	sintetizador.lang = 'pt-BR';

	if (retorno) {
		sintetizador.onend = retorno;
	}

	speechSynthesis.cancel();
	speechSynthesis.speak(sintetizador);
}

function tratarEventoLeitor(evt) {
	const habilitar = document.getElementById('habilitar');

	if (!habilitar || habilitar.checked) {
		if (evt.ctrlKey && evt.which === 39) {
			moverFoco(1);

		} else if (evt.ctrlKey && evt.which === 37) {
				moverFoco(-1);
		}

	} else {
		const ultimo = document.querySelector('.screen-reader-effect');

		if (ultimo) {
			ultimo.classList.remove('screen-reader-effect');
		}

		indice = 0;
	}
}

document.addEventListener('keydown', tratarEventoLeitor);
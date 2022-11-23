async function validarCEP(entrada) {
	var cep;
	const exp = /\-|\.|\/|\(|\)| /g

	const bloco = document.getElementById('erro_endereco');
	const titulo = document.getElementById('titulo_endereco');
	const rua = document.getElementById('rua');
	const bairro = document.getElementById('bairro');
	const cidade = document.getElementById('cidade');
	const estado = document.getElementById('estado');
	const mensagem = document.getElementById('erro');
	const leitor = document.getElementById('erro_leitor');
	const botao = document.getElementById('salvar');
	const valido = document.getElementById('endereco_valido');

	bloco.style.display = 'none';
	titulo.style.display = 'none';
	rua.style.display = 'none';
	bairro.style.display = 'none';
	cidade.style.display = 'none';
	estado.style.display = 'none';
	mensagem.style.display = 'none';

	cep = entrada.value.replace(exp, '');

	const parametros = {
		method: 'GET',
		mode: 'cors',
		cache: 'default'
	}

	if (cep.length == 8) {
		await fetch(`https://viacep.com.br/ws/${cep}/json/`, parametros)
			.then(resposta => {
				resposta.json().then(dados => {
					if (dados.erro != true) {
						if (!leitor) {
							bloco.style.display = 'block';
							titulo.style.display = 'block';
							rua.style.display = 'block';
							bairro.style.display = 'block';
							cidade.style.display = 'block';
							estado.style.display = 'block';
							titulo.innerHTML = 'CEP';
				  			rua.innerHTML = dados.logradouro;
				  			bairro.innerHTML = dados.bairro;
				  			cidade.innerHTML = dados.localidade;
				  			estado.innerHTML = dados.uf;
				  		}

			  			valido.value = 'sim';
			  			botao.disabled = false;

					} else {
						if (!leitor) {
							bloco.style.display = 'block';
							titulo.style.display = 'block';
							mensagem.style.display = 'block';
							titulo.innerHTML = 'Aviso';
							mensagem.innerHTML = 'Informe um CEP válido';
						} else {
							audio('Informe um CEP válido');
						}

						valido.value = 'nao';
						botao.disabled = true;
					}
				});
			})
			.catch(erro => {
				if (!leitor) {
					bloco.style.display = 'block';
					titulo.style.display = 'block';
					mensagem.style.display = 'block';
					titulo.innerHTML = 'Aviso';
					mensagem.innerHTML = 'Informe um CEP válido';
				} else {
					audio('Informe um CEP válido');
				}

				valido.value = 'nao';
				botao.disabled = true;
			});
	}
}

function validarCPF(entrada) {
	const invalidos = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999'];

	const bloco = document.getElementById('erro_documento');
	const titulo = document.getElementById('titulo_documento');
	const mensagem = document.getElementById('mensagem_documento');
	const leitor = document.getElementById('erro_leitor');
	const botao = document.getElementById('salvar');
	const valido = document.getElementById('documento_valido');

	var cpf, numeros, digito1, digito2, checado, resultado, controle;
	const exp = /\-|\.|\/|\(|\)| /g

	cpf = entrada.value.replace(exp, '');

	if (cpf.length == 11 && !invalidos.includes(cpf)) {
		numeros = cpf.slice(0, -2);
		digito1 = cpf[9];
		digito2 = cpf[10];

		if (checarDigitoCPF(numeros, digito1) && checarDigitoCPF(numeros + digito1, digito2)) {
			controle = true;
		} else {
			controle = false;
		}
	} else {
		controle = false;
	}

	if (!controle) {
		if (!leitor) {
			bloco.style.display = 'block';
			titulo.style.display = 'block';
			mensagem.style.display = 'block';
			titulo.innerHTML = 'Aviso';
			mensagem.innerHTML = 'Informe um documento válido';

		} else {
			audio('Informe um documento válido');
		}

		botao.disabled = true;
		valido.value = 'nao';
	} else {
		botao.disabled = false;
		valido.value = 'sim';
	}
}

function checarDigitoCPF(numero, digito) {
	var checado, resultado;
	
	checado = numero
		.split('')
		.map((item, indice) => {
			const res = item * (numero.length + 1 - indice);
			return res;
		})
		.reduce((x, y) => {
			return x + y;
		});

	resultado = 11 - (checado % 11);

	if (resultado === 10 || resultado === 11) {
		resultado = 0;
	}

	return resultado.toString() === digito;
}

function validarCNPJ(entrada) {
	const invalidos = ['00000000000000', '11111111111111', '22222222222222', '33333333333333', '44444444444444', '55555555555555', '66666666666666', '77777777777777', '88888888888888', '99999999999999'];

	var cnpj, posicao, tamanho, numeros, digitos, soma, resultado, i, iguais, controle;
	const exp = /\-|\.|\/|\(|\)| /g

	const bloco = document.getElementById('erro_documento');
	const titulo = document.getElementById('titulo_documento');
	const mensagem = document.getElementById('mensagem_documento');
	const leitor = document.getElementById('erro_leitor');
	const botao = document.getElementById('salvar');
	const valido = document.getElementById('documento_valido');

	bloco.style.display = 'none';
	titulo.style.display = 'none';
	mensagem.style.display = 'none';

	cnpj = entrada.value.replace(exp, '');

	if (cnpj.length == 14 && !invalidos.includes(cnpj)) {
		tamanho = cnpj.length - 2;
		numeros = cnpj.substring(0, tamanho);
		digitos = cnpj.substring(tamanho);
		soma = 0;
		posicao = tamanho - 7;

		for (i = tamanho; i >= 1; i--) {
			soma += numeros.charAt(tamanho - i) * posicao--;
			if (posicao < 2) {
				posicao = 9;
			}
		}

		resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;

		if (resultado != digitos.charAt(0)) {
			controle = false;

		} else {
			tamanho += 1;
			numeros = cnpj.substring(0, tamanho);
			soma = 0;
			posicao = tamanho - 7;

			for (i = tamanho; i >= 1; i--) {
				soma += numeros.charAt(tamanho - i) * posicao--;
				if (posicao < 2) {
					posicao = 9;
				}
			}

			resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;

			if (resultado != digitos.charAt(1)) {
        		controle = false;

			} else {
				controle = true;
			}
		}
	} else {
		controle = false;
	}

	if (!controle) {
		if (!leitor) {
			bloco.style.display = 'block';
			titulo.style.display = 'block';
			mensagem.style.display = 'block';
			titulo.innerHTML = 'Aviso';
			mensagem.innerHTML = 'Informe um documento válido';
		} else {
			audio('Informe um documento válido');
		}

		valido.value = 'nao';
		botao.disabled = true;
	} else {
		valido.value = 'sim';
		botao.disabled = false;
	}
}

function validarDados() {
	const documento = document.getElementById('documento_valido').value;
	const endereco = document.getElementById('endereco_valido').value;
	const botao = document.getElementById('salvar');

	const bloco = document.getElementById('erro_documento');
	const titulo = document.getElementById('titulo_documento');
	const mensagem = document.getElementById('mensagem_documento');
	const leitor = document.getElementById('erro_leitor');

	bloco.style.display = 'none';
	titulo.style.display = 'none';
	mensagem.style.display = 'none';

	if (documento == 'sim' && endereco == 'sim') {
		botao.disabled = true;
		return true;
	} 

	if (documento == 'sim' && endereco == 'nao') {
		if (!leitor) {
			bloco.style.display = 'block';
			titulo.style.display = 'block';
			mensagem.style.display = 'block';
			titulo.innerHTML = 'Aviso';
			mensagem.innerHTML = 'CEP continua inválido';
		} else {
			audio('CEP continua inválido');
		}
	}

	if (documento == 'nao' && endereco == 'sim') {
		if (!leitor) {
			bloco.style.display = 'block';
			titulo.style.display = 'block';
			mensagem.style.display = 'block';
			titulo.innerHTML = 'Aviso';
			mensagem.innerHTML = 'Documento continua inválido';
		} else {
			audio('Documento continua inválido');
		}
	}

	if (documento == 'nao' && endereco == 'nao') {
		if (!leitor) {
			bloco.style.display = 'block';
			titulo.style.display = 'block';
			mensagem.style.display = 'block';
			titulo.innerHTML = 'Aviso';
			mensagem.innerHTML = 'Documento e CEP continuam inválidos';
		} else {
			audio('Documento e CEP continuam inválidos');
		}
	}

	botao.disabled = false;
	return false;
}
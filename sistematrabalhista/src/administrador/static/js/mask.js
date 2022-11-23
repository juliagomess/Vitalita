function mascaraCEP(cep){
	if(mascaraInteiro(cep)==false){
		event.returnValue = false;
	}       
	return formataCampo(cep, '00.000-000', event);
}

function mascaraTelefone(tel){  
	if(mascaraInteiro(tel)==false){
		event.returnValue = false;
	}       
	return formataCampo(tel, '(00) 0000-0000', event);
}

function mascaraCelular(cel){
	if(mascaraInteiro(cel)==false){
		event.returnValue = false;
	}

	return formataCampo(cel, '(00) 00000-0000', event);
}

function mascaraCPF(cpf){
	if(mascaraInteiro(cpf)==false){
		event.returnValue = false;
	}       
	return formataCampo(cpf, '000.000.000-00', event);
}

function mascaraCNPJ(cnpj){
    if(mascaraInteiro(cnpj)==false){
        event.returnValue = false;
    }       
    return formataCampo(cnpj, '00.000.000/0000-00', event);
}

function mascaraInteiro(){
	if (event.keyCode < 48 || event.keyCode > 57){
		event.returnValue = false;
		return false;
	}
	return true;
}

function formataCampo(campo, mascara, evento) { 
	let existeMascara; 

	let digitado = evento.keyCode;
	let exp = /\-|\.|\/|\(|\)| /g
	let numeros = campo.value.toString().replace(exp, ''); 

	let posicao = 0;    
	let novoValor= '';
	let tamanhoMascara = numeros.length;

    if (digitado != 8) {
       	for(i=0; i <= tamanhoMascara; i++) { 
       		existeMascara  = ((mascara.charAt(i) == '-') || (mascara.charAt(i) == '.')
       			|| (mascara.charAt(i) == '/')) 
       		existeMascara  = existeMascara || ((mascara.charAt(i) == '(') 
       			|| (mascara.charAt(i) == ')') || (mascara.charAt(i) == ' ')) 
       		
       		if (existeMascara) { 
       			novoValor += mascara.charAt(i); 
       			tamanhoMascara++;
       		} else { 
       			novoValor += numeros.charAt(posicao); 
       			posicao++; 
       		}              
    	}      
      	campo.value = novoValor;
       	return true; 
    } else { 
     	return true; 
    }
}
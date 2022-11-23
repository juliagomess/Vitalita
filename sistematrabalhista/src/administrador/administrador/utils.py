from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives

from regex import subf
from pybase64 import urlsafe_b64decode
from PIL import Image
from xhtml2pdf import pisa

import random
import hashlib
import io
import re

def send_mail(assunto, pagina, contexto, lista_destinatarios, 
	origem, falha_silenciosa=True):

	mensagem_folha = render_to_string(pagina, contexto)

	mensagem_texto = striptags(mensagem_folha)

	email = EmailMultiAlternatives(
		subject=assunto, body=mensagem_texto, 
		from_email=origem, to=lista_destinatarios
	)

	email.attach_alternative(mensagem_folha, 'text/html')
	email.send(fail_silently=falha_silenciosa)

def random_password(amostra, tamanho):
	senha = ''.join((random.choice(amostra) for i in range(tamanho)))
	return senha

def hash_password(senha):
	return hashlib.sha256(senha.encode()).hexdigest()

def rebuild_image(url):
	endereco = subf('^data:image/png;base64,', '', url)
	decodifcado = urlsafe_b64decode(endereco)
	imagem = Image.open(io.BytesIO(decodifcado))

	foto = io.BytesIO()
	imagem.save(foto, 'png')
	foto.seek(0)

	return foto

def render_to_pdf(pagina, contexto={}):
	fragmento = get_template(pagina)
	folha = fragmento.render(contexto)
	resultado = io.BytesIO()

	pdf = pisa.pisaDocument(io.BytesIO(folha.encode('utf-8')), resultado)

	if not pdf.err:
		return HttpResponse(resultado.getvalue(), content_type='application/pdf')
	
	return None

def validate_cpf(cpf):
	cpf = str(cpf)
	cpf = re.sub(r'[^0-9]', '', cpf)

	if not cpf or len(cpf) != 11:
		return False

	base = cpf[:-2]
	indice_reverso = 10
	total = 0

	for indice in range(19):
		if indice > 8:
			indice -= 9

		total += int(base[indice]) * indice_reverso
		indice_reverso -= 1

		if indice_reverso < 2:
			indice_reverso = 11

			digito = 11 - (total % 11)

			if digito > 9:
				digito = 0

			total = 0
			base += str(digito)

	sequencial = base == str(base[0]) * len(cpf)

	if cpf == base and not sequencial:
		return True
	else:
		return False

def validate_cnpj(cnpj):
	cnpj = str(cnpj)
	cnpj = re.sub(r'[^0-9]', '', cnpj)

	if not cnpj or len(cnpj) != 14:
		return False

	sequencial = cnpj == str(cnpj[0]) * len(cnpj)

	if sequencial:
		return False

	try:
		base = _calculate_cnpj_digit(cnpj, 1)
		base = _calculate_cnpj_digit(base, 2)
	except:
		return False

	if base == cnpj:
		return True
	else:
		return False
	
def _calculate_cnpj_digit(cnpj, digito):
	regressivos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

	if digito == 1:
		regressivos = regressivos[1:]
		base = cnpj[:-2]

	elif digito == 2:
		regressivos = regressivos
		base = cnpj

	else:
		return None

	total = 0

	for indice, regressivo in enumerate(regressivos):
		total += int(cnpj[indice]) * regressivo

	digito = 11 - (total % 11)
	digito = digito if digito <= 9 else 0

	base += str(digito)
	return base
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
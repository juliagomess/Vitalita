from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import connection
from empresa.utils import render_to_pdf

# Create your views here.
@login_required(login_url='login')
def associatedlist_view(request):
	associados = []

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM associado ORDER BY nome ASC")
		resultados = cursor.fetchall()

		for resultado in resultados:
			associado = {
				'id': resultado[0],
				'foto': settings.MEDIA_URL + resultado[1],
				'nome': resultado[2],
				'data_nascimento': resultado[3],
				'cpf': resultado[4],
				'celular': resultado[5],
				'email': resultado[6],
				'cep': resultado[8],
				'numero': resultado[9],
				'pcd': resultado[10],
				'outras_informacoes': resultado[11],
				'instituicao_ensino': resultado[12],
				'curso_extra': resultado[13],
				'empresa_trabalhada': resultado[14],
				'cargo_ocupado': resultado[15],
				'laudo_medico': resultado[16],
			}

			associados.append(associado)


	contexto = {
		'associados': associados,
	}

	return render(request, 'associated/list.html', contexto)


@login_required(login_url='login')
def associatedread_view(request, id=0):
	if id == 0:
		return redirect('associatedlist')

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM associado WHERE id=%s", [id])
		resultado = cursor.fetchone()

		if resultado != None:
			if resultado[16] != '':
				laudo = settings.MEDIA_URL + resultado[16]
			else:
				laudo = None

			formulario = {
				'id': resultado[0],
				'foto': settings.MEDIA_URL + resultado[1],
				'nome': resultado[2],
				'data_nascimento': resultado[3],
				'cpf': resultado[4],
				'celular': resultado[5],
				'email': resultado[6],
				'cep': resultado[8],
				'numero': resultado[9],
				'pcd': resultado[10],
				'outras_informacoes': resultado[11],
				'instituicao_ensino': resultado[12],
				'curso_extra': resultado[13],
				'empresa_trabalhada': resultado[14],
				'cargo_ocupado': resultado[15],
				'laudo_medico': laudo,
			}

			contexto = {
				'form': formulario,
			}

			return render(request, 'associated/read.html', contexto)

		else:
			return redirect('associatedlist')

@login_required(login_url='login')
def associatedpdf_view(request, id=0):
	if id == 0:
		return redirect('associatedlist')

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM associado WHERE id=%s", [id])
		resultado = cursor.fetchone()

		if resultado != None:
			formulario = {
				'id': resultado[0],
				'foto': settings.MEDIA_ROOT + '/' + resultado[1],
				'nome': resultado[2],
				'data_nascimento': resultado[3],
				'cpf': resultado[4],
				'celular': resultado[5],
				'email': resultado[6],
				'cep': resultado[8],
				'numero': resultado[9],
				'pcd': resultado[10],
				'outras_informacoes': resultado[11],
				'instituicao_ensino': resultado[12],
				'curso_extra': resultado[13],
				'empresa_trabalhada': resultado[14],
				'cargo_ocupado': resultado[15],
			}

			contexto = {
				'form': formulario,
			}

			pdf = render_to_pdf('associated/pdf.html', contexto)

			if pdf:
				resposta = HttpResponse(pdf, content_type='application/pdf')
				nomearquivo = resultado[2].replace(' ', '_').lower() + '.pdf'
				conteudo = 'inline; filename=%s' % (nomearquivo)
				resposta['Content-Disposition'] = conteudo
				return resposta

			else:
				return redirect('associatedread', id=id)
		else:
			return redirect('associatedlist')
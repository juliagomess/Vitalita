from django.conf import settings
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection
import os

# Create your views here.
@login_required(login_url='login')
def home_view(request):
	return render(request, 'session/home/index.html', {})

@login_required(login_url='login')
def courselist_view(request):
	cursos = []

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM curso ORDER BY titulo ASC")
		resultados = cursor.fetchall()

		for resultado in resultados:
			curso = {
				'id': resultado[0],
				'logo': settings.MEDIA_URL + resultado[1],
				'titulo': resultado[2],
				'data_exp': resultado[4],
				'descricao': resultado[5],
			}

			cursos.append(curso)

	contexto = {
		'cursos': cursos
	}

	return render(request, 'session/course/list.html', contexto)

@login_required(login_url='login')
def courseread_view(request, id=0):
	if id == 0:
		return redirect('courselist')

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM curso WHERE id=%s", [id])
		resultado = cursor.fetchone()

		if resultado != None:
			formulario = {
				'id': resultado[0],
				'logo': settings.MEDIA_URL + resultado[1],
				'titulo': resultado[2],
				'url': resultado[3],
				'data_exp': resultado[4],
				'descricao': resultado[5],
			}

			contexto = {
				'form': formulario
			}

			return render(request, 'session/course/read.html', contexto)
		else:
			return redirect('courselist')

@login_required(login_url='login')
def eventlist_view(request):
	eventos = []

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM evento ORDER BY titulo ASC")
		resultados = cursor.fetchall()

		for resultado in resultados:
			evento = {
				'id': resultado[0],
				'logo': settings.MEDIA_URL + resultado[1],
				'titulo': resultado[2],
				'data_exp': resultado[4],
				'descricao': resultado[5],
			}

			eventos.append(evento)

	contexto = {
		'eventos': eventos
	}

	return render(request, 'session/event/list.html', contexto)

@login_required(login_url='login')
def eventread_view(request, id=0):
	if id == 0:
		return redirect('eventlist')

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM evento WHERE id=%s", [id])
		resultado = cursor.fetchone()

		if resultado != None:
			formulario = {
				'id': resultado[0],
				'logo': settings.MEDIA_URL + resultado[1],
				'titulo': resultado[2],
				'url': resultado[3],
				'data_exp': resultado[4],
				'descricao': resultado[5],
			}

			contexto = {
				'form': formulario
			}

			return render(request, 'session/event/read.html', contexto)
		else:
			return redirect('eventlist')

@login_required(login_url='login')
def gamelist_view(request):
	jogos = []

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM jogo ORDER BY titulo ASC")
		resultados = cursor.fetchall()

		for resultado in resultados:
			jogo = {
				'id': resultado[0],
				'logo': settings.MEDIA_URL + resultado[1],
				'titulo': resultado[2],
				'url': resultado[3],
				'descricao': resultado[4],
			}

			jogos.append(jogo)

	contexto = {
		'jogos': jogos
	}

	return render(request, 'session/game/list.html', contexto)

@login_required(login_url='login')
def gameread_view(request, id=0):
	if id == 0:
		return redirect('gamelist')

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM jogo WHERE id=%s", [id])
		resultado = cursor.fetchone()

		if resultado != None:
			formulario = {
				'id': resultado[0],
				'logo': settings.MEDIA_URL + resultado[1],
				'titulo': resultado[2],
				'url': resultado[3],
				'descricao': resultado[4],
			}

			contexto = {
				'form': formulario
			}

			return render(request, 'session/game/read.html', contexto)
		else:
			return redirect('gamelist')

@login_required(login_url='login')
def joblist_view(request):
	vagas = []

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM vaga WHERE data_exp >= CURDATE() ORDER BY titulo ASC")
		resultados = cursor.fetchall()

		for resultado in resultados:
			cursor.execute("SELECT * FROM empresa WHERE id=%s", [resultado[1]])
			empresa = cursor.fetchone()

			if empresa:
				vaga = {
					'id': resultado[0],
					'razao_social': empresa[3],
					'email': empresa[7],
					'logo': settings.MEDIA_URL + resultado[2],
					'titulo': resultado[3],
					'data_exp': resultado[4],
					'descricao': resultado[5],
				}

				vagas.append(vaga)

	contexto = {
		'vagas': vagas
	}

	return render(request, 'session/job/list.html', contexto)

@login_required(login_url='login')
def jobread_view(request, id=0):
	if id == 0:
		return redirect('joblist')

	try:
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM vaga WHERE id=%s", [id])
			resultado = cursor.fetchone()

			if resultado:
			
				cursor.execute("SELECT * FROM empresa WHERE id=%s", [resultado[1]])
				empresa = cursor.fetchone()

				if empresa:
					formulario = {
						'id': resultado[0],
						'razao_social': empresa[3],
						'email': empresa[7],
						'logo': settings.MEDIA_URL + resultado[2],
						'titulo': resultado[3],
						'url': resultado[8],
						'data_exp': resultado[4],
						'descricao': resultado[5],
					}

					contexto = {
						'form': formulario
					}

					return render(request, 'session/job/read.html', contexto)
				
				else:
					return redirect('joblist')
			else:
				return redirect('joblist')
	except:
		return redirect('joblist')

@login_required(login_url='login')
def videolessonlist_view(request):
	videoaulas = []

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM videoaula ORDER BY titulo ASC")
		resultados = cursor.fetchall()

		for resultado in resultados:
			videoaula = {
				'id': resultado[0],
				'logo': settings.MEDIA_URL + resultado[1],
				'titulo': resultado[2],
				'url': resultado[3],
				'descricao': resultado[4],
			}

			videoaulas.append(videoaula)

	contexto = {
		'videoaulas': videoaulas
	}

	return render(request, 'session/videolesson/list.html', contexto)

@login_required(login_url='login')
def videolessonread_view(request, id=0):
	if id == 0:
		return redirect('videolessonlist')

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM videoaula WHERE id=%s", [id])
		resultado = cursor.fetchone()

		if resultado != None:
			formulario = {
				'id': resultado[0],
				'logo': settings.MEDIA_URL + resultado[1],
				'titulo': resultado[2],
				'url': 'https://www.youtube.com/embed/' + resultado[3].split('=')[1].split('&ab_channel')[0],
				'descricao': resultado[4],
			}

			contexto = {
				'form': formulario
			}

			return render(request, 'session/videolesson/read.html', contexto)
		else:
			return redirect('videolessonlist')
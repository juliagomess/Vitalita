from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection

from administradores.models import Administrador
from associados.models import Associado 
from empresas.models import Empresa

from .backend import BackendLogin
from .forms import FormLogin, FormTrocar, FormCurriculo
from .utils import rebuild_image, render_to_pdf

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrador.serializers import UserSerializer, GroupSerializer

import os, requests

@csrf_protect
def login_view(request):
	if request.method == 'POST':
		try:
			formulario = FormLogin(request.POST)

			if formulario.is_valid():
				campos = formulario.clean_form()

				administrador = BackendLogin.authenticate(request, campos['email'], campos['senha_hash'])

				if administrador != None and administrador != False:
					administrador.is_authenticated = True
					administrador.save()

					login(request, administrador, backend='administrador.backend.BackendLogin')
					return redirect('adminlist')

				else:
					formulario = request.POST

					if administrador == False:
						erro = 'Senha não confere'

					else:
						erro = 'Não existe administrador com esse email'
			else:
				formulario = request.POST
				erro = 'Preencher campos corretamente'
		except:
			formulario = request.POST
			erro = 'Não foi possível realizar o login. Tente novamente'
	else:
		formulario = { 'email': '', 'senha': '' }
		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
	}

	contexto.update(csrf(request))
	return render(request, 'login/index.html', contexto)

def forgot_view(request):
	return render(request, 'login/forgot.html', {})

def readmore_view(request):
	return render(request, 'login/readmore.html', {})

def logout_view(request):
	try:
		email = request.user.email
		logout(request)
		administrador = Administrador.objects.get(email=email)
		administrador.is_authenticated = False
		administrador.save()
	finally:
		return redirect('login')

@login_required(login_url='login')
@csrf_protect
def changepassword_view(request):
	if request.method == 'POST':
		formulario = FormTrocar(request.POST)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				administrador = Administrador.objects.get(email=campos['email'])

				if campos['senha_hash'] == campos['confirma_hash']:
					administrador.senha_hash = campos['senha_hash']
					administrador.save()
					return redirect('adminlist')

				else:
					formulario = request.POST
					erro = 'Senhas não são idênticas'

			except:
				formulario = request.POST
				erro = 'Email não cadastrado'
		else:
			formulario = request.POST
			erro = 'Preencher campos corretamente'
	else:
		formulario = {
			'email': '',
			'senha': '',
			'confirma': ''
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
	}

	contexto.update(csrf(request))
	return render(request, 'option/changepassword.html', contexto)

@login_required(login_url='login')
def joblist_view(request):
	vagas = []

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM vaga WHERE data_exp >= CURDATE() ORDER BY titulo ASC")
		resultados = cursor.fetchall()

		for resultado in resultados:
			try:
				empresa = Empresa.objects.get(id=resultado[1])

			except:
				empresa = None

			if empresa:
				vaga = {
					'id': resultado[0],
					'razao_social': empresa.razao_social,
					'email': empresa.email,
					'logo': settings.MEDIA_URL + resultado[2],
					'titulo': resultado[3],
					'data_exp': resultado[5],
					'descricao': resultado[6],
				}

				vagas.append(vaga)

	contexto = {
		'vagas': vagas
	}

	return render(request, 'job/list.html', contexto)

@login_required(login_url='login')
def jobread_view(request, id=0):
	if id == 0:
		return redirect('joblist')

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM vaga WHERE id=%s", [id])
		resultado = cursor.fetchone()

		if resultado:
			try:
				empresa = Empresa.objects.get(id=resultado[1])

				formulario = {
					'id': resultado[0],
					'razao_social': empresa.razao_social,
					'email': empresa.email,
					'logo': settings.MEDIA_URL + resultado[2],
					'titulo': resultado[3],
					'url': resultado[4],
					'data_exp': resultado[5],
					'descricao': resultado[6],
				}

				contexto = {
					'form': formulario
				}

				return render(request, 'job/read.html', contexto)

			except:
				return redirect('joblist')
		else:
			return redirect('joblist')

@login_required(login_url='login')
def jobpdf_view(request, id=0):
	if id == 0:
		return redirect('joblist')

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM vaga WHERE id=%s", [id])
		resultado = cursor.fetchone()

		if resultado:
			try:
				empresa = Empresa.objects.get(id=resultado[1])

				formulario = {
					'id': resultado[0],
					'razao_social': empresa.razao_social,
					'email': empresa.email,
					'logo': settings.MEDIA_ROOT + '/' + resultado[2],
					'titulo': resultado[3],
					'url': resultado[4],
					'data_exp': resultado[5],
					'descricao': resultado[6],
				}

				contexto = {
					'form': formulario
				}

				pdf = render_to_pdf('job/pdf.html', contexto)

				if pdf:
					resposta = HttpResponse(pdf, content_type='application/pdf')
					nomearquivo = resultado[3].replace(' ', '_').lower() + '.pdf'
					conteudo = 'inline; filename=%s' % (nomearquivo)
					resposta['Content-Disposition'] = conteudo
					return resposta

				else:
					return redirect('jobread', id=id)
			except:
				return redirect('joblist')
		else:
			return redirect('joblist')

@login_required(login_url='login')
def resumelist_view(request):
	curriculos = []

	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM curriculo ORDER BY created_at DESC")
		resultados = cursor.fetchall()

		for resultado in resultados:
			try:
				associado = Associado.objects.get(id=resultado[1])
			except:
				associado = None

			if associado:
				curriculo = {
					'id': resultado[0],
					'nome': associado.nome,
					'email': associado.email,
					'instituicao_ensino': resultado[2],
					'curso_extra': resultado[3],
					'empresa_trabalhada': resultado[4],
					'cargo_ocupado': resultado[5],
					'laudo_medico': resultado[6],
				}

				curriculos.append(curriculo)

	contexto = {
		'curriculos': curriculos,
	}

	return render(request, 'resume/list.html', contexto)

@login_required(login_url='login')
def resumeread_view(request, id=0):
	if id == 0:
		return redirect('resumelist')

	if request.method == 'POST':
		formulario = FormCurriculo(request.POST, request.FILES or None)

		if formulario.is_valid():
			campos = formulario.clean_form()

			if 'novo_laudo_medico' in request.FILES:
				arquivo = request.FILES['novo_laudo_medico']
				caminho = 'curriculo/' + str(campos['associado_id']) + '/' + arquivo.name

				with open(settings.MEDIA_ROOT + '/' + caminho, 'wb+') as destino:
					for fatia in arquivo.chunks():
						destino.write(fatia)

				if campos['laudo_medico'] != '':
					if os.path.exists(settings.MEDIA_ROOT + '/' + campos['laudo_medico']):
						os.remove(settings.MEDIA_ROOT + '/' + campos['laudo_medico'])

			else:
				caminho = campos['laudo_medico']

			with connection.cursor() as cursor:
				cursor.execute("UPDATE associado SET instituicao_ensino=%s, curso_extra=%s, empresa_trabalhada=%s, cargo_ocupado=%s, laudo_medico=%s WHERE id=%s",
				[
					campos['instituicao_ensino'], 
					campos['curso_extra'], 
					campos['empresa_trabalhada'], 
					campos['cargo_ocupado'],
					caminho,
					campos['associado_id']
				]
			)

			return redirect('resumedelete', id=id)

		else:
			return redirect('resumelist')
	else:
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM curriculo WHERE id=%s", [id])
			resultado = cursor.fetchone()

			if resultado:
				try:
					associado = Associado.objects.get(id=resultado[1])

					if resultado[6] != '':
						laudo_medico = settings.MEDIA_URL + resultado[6]
					else:
						laudo_medico = None

					formulario = {
						'id': resultado[0],
						'associado_id': resultado[1],
						'nome': associado.nome,
						'email': associado.email,
						'instituicao_ensino': resultado[2],
						'curso_extra': resultado[3],
						'empresa_trabalhada': resultado[4],
						'cargo_ocupado': resultado[5],
						'laudo_medico': resultado[6],
						'download': laudo_medico,
					}

					contexto = {
						'form': formulario,
					}

					return render(request, 'resume/read.html', contexto)

				except:
					return redirect('resumelist')
			else:
				return redirect('resumelist')

@login_required(login_url='login')
def resumedelete_view(request, id=0):
	if id == 0:
		return redirect('resumelist')

	with connection.cursor() as cursor:
		cursor.execute("DELETE FROM curriculo WHERE id=%s", [id])

	return redirect('resumelist')



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
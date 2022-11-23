from django.conf import settings
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection

from session.models import LoginAssociado
from .backend import BackendLogin
from .forms import FormLogin, FormRedefinir, FormTrocar
from .utils import rebuild_image, send_mail, hash_password, random_password

@csrf_protect
def login_view(request):
	if request.method == 'POST':
		try:
			formulario = FormLogin(request.POST)
			
			if formulario.is_valid():
				campos = formulario.clean_form()

				associado = BackendLogin.authenticate(request, campos['email'], campos['senha_hash'])

				if associado != None and associado != False:
					associado.is_authenticated = True
					associado.save()

					login(request, associado, backend='associado.backend.BackendLogin')
					return redirect('home')

				else:
					formulario = request.POST

					if associado == False:
						erro = 'Senha não confere'

					else:
						erro = 'Não existe associado com esse email'
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
		associado = LoginAssociado.objects.get(email=email)
		associado.delete()
	finally:
		return redirect('login')
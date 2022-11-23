from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Evento
from .forms import FormCadastro, FormEditar

# Create your views here.
@login_required(login_url='login')
def eventlist_view(request):
	eventos = Evento.objects.all()

	contexto = {
		'eventos': eventos,
	}
	return render(request, 'event/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def eventcreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = FormCadastro(request.POST, request.FILES)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				novo_evento = Evento.objects.create(logo=campos['logo'], titulo=campos['titulo'],  url=campos['url'], data_exp=campos['data_exp'], descricao=campos['descricao'])
				novo_evento.save()
				return redirect('eventlist')

			except:
				formulario = request.POST
				erro = 'Não foi possível cadastrar novo evento'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		formulario = {
			'logo': None,
			'titulo': '',
			'url': '',
			'data_exp': '',
			'descricao': '',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'event/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def eventedit_view(request, id=0):
	if id == 0:
		return redirect('eventlist')

	editar = True

	if request.method == 'POST':
		formulario = FormEditar(request.POST, request.FILES or None)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_evento = Evento.objects.get(id=id)

				if 'logo' in request.FILES:
					editar_evento.removeLogo()
					editar_evento.logo = campos['logo']
				
				editar_evento.titulo = campos['titulo']
				editar_evento.url = campos['url']
				editar_evento.data_exp = campos['data_exp']
				editar_evento.descricao = campos['descricao']
				editar_evento.save()
				return redirect('eventlist')

			except:
				formulario = request.POST
				erro = 'Não foi possível atualizar este evento'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Evento.objects.get(id=id)
			erro = None

		except:
			return redirect('eventlist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'event/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def eventdelete_view(request, id=0):
	if id == 0:
		return redirect('eventlist')

	if request.method == 'POST':	
		try:
			evento = Evento.objects.get(id=id)
			evento.delete()

		finally:
			return redirect('eventlist')
	else:
		return redirect('eventlist')
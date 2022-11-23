from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Jogo
from .forms import FormCadastro, FormEditar

# Create your views here.
@login_required(login_url='login')
def gamelist_view(request):
	jogos = Jogo.objects.all()

	contexto = {
		'jogos': jogos,
	}
	return render(request, 'game/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def gamecreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = FormCadastro(request.POST, request.FILES)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				novo_jogo = Jogo.objects.create(logo=campos['logo'], titulo=campos['titulo'], url=campos['url'], descricao=campos['descricao'])
				novo_jogo.save()
				return redirect('gamelist')

			except:
				formulario = request.POST
				erro = 'Não foi possível cadastrar novo jogo'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		formulario = {
			'logo': None,
			'titulo': '',
			'url': '',
			'descricao': '',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'game/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def gameedit_view(request, id=0):
	if id == 0:
		return redirect('gamelist')

	editar = True

	if request.method == 'POST':
		formulario = FormEditar(request.POST, request.FILES or None)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_jogo = Jogo.objects.get(id=id)

				if 'logo' in request.FILES:
					editar_jogo.removeLogo()
					editar_jogo.logo = campos['logo']

				editar_jogo.titulo = campos['titulo']
				editar_jogo.url = campos['url']
				editar_jogo.descricao = campos['descricao']
				editar_jogo.save()
				return redirect('gamelist')

			except:
				formulario = request.POST
				erro = 'Não foi possível atualizar este jogo'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Jogo.objects.get(id=id)
			erro = None

		except:
			return redirect('gamelist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'game/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def gamedelete_view(request, id=0):
	if id == 0:
		return redirect('gamelist')

	if request.method == 'POST':	
		try:
			jogo = Jogo.objects.get(id=id)
			jogo.delete()

		finally:
			return redirect('gamelist')
	else:
		return redirect('gamelist')
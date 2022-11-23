from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Videoaula
from .forms import FormCadastro, FormEditar

# Create your views here.
@login_required(login_url='login')
def videolessonlist_view(request):
	videoaulas = Videoaula.objects.all()

	contexto = {
		'videoaulas': videoaulas,
	}
	return render(request, 'videolesson/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def videolessoncreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = FormCadastro(request.POST, request.FILES)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				nova_videoaula = Videoaula.objects.create(logo=campos['logo'], titulo=campos['titulo'], url=campos['url'], descricao=campos['descricao'])
				nova_videoaula.save()
				return redirect('videolessonlist')

			except:
				formulario = request.POST
				erro = 'Não foi possível cadastrar nova videoaula'
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
	return render(request, 'videolesson/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def videolessonedit_view(request, id=0):
	if id == 0:
		return redirect('videolessonlist')

	editar = True

	if request.method == 'POST':
		formulario = FormEditar(request.POST, request.FILES or None)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_videoaula = Videoaula.objects.get(id=id)

				if 'logo' in request.FILES:
					editar_videoaula.removeLogo()
					editar_videoaula.logo = campos['logo']

				editar_videoaula.titulo = campos['titulo']
				editar_videoaula.url = campos['url']
				editar_videoaula.descricao = campos['descricao']
				editar_videoaula.save()
				return redirect('videolessonlist')

			except:
				formulario = request.POST
				erro = 'Não foi possível atualizar esta videoaula'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Videoaula.objects.get(id=id)
			erro = None

		except:
			return redirect('videolessonlist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'videolesson/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def videolessondelete_view(request, id=0):
	if id == 0:
		return redirect('videolessonlist')

	if request.method == 'POST':	
		try:
			videoaula = Videoaula.objects.get(id=id)
			videoaula.delete()

		finally:
			return redirect('videolessonlist')
	else:
		return redirect('videolessonlist')
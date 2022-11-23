from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Curso
from .forms import FormCadastro, FormEditar

# Create your views here.
@login_required(login_url='login')
def courselist_view(request):
	cursos = Curso.objects.all()

	contexto = {
		'cursos': cursos,
	}
	return render(request, 'course/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def coursecreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = FormCadastro(request.POST, request.FILES)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				novo_curso = Curso.objects.create(logo=campos['logo'], titulo=campos['titulo'],  url=campos['url'], data_exp=campos['data_exp'], descricao=campos['descricao'])
				novo_curso.save()
				return redirect('courselist')

			except:
				formulario = request.POST
				erro = 'Não foi possível cadastrar novo curso'
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
	return render(request, 'course/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def courseedit_view(request, id=0):
	if id == 0:
		return redirect('courselist')

	editar = True

	if request.method == 'POST':
		formulario = FormEditar(request.POST, request.FILES or None)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_curso = Curso.objects.get(id=id)

				if 'logo' in request.FILES:
					editar_curso.removeLogo()
					editar_curso.logo = campos['logo']

				editar_curso.titulo = campos['titulo']
				editar_curso.url = campos['url']
				editar_curso.data_exp = campos['data_exp']
				editar_curso.descricao = campos['descricao']
				editar_curso.save()
				return redirect('courselist')

			except:
				formulario = request.POST
				erro = 'Não foi possível atualizar este curso'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Curso.objects.get(id=id)
			erro = None

		except:
			return redirect('courselist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'course/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def coursedelete_view(request, id=0):
	if id == 0:
		return redirect('courselist')

	if request.method == 'POST':	
		try:
			curso = Curso.objects.get(id=id)
			curso.delete()

		finally:
			return redirect('courselist')
	else:
		return redirect('courselist')
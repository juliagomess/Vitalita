from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Vaga
from .forms import FormCadastro, FormEditar

# Create your views here.
@login_required(login_url='login')
def joblist_view(request):
	vagas = Vaga.objects.filter(empresa_id=request.user.id)

	contexto = {
		'vagas': vagas,
	}
	return render(request, 'job/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def jobcreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = FormCadastro(request.POST, request.FILES)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				nova_vaga = Vaga.objects.create(empresa_id=request.user.id, logo=campos['logo'], titulo=campos['titulo'],  url=campos['url'], data_exp=campos['data_exp'], descricao=campos['descricao'])
				nova_vaga.save()
				return redirect('joblist')

			except:
				formulario = request.POST
				erro = 'Não foi possível cadastrar nova vaga'
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
	return render(request, 'job/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def jobedit_view(request, id=0):
	if id == 0:
		return redirect('joblist')

	editar = True

	if request.method == 'POST':
		formulario = FormEditar(request.POST, request.FILES or None)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_vaga = Vaga.objects.get(id=id)

				if 'logo' in request.FILES:
					editar_vaga.removeLogo()
					editar_vaga.logo = campos['logo']

				editar_vaga.titulo = campos['titulo']
				editar_vaga.url = campos['url']
				editar_vaga.data_exp = campos['data_exp']
				editar_vaga.descricao = campos['descricao']
				editar_vaga.save()

				return redirect('joblist')

			except:
				formulario = request.POST
				erro = 'Não foi possível atualizar este vaga'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Vaga.objects.get(id=id)
			erro = None

		except:
			return redirect('joblist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar
	}

	contexto.update(csrf(request))
	return render(request, 'job/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def jobdelete_view(request, id=0):
	if id == 0:
		return redirect('joblist')

	if request.method == 'POST':	
		try:
			vaga = Vaga.objects.get(id=id)
			vaga.delete()

		finally:
			return redirect('joblist')
	else:
		return redirect('joblist')
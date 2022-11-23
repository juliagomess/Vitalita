from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Empresa
from .forms import FormCadastro, FormEditar
from administrador.utils import validate_cnpj

# Create your views here.
@login_required(login_url='login')
def companylist_view(request):
	empresas = Empresa.objects.all()

	contexto = {
		'empresas': empresas,
	}

	return render(request, 'company/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def companycreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = FormCadastro(request.POST, request.FILES)

		if formulario.is_valid():
			campos = formulario.clean_form()

			if Empresa.objects.filter(email=campos['email']) | Empresa.objects.filter(cnpj=campos['cnpj']):
				formulario = request.POST
				
				if Empresa.objects.filter(email=campos['email']):
					erro = 'Já existe empresa com esse email cadastrado'
				else:
					erro = 'Já existe empresa com esse CNPJ'
			else:
				if validate_cnpj(campos['cnpj']):
					try:
						nova_empresa = Empresa.objects.create(foto=campos['foto'], logo=campos['logo'], razao_social=campos['razao_social'],
							nome_contato=campos['nome_contato'], cnpj=campos['cnpj'], telefone=campos['telefone'], cep=campos['cep'], 
							numero=campos['numero'], email=campos['email'], senha_hash=campos['senha_hash'], acessibilidade=campos['acessibilidade'])

						nova_empresa.save()
						return redirect('companylist')
					except:
						formulario = request.POST
						erro = 'Não foi possível cadastrar nova empresa'
				else:
					formulario = request.POST
					erro = 'CNPJ inválido'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		formulario = {
			'logo': None,
			'foto': None,
			'razao_social': '', 
			'cnpj': '', 
			'nome_contato': '', 
			'email': '', 
			'senha': '', 
			'telefone': '',
			'cep': '',  
			'numero': '',
			'acessibilidade': 'nenhum',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar,
	}

	contexto.update(csrf(request))
	return render(request, 'company/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def companyedit_view(request, id=0):
	if id == 0:
		return redirect('companylist')

	editar = True

	if request.method == 'POST':
		formulario = FormEditar(request.POST, request.FILES or None)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_empresa = Empresa.objects.get(id=id)

				if 'foto' in request.FILES:
					editar_empresa.removePhoto()
					editar_empresa.foto = campos['foto']

				if 'logo' in request.FILES:
					editar_empresa.removeLogo()
					editar_empresa.logo = campos['logo']

				editar_empresa.razao_social = campos['razao_social']
				editar_empresa.nome_contato = campos['nome_contato']
				editar_empresa.telefone = campos['telefone']
				editar_empresa.cep = campos['cep']
				editar_empresa.cnpj = campos['cnpj']
				editar_empresa.numero = campos['numero']
				editar_empresa.acessibilidade = campos['acessibilidade']

				if request.POST.get('senha') != '':
					editar_empresa.senha_hash = campos['senha_hash']

				if editar_empresa.email != campos['email']:
					if not Empresa.objects.filter(email=campos['email']):
						editar_empresa.email = campos['email']
						editar_empresa.save()
						return redirect('companylist')

					else:
						formulario = request.POST
						erro = 'Já existe empresa com esse email cadastrado'
				else:
					editar_empresa.email = campos['email']
					editar_empresa.save()
					return redirect('companylist')

			except:
				formulario = request.POST
				erro = 'Não foi possível atualizar este empresa'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Empresa.objects.get(id=id)
			erro = None

		except:
			return redirect('companylist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar,
	}

	contexto.update(csrf(request))
	return render(request, 'company/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def companydelete_view(request, id=0):
	if id == 0:
		return redirect('companylist')

	if request.method == 'POST':
		try:
			empresa = Empresa.objects.get(id=id)
			empresa.delete()
		finally:
			return redirect('companylist')
	else:
		return redirect('companylist')
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Associado
from .forms import FormCadastro, FormEditar
from administrador.utils import validate_cpf
from django.db import connection
from django.conf import settings
from administrador.utils import render_to_pdf
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login')
def associatedlist_view(request):
	associados = Associado.objects.all()

	contexto = {
		'associados': associados,
	}

	return render(request, 'associated/list.html', contexto)

@login_required(login_url='login')
@csrf_protect
def associatedcreate_view(request):
	editar = False

	if request.method == 'POST':
		formulario = FormCadastro(request.POST, request.FILES)

		if formulario.is_valid():
			campos = formulario.clean_form()

			if Associado.objects.filter(email=campos['email']) | Associado.objects.filter(cpf=campos['cpf']):
				formulario = request.POST
				
				if Associado.objects.filter(email=campos['email']):
					erro = 'Já existe associado com esse email cadastrado'
				else:
					erro = 'Já existe associado com esse CPF'
			else:
				if validate_cpf(campos['cpf']):
					try:
						novo_associado = Associado.objects.create(foto=campos['foto'], nome=campos['nome'], cpf=campos['cpf'], 
							celular=campos['celular'], cep=campos['cep'], data_nascimento=campos['data_nascimento'], 
							numero=campos['numero'], email=campos['email'], senha_hash=campos['senha_hash'], pcd=campos['pcd'], 
							outras_informacoes=campos['outras_informacoes'], acessibilidade=campos['acessibilidade'])

						novo_associado.save()
						return redirect('associatedlist')
					except:
						formulario = request.POST
						erro = 'Não foi possível cadastrar novo associado'
				else:
					formulario = request.POST
					erro = 'CPF inválido'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		formulario = {
			'foto': None,
			'nome': '', 
			'data_nascimento': '',
			'cpf': '', 
			'email': '', 
			'senha': '', 
			'celular': '',
			'cep': '',  
			'numero': '',
			'pcd': '',
			'outras_informacoes': '',
			'acessibilidade': 'nenhum',
		}

		erro = None

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar,
	}

	contexto.update(csrf(request))
	return render(request, 'associated/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def associatededit_view(request, id=0):
	if id == 0:
		return redirect('associatedlist')

	editar = True

	if request.method == 'POST':
		formulario = FormEditar(request.POST, request.FILES or None)

		if formulario.is_valid():
			campos = formulario.clean_form()

			try:
				editar_associado = Associado.objects.get(id=id)

				if 'foto' in request.FILES:
					editar_associado.removePhoto()
					editar_associado.foto = campos['foto']

				editar_associado.nome = campos['nome']
				editar_associado.data_nascimento = campos['data_nascimento']
				editar_associado.celular = campos['celular']
				editar_associado.cep = campos['cep']
				editar_associado.cpf = campos['cpf']
				editar_associado.numero = campos['numero']
				editar_associado.pcd = campos['pcd']
				editar_associado.outras_informacoes = campos['outras_informacoes']
				editar_associado.acessibilidade = campos['acessibilidade']

				if request.POST.get('senha') != '':
					editar_associado.senha_hash = campos['senha_hash']

				if editar_associado.email != campos['email']:
					if not Associado.objects.filter(email=campos['email']):
						editar_associado.email = campos['email']
						editar_associado.save()
						return redirect('associatedlist')

					else:
						formulario = request.POST
						erro = 'Já existe associado com esse email cadastrado'
				else:
					editar_associado.email = campos['email']
					editar_associado.save()
					return redirect('associatedlist')

			except:
				formulario = request.POST
				erro = 'Não foi possível atualizar este associado'
		else:
			formulario = request.POST
			erro = 'Alguns campos não foram preenchidos corretamente'
	else:
		try:
			formulario = Associado.objects.get(id=id)
			erro = None

		except:
			return redirect('associatedlist')

	contexto = {
		'form': formulario,
		'erro': erro,
		'editar': editar,
	}

	contexto.update(csrf(request))
	return render(request, 'associated/form.html', contexto)

@login_required(login_url='login')
@csrf_protect
def associateddelete_view(request, id=0):
	if id == 0:
		return redirect('associatedlist')

	if request.method == 'POST':
		try:
			associado = Associado.objects.get(id=id)
			associado.delete()
		finally:
			return redirect('associatedlist')
	else:
		return redirect('associatedlist')

@login_required(login_url='login')
def associatedpdf_view(request, id=0):
	if id == 0:
		return redirect('associatedlist')

	try:
		associado = Associado.objects.get(id=id)
		formulario = {
			'id': id,
			'foto': settings.MEDIA_ROOT + '/' + associado.foto.name,
			'nome': associado.nome,
			'data_nascimento': associado.data_nascimento,
			'cpf': associado.cpf,
			'celular': associado.celular,
			'email': associado.email,
			'cep': associado.cep,
			'numero': associado.numero,
			'pcd': associado.pcd,
			'outras_informacoes': associado.outras_informacoes,
			'instituicao_ensino': associado.instituicao_ensino,
			'curso_extra': associado.curso_extra,
			'empresa_trabalhada': associado.empresa_trabalhada,
			'cargo_ocupado': associado.cargo_ocupado,
		}

		contexto = {
			'form': formulario,
		}

		pdf = render_to_pdf('associated/pdf.html', contexto)

		if pdf:
			resposta = HttpResponse(pdf, content_type='application/pdf')
			nomearquivo = associado.nome.replace(' ', '_').lower() + '.pdf'
			conteudo = 'inline; filename=%s' % (nomearquivo)
			resposta['Content-Disposition'] = conteudo
			return resposta

		else:
			return redirect('associatedlist', id=id)

	except:
		return redirect('associatedlist')
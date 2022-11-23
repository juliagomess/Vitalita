from django import forms
import hashlib

class FormCadastro(forms.Form):
	nome = forms.CharField(label='Nome', max_length=45)
	cpf = forms.CharField(label='CPF', max_length=14)
	data_nascimento = forms.DateField(label='Data de nascimento')
	email = forms.EmailField(label='E-mail', max_length=45)
	senha =	forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput)
	celular = forms.CharField(label='Telefone', max_length=15)
	cep = forms.CharField(label='CEP', max_length=10)
	numero = forms.CharField(label='Número', max_length=5)
	pcd = forms.CharField(label='PCD', max_length=3)
	outras_informacoes = forms.CharField(label='Outras informações', widget=forms.Textarea, required=False, max_length=255)
	acessibilidade = forms.CharField(label='Acessibilidade', max_length=6)
	foto = forms.ImageField(label='Foto')

	def clean_form(self):
		foto = self.cleaned_data.get('foto')
		nome = self.cleaned_data.get('nome')
		data_nascimento = self.cleaned_data.get('data_nascimento')
		cpf = self.cleaned_data.get('cpf')
		email =	self.cleaned_data.get('email')
		senha =	self.cleaned_data.get('senha')
		celular = self.cleaned_data.get('celular')
		cep = self.cleaned_data.get('cep')
		numero = self.cleaned_data.get('numero')
		pcd = self.cleaned_data.get('pcd')
		outras_informacoes = self.cleaned_data.get('outras_informacoes')
		acessibilidade = self.cleaned_data.get('acessibilidade')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()

		if pcd == 'sim':
			pcd = True
		else:
			pcd = False

		return { 
			'foto': foto,
			'nome': nome,
			'data_nascimento': data_nascimento,
			'cpf': cpf, 
			'email': email, 
			'senha_hash': senha_hash, 
			'celular': celular,
			'cep': cep,  
			'numero': numero,
			'pcd': pcd,
			'outras_informacoes': outras_informacoes,
			'acessibilidade': acessibilidade,
		}

class FormEditar(forms.Form):
	nome = forms.CharField(label='Nome', max_length=45)
	cpf = forms.CharField(label='CPF', max_length=14)
	data_nascimento = forms.DateField(label='Data de nascimento')
	email = forms.EmailField(label='E-mail', max_length=45)
	senha =	forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput, required=False)
	celular = forms.CharField(label='Telefone', max_length=15)
	cep = forms.CharField(label='CEP', max_length=10)
	numero = forms.CharField(label='Número', max_length=5)
	pcd = forms.CharField(label='PCD', max_length=3)
	outras_informacoes = forms.CharField(label='Outras informações', widget=forms.Textarea, required=False, max_length=255)
	acessibilidade = forms.CharField(label='Acessibilidade', max_length=6)
	foto = forms.ImageField(label='Foto', required=False)

	def clean_form(self):
		foto = self.cleaned_data.get('foto')
		nome = self.cleaned_data.get('nome')
		data_nascimento = self.cleaned_data.get('data_nascimento')
		cpf = self.cleaned_data.get('cpf')
		email =	self.cleaned_data.get('email')
		senha =	self.cleaned_data.get('senha')
		celular = self.cleaned_data.get('celular')
		cep = self.cleaned_data.get('cep')
		numero = self.cleaned_data.get('numero')
		pcd = self.cleaned_data.get('pcd')
		outras_informacoes = self.cleaned_data.get('outras_informacoes')
		acessibilidade = self.cleaned_data.get('acessibilidade')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()

		if pcd == 'sim':
			pcd = True
		else:
			pcd = False

		return { 
			'foto': foto,
			'nome': nome,
			'data_nascimento': data_nascimento,
			'cpf': cpf, 
			'email': email, 
			'senha_hash': senha_hash, 
			'celular': celular,
			'cep': cep,  
			'numero': numero,
			'pcd': pcd,
			'outras_informacoes': outras_informacoes,
			'acessibilidade': acessibilidade,
		}
from django import forms
import hashlib

class FormCadastro(forms.Form):
	razao_social = forms.CharField(label='Razão Social', max_length=45)
	cnpj = forms.CharField(label='CNPJ', max_length=18)
	nome_contato = forms.CharField(label='Nome do contato', max_length=45)
	email = forms.EmailField(label='E-mail', max_length=45)
	senha =	forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput)
	telefone = forms.CharField(label='Telefone', max_length=14)
	cep = forms.CharField(label='CEP', max_length=10)
	numero = forms.CharField(label='Número', max_length=5)
	acessibilidade = forms.CharField(label='Acessibilidade', max_length=6)
	foto = forms.ImageField(label='Foto')
	logo = forms.ImageField(label='Logo')

	def clean_form(self):
		logo = self.cleaned_data.get('logo')
		foto = self.cleaned_data.get('foto')
		razao_social = self.cleaned_data.get('razao_social')
		nome_contato = self.cleaned_data.get('nome_contato')
		cnpj = self.cleaned_data.get('cnpj')
		email =	self.cleaned_data.get('email')
		senha =	self.cleaned_data.get('senha')
		telefone = self.cleaned_data.get('telefone')
		cep = self.cleaned_data.get('cep')
		numero = self.cleaned_data.get('numero')
		acessibilidade = self.cleaned_data.get('acessibilidade')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()

		return { 
			'logo': logo,
			'foto': foto,
			'razao_social': razao_social, 
			'cnpj': cnpj, 
			'nome_contato': nome_contato, 
			'email': email, 
			'senha_hash': senha_hash, 
			'telefone': telefone,
			'cep': cep,  
			'numero': numero,
			'acessibilidade': acessibilidade,
		}

class FormEditar(forms.Form):
	razao_social	= 	forms.CharField(label='Razão Social', max_length=45)
	cnpj 			=	forms.CharField(label='CNPJ', max_length=18)
	nome_contato	=	forms.CharField(label='Nome do contato', max_length=45)
	email 			=	forms.EmailField(label='E-mail', max_length=45)
	senha 			=	forms.CharField(label='Senha', max_length=20, widget=forms.PasswordInput, required=False)
	telefone 		=	forms.CharField(label='Telefone', max_length=14)
	cep				=	forms.CharField(label='CEP', max_length=10)
	numero			=	forms.CharField(label='Número', max_length=5)
	acessibilidade = forms.CharField(label='Acessibilidade', max_length=6)
	foto 			=	forms.ImageField(label='Foto', required=False)
	logo			=	forms.ImageField(label='Logo', required=False)

	def clean_form(self):
		logo = self.cleaned_data.get('logo')
		foto = self.cleaned_data.get('foto')
		razao_social = self.cleaned_data.get('razao_social')
		nome_contato = self.cleaned_data.get('nome_contato')
		cnpj = self.cleaned_data.get('cnpj')
		email =	self.cleaned_data.get('email')
		senha =	self.cleaned_data.get('senha')
		telefone = self.cleaned_data.get('telefone')
		cep = self.cleaned_data.get('cep')
		numero = self.cleaned_data.get('numero')
		acessibilidade = self.cleaned_data.get('acessibilidade')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()

		return { 
			'logo': logo,
			'foto': foto,
			'razao_social': razao_social, 
			'cnpj': cnpj, 
			'nome_contato': nome_contato, 
			'email': email, 
			'senha_hash': senha_hash, 
			'telefone': telefone,
			'cep': cep,  
			'numero': numero,
			'acessibilidade': acessibilidade,
		}
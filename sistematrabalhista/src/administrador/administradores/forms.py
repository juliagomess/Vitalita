from django import forms
import hashlib

class FormCadastro(forms.Form):
	nome = forms.CharField(label='Nome', max_length=45)
	rf = forms.CharField(label='RF', max_length=8)
	email =	forms.EmailField(label='Email')
	senha =	forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput)
	acessibilidade = forms.CharField(label='Acessibilidade', max_length=6)
	foto = forms.ImageField(label='Foto')

	def clean_form(self):
		foto = self.cleaned_data.get('foto')
		nome = self.cleaned_data.get('nome')
		rf = self.cleaned_data.get('rf')
		email =	self.cleaned_data.get('email')
		senha =	self.cleaned_data.get('senha')
		acessibilidade = self.cleaned_data.get('acessibilidade')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()

		return { 
			'foto': foto,
			'nome': nome,
			'rf': rf, 
			'email': email, 
			'senha_hash': senha_hash,
			'acessibilidade': acessibilidade,
		}

class FormEditar(forms.Form):
	nome = forms.CharField(label='Nome', max_length=45)
	rf = forms.CharField(label='RF', max_length=8)
	email =	forms.EmailField(label='Email')
	senha =	forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput, required=False)
	acessibilidade = forms.CharField(label='Acessibilidade', max_length=6)
	foto = forms.ImageField(label='Foto', required=False)

	def clean_form(self):
		foto = self.cleaned_data.get('foto')
		nome = self.cleaned_data.get('nome')
		rf = self.cleaned_data.get('rf')
		email =	self.cleaned_data.get('email')
		senha =	self.cleaned_data.get('senha')
		acessibilidade = self.cleaned_data.get('acessibilidade')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()

		return { 
			'foto': foto,
			'nome': nome,
			'rf': rf, 
			'email': email, 
			'senha_hash': senha_hash,
			'acessibilidade': acessibilidade,
		}
from django import forms
import hashlib

class FormLogin(forms.Form):
	email = forms.EmailField(label='Email')
	senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput)

	def clean_form(self):
		email = self.cleaned_data.get('email')
		senha = self.cleaned_data.get('senha')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()

		return { 'email': email, 'senha_hash': senha_hash }

class FormTrocar(forms.Form):
	email = forms.EmailField(label='Email')
	senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput)
	confirma = forms.CharField(label='Confirma', max_length=100, widget=forms.PasswordInput)

	def clean_form(self):
		email = self.cleaned_data.get('email')
		senha = self.cleaned_data.get('senha')
		confirma = self.cleaned_data.get('confirma')

		senha_hash = hashlib.sha256(senha.encode()).hexdigest()
		confirma_hash = hashlib.sha256(confirma.encode()).hexdigest()

		return {
			'email': email,
			'senha_hash': senha_hash,
			'confirma_hash': confirma_hash,
		}

class FormRedefinir(forms.Form):
	email = forms.EmailField(label='Email')

	def clean_form(self):
		email = self.cleaned_data.get('email')
		
		return { 'email': email }
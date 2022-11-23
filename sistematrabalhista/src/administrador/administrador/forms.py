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

class FormCurriculo(forms.Form):
	associado_id = forms.IntegerField(label='ID do associado')
	email = forms.EmailField(label='Email do associado')
	instituicao_ensino = forms.CharField(label='Instituições de ensino', max_length=255, required=False)
	curso_extra = forms.CharField(label='Cursos extras', max_length=255, required=False)
	empresa_trabalhada = forms.CharField(label='Empresas', max_length=255, required=False)
	cargo_ocupado = forms.CharField(label='Cargos', max_length=255, required=False)
	laudo_medico = forms.CharField(label='Laudo médico', max_length=100, required=False)
	novo_laudo_medico = forms.FileField(label='Novo laudo médico', required=False)

	def clean_form(self):
		associado_id =	self.cleaned_data.get('associado_id')
		email = self.cleaned_data.get('email')
		instituicao_ensino = self.cleaned_data.get('instituicao_ensino')
		curso_extra = self.cleaned_data.get('curso_extra')
		empresa_trabalhada = self.cleaned_data.get('empresa_trabalhada')
		cargo_ocupado = self.cleaned_data.get('cargo_ocupado')
		laudo_medico = self.cleaned_data.get('laudo_medico')
		novo_laudo_medico = self.cleaned_data.get('novo_laudo_medico')

		return {
			'associado_id': associado_id,
			'email': email,
			'instituicao_ensino': instituicao_ensino,
			'curso_extra': curso_extra,
			'empresa_trabalhada': empresa_trabalhada,
			'cargo_ocupado': cargo_ocupado,
			'laudo_medico': laudo_medico,
			'novo_laudo_medico': novo_laudo_medico,
		}

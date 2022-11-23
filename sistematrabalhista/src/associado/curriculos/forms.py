from django import forms

# Create your form here.
class FormCadastro(forms.Form):
	instituicao_ensino = forms.CharField(label='Instituições de ensino', max_length=255, required=False)
	curso_extra = forms.CharField(label='Cursos extras', max_length=255, required=False)
	empresa_trabalhada = forms.CharField(label='Empresas trabalhadas', max_length=255, required=False)
	cargo_ocupado = forms.CharField(label='Cargos ocupados', max_length=255, required=False)
	laudo_medico = forms.FileField(label='Laudo médico', required=False)

	def clean_form(self):
		instituicao_ensino = self.cleaned_data.get('instituicao_ensino')
		curso_extra  = self.cleaned_data.get('curso_extra')
		empresa_trabalhada = self.cleaned_data.get('empresa_trabalhada')
		cargo_ocupado = self.cleaned_data.get('cargo_ocupado')
		laudo_medico = self.cleaned_data.get('laudo_medico')

		return { 
			'instituicao_ensino': instituicao_ensino, 
			'curso_extra': curso_extra, 
			'empresa_trabalhada': empresa_trabalhada, 
			'cargo_ocupado': cargo_ocupado, 
			'laudo_medico': laudo_medico 
		}

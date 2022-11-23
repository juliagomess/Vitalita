from django.db import models

def uploadfolder(instance, filename):
	return 'curriculo/{0}/{1}'.format(instance.associado_id, filename)

# Create your models here.
class Curriculo(models.Model):
	associado_id = models.IntegerField(verbose_name='ID do associado')
	instituicao_ensino = models.CharField(verbose_name='Instituições de ensino', max_length=255, blank=True, null=False)
	curso_extra = models.CharField(verbose_name='Cursos extras', max_length=255, blank=True, null=False)
	empresa_trabalhada = models.CharField(verbose_name='Empresas trabalhadas', max_length=255, blank=True, null=False)
	cargo_ocupado = models.CharField(verbose_name='Cargos ocupados', max_length=255, blank=True, null=False)
	laudo_medico = models.FileField(verbose_name='Laudo médico', upload_to=uploadfolder, blank=True, null=False)
	created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return self.associado_id

	class Meta:
		db_table = 'curriculo'
		verbose_name = 'Curriculo'
		verbose_name_plural = 'Curriculo'
		ordering = ['associado_id']
from django.db import models

# Create your models here.
class LoginAssociado(models.Model):
	id = models.IntegerField(verbose_name='ID', primary_key=True)
	foto = models.CharField(verbose_name='Foto', max_length=150)
	nome = models.CharField(verbose_name='Razão social', max_length=45)
	email = models.EmailField(verbose_name='E-mail', unique=True, max_length=45)
	senha_hash = models.CharField(verbose_name='Senha', max_length=64)
	pcd = models.BooleanField(verbose_name='PCD', default=False)
	acessibilidade = models.CharField(verbose_name='Acessibilidade', max_length=6, blank=True, null=False)
	
	is_authenticated	=	models.BooleanField(verbose_name='Autenticado', default=False)
	last_login			=	models.DateTimeField(verbose_name='Último login', blank=True, null=True)
	created_at			=	models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	updated_at			=	models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return self.nome

	class Meta:
		db_table = 'login_associado'
		verbose_name = 'Login de Associado'
		verbose_name_plural = 'Login de Associados'
		ordering = ['nome']
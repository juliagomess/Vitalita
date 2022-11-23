from django.db import models
from django.conf import settings
from PIL import Image
import os

# Create your models here.
class Administrador(models.Model):
	foto = models.ImageField(verbose_name='Foto', upload_to='foto/admin', null=False, blank=False)
	nome = models.CharField(verbose_name='Nome', max_length=45)
	rf = models.CharField(verbose_name='RF', max_length=8, unique=True)
	email = models.EmailField(verbose_name='Email', unique=True, max_length=45)
	senha_hash = models.CharField(verbose_name='Hash senha', max_length=64)
	acessibilidade = models.CharField(verbose_name='Acessibilidade', max_length=6, blank=True, null=False)

	is_authenticated = models.BooleanField(verbose_name='Autenticado', default=False)
	last_login = models.DateTimeField(verbose_name='Último login', blank=True, null=True)
	created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return self.nome

	def delete(self, *args, **kwargs):
		self.removePhoto()
		super().delete(*args, **kwargs)

	def removePhoto(self):
		self.foto.delete()

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		self.resizeImage(self.foto.name, 800)

	@staticmethod
	def resizeImage(nome, novalargura):
		caminho = os.path.join(settings.MEDIA_ROOT, nome)
		imagem = Image.open(caminho)

		largura, altura = imagem.size
		novaaltura = round((novalargura * altura) / largura)

		if largura <= novalargura:
			imagem.close()
		
		else:
			novaimagem = imagem.resize((novalargura, novaaltura), Image.ANTIALIAS)
			novaimagem.save(caminho, optimize=True, quality=60)
			novaimagem.close()

	class Meta:
		db_table = 'administrador'
		verbose_name = 'Administrador'
		verbose_name_plural = 'Administradores'
		ordering = ['nome']
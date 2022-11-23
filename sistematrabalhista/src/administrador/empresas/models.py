from django.db import models
from django.conf import settings
from PIL import Image
import os

# Create your models here.
class Empresa(models.Model):
	foto = models.ImageField(verbose_name='Foto', upload_to='foto/empresa', null=False, blank=False)
	logo = models.ImageField(verbose_name='Logo', upload_to='logo/empresa', null=False, blank=False)
	razao_social = models.CharField(verbose_name='Razão social', max_length=45)
	cnpj = models.CharField(verbose_name='CNPJ', max_length=18, unique=True)
	
	nome_contato = models.CharField(verbose_name='Nome do contato', max_length=45)
	telefone = models.CharField(verbose_name='Telefone', max_length=14)

	email =	models.EmailField(verbose_name='E-mail', unique=True, max_length=45)
	senha_hash = models.CharField(verbose_name='Hash senha', max_length=64)
	
	cep = models.CharField(verbose_name='CEP', max_length=10)
	numero = models.CharField(verbose_name='Número', max_length=5)
	acessibilidade = models.CharField(verbose_name='Acessibilidade', max_length=6, blank=True, null=False)
	
	created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	def __str__(self):
		return self.razao_social

	def delete(self, *args, **kwargs):
		self.removePhoto()
		self.removeLogo()
		super().delete(*args, **kwargs)

	def removePhoto(self):
		self.foto.delete()

	def removeLogo(self):
		self.logo.delete()

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		self.resizeImage(self.foto.name, 800)
		self.resizeImage(self.logo.name, 800)

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
		db_table = 'empresa'
		verbose_name = 'Empresa'
		verbose_name_plural = 'Empresas'
		ordering = ['razao_social']
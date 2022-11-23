from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.db import connection
from session.models import LoginAssociado

class BackendLogin(BaseBackend):
	def authenticate(request, email=None, senha=None):
		try:
			with connection.cursor() as cursor:
				cursor.execute("SELECT id, foto, nome, email, senha_hash, pcd, acessibilidade FROM associado WHERE email=%s", [email])
				resultado = cursor.fetchone()

				if resultado != None:
					campos = {
						'id': resultado[0],
						'foto': settings.MEDIA_URL + resultado[1],
						'nome': resultado[2],
						'email': resultado[3],
						'senha_hash': resultado[4],
						'pcd': resultado[5],
						'acessibilidade': resultado[6],
					}

					if senha == campos['senha_hash']:
						if LoginAssociado.objects.filter(id=campos['id']):
							sessao = LoginAssociado.objects.get(id=campos['id'])
							sessao.delete()

						associado = LoginAssociado.objects.create(id=campos['id'], foto=campos['foto'], nome=campos['nome'], 
										email=campos['email'], senha_hash=campos['senha_hash'], pcd=campos['pcd'], acessibilidade=campos['acessibilidade'])
						return associado

					else:
						return False
				else:
					return None
		except:
			return None

	def get_user(self, id):
		try:
			return LoginAssociado.objects.get(id=id)

		except:
			return None
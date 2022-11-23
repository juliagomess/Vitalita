from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.db import connection
from core.models import LoginEmpresa

class BackendLogin(BaseBackend):
	def authenticate(request, email=None, senha=None):
		try:
			with connection.cursor() as cursor:
				cursor.execute("SELECT id, foto, logo, razao_social, email, senha_hash, acessibilidade FROM empresa WHERE email=%s", [email])
				resultado = cursor.fetchone()

				if resultado != None:
					campos = {
						'id': resultado[0],
						'foto': settings.MEDIA_URL + resultado[1],
						'logo': settings.MEDIA_URL + resultado[2],
						'razao_social': resultado[3],
						'email': resultado[4],
						'senha_hash': resultado[5],
						'acessibilidade': resultado[6]
					}

					print(campos)

					if senha == campos['senha_hash']:
						if LoginEmpresa.objects.filter(id=campos['id']):
							sessao = LoginEmpresa.objects.get(id=campos['id'])
							sessao.delete()

						empresa = LoginEmpresa.objects.create(id=campos['id'], foto=campos['foto'], logo=campos['logo'],
									razao_social=campos['razao_social'], senha_hash=campos['senha_hash'], acessibilidade=campos['acessibilidade'])
						return empresa

					else:
						return False
				else:
					return None
		except:
			return None

	def get_user(self, id):
		try:
			return LoginEmpresa.objects.get(id=id)

		except:
			return None
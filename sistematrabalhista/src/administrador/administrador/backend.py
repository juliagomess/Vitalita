from django.contrib.auth.backends import BaseBackend
from administradores.models import Administrador

class BackendLogin(BaseBackend):
	def authenticate(request, email=None, senha=None):
		try:
			administrador = Administrador.objects.get(email=email)

			if administrador.senha_hash == senha:
				return administrador

			else:
				return False
		except:
			return None

	def get_user(self, id):
		try:
			return Administrador.objects.get(id=id)

		except:
			return None
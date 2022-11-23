"""administrador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from administrador.views import UserViewSet,GroupViewSet
from administrador.views import login_view, forgot_view, readmore_view, logout_view
from administrador.views import changepassword_view, joblist_view, jobread_view, jobpdf_view
from administrador.views import resumelist_view, resumeread_view, resumedelete_view
from administradores.views import adminlist_view, admincreate_view, adminedit_view, admindelete_view
from associados.views import associatedlist_view, associatedcreate_view, associatededit_view, associateddelete_view, associatedpdf_view
from cursos.views import courselist_view, coursecreate_view, courseedit_view, coursedelete_view
from empresas.views import companylist_view, companycreate_view, companyedit_view, companydelete_view
from eventos.views import eventlist_view, eventcreate_view, eventedit_view, eventdelete_view
from jogos.views import gamelist_view, gamecreate_view, gameedit_view, gamedelete_view
from videoaulas.views import videolessonlist_view, videolessoncreate_view, videolessonedit_view, videolessondelete_view

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

base = 'extcomp/administrador/'

urlpatterns = [
	path(base + 'superadmin/', admin.site.urls),

	path(base , login_view, name='login'),
	path(base + 'esquecidados/', forgot_view, name='forgot'),
	path(base + 'saibamais/', readmore_view, name='readmore'),
	path(base + 'trocarsenha/', changepassword_view, name='changepassword'),
	path(base + 'sair/', logout_view, name='logout'),

	path(base + 'administradores/', adminlist_view, name='adminlist'),
	path(base + 'administradores/formulario/', admincreate_view, name='admincreate'),
	path(base + 'administradores/formulario/<int:id>/', adminedit_view, name='adminedit'),
	path(base + 'administradores/excluir/<int:id>/', admindelete_view, name='admindelete'),

	path(base + 'associados/', associatedlist_view, name='associatedlist'),
	path(base + 'associados/formulario/', associatedcreate_view, name='associatedcreate'),
	path(base + 'associados/formulario/<int:id>/', associatededit_view, name='associatededit'),
	path(base + 'associados/excluir/<int:id>/', associateddelete_view, name='associateddelete'),
	path(base + 'associados/pdf/<int:id>/', associatedpdf_view, name='associatedpdf'),

	path(base + 'curriculos/', resumelist_view, name='resumelist'),
	path(base + 'curriculos/<int:id>/', resumeread_view, name='resumeread'),
	path(base + 'curriculos/excluir/<int:id>/', resumedelete_view, name='resumedelete'),

	path(base + 'cursos/', courselist_view, name='courselist'),
	path(base + 'cursos/formulario/', coursecreate_view, name='coursecreate'),
	path(base + 'cursos/formulario/<int:id>/', courseedit_view, name='courseedit'),
	path(base + 'cursos/excluir/<int:id>/', coursedelete_view, name='coursedelete'),

	path(base + 'empresas/', companylist_view, name='companylist'),
	path(base + 'empresas/formulario/', companycreate_view, name='companycreate'),
	path(base + 'empresas/formulario/<int:id>/', companyedit_view, name='companyedit'),
	path(base + 'empresas/excluir/<int:id>/', companydelete_view, name='companydelete'),

	path(base + 'eventos/', eventlist_view, name='eventlist'),
	path(base + 'eventos/formulario/', eventcreate_view, name='eventcreate'),
	path(base + 'eventos/formulario/<int:id>/', eventedit_view, name='eventedit'),
	path(base + 'eventos/excluir/<int:id>/', eventdelete_view, name='eventdelete'),

	path(base + 'jogos/', gamelist_view, name='gamelist'),
	path(base + 'jogos/formulario/', gamecreate_view, name='gamecreate'),
	path(base + 'jogos/formulario/<int:id>/', gameedit_view, name='gameedit'),
	path(base + 'jogos/excluir/<int:id>/', gamedelete_view, name='gamedelete'),

	path(base + 'vagas/', joblist_view, name='joblist'),
	path(base + 'vagas/<int:id>/', jobread_view, name='jobread'),
	path(base + 'vagas/pdf/<int:id>/', jobpdf_view, name='jobpdf'),

	path(base + 'videoaulas/', videolessonlist_view, name='videolessonlist'),
	path(base + 'videoaulas/formulario/', videolessoncreate_view, name='videolessoncreate'),
	path(base + 'videoaulas/formulario/<int:id>/', videolessonedit_view, name='videolessonedit'),
	path(base + 'videoaulas/excluir/<int:id>/', videolessondelete_view, name='videolessondelete'),

	re_path(r'^extcomp/administrador/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT }),
	re_path(r'^extcomp/administrador/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT }),

	path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
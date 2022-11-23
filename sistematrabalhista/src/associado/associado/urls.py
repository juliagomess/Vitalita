"""associado URL Configuration

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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from associado.views import login_view, forgot_view, readmore_view, logout_view
from curriculos.views import resumecreate_view, resumelist_view, resumeedit_view, resumepdf_view
from session.views import home_view
from session.views import courselist_view, courseread_view
from session.views import eventlist_view, eventread_view
from session.views import gamelist_view, gameread_view
from session.views import joblist_view, jobread_view
from session.views import videolessonlist_view, videolessonread_view

base = 'extcomp/associado/'

urlpatterns = [
	path(base, login_view, name='login'),
	path(base + 'esquecidados/', forgot_view, name='forgot'),
	path(base + 'saibamais/', readmore_view, name='readmore'),
	path(base + 'sair/', logout_view, name='logout'),

	path(base + 'inicio/', home_view, name='home'),

	path(base + 'curriculos/', resumecreate_view, name='resumecreate'),
	path(base + 'curriculos/', resumelist_view, name='resumelist'),
	path(base + 'curriculos/formulario/', resumecreate_view, name='resumecreate'),
	path(base + 'curriculos/formulario/<int:id>/', resumeedit_view, name='resumeedit'),
	path('curriculos/formulario/pdf/', resumepdf_view, name='resumepdf'),

	path(base + 'cursos/', courselist_view, name='courselist'),
	path(base + 'cursos/<int:id>/', courseread_view, name='courseread'),

	path(base + 'eventos/', eventlist_view, name='eventlist'),
	path(base + 'eventos/<int:id>/', eventread_view, name='eventread'),

	path(base + 'jogos/', gamelist_view, name='gamelist'),
	path(base + 'jogos/<int:id>/', gameread_view, name='gameread'),

	path(base + 'vagas/', joblist_view, name='joblist'),
	path(base + 'vagas/<int:id>/', jobread_view, name='jobread'),

	path(base + 'videoaulas/', videolessonlist_view, name='videolessonlist'),
	path(base + 'videoaulas/<int:id>/', videolessonread_view, name='videolessonread'),

	re_path(r'^extcomp/associado/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT }),
	re_path(r'^extcomp/associado/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT }),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('apresentacao', views.apresentacao_view, name="apresentacao"),
    path('competecias', views.competencias_view, name="competencias"),
    path('formacao', views.formacao_view, name="formacao"),
    path('projetos', views.projetos_view, name="projetos"),
    path('licenciatura', views.licenciatura_view, name="licenciatura"),
    path('blog', views.blog_page_view, name="blog"),
    path('new_post', views.novo_post_view, name="new_post"),
    path('edit_post/<int:post_id>', views.edita_post_view, name="edit_post"),
    path('apaga_post/<int:post_id>', views.apaga_post_view, name="apaga_post"),
    path('quizz', views.quizz, name="quizz"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
]

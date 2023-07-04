from django.urls import path
from .views import home,salvar,editar,update,delete,cadastro,login_view


urlpatterns = [
path('',login_view,name='login'),
path('home/',home,name='home'),
path('cadastro/',cadastro,name='cadastro'),
path('salvar/',salvar,name='salvar'),
path('editar/<int:id>',editar,name='editar'),
path('update/<int:id>',update,name='update'),
path('delete/<int:id>',delete,name='delete'),
]

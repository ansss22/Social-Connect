from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.logout, name='logout'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('profil/', views.profil, name='profil'),
    path('modifier/', views.modifier, name='modifier'),
    path('ajouter/', views.ajouter, name='ajouter'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


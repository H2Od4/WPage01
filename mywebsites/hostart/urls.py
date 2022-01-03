# hier stehen die Links zu den einzelnen seiten "html seiten"

from django.urls import path
from . import views
# mit "app_name" (Application namespaces) werden Namensbereiche definiert
app_name = 'hostart'
# in "urlpatterns" werden die Pfade der Seiten (App's) definiert
# die Idee ist, hier mit "name" eine globale Name zu definieren
# welches überall einfach zu verwenden ist! Der Pfad kann sich ändern
# aber der Name muss nicht überall zum Beispiel angepasst werden
# _
# "urlpatterns enthält eine reihe von Pfade und deren enthalten Sichten
# für die "http://127.0.0.1:8000/" Haupt-URL ist '' (blank) zu setzen
urlpatterns = [
    path('', views.vindex, name='index'),
    path('login/', views.vlogin, name='login'),
    path('logout/', views.vlogout, name='logout'),
    path('register/', views.vregister, name='register'),

]

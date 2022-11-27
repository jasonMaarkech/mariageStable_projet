
from django.urls import path
from infoapp import views
urlpatterns = [
path('',views.index, name='index'),#pour ouvrire la page initiale
path('GenEtab',views.GenEtab, name='GenEtab'),#pour chercher aleatoirement seulement les informations des etbalissement
path('GenEtud',views.GenEtud, name='GenEtud'),#pour chercher aleatoirement seulement les informations des etudiant

]

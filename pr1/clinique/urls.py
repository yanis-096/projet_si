 
# clinique/urls.py

from django.urls import path
from .views import ajouter_patient, liste_rendezvous_par_medecin,ajouter_medecin,prendre_rendezvous,login_or_add_patient,EspacePatientView

urlpatterns = [
    path('liste_rendezvous_par_medecin/', liste_rendezvous_par_medecin, name='liste_rendezvous_par_medecin'),
    # Vous pouvez ajouter d'autres URL pour les autres vues ici
]

# clinique/urls.py

urlpatterns = [
    path('Ajouter_Patient/', ajouter_patient, name='Ajouter_Patient'),
    path('liste_rendezvous_par_medecin/', liste_rendezvous_par_medecin, name='liste_rendezvous_par_medecin'),
    # Ajoutez d'autres URLs au besoin
    path('Ajouter_Medecin/',ajouter_medecin,name='Ajouter_Medecin'),
        path('prendre_rendezvous/', prendre_rendezvous, name='prendre_rendezvous'),
        path('login_or_add_patient/',login_or_add_patient,name='login_or_add_patient'),
        path('espace_patient/', EspacePatientView.as_view(), name='Espace_Patient'),
        

]

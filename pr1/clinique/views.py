# clinique/views.py

from django.shortcuts import render, redirect
from .models import RendezVous, Departement,Medecin
from .forms import PatientForm,MedecinForm,RendezVousForm
from django.contrib.auth import login, authenticate
from .forms import  PatientForm,PatientLoginForm
from django.views.generic import TemplateView
from django.views.generic import TemplateView
from django.views import View

# def liste_rendezvous_cardiologie(request):
#     # Récupérer les rendez-vous spécifiques à la cardiologie
#     rendezvous_cardiologie = RendezVous.objects.filter(medecin__specialite='Cardiologie')

#     # Récupérer les informations spécifiques à la cardiologie
#     departement_cardiologie = Departement.objects.get(nom='Cardiologie')

#     # Passer les données au template
#     context = {
#         'rendezvous_cardiologie': rendezvous_cardiologie,
#         'departement_cardiologie': departement_cardiologie,
#     }

#     return render(request, 'clinique/liste_rendezvous_cardiologie.html', context)


def liste_rendezvous_par_medecin(request):
    # Récupérer tous les médecins
    medecins = Medecin.objects.all()

    # Créer un dictionnaire pour stocker les rendez-vous par médecin
    rendezvous_par_medecin = {}

    # Boucler à travers chaque médecin
    for medecin in medecins:
        # Récupérer les rendez-vous pour ce médecin
        rendezvous = RendezVous.objects.filter(medecin=medecin)

        # Ajouter la paire médecin-rendezvous au dictionnaire
        rendezvous_par_medecin[medecin] = rendezvous

    # Passer les données au template
    context = {
        'rendezvous_par_medecin': rendezvous_par_medecin,
    }

    return render(request, 'clinique/liste_rendezvous_par_medecin.html', context)



# clinique/views.py
def ajouter_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')  # Redirigez vers la liste des patients ou toute autre vue souhaitée
    else:
        form = PatientForm()

    return render(request, 'clinique/Ajouter_Patient.html', {'form': form})

def ajouter_medecin(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')  # Redirigez vers la liste des patients ou toute autre vue souhaitée
    else:
        form = MedecinForm()

    return render(request, 'clinique/Ajouter_Medecin.html', {'form': form})

# clinique/views.py



def prendre_rendezvous(request):
    medecins = Medecin.objects.all()

    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('templates/clinique/Espace_Patient.html')  # Redirigez vers la liste des rendez-vous ou une autre vue souhaitée
    else:
        form = RendezVousForm()

    return render(request, 'clinique/prendre_rendezvous.html', {'form': form, 'medecins': medecins})

class EspacePatientView(TemplateView):
    template_name = 'clinique/Espace_Patient.html'
    def get(self, request, *args, **kwargs):
        # Your logic for handling GET requests
        return render(request, self.template_name, {})
  

def login_or_add_patient(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return render(request,'clinique:Espace_Patient.html')  # Renvoyer la page HTML directement
            else:
                # L'utilisateur n'existe pas ou le mot de passe est incorrect
                # Gérer le cas d'erreur ici
                return render(request, 'clinique/login_or_add_patient.html', {'form': form, 'error_message': 'Email ou mot de passe incorrect'})
    else:
        form = PatientLoginForm()

    return render(request, 'clinique/login_or_add_patient.html', {'form': form})



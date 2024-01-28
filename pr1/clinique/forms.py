 
# clinique/forms.py

from django import forms
from .models import Patient,Medecin,RendezVous
from datetime import datetime, timedelta
from django.contrib.auth.forms import AuthenticationForm



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),  # Utilisez un widget de mot de passe pour masquer le texte
        }

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields ='__all__'
        widgets = {
            'password': forms.PasswordInput(),  # Utilisez un widget de mot de passe pour masquer le texte
        }


class RendezVousForm(forms.ModelForm):

    dates_list = [(datetime.now() + timedelta(days=i)).date() for i in range(1, 8)]
    heures_list = [('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('14:00', '14:00'), ('15:00', '15:00')]

    date_rdz = forms.DateField(widget=forms.SelectDateWidget(years=[d.year for d in dates_list]))
    heure_rdz = forms.ChoiceField(choices=heures_list)

    class Meta:
        model = RendezVous
        fields=['patient']



class PatientLoginForm(AuthenticationForm):
    class Meta:
        model = Patient  # Remplacez YourUserModel par le modèle de votre utilisateur
        fields = ['email', 'password']  # Remplacez par les champs nécessaires



class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email', required=True)

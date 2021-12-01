from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import user, usercontact, newProduct, informe, terrenocrud
from django.contrib.auth.models import User

class contactForm(forms.ModelForm):

    class Meta : 
        model = usercontact
        #fields = ["name", "email", "msn", "obser"]
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'msn': forms.TextInput(attrs={'placeholder': 'Mensaje'}),
            'obser': forms.TextInput(attrs={'placeholder': 'Observacion'}),
        }

class terrenocrudForm(forms.ModelForm):
    
    class Meta : 
        model = informe
        #fields = ["personal", "nomtec", "asunto", "nomempresa", "anteceden", 
        # "observacion", "observacion1"]
        fields = '__all__'
        widgets = {
            'personal': forms.TextInput(attrs={'placeholder': 'Nombre del personal'}),
            'nomtec': forms.TextInput(attrs={'placeholder': 'Nombre del tecnico'}),
            'asunto': forms.TextInput(attrs={'placeholder': 'Asunto'}),
            'nomempresa': forms.TextInput(attrs={'placeholder': 'Empresa'}),
            'anteceden': forms.TextInput(attrs={'placeholder': 'Por que la visita'}),
            'observacion': forms.TextInput(attrs={'placeholder': 'Observacion'}),
            'observacion1': forms.TextInput(attrs={'placeholder': 'Observacion2'}),

        }

class registroInforme(forms.ModelForm):
    class Meta : 
        model = informe
        fields = '__all__'
        


class registroUser(forms.ModelForm):
    class Meta : 
        model = user
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'snom': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'password': forms.TextInput(attrs={'placeholder': 'Contraseña'}),
        }

class addProduct(forms.ModelForm):
    class Meta : 
        model = newProduct
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    class Meta : 
        model = User
        fields = ["username", "first_name", "email", "password1", "password2"]


        
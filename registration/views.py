from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django import forms

class SingupView( CreateView ):
    form_class=UserCreationForm
    template_name='registration/registro.html'


    def get_success_url(self):
        return reverse_lazy('login')+'?register'

    def get_form(self, form_class=None):
        form=super(SingupView, self).get_form()
        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb2',
                                'placeholder':'Nombre de usuario'})
        return form
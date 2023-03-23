from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView
from . import models
from . import forms


class Projectlv(ListView):
      model= models.Project
      template_name= 'project/list.html'
      
class PCV(CreateView):
      model = models.Project
      form_class = forms.PCF
      template_name= 'project/create.html'
      success_url = reverse_lazy('p_l')
      
from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . import models
from . import forms


class Projectlv(ListView):
      model= models.Project
      template_name= 'project/list.html'
      paginate_by = 6

      def get_queryset(self):
            query_set= super().get_queryset()
            where = {}
            q=self.request.GET.get('q',None)
            if q: where['title__icontains'] = q
            return query_set.filter(**where)
class PCV(CreateView):
      model = models.Project
      form_class = forms.PCF
      template_name= 'project/create.html'
      success_url = reverse_lazy('p_l')

      
class PUV(UpdateView):
      model = models.Project
      form_class = forms.PUF
      template_name= 'project/update.html'
      def get_success_url(self):
            return reverse('p_u',args=[self.object.id]) 


class PDV(DeleteView):
      model = models.Project
      template_name= 'project/delete.html'
      success_url= reverse_lazy('p_l')

#Tasks
class TCV(CreateView):
      model = models.Task
      fields = ['project', 'description'] 

      http_method_names= ['post']

      def get_success_url(self): 
             return reverse('p_u',args=[self.object.project.id])

class TUV(UpdateView):
      model = models.Task
      fields = ['is_completed'] 

      http_method_names= ['post']

      def get_success_url(self): 
             return reverse('p_u',args=[self.object.project.id])

class TDV(DeleteView):
      model = models.Task

      def get_success_url(self): 
             return reverse('p_u',args=[self.object.project.id])               
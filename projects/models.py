from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class ProjectsStatus(models.IntegerChoices):
      PENDING=   1, 'Pending',
      COMPLETED= 2, 'Completed',
      POSTPONED= 3, 'Postponed',
      CANCELED=  4, 'Canceled'
    

class Project(models.Model):
      title= models.CharField(max_length=255)
      description= models.TextField()
      created_at= models.DateTimeField(auto_now_add=True)
      ubdated_at= models.DateTimeField(auto_now=True)
      category=models.ForeignKey(Category, on_delete=models.PROTECT)
      user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
      status=models.IntegerField(choices=ProjectsStatus.choices,default=ProjectsStatus.PENDING)
     
      
      def __str__(self):
        return self.title

class Task(models.Model):
      descrirtion= models.TextField()
      is_compleated= models.BooleanField(default=False)
      project= models.ForeignKey(Project,on_delete=models.CASCADE)
      def __str__(self):
          return self.descrirtion


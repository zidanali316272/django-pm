from django.urls import path,include
from . import views

urlpatterns = [

path('',views.Projectlv.as_view(), name='p_l'),
path('p/c',views.PCV.as_view(), name='p_c')
]
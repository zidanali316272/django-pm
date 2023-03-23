from django.urls import path,include
from . import views

urlpatterns = [

path('',views.Projectlv.as_view(), name='p_l'),
path('p/c',views.PCV.as_view(), name='p_c'),
path('p/u/<int:pk>',views.PUV.as_view(), name='p_u'),
path('p/d/<int:pk>',views.PDV.as_view(), name='p_d'),
path('t/c',views.TCV.as_view(), name='t_c'),
path('t/u/<int:pk>',views.TUV.as_view(), name='t_u'),
path('t/d/<int:pk>',views.TDV.as_view(), name='t_d'),

]
from django.urls import path 
from . import views


urlpatterns = [path('', views.portfolio, name='portfolio'),
               path('selectSubjects/<int:reg>', views.selectSubjects, name='selectSubjects'),
              ]



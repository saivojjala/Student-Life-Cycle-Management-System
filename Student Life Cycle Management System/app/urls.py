from django.urls import path 
from . import views


urlpatterns = [path('', views.portfolio, name='portfolio'),
               path('selectSubjects/<int:reg>', views.selectSubjects, name='selectSubjects'),
               path('viewGrades/<int:reg>', views.viewGrades, name='viewGrades'),
               path('viewAttendance/<int:reg>', views.viewAttendance, name='viewAttendance'),
               path('<int:reg>', views.goHome, name='goHome'),
              ]



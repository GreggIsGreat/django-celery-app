from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emailtin/', views.emailtin, name='emailtin'),
    path('prgbar/', views.prgbar, name='prgbar')
    # path('employee_database/', views.employeedata.as_view()),

]
# path('emailtin/', emailtin.as_view(), name="emailtin"),
# path('prgbar/', prgbar.as_view(), name="prgbar"),
# path('', index.as_view(), name="index"),
# # path('employee_database/', views.employeedata.as_view()),
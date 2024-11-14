from django.urls import path
from . import views

urlpatterns=[
    path('emp/',views.EmployeeApi.as_view()),
    path('emp/<int:pk>/',views.EmployeeDetials.as_view())
]
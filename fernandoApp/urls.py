from django.urls import path
from .views import PacienteListCreateAPIView, PacienteDetailAPIView

urlpatterns = [
    path('pacientes/', PacienteListCreateAPIView.as_view(), name='paciente_list_create'),
    
    path('pacientes/<str:run>/', PacienteDetailAPIView.as_view(), name='paciente_detail'),
]
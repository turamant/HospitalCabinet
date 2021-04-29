from django.urls import path
from django.views.generic import TemplateView

from clinic.views import ListDoctor, DetailDoctor, ListPacient, DetailPacient, \
    DetailReception, CreateReceptionPacient, \
    ListReceptionPacient, detail_reception_pacient

urlpatterns = [
    path('',TemplateView.as_view(template_name='clinica/clinic_main.html'), name='clinic_main'),
    path('doctor/', ListDoctor.as_view(), name='list_doctor'),
    path('doctor/<slug:slug>/', DetailDoctor.as_view(), name='detail_doctor'),
    path('pacient/', ListPacient.as_view(), name='list_pacient'),
    path('pacient/<slug:slug>/', DetailPacient.as_view(), name='detail_pacient'),
    path('create/reception/pacient/',CreateReceptionPacient.as_view(), name='create_reception_pacient'),
    path('reception_pacient/',ListReceptionPacient.as_view(), name='list_reception_pacient'),
    #path('reception_pacient/<slug:slug>/', DetailReceptionPacient.as_view(), name='detail_reception_pacient'),
    #path('reception_pacient/',list_reception_pacient, name='list_reception_pacient'),
    path('reception_pacient/<slug:slug>/', detail_reception_pacient, name='detail_reception_pacient'),



]
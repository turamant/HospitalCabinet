from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from clinic.models import Doctor, Pacient, ReceptionPacient


# Doctor ===============
class ListDoctor(ListView):
    model = Doctor
    context_object_name = 'doctors'
    template_name = 'clinica/list_doctor.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_doctors'] = Doctor.objects.all().count()
        return context

class DetailDoctor(DetailView):
    model = Doctor
    template_name = 'clinica/detail_doctor.html'
    slug_field = 'url'


# Pacient ================
class ListPacient(ListView):
    model = Pacient
    context_object_name = 'pacients'
    template_name = 'clinica/list_pacient.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_pacients'] = Pacient.objects.all().count()
        return context

class DetailPacient(DetailView):
    model = Pacient
    template_name = 'clinica/detail_pacient.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['receptions'] = ReceptionPacient.objects.filter(number_card=1)
        context['receptions'] = ReceptionPacient.objects.all()
        return context

# Reception ====================
class CreateReceptionPacient(CreateView):
    model = ReceptionPacient
    template_name = 'clinica/create_reception_pacient.html'
    fields = '__all__'
    success_url = reverse_lazy('create_reception_pacient')

class ListReceptionPacient(ListView):
    model = ReceptionPacient
    template_name = 'clinica/list_reception_pacient.html'
    context_object_name = 'receptions'

def list_reception_pacient(request):
    return render(request, 'clinica/list_reception_pacient.html', {'receptions':ReceptionPacient.objects.all()})

def detail_reception_pacient(request, slug):
    recept = ReceptionPacient.objects.get(url=slug)
    return render(request, 'clinica/detail_reception_pacient.html', {'recept':recept})

class DetailReception(DetailView):
    model = ReceptionPacient
    template_name = 'clinica/detail_reception_pacient.html'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        return context





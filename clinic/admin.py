from django.contrib import admin

# Register your models here.
from clinic.models import Kabinet, Speciality, ServiceList, PhotoDoctor, \
    Doctor, Pacient, ReceptionPacient, DocumentPacient


@admin.register(Kabinet)
class KabinetAdmin(admin.ModelAdmin):
    list_display = ('number',)
    prepopulated_fields = {'url':('number',),}

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('title_speciality',)
    prepopulated_fields = {'url':('title_speciality',),}

@admin.register(ServiceList)
class ServiceListAdmin(admin.ModelAdmin):
    list_display = ('title_service',
                    'code_service',
                    'price_service')
    prepopulated_fields = {'url':('title_service',),}

@admin.register(PhotoDoctor)
class PhotoDoctorAdmin(admin.ModelAdmin):
    list_display = ('title','doctor','image',)
    prepopulated_fields ={'url':('title',),}

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('tab_number','family','name',
                    'date_from_begin',
                    'kabinet_number',
                    'special','mail')
    prepopulated_fields = {'url':('family',),}

@admin.register(DocumentPacient)
class DocumentPacientAdmin(admin.ModelAdmin):
    list_display = ('title','file','image','pacient')
    prepopulated_fields = {'url':('title',),}


@admin.register(Pacient)
class PacientAdmin(admin.ModelAdmin):
    list_display = ('number_card', 'family','photo',
                    'name','birthday','adress',
                    'phone', 'mail')
    prepopulated_fields = {'url':('family',),}

@admin.register(ReceptionPacient)
class ReceptionPacientAdmin(admin.ModelAdmin):
    list_display = ('code_reception',
                    'date_reception',
                    'time_reception',
                    'number_card',
                    'tab_number',
                    'code_service')
    prepopulated_fields = {'url':('code_reception',),}

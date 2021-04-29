from django.db import models

# Create your models here.
from django.urls import reverse


class Kabinet(models.Model):
    number = models.CharField(max_length=3)
    url = models.SlugField(max_length=3)

    def __str__(self):
        return self.number

class Speciality(models.Model):
    title_speciality = models.CharField(max_length=200)
    url = models.SlugField(max_length=200)

    def __str__(self):
        return self.title_speciality

class ServiceList(models.Model):
    title_service = models.CharField(max_length=200)
    url = models.SlugField(max_length=200)
    code_service = models.CharField(max_length=4)
    price_service = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title_service



class PhotoDoctor(models.Model):
    title = models.CharField(max_length=100, null=True, default='kiss')
    image = models.ImageField(upload_to='clinica/doctors/', null=True)
    url = models.SlugField(max_length=100)
    doctor = models.ForeignKey(to="Doctor",
                               on_delete=models.CASCADE,
                               related_name='doctors')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_doctor', kwargs={'slug':self.url})

class Doctor(models.Model):
    tab_number = models.CharField(max_length=4)
    family = models.CharField(max_length=200)
    url = models.SlugField(max_length=200)
    name = models.CharField(max_length=200)
    date_from_begin = models.DateField()
    kabinet_number = models.ForeignKey(to=Kabinet, on_delete=models.CASCADE)
    special = models.ForeignKey(to=Speciality, on_delete=models.CASCADE)
    mail = models.EmailField(unique=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.family

    def get_absolute_url(self):
        return reverse('detail_doctor', kwargs={'slug':self.url})

class DocumentPacient(models.Model):
    title = models.CharField(max_length=200,null=True,default='kiss')
    file = models.FileField(upload_to='clinica/pacients/documents/', null=True)
    image = models.ImageField(upload_to='clinica/pacients/images/', null=True)
    url = models.SlugField(max_length=200)
    pacient = models.ForeignKey(to="Pacient",
                               on_delete=models.CASCADE,
                               related_name='pacients')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_pacient', kwargs={'slug':self.url})

class Pacient(models.Model):
    number_card = models.CharField(max_length=4)
    family = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pacients/photo/', null=True)
    url = models.SlugField(max_length=200)
    name = models.CharField(max_length=200)
    birthday = models.DateField()
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    mail = models.EmailField(unique=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.family

    def get_absolute_url(self):
        return reverse('detail_pacient', kwargs={'slug':self.url})

class ReceptionPacient(models.Model):
    code_reception = models.CharField(max_length=200)
    url = models.SlugField(max_length=200)
    date_reception = models.DateField()
    time_reception = models.TimeField()
    number_card = models.ForeignKey(to=Pacient,
                                on_delete=models.CASCADE,
                                related_name='number_cards')

    tab_number = models.ForeignKey(to=Doctor,
                               on_delete=models.CASCADE,
                               related_name='tab_numbers')

    code_service = models.ForeignKey(to=ServiceList,
                                    on_delete=models.CASCADE,
                                    related_name='code_services')
    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('detail_reception_pacient', kwargs={"slug":self.url})


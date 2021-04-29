from django import forms

from clinic.models import Pacient, Doctor, ServiceList, Reception


class ReceptionPatientForm(forms.ModelForm):
    code_reception = forms.IntegerField(label='Код приёма')
    url = forms.SlugField(label='Url')
    date_reception = forms.DateField(label='Дата приёма')
    time_reception =forms.TimeField(label='Время приёма')
    number_card = forms.ModelChoiceField(
        queryset=Pacient.objects.all(),label='Пациент',
        help_text='Не забудь задать пациента!',
        widget=forms.widgets.Select(attrs={'size':8})
    )
    tab_number = forms.ModelChoiceField(
        queryset=Doctor.objects.all(), label='Доктор',
        widget=forms.widgets.Select(attrs={'size':8})
    )
    code_service = forms.ModelChoiceField(
        queryset= ServiceList.objects.all(), label='Услуги',
        widget=forms.widgets.Select(attrs={'size':10})
    )

    class Meta:
        model = Reception
        fields = ('code_reception', 'url', 'date_reception',
                  'time_reception', 'number_card', 'tab_number',
                  'code_service')

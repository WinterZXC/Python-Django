from django.db import models
from django.forms import ModelForm
from django.forms import modelformset_factory
from django import forms
from django.forms import inlineformset_factory
# Create your models here.
class Companies(models.Model):
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=7)
    date = models.DateField()
    capital = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    personal_code = models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Capital(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    companies_id = models.ForeignKey(Companies, on_delete=models.CASCADE,
                                     related_name="capital_companies", null=True,
                                     blank=True, db_constraint=False)
    capital = models.CharField(max_length=50)
    physical_person = models.BooleanField()
    founder = models.BooleanField()

    def __str__(self):
        return self.capital

class CapitalForm(ModelForm):
    class Meta:

        model = Capital
        fields = ['user_id', 'capital', 'physical_person', 'founder']

        widgets = {
            'capital': forms.TextInput(attrs={
                'onfocus': 'this.oldvalue = this.value;',
                'onchange': 'updateCount(this);this.oldvalue = this.value;',
                'type': 'number'
            }),
            'founder': forms.HiddenInput(attrs={'value': 'False'}),
        }

    def __init__(self, *args, **kwargs):
        super(CapitalForm, self).__init__(*args, **kwargs)

        self.initial['user_id'] = '1'

class CapitalFormCreate(ModelForm):
    class Meta:

        model = Capital
        fields = ['user_id', 'capital', 'physical_person', 'founder']
        widgets = {
            'capital': forms.TextInput(attrs={
                'onfocus': 'this.oldvalue = this.value;',
                'onchange': 'updateCount(this);this.oldvalue = this.value;',
                'type': 'number'
            }),
            'founder': forms.HiddenInput(attrs={'value': 'True'}),
        }

    def __init__(self, *args, **kwargs):
        super(CapitalFormCreate, self).__init__(*args, **kwargs)

        self.initial['user_id'] = '1'
CapitalFormSet = modelformset_factory(
    Capital, form=CapitalForm, extra=1
)
CapitalFormCreateSet = modelformset_factory(
    Capital, form=CapitalFormCreate, extra=1
)
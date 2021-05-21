from django.shortcuts import render

from django.views import generic

from .models import Patient, Gene, ScoreType
# Create your views here.


class PatientsView(generic.ListView):
    template_name = 'gen/patients.html'

    context_object_name = 'patients'

    def get_queryset(self):
        return Patient.objects.order_by( 'last_name', 'first_name')



class GenesView(generic.ListView):
    template_name = 'gen/genes.html'

    def get_queryset(self):
        return Gene.objects.order_by( 'name')

class ScoreTypesView(generic.ListView):
    template_name = 'gen/score_types.html'

    def get_queryset(self):
        return ScoreType.objects.order_by('name')

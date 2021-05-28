from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Patient, Gene, ScoreType, PatientForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GeneNameForm


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


def add_patient(request):

    if request.method == 'POST':

        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            #messages.info(request, 'Patient has been added.')
            return HttpResponseRedirect(reverse('gen:patients'))

    else:
        form = PatientForm()

    return render(request, 'gen/patient.html', {'form': form})       

def edit_patient(request, patient_id):

    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':

        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():

            form.save()

            #messages.info(request, 'Patient has been successfully saved')

            return HttpResponseRedirect(reverse('gen:patients'))  

        else:
            pass
            #messages.error(request, 'Patient has not been saved.')             

    else:
        form = PatientForm(instance=patient)

    return render(request, 'gen/patient.html', {'form': form, 'patient': patient, 'gene_name_form': GeneNameForm()})  



def delete_patient(request, patient_id):

    patient = get_object_or_404(Patient, pk=patient_id)
    patient.delete()
    return HttpResponseRedirect(reverse('gen:patients'))

def add_gene(request, patient_id):

    patient = get_object_or_404(Patient, pk=patient_id)

    if request.method == 'POST':
        form = GeneNameForm(request.POST)

        if form.is_valid():
            gene_name = form.cleaned_data['gene_name']

            gene = Gene.objects.get(name = gene_name)
            patient.damaged_genes.add(gene)
            patient.save()


    return  HttpResponseRedirect(reverse('gen:edit_patient', args=(patient.id,))) 

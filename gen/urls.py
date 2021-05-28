
from django.urls import path

from . import views

app_name = 'gen'

urlpatterns = [
    path('patients', views.PatientsView.as_view(), name='patients'),
    path('patients/add', views.add_patient, name='add_patient'),
    path('patients/<int:patient_id>/add_gene', views.add_gene, name='add_gene'),
    path('patients/<int:patient_id>', views.edit_patient, name='edit_patient'),
    path('patients/delete/<int:patient_id>', views.delete_patient, name='delete_patient'),
    path('genes', views.GenesView.as_view(), name='genes'),
    path('score_types', views.ScoreTypesView.as_view(), name='score_types'),
]
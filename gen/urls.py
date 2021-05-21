
from django.urls import path

from . import views

app_name = 'gen'
urlpatterns = [
    path('patients', views.PatientsView.as_view(), name='patients'),
    path('genes', views.GenesView.as_view(), name='genes'),
    path('score_types', views.ScoreTypesView.as_view(), name='score_types'),
]

from django import forms

class GeneNameForm(forms.Form):
    gene_name = forms.CharField(label='Gene', max_length=100)
from django.contrib import admin

from .models import Patient, Gene, Score, ScoreType

admin.site.register(Patient)
admin.site.register(Gene)
admin.site.register(ScoreType)
admin.site.register(Score)

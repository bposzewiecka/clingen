from django.db import models


class ScoreType(models.Model):
    name = models.CharField(max_length=200, unique = True)
    source_publication =  models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Gene(models.Model): 
    name =  models.CharField(max_length=200, unique = True)
    chromosome = models.CharField(max_length=20)
    start_coordinate = models.IntegerField()
    end_coordinate = models.IntegerField()
    score_types = models.ManyToManyField(ScoreType, through='Score')

    def __str__(self):
        return self.name + ' ' + self.chromosome + ':' + str(self.start_coordinate) + '-' + str(self.end_coordinate)

class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)
    date_of_birth = models.DateTimeField()
    phenotype = models.CharField(max_length=4000)
    damaged_genes = models.ManyToManyField(Gene)

    def __str__(self):
        return self.first_name + self.last_name

class Score(models.Model):
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    score_type = models.ForeignKey(ScoreType, on_delete=models.CASCADE)
    value = models.FloatField()

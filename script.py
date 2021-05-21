from django.db import transaction

@transaction.atomic
def read_genes():

    from gen.models import Gene

    with open('genes.txt') as f:

        f.readline()

        prev_names = set()

        for line in f:
            line = line.split()
            chromosome, start_coordinate, end_coordinate, name = line[0], int(line[1]), int(line[2]), line[3].upper()


            if name not in prev_names:
                gene = Gene(name = name, chromosome = chromosome, start_coordinate = start_coordinate ,
                    end_coordinate = end_coordinate)
                gene.save()

                prev_names.add(name)

read_genes()

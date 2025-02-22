import csv
from . import db
from .models import Movie


def carregar_csv(arquvio):
    with open(arquvio, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            winner = row['winner'].lower() == 'yes'
            movie = Movie(
                year=int(row['year']),
                title=row['title'],
                studios=row['studios'],
                producers=row['producers'],
                winner=winner
            )
            db.session.add(movie)
        db.session.commit()

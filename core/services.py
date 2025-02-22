from .models import Movie
from collections import defaultdict

def agrupar_produtoras(filmes_ganhadores):
    produtoras_agrupadas = defaultdict(list)
    for filme in filmes_ganhadores:
        produtoras = [p.strip() for p in filme.producers.split(',')]
        for produtora in produtoras:
            if produtora:
                produtoras_agrupadas[produtora].append(filme.year)
    return produtoras_agrupadas

def calcular_intervalos():

    filmes_ganhadores = Movie.query.filter_by(winner=True).all()

    produtoras_agrupadas = agrupar_produtoras(filmes_ganhadores)

    intervalo_maior = []
    intervalo_menor = []
    intervalo_maximo = -1
    intervalo_minimo = float('inf')

    for produtora, anos in produtoras_agrupadas.items():
        if len(anos) < 2:
            continue
        anos.sort()
        for i in range(1, len(anos)):
            intervalo = anos[i] - anos[i - 1]
            premio = {
                'producer': produtora,
                'interval': intervalo,
                'previousWin': anos[i - 1],
                'followingWin': anos[i]
            }
            if intervalo > intervalo_maximo:
                intervalo_maior = [premio]
                intervalo_maximo = intervalo

            elif intervalo == intervalo_maximo:
                intervalo_maior.append(premio)

            if intervalo < intervalo_minimo:
                intervalo_menor = [premio]
                intervalo_minimo = intervalo

            elif intervalo == intervalo_minimo:
                intervalo_menor.append(premio)

    return {'max': intervalo_maior, 'min': intervalo_menor}
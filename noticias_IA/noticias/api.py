import requests
def obtener_noticias_ia():
    url = 'https://newsapi.org/v2/everything'
    parametros = {
        'q': 'inteligencia artificial',
        'apiKey': '6a0af18e61864407afa45e5829aab672',
        'language': 'es',
        'pageSize': 10,
        'sortBy': 'publishedAt'
    }
    
    respuesta = requests.get(url, params=parametros)
    
    if respuesta.status_code == 200:
        return respuesta.json()['articles']
    else:
        return None
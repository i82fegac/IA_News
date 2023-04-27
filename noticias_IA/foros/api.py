import requests

def obtener_preguntas_ia():
    base_url = 'https://api.stackexchange.com/2.3/search/advanced'
    parametros = '?order=desc&sort=votes&q=inteligencia%20artificial&site=stackoverflow&pagesize=10'
    url = base_url + parametros
    
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        return respuesta.json()['items']
    else:
        return None

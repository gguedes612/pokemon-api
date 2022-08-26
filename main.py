from requests import get


def pegar_pokemon(pokemon):
    api = 'https://pokeapi.co/api/v2/pokemon/'
    return type(get(api+pokemon).json())
  
def pegar_tipo(pokemon):
    tipos = []
    for item in pokemon['types']:
        tipos.append(item['type']['name'])
    return tipos
    


print(pegar_pokemon('gengar'))


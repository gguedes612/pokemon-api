from requests import get

class Pokemon:
    
    def __init__(self,nome):
        api_pokemon = get(f'https://pokeapi.co/api/v2/pokemon/{nome}/').json()
        api_species = get(f'https://pokeapi.co/api/v2/pokemon-species/{nome}/').json()
        
        self.nome = api_pokemon['name']
        self.types =  api_pokemon['types']
        self.description = api_species["flavor_text_entries"][9]["flavor_text"]
        self.sprite = api_pokemon["sprites"]["front_default"]
    
    def get_nome(self):
        return self.nome
    
    def get_types(self):
        type = []
        
        for types in self.types:
            type.append(types['type']['name'])
        return type
    
    def get_description(self):
        return self.description
    
    def get_sprite(self):
        return self.sprite
        
teste = Pokemon('gengar')
print(teste.get_nome())
print(teste.get_types())
print(teste.get_description())
print(teste.get_sprite())

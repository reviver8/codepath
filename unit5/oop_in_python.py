class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution
    
    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    
    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if self.is_caught == True:
            print(f"{self.name} I choose you!")
        else:
            print("{} is wild! Catch them if you can!".format(self.name))

    def add_type(self, new_type):
        self.types.append(new_type)

#problem 7, get pokemon with the same type
def get_by_type(my_pokemon_set, pokemon_type):
    sol_lst = []
    for pokemon in my_pokemon_set:
        #iterates throughout one pokemon's type list
        for type in pokemon.types:
            if type == pokemon_type:
                sol_lst.append(pokemon.name)
    return sol_lst

def get_by_type2(my_pokemon_set, pokemon_type):
    sol_lst = []
    for pokemon in my_pokemon_set:
        #checks if the input type is in the pokemon's type list
        if pokemon_type in pokemon.types:
            sol_lst.append(pokemon.name)
    return sol_lst

#problem 8
#get the evolutionary line for 1 particular pokemon
def get_evolutionary_line(starter_pokemon):
    '''goal: return a list of pokemon
    that the starter_pokemon can evolve into'''
    evolution_lst = []
    curr_pokemon = starter_pokemon
    evolution_lst.append(curr_pokemon.name)

    while curr_pokemon.evolution != None:
        evolution_lst.append(curr_pokemon.evolution.name)   
        curr_pokemon = curr_pokemon.evolution
    return evolution_lst





pikachu = Pokemon("Pikachu", ["Electric"])
squirtle = Pokemon("Squirtle", ["Water"])
# squirtle.catch()
# squirtle.print_pokemon()
# squirtle.choose()

rattata = Pokemon("Rattata", ["Normal"])
# rattata.choose()

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.choose()

jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()


diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type2(my_pokemon, "Normal")
print(normal_pokemon)

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)
charmander_list = get_evolutionary_line(charmander)
#print(charmander_list)
charmeleon_list = get_evolutionary_line(charmeleon)
#print(charmeleon_list)
charizard_list = get_evolutionary_line(charizard)
#print(charizard_list)




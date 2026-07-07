class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
        
    def add_item(self, item_name):
        valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid:
            self.furniture.append(item_name)
                
def of_personality_type(townies, personality_type):
    result = []
    for town in townies:
        if town.personality == personality_type:
            result.append(town.name)
    return result 


def message_received(start_villager, target_villager):
    curr_villager = start_villager
    while True:
        if curr_villager.neighbor is None:
            return False
        if curr_villager.neighbor == target_villager:
            return True
        curr_villager = curr_villager.neighbor


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider

print(message_received(isabelle, kk_slider))
print(message_received(kk_slider, isabelle))


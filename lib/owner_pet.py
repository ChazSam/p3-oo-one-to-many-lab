import ipdb
class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in self.PET_TYPES:
            raise Exception
        else:
            Pet.all.append((self))
            

class Owner(Pet):
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        newList=[]
        for pet in Pet.all:
            if pet.owner==self:
                newList.append(pet)

        return newList
    
    def add_pet(self, pet):        
        pet.owner = self  

    # def sort_pets_by_name(self):
    #     #ipdb.set_trace()
    #     pass
    
    def get_sorted_pets(self):
        y = self.pets()
        y.sort(key=lambda x: x.name)
        return y

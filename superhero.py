class Superheroes:
    def __init__(self, name, power, tools, damage_points):
        self.name = name
        self.power = power
        self.tools = tools
        self.damage_points = damage_points
        self.health_points = 100


    def __repr__(self):
        return f"Superhero: {self.name}"

    def is_alive(self):
        return self.health_points >= 0
        
    def damage(self, enemy):
        enemy.health_points = enemy.health_points - self.damage_points    
        print(f"{self.name} attacks {enemy.name}! \n{enemy.name} health={enemy.health_points}")
    


Dr_strange = Superheroes("Dr.Strange", "Astral projection","Magic cape", 15)
Scarlet_Witch = Superheroes("Scarlett Witch", "Telekinesis", "Headpiece", 18)

# Dr_strange.attacks(Scarlet_Witch)
# print(Scarlet_Witch.is_alive())


while Dr_strange.is_alive() and Scarlet_Witch.is_alive():
    Dr_strange.damage(Scarlet_Witch)
    Scarlet_Witch.damage(Dr_strange)

def winner():
    return 
print("")








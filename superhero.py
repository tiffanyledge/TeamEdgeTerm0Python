class Superheroes:
    def __init__(self, name, power, tools, damage):
        self.name = name
        self.power = power
        self.tools = tools
        self.attack_damage = damage
        self.health_point = 100


    def __repr__(self):
        return f"Superhero: {self.name}"
   
    def is_alive(self):
        return self.health_points > 0
           
    def attack(self, enemy):
        enemy.health_points = enemy.health_points - self.damage    
        print(f"{self.name} attacks {enemy.name}!/n {enemy.name} health={enemy.health_points}")
    


Dr_strange = Superheroes("Dr.Strange", "Astral projection","Magic cape", 15)
Scarlet_Witch = Superheroes("Scarlett Witch", "Telekinesis", "Headpiece", 18)

while Dr_strange.is.alive() and Scarlet_Witch.is.alive():
    Dr_strange.attacks(Scarlet_Witch)
    Scarlet_Witch.attacks(Dr_strange)







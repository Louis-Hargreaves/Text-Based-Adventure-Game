import random
class Captain():
    treasure = 0
    xp = 0
    weapons = []
    def __init__(self, name):
        self.name = name
    def add_treasure(self, integer):
        self.treasure += integer
    def add_xp(self, integer):
        self.xp += integer
    def add_cannon(self, integer):
        self.cannons += integer
    def add_weapon(self, string):
        self.weapons.insert(0, string) #Newest weapon at start of list



class Ship():
    privateer_count = 2
    buccaneer_count = 0
    batallion_count = 0
    def __init__(self, name):
        self.name = name

    def add_privateer(self, integer):
        self.privateer_count += integer
    def add_buccaneer(self, integer):
        self.buccaneer_count += integer
    def add_batallion(self, integer):
        self.batallion_count += integer
    def damage_function(self, damage):
        death = False
        batallions_required = int(damage / 15)
        if self.batallion_count < batallions_required:
            damage = damage - (self.batallion_count * 15)
            self.batallion_count = 0
        else:
            damage = damage - (batallions_required * 15)
            self.batallion_count -= batallions_required
        buccaneers_required = int(damage / 5)
        if self.buccaneer_count < buccaneers_required:
            damage = damage - (self.buccaneer_count * 5)
            self.buccaneer_count = 0
        else:
            damage = damage - (buccaneers_required * 5)
            self.buccaneer_count -= buccaneers_required
        privateers_required = int(damage)
        if self.privateer_count >= privateers_required:
            self.privateer_count -= privateers_required
        else:
            death = True
            buccaneers_required = int(damage / 5) + 1
            if self.buccaneer_count >= buccaneers_required:
                self.buccaneer_count -= buccaneers_required
                death = False
            else:
                damage = damage - (self.buccaneer_count * 5)
                self.buccaneer_count = 0

                batallions_required = int(damage / 15) + 1
                if self.batallion_count >= batallions_required:
                    self.batallion_count -= batallions_required
                    death = False
                else:
                    self.batallion_count = 0
        return death




class Pirate_Bay():
    def __init__(self, captain_xp):
        self.privateer_price = 5000    #1 point
        self.buccaneer_price = 15000    #5 points
        self.batallion_price = 30000    #20 points
        self.weapon_prices = [["sword", 100000], ["musket", 400000]]


class Island():
    def __init__(self, captain_xp):
        self.treasure_map = [False, False, False, False, False, False, False, False, False]
        self.treasure = random.randint(0, 8)
        self.treasure_map[self.treasure] = True
        self.treasure = random.randint(1, 1 + (captain_xp * 100))
        self.captain_xp = captain_xp

        self.crab = 1 #Holds 50 xp
        if captain_xp >= 400:
            self.gibbon = random.randint(1, 4)  #Holds 75xp
        if captain_xp >= 2000:
            if self.captain_xp <= 12000:
                native_integer = 1000 - ((captain_xp - 2000) / 10)
            else:
                native_integer = 0.001
            self.native = random.randint(1, captain_xp / native_integer) #Holds 100xp

    def search(self):
        y = int(input('''
  Treasure Map
-----------------
1       2       3

4       5       6

7       8       9
-----------------
Type the number you believe the treasure is located in: '''))
        if self.treasure_map[y - 1] == True:
            print("Lucky you, you've found {} treasure.".format(self.treasure))
            return self.treasure
        else:
            print("Unlucky. You didn't find the treasure.")
            chance_of_crab = random.randint(1, 9)
            if chance_of_crab > 7:
                crab = True
            else:
                crab = False
            if self.captain_xp >= 400:
                chance_of_gibbon = random.randint(1, 9)
                if chance_of_gibbon > 7:
                    gibbon = True
                else:
                    gibbon = False
            else:
                gibbon = False
            if self.captain_xp >= 2000:
                chance_of_native = random.randint(1, 9)
                if chance_of_native > 5:
                    native = True
                else:
                    native = False
            else:
                native = False
            encounters = (crab, gibbon, native)
            return encounters
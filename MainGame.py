from Classes import *
import Help
import random

def Play():
    captain = Captain("Louis")
    del captain.weapons[:]
    ship = Ship("HMS HARGREAVES")
    playing = True
    location = "Pirate Bay"
    #Start off at Pirate Bay
    while playing == True:
        choice = input('''
Hi {0},
you are currently at {1} and {2} is docked not too far from us. What would you like to do: '''.format(captain.name, location, ship.name))
        #Changing location
        if choice.lower() == "search":
            island = Island(captain.xp)
            location = "a new remote island"
        elif location != "Pirate Bay" and choice.lower() == "home":
            location = "Pirate Bay"

        #Checking Inventory and help
        elif choice.lower() == 'help':
            print(Help.commands())
        elif choice.lower() == "balance":
            print("Your current balance is: {0}".format(captain.treasure))
        elif choice.lower() == "xp":
            print("Your current experience is: {0}".format(captain.xp))
        elif choice.lower() == "crew":
            print('''
This is your crew
Privateers: {0}
Baccaneers: {1}
Batallions: {2}'''.format(ship.privateer_count, ship.buccaneer_count, ship.batallion_count))
        elif choice.lower() == "weapons":
            if len(captain.weapons) > 0:
                print("In your inventory is:")
                for x in captain.weapons:
                    print(x)
            else:
                print("You don't have any weapons at the moment.")

        #Digging for treasure
        elif choice.lower() == "dig" and location != "a new remote island":
            print("You can't dig here.")
        elif choice.lower() == "dig" and location == "a new remote island":
            while choice.lower() == "dig":
                search_results = island.search()
                if type(search_results) == tuple:

                    #Works out the damage taken off of the ships' crew

                    if search_results[0] == True:
                        print("\n" + "You encountered a crab. It gave {} points of damage".format(island.crab))
                        death = ship.damage_function(island.crab)
                        if death == True:
                            print("You died.")
                            playing = False
                            break
                        else:
                            captain.add_xp(50)
                            print('''
Your ship now looks like:
Privateers: {0}
Buccaneers: {1}
Batallions: {2}'''.format(ship.privateer_count, ship.buccaneer_count, ship.batallion_count))


                    if search_results[1] == True and captain.xp >= 400:
                        print("\n" + "You encountered a gibbon. It gave {} points of damage".format(island.gibbon))
                        death = ship.damage_function(island.gibbon)
                        if death == True:
                            print("You died.")
                            playing = False
                            break
                        else:
                            captain.add_xp(75)
                            print('''
Your ship now looks like:
Privateers: {0}
Buccaneers: {1}
Batallions: {2}'''.format(ship.privateer_count, ship.buccaneer_count, ship.batallion_count))


                    if search_results[2] == True and captain.xp >= 2000:
                        print("\n" + "You encountered a native. It gave you {} points of damage.".format(island.native))
                        death = ship.damage_function(island.native)
                        if death == True:
                            print("You died.")
                            playing = False
                            break
                        else:
                            captain.add_xp(100)
                            print('''
Your ship now looks like:
Privateers: {0}
Buccaneers: {1}
Batallions: {2}'''.format(ship.privateer_count, ship.buccaneer_count, ship.batallion_count))

                    #Allows the captain to have another chance to find the treasure on the same island

                    dig_again = input("Type 'dig' to have another go: ")
                    if dig_again == "dig":
                        continue
                    else:
                        break
                else:
                    captain.add_treasure(search_results)
                    captain.add_xp(250)
                    location = "Pirate Bay"
                    choice = False
                    break

        #Pirate Bay activities
        elif location == "Pirate Bay":
            pirate_bay = Pirate_Bay(captain.xp)
            if choice.lower() == "home":
                print("You are already at Pirate Bay.")
            elif choice.lower() == "shop":
                choice = input("Welcome to the shop, type 'help' for commands or purchase an item: ")
                if choice.lower() == 'help':
                    print(Help.commands())


                #This section tackles the purchasing of items in the shop
            
                elif choice.lower() == "purchase sword":
                    if "sword" in captain.weapons:
                        print("You have already bought the sword")
                    elif captain.treasure >= 100000:
                        captain.add_treasure(-100000)
                        captain.add_weapon("sword")
                        print("You bought the sword.")
                    else:
                        print("You can't afford the sword. It costs 100000.")

                elif choice.lower() == "purchase musket":
                    if "musket" in captain.weapons:
                        print("You have already bought the musket.")
                    elif captain.treasure >= 400000:
                        captain.add_treasure(-400000)
                        captain.add_weapon("musket")
                        print("You bought the musket")
                    else:
                        print("You can't afford the musket. It costs 400000")

                elif choice.lower() == "purchase privateer" or choice.lower() == "purchase buccaneer" or choice.lower() == "purchase batallion":
                    item = choice.split(" ")[1]
                    cost = 0
                    while cost <= captain.treasure:
                        if item == "privateer":
                            item_price = pirate_bay.privateer_price
                            if cost > 0:
                                captain.add_treasure(-cost)
                                ship.add_privateer(stock_amount)
                                break
                        if item == "buccaneer":
                            item_price = pirate_bay.buccaneer_price
                            if cost > 0:
                                captain.add_treasure(-cost)
                                ship.add_buccaneer(stock_amount)
                                break
                        if item == "batallion":
                            item_price = pirate_bay.batallion_price
                            if cost > 0:
                                captain.add_treasure(-cost)
                                ship.add_batallion(stock_amount)
                                break

                        stock_amount = int(input("The cost of an individual {0} is {1} treasure. How many would you like to purchase: ".format(item, item_price)))
                        cost = stock_amount * item_price
                        if cost > captain.treasure:
                            print("You can't afford it.")
                else:
                    print("We don't recognise that command.")

            elif choice.lower() == 'fight':
                enemy_ship_crew = random.randint(25, 100)
                if enemy_ship_crew <= ship.privateer_count + (ship.buccaneer_count * 5) + (ship.batallion_count * 15):
                    if len(captain.weapons) == 2:
                        best_weapon = "musket"
                    if len(captain.weapons) == 1:
                        best_weapon = captain.weapons[0]
                    elif len(captain.weapons) == 0:
                        print("You died.")
                        playing = False
                    print(best_weapon)
                    print(enemy_ship_crew)
                    if best_weapon == "sword":
                        chance_of_winning = "half"
                        x = random.randint(1,2)
                        if x == 1:
                            print("You managed to kill the enemy captain.")
                            playing = False
                        else:
                            ship.damage_function(enemy_ship_crew)
                            print("You failed to beat the enemy captain and lost members of your crew.")
                    elif best_weapon == "musket":
                        chance_of_winning = "full"
                        print("Congratulations, you've won the game")
                        playing = False
                    else:
                        ship.damage_function(enemy_ship_crew)
                        print("You failed to beat the enemy captain and lost members of your crew.")
                        playing = False
                else:
                    print("You died")
                    playing = False

x = True
while x == True:
    Play()
    y = input("Type 'play' to play again: ")
    if y == 'play':
        continue
    else:
        break


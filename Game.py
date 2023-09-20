import random
from datetime import datetime
from typing import Dict, Callable

"""Alex Cersosimo ,
CIS 163 ,
2/15/23
"""

"""Imports all of the needed information for the functions."""
# from npc import *
# from item import *
# from location import *


"""Sets the names and messaging operations for the NPC's in-game."""


class NPCs:
    def __init__(self, name: str, description: str):
        self.name = name
        self._description = description
        self._messages = []
        self._message_number = 0

    def get_name(self):
        return self.name

    def get_description(self):
        return self._description

    """Increases the message number when getting and displaying the messages. """

    def get_message(self):
        if self._message_number < len(self._messages):
            message = self._messages[self._message_number]
            self._message_number = self._message_number + 1
            return message
        else:
            self._message_number = 0

    """Allows NPC's to talk """
    def add_message(self, message):
        self._messages.append(message)

    def __str__(self):
        return f"{self.name} - {self._description}"


"""Creates the item class for the game. Each item has a description, assigned weight, and amount of calories. 
Also creates the return str function."""


class Item:
    def __init__(self, name: str, description: str, calories: int, weight: int):
        if not name:
            raise ValueError("Name cannot be blank")
        self.name = name
        self.description = description
        if not isinstance(calories, int) or calories < 0 or calories > 1000:
            raise ValueError("calories must be between 0 and 1000.")
        self._calories = calories
        if not isinstance(weight, int) or weight < 0 or weight > 500:
            raise ValueError("Cannot carry more than 500")
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self._calories} calories) ({self.weight}):  {self.description}"


"""Contains the information for all the locations in the game . Getters and setters for the NPC's and items locations 
are set where items are on the player or on the map."""

class Location:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._items = []
        self.neighbors = {}
        self.visited = False
        self.NPCs = []

    """These call the parameters for if a location was visited on the map."""

    def set_visited(self) -> None:
        self.visited = True

    def get_visited(self) -> bool:
        return self.visited

    """Has two Raise Errors when either the player enters a direction already in dictionary or a blank one. """

    def add_location(self, direction, location):
        if not direction:
            raise ValueError("Direction cannot be empty")
        if direction in self.neighbors:
            raise KeyError("Direction already in dictionary")
        self.neighbors[direction] = location

    """Code to set, get, and add items or NPC's in the game"""

    def add_npc(self, npc: NPCs):
        self.NPCs.append(npc)

    def get_npc(self) -> list[NPCs]:
        return self.NPCs

    def get_items(self) -> list[Item]:
        return self._items

    def add_item(self, item: Item):
        self._items.append(item)

    def remove_item(self, item: Item):
        self._items.remove(item)

    """Getters/Setters for adding neighbors to the list + directions for locaitons"""

    def get_neighbors(self):
        return self.neighbors

    def add_neighbor(self, direction: str, neighbor):
        self.neighbors[direction] = neighbor

    def remove_neighbor(self, direction):
        if direction in self.neighbors:
            del self.neighbors[direction]

    def __str__(self) -> str:
        return f"{self._name} - {self._description}"


"""Builds out the logic and functions of the game. Allowing them to be called and connected."""


class Game:
    def __init__(self):
        print("Game Constructor")
        self.in_progress = True
        self.commands = self.setup_commands()
        self.current_weight = 0
        self.game_items = []
        self.game_locations = []
        self.create_world()
        self.current_location = self.random_location()
        self.elf_needed_calories = 500
        self.visited = []

    """Sets up the words users can implement to operate the game. """

    def setup_commands(self) -> Dict[str, Callable]:
        commands = {
            "go": self.go,
            "talk": self.talk,
            "look": self.look,
            "help": self.show_help,
            "give": self.give,
            "take": self.take,
            "meet": self.meet,
            "quit": self.quit,
            "show_items": self.show_items
        }
        return commands

    def random_location(self) -> Location:
        return random.choice(self.game_locations)

    """Shows list of commands in case user gets stuck."""

    """Holds all of the objects, characters, and locations within the game."""

    def create_world(self) -> None:

        """All the objects a user can pick up. Along with their description, calories , and weight"""

        item1 = Item("Apple", "A juicy and delicious fruit", 95, 150)
        item2 = Item("Sword", "A sharp and sturdy sword", 0, 250)
        item3 = Item("Sandwich", "A delicious ham and cheese sandwich", 250, 150)
        item4 = Item("Chair", "A comfortable and sturdy wooden chair", 0, 100)
        item5 = Item("Chocolate", "A sweet and decadent treat", 50, 50)
        item6 = Item("Laptop", "A sleek and powerful computer", 0, 120)
        item7 = Item("Banana", "A sweet and nutritious fruit", 50, 100)
        item8 = Item("Backpack", "A spacious and durable backpack", 0, 100)
        item9 = Item("Steak", "A juicy and flavorful cut of meat", 200, 300)
        item10 = Item("Lamp", "A stylish and functional lamp", 0, 300)
        item11 = Item("Magic Brownie", "A delicious and succulent brownie...priceless", 900, 0)

        """Non-playable characters to interact with. Unfortunately, unfinished."""

        green_dragon = NPCs("green Dragon", "A giant, fire-breathing dragon guards mounds of gold.")
        tired_knight = NPCs("tired Knight", "A battle-worn knight resting on a lounge chair")
        elf = NPCs("elf", "Ye high elf of Asguard")
        old_wizard = NPCs("old_wizard", "A wise-old wizard lost deep in meditation.")
        goblin = NPCs("goblin", "a green evil goblin hunching over a science textbook.")

        green_dragon.add_message("Halt, who goes there?")
        green_dragon.add_message("Ah, a curious warrior...")
        green_dragon.add_message("I shall warn you against traveling into the dangerous woods.")

        tired_knight.add_message("Please, stop ... I promise I give up.")
        tired_knight.add_message("Oh... it's just you... a CS student... Be careful with that Elf.")
        tired_knight.add_message("Maybe after you unfreeze this place, we can go slay that dragon next.")

        old_wizard.add_message("YOU SHALL NOT PASS!")
        old_wizard.add_message("Oh, it is just you.")
        old_wizard.add_message("""I would recommend the magic brownie. Magic scrolls tell of its mighty power to fulfill
                               hunger in the lands between.""")

        elf.add_message("Im hungry, bring me food and Ill reward you.")
        elf.add_message("I told you... I NEED FOOD")
        elf.add_message("That's it, silent treatment until I see some food")

        goblin.add_message("Hey man, do you have the answer to number 14 on page 60?")
        goblin.add_message("What? you've never seen a bio-major goblin before?")
        goblin.add_message("Would you believe me if I told you my first major was communications")

        """These are all of the locations the player can visit, along with their description."""

        kirkhoff_downstairs = Location('kirkhoff_downstairs', "Areas for eating, along with kitchens and rooms")
        kirkhoff_downstairs.add_item(item4)
        kirkhoff_downstairs.add_item(item1)
        kirkhoff_downstairs.add_npc(green_dragon)

        mary_idema = Location('mary_idema', "Large opening with lounge area")
        mary_idema.add_item(item6)
        mary_idema.add_npc(tired_knight)

        library = Location('library', "Big building with basement that leads to kirkhoff")
        library.add_item(item3)
        library.add_item(item8)
        library.add_npc(old_wizard)

        laker_village = Location('laker_village', "Village apartments with no one around.")
        laker_village.add_item(item10)

        commons = Location('commons', "Living area near Mackinaw")
        commons.add_item(item5)
        commons.add_item(item9)
        commons.add_npc(goblin)

        woods = Location('woods', "woods in the back of campus with a blue bridge")
        woods.add_item(item8)
        woods.add_npc(elf)

        alumni_house = Location('alumni_house', "Office near the north of campus")
        alumni_house.add_item(item2)

        padnos_hall = Location('padnos_hall', "Science hall letting in a bunch of light")
        padnos_hall.add_item(item7)
        padnos_hall.add_item(item11)

        parking_lot = Location("parking_lot", """ITS A TRAP! Unfortunately you fell for one of the elf's spells and are"
                                              "doomed to wandering the parking lot for eternity...restart from"
                                              "the beginning... if you dare.""")

        """Connects all locations with directions. Allows players to travel through locations."""

        padnos_hall.add_location("north", alumni_house)
        padnos_hall.add_location("east", commons)
        padnos_hall.add_location("south", kirkhoff_downstairs)

        kirkhoff_downstairs.add_location("north", commons)
        kirkhoff_downstairs.add_location("east", mary_idema)
        kirkhoff_downstairs.add_location("south", laker_village)
        kirkhoff_downstairs.add_location("west", parking_lot)

        library.add_location("north", alumni_house)
        library.add_location("east", kirkhoff_downstairs)
        library.add_location("south", laker_village)
        library.add_location("west", parking_lot)

        mary_idema.add_location("north", alumni_house)
        mary_idema.add_location("east", woods)
        mary_idema.add_location("south", laker_village)

        woods.add_location("north", alumni_house)
        woods.add_location("south", laker_village)
        woods.add_location("west", commons)

        laker_village.add_location("north", kirkhoff_downstairs)
        laker_village.add_location("east", woods)
        laker_village.add_location("west", parking_lot)

        commons.add_location("north", alumni_house)
        commons.add_location("east", woods)
        commons.add_location("south", laker_village)
        commons.add_location("west", kirkhoff_downstairs)

        alumni_house.add_location("east", woods)
        alumni_house.add_location("south", commons)

        """Appends all of the locations to randomize a location."""

        self.game_locations.append(mary_idema)
        self.game_locations.append(padnos_hall)
        self.game_locations.append(kirkhoff_downstairs)
        self.game_locations.append(library)
        self.game_locations.append(laker_village)
        self.game_locations.append(commons)
        self.game_locations.append(alumni_house)
        self.game_locations.append(woods)
        self.game_locations.append(parking_lot)

        """Adds the location for randomization."""

    """Allows the game to run and is SUPPOSED to check if the game is done when elf.needed_calories is = 500"""

    def play(self) -> None:
        print("""Welcome to Elf Adventure! In this game you have to navigate GVSU's campus, in order to
              satisfy an evil High Elf from Asguard. But be careful, there are traps laying around every corner.""")
        self.list_commands()

        while self.in_progress:
            user_response = input("\nEnter a command please: ")
            tokens = user_response.split()
            command = tokens[0]
            del tokens[0]
            target = ' '.join(tokens)
            if command in self.commands:
                function = self.commands[command]
                function(target)
            else:
                print(f"Invalid command '{command}'. Try these commands.")
                self.list_commands()

        """This sets up the calories needed to be turned into the elf and beat the game."""

        if self.elf_needed_calories > 0 or self.elf_needed_calories < 500:
            print("Go back to the beginning")
        else:
            print("Congrats! You've given me my calories!", "The campus is saved!")

    """Prints the list of commands available to the player."""

    def list_commands(self) -> None:
        print("Appropriate commands: ")
        for command in self.commands:
            print(f"\t-{command}")

    """Shows the help menu, so what commands are accessible to the player."""

    def show_help(self, target =''):
        print(f"\nCurrent time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("Here are the available commands:")
        for command in self.commands:
            print(f"- {command}")

    """Allows the player to interact with the NPC's around them if there are any. If not it will print "No one is here"."""

    def talk(self, target) -> None:
        npcs = self.current_location.get_npc()
        npc_found = False
        for npc in npcs:
            if npc.name == target:
                npc_found = True
                message = npc.get_message()
                print(f"{npc.get_name}: {message}")
        if not npc_found:
            print(f"There is no {target} here to talk to.")

    """When typed, the description should be called if there is an NPC at the location."""

    def meet(self, target) -> None:
        npcs = self.current_location.get_npc()
        npc_found = False
        for npc in npcs:
            if npc.get_name() == target:
                npc_found = True
                print(f"{npc.get_name()}: {npc.get_description()}")
        if not npc_found:
            print(f"There is no {target} here to talk to.")

    """This function checks if there are any items or NPC's are in the area 
    and displays the direction a player can go"""

    def look(self, target) -> None:
        print(self.current_location)
        items = self.current_location.get_items()
        if items:
            for item in items:
                print(item)
        else:
            print("There is nothing here")
        npcs = self.current_location.get_npc()
        if npcs:
            for npc in npcs:
                print(npc)
        else:
            print("There is no one here")
        neighbors = self.current_location.get_neighbors()
        if neighbors:
            for direction, location in neighbors.items():
                if location.get_visited():
                    print(direction, str(location))
                else:
                    print(direction)
        else:
            print("No where to go.")

    """Allows the player to pick up items. There are limits for how much weight they can carry as well as a description
    of what the player picks up."""

    def take(self, target: str) -> None:
        location = self.current_location
        items = location.get_items()
        item_found = False
        for item in items:

            if target == item.name:
                self.current_location.get_items().remove(item)
                self.game_items.append(item)
                self.current_weight += item.weight
                item_found = True
        if not item_found:
            print("item not there")

    """This command lets the player give/drop an item. If they enter a wrong input 
    it will print "you do not have that item".It also checks if the item is in the woods, 
    which is essentially giving the elf the calories. Once given enough calories the game will (should) end. 
    If not, then the game will teleport the player to a random place."""

    def give(self, target) -> None:
        item_found = False
        for item in self.game_items:
            if item.name == target:
                item_found = True
                self.game_items.remove(item)
                self.game_locations.append(item)
                self.game_items =- self.current_weight
            else:
                if item.name == target:
                    print("You do not have that item")
        if self.game_locations.append(target):
            self.game_items -= self.current_weight
        print(f"You gave {target} to {self.current_location.get_npc()}.")

        if self.game_locations == "Woods" and hasattr(item, "calories"):
            self.elf_needed_calories -= item.calories
            if self.elf_needed_calories <= 0:
                print("You've collected enough calories and won the game!")
        else:
            print(f"You have {self.elf_needed_calories} calories left to collect.")

        if self.game_locations == "Woods" and not hasattr(Item, "calories"):
            self.current_location = self.random_location()

    """Allows the player to move if the weight they are carrying is less than 300. Also checks if the direction the player typed
    was usable."""

    def go(self, target):
        self.visited = True
        if self.current_weight > 300:
            print("You are carrying too much weight to move!")
            return
        if target in self.current_location.neighbors:
            self.current_location = self.current_location.neighbors[target]
            print(f"You have moved to {self.current_location._name}.")
        else:
            print("You can't go in that direction from here.")

    """Displays the current items in the players inventory + the total weight of the items.
    Unfortunately, it gives me an error that says "'Game' object has no attribute 'show_items' even though it does?"""

    def show_items(self, args: str = None) -> None:
        print(f"You are carrying {len(self.game_items)} items:")
        for item in self.game_items:
            print(f"- {item.name}")
        else:
            print(self.current_weight)

    """Quit operation that allows the user to quit the game given the command."""

    def quit(self, args: str = None) -> None:
        confirm = input("Are you sure you want to quit? Type 'y' to confirm or any other key to continue: ")
        if confirm.lower() == 'y':
            print("You have quit the game. Better luck next time!")
            exit()
        else:
            print("Returning to game...")

    """Prints location name."""
    def get_location_by_name(self, name):
        for location in self.game_locations:
            if location.get_name() == name:
                return location
        return None


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()




from npc import NPCs
from item import Item
import random

"""Contains the information for all the locations in the game and all of the information the subclasses would need to make the operations.
Getters and setters for the NPC's and items locations set where items are on the player or on the map."""

class Location:
    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description
        self._items = []
        self.neighbors = {}
        self.visited = False
        self.direction

    """These set the parameters for if a location was visited on the map."""

    def set_visited(self) -> None:
        self.visited = True

    def get_visited(self) -> bool:
        return self.visited

    """Has two Raise Errors when either the player enters a direction already in dictionary or a blank one. """

    def add_location(self, direction, location):
        self.location[direction] = location
        return self

    # #if not self.direction:
    #     raise ValueError("Direction cannot be empty")
    #     if direction in self.neighbors:
    #         raise KeyError("Direction already in dictionary")
    # self.neighbors[direction] = location

    """Code to set, get, and add items or NPC's in the game"""
    def add_npc(self, npc: NPCs):
        self._NPC.append(npc)

    def get_npc(self) -> list[NPCs]:
        return self.NPC

    def get_items(self) -> list[Item]:
        return self.items

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
        return f"{self.name} - {self.description}"


"""Creates the item class for the game. Each item has a description, assigned weight, and amount of calories. Also creates
the return str function."""

class Item:
    def __init__(self, name: str, description: str, calories: int, weight: int):
        if not name:
            raise ValueError("Name cannot be blank")
        self.name = name
        self.description = description
        if not isinstance(calories,int) or calories < 0 or calories > 1000:
            raise ValueError("calories must be between 0 and 1000.")
        self._calories = calories
        if not isinstance(weight,int) or weight < 0 or weight > 500:
            raise ValueError("Cannot carry more than 500")
        self.weight = weight



    def __str__(self):
        return f"{self.name} ({self._calories} calories) ({self.weight}):  {self.description}"


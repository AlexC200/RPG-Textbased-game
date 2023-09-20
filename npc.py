
"""Sets up the NPC Class and parameters for all the NPC's in the game. Each NPC has 3 messages, or perhaps an item.
Can be given items as well"""

class NPCs:
    def __init__(self, name: str, description: str, _messages: str, _message_number = int):
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
            message = self._messages [self._message_number]
            self._message_number = self._message_number + 1
            return message
        else:
            return None

    def add_message(self,message):
        self._messages.append(message)

    def __str__(self):
        return f"{self.name} - {self._description}"

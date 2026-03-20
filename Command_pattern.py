class Command:
    def execute(self):
        raise NotImplementedError
    def undo(self):
        raise NotImplementedError

class MoveCommand(Command):
    def __init__(self, character, dx, dy):
        self.character = character
        self.dx = dx
        self.dy = dy

    def execute(self):
        self.character.x += self.dx
        self.character.y += self.dy

    def undo(self):
        self.character.x -= self.dx
        self.character.y -= self.dy

class CommandInvoker:
    def __init__(self):
        self._history = []

    def execute(self, command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if self._history:
            last_command = self._history.pop()
            last_command.undo()

# --- Demo ---
class Player:
    def __init__(self, name):
        self.name = name
        self.x, self.y = 0, 0
    def __repr__(self):
        return f"<{self.name} at ({self.x},{self.y})>"

if __name__ == "__main__":
    player = Player("Hero")
    invoker = CommandInvoker()

    invoker.execute(MoveCommand(player, 3, 0))
    invoker.execute(MoveCommand(player, 0, 2))
    print(f"Current: {player}")  # Hero at (3,2)

    invoker.undo()
    print(f"After undo: {player}")  # Hero at (3,0)
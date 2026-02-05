# memory.py

class ConversationMemory:
    def __init__(self):
        self.history = []
        self.turns = 0

    def add(self, role, message):
        self.history.append({"role": role, "message": message})
        self.turns += 1

    def get_history_text(self):
        return "\n".join(
            [f"{h['role']}: {h['message']}" for h in self.history]
        )

class ContextManager:
    def __init__(self):
        self.last_intent = None

    def set_last_intent(self, intent):
        self.last_intent = intent

    def get_last_intent(self):
        return self.last_intent

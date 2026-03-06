import context_manager
import intents
import utils


class Chatbot:
    def __init__(self):
        self.context = context_manager.ContextManager()
        self.intents = intents.INTENTS

    def process_input(self, text):
        text = utils.clean_text(text)

        for intent, data in self.intents.items():
            keywords = data.get("keywords", [])

            for keyword in keywords:
                if keyword in text:
                    self.context.set_last_intent(intent)
                    return intent

        return "unknown"

    def get_response(self, intent):
        if intent == "unknown":
            last = self.context.get_last_intent()
            if last:
                return f"You were asking about {last}. Please be more specific."
            return "Sorry, I did not understand that."

        return self.intents[intent]["response"]

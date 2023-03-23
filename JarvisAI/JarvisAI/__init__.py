import os
import json
import logging
import requests

try:
    from utils import input_output
    from brain import intent_classification
    from brain import ner
    from features_manager import action_map
    from brain.auth import verify_user
except:
    from JarvisAI.utils import input_output
    from JarvisAI.brain import intent_classification
    from JarvisAI.brain import ner
    from JarvisAI.features_manager import action_map
    from JarvisAI.brain.auth import verify_user


def action_handler(intent, query):
    if intent in action_map:
        logging.info(f"Intent {intent} matched. Calling action {action_map[intent]}")
        entities = ner.perform_ner(query=query)
        return action_map[intent](query=query, intent=intent, entities=entities, input_output_fun=input_output)
    else:
        logging.info(f"Intent {intent} not found in action map.")
        return "Sorry, I don't know how to handle this intent."


# function to add new actions to the actions_map dictionary
def add_action(intent: str, action: object):
    """Add a new action to the action map.
    @param intent: (String) The intent to be mapped to the action.
    @param action: (Object) The function to call when the intent is matched.
    @return: (String) The message to be displayed to the user.
    """
    try:
        action_map[intent] = action

        if not os.path.exists('actions.json'):
            url = "https://raw.githubusercontent.com/Dipeshpal/Jarvis_AI/master/JarvisAI/JarvisAI/actions.json"
            data = requests.get(url).json()
            with open('actions.json', 'w') as f:
                json.dump(data, f)

        with open("actions.json", "r") as f:
            actions = json.load(f)

        # Check for duplicates
        duplicates = [i for i, act in enumerate(actions) if act["intent"] == intent]
        if len(duplicates) > 1:
            for i in duplicates[1:]:
                actions.pop(i)
            logging.warning(f"Duplicate actions found for intent {intent}. Only the first action will be used.")
            print(f"Found {len(duplicates)} duplicates for intent '{intent}'. Deleted all but the first.")

        # Check if the action already exists
        action_exists = False
        for i, act in enumerate(actions):
            if act["intent"] == intent:
                action_exists = True
                action_index = i
                break

        if action_exists:
            print(f"Previous examples for intent '{intent}': {actions[action_index]['example']}")
            overwrite = input(f"Intent '{intent}' already exists. Do you want to overwrite? (y/n)")
            if overwrite.lower() == "y":
                num_examples = int(input("How many examples do you want to add? (maximum 3): "))
                examples = []
                for i in range(num_examples):
                    examples.append(input(f"Enter example {i + 1} for intent {intent}: "))
                actions[action_index] = {
                    "intent": intent,
                    "example": examples
                }
            else:
                return "Intent not overwritten."
        else:
            num_examples = int(input("How many examples do you want to add? (maximum 10): "))
            examples = []
            for i in range(num_examples):
                examples.append(input(f"Enter example {i + 1} for intent {intent}: "))
            actions.append({
                "intent": intent,
                "example": examples
            })

        # Write the updated actions back to the file
        with open("actions.json", "w") as f:
            json.dump(actions, f, indent=4)

        logging.info(f"Action for intent {intent} has been added/updated. Train new model to use this action.")
        print(f"Action for intent {intent} has been added/updated. Train new model to use this action.")
        return f"Action for intent {intent} has been added/updated. Train new model to use this action."
    except Exception as e:
        logging.error(f"Error adding action: {e}")
        raise f"Error adding action: {e}"


class JarvisAI(input_output.JarvisInputOutput):
    def __init__(self, input_mechanism='text', output_mechanism='text',
                 google_speech_api_key=None, backend_tts_api='pyttsx3',
                 use_whisper_asr=False, display_logs=False,
                 api_key=None):
        super().__init__(input_mechanism=input_mechanism, output_mechanism=output_mechanism,
                         google_speech_api_key=google_speech_api_key, backend_tts_api=backend_tts_api,
                         use_whisper_asr=use_whisper_asr, duration_listening=5, display_logs=display_logs,
                         api_key=api_key)

        if os.path.exists('jarvis.log'):
            os.remove('jarvis.log')

        self.display_logs = display_logs
        if not self.display_logs:
            logging.basicConfig(filename='jarvis.log', level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.DEBUG)

        if not os.path.exists('actions.json'):
            url = "https://raw.githubusercontent.com/Dipeshpal/Jarvis_AI/master/JarvisAI/JarvisAI/actions.json"
            data = requests.get(url).json()
            with open('actions.json', 'w') as f:
                json.dump(data, f)


    def handle_input(self):
        try:
            if self.input_mechanism == 'text':
                return self.text_input()
            elif self.input_mechanism == 'voice':
                return self.voice_input()
            else:
                available_input_mechanisms = ['text', 'voice']
                logging.error(f"Invalid input mechanism: {self.input_mechanism}. Available input mechanisms are: "
                              f"{available_input_mechanisms}")
                raise Exception("Invalid input mechanism. Available input mechanisms are: {available_input_mechanisms}")
        except Exception as e:
            logging.exception(f"An error occurred while handling input. Error: {e}")
            return f"An error occurred while handling input. Error: {e}"

    def handle_output(self, text):
        try:
            if self.output_mechanism == 'text':
                self.text_output(text)
            elif self.output_mechanism == 'voice':
                self.voice_output(text=text)
            elif self.output_mechanism == 'both':
                self.text_output(text)
                self.voice_output(text=text)
            else:
                available_output_mechanisms = ['text', 'voice', 'both']
                logging.error(f"Invalid output mechanism: {self.output_mechanism}. Available output mechanisms are: "
                              f"{available_output_mechanisms}")
                raise f"Invalid output mechanism: {self.output_mechanism}. Available output mechanisms are: " \
                      f"{available_output_mechanisms}"
        except Exception as e:
            logging.exception(f"An error occurred while handling output. Error: {e}")
            self.handle_output(f"An error occurred while handling output. Error: {e}")

    def take_action(self, intent, query):
        try:
            if not os.path.exists('actions.json'):
                # TODO: Add a default actions.json file
                logging.error("actions.json file not found.")
                return "actions.json file not found."

            # load the JSON file containing the list of available actions and their respective commands
            with open('actions.json', 'r') as f:
                actions = json.load(f)

            # check if the intent matches any of the available actions
            for action in actions:
                if action['intent'] == intent:
                    # if the intent matches, do the action
                    try:
                        return action_handler(intent, query)
                    except Exception as e:
                        logging.exception(f"An error occurred while performing action. Error: {e}")
                        self.handle_output(f"An error occurred while performing action. Error: {e}")

            print(f"Intent {intent} not found in actions.json.")
            # if no action is matched, return a default message
            return "Sorry, I don't know how to handle this intent."
        except Exception as e:
            logging.exception(f"An error occurred while taking action. Error: {e}")
            return f"An error occurred while taking action. Error: {e}"

    # don't change this function, do not try to remove verify_user otherwise Jarvis will not work
    @verify_user
    def start(self):
        while True:
            try:
                query = self.handle_input()
                if query == "" or query is None:
                    continue
                if query == 'exit':
                    self.handle_output("Exiting...")
                    break
                else:
                    # NOTE: The query is passed to the intent classification function to get the intent
                    intent, _ = intent_classification.classify_intent(secret_key=self.api_key, text=query)
                    print(f"Intent: {intent}")
                    intent = intent.replace("_", " ")
                    # PATCH BELOW for date and time if-else
                    if 'time' in intent:
                        print(f"Intent: date / {intent}")
                    else:
                        print(f"Intent: {intent}")
                    logging.debug(f"Input: {query}, Intent: {intent}")
                    response = self.take_action(intent, query)
                    self.handle_output(response)
            except Exception as e:
                logging.exception(f"An error occurred while running Jarvis. Error: {e}")
                self.handle_output(f"An error occurred while running Jarvis. Error: {e}")
                raise f"An error occurred while running Jarvis. Error: {e}"


if __name__ == "__main__":
    def custom_function(*args, **kwargs):
        command = kwargs.get('query')
        entities = kwargs.get('entities')
        print(entities)
        # write your code here to do something with the command
        # perform some tasks # return is optional
        return command + ' Executed'


    jarvis = JarvisAI(input_mechanism='text', output_mechanism='text',
                      google_speech_api_key=None, backend_tts_api='pyttsx3',
                      use_whisper_asr=False, display_logs=False,
                      api_key='527557f2-0b67-4500-8ca0-03766ade589a')
    # add_action("general", custom_function)
    jarvis.start()

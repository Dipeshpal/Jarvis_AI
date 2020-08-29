import json
import re
import importlib


class Action:
    """
    Class to take action according to user input
    """
    def take_action(self, inp):
        with open("configs/jarvis_features_config.json", "r") as json_file:
            json_dict_features_data = json.load(json_file)

        for i in json_dict_features_data:
            regex_exp = i["regex"]
            import_statement = i["import"]
            function_name = i["function_name"]

            if re.search(regex_exp, inp):
                mymodule = importlib.import_module(import_statement)
                response = getattr(mymodule, function_name)(inp)
                return response
            else:
                return "Sorry I couldn't understand, try again"


if __name__ == '__main__':
    obj = Action()
    obj.take_action("pass")

import re
import importlib


class Action:
    """
    Class to take action according to user input
    """
    def __init__(self, jarvis_features_config, user_config):
        self.jarvis_features_config = jarvis_features_config
        self.user_config = user_config

    def take_action(self, inp, user_config):
        inp = inp.lower()
        for i in self.jarvis_features_config:
            regex_exp = i["regex"]
            import_statement = i["import"]
            function_name = i["function_name"]

            if re.search(regex_exp, inp):
                mymodule = importlib.import_module(import_statement)
                response = getattr(mymodule, function_name)(inp)
                return response


if __name__ == '__main__':
    obj = Action()
    obj.take_action("pass")

import re
import importlib


class Action:
    def __init__(self):
        pass

    def take_action(self, data, models):
        features_config = data['features_config']
        for i in features_config:
            regex_exp = i["regex"]
            import_statement = i["import"]
            function_name = i["function_name"]

            if re.search(regex_exp, data['user_input']):
                if data['DEV_MODE']:
                    mymodule = importlib.import_module(import_statement)
                else:
                    mymodule = importlib.import_module('JarvisAI.' + import_statement)
                response = getattr(mymodule, function_name)(data, models)
                return response

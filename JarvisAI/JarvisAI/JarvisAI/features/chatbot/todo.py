import os
import json


def read_notes_if_exist():
    my_db_path = 'my_db/'
    if not os.path.exists(my_db_path):
        os.mkdir(my_db_path)
    if os.path.exists(f'{my_db_path}notes.json'):
        with open(f'{my_db_path}notes.json', 'r') as notes_json:
            previous_data = json.load(notes_json)
    else:
        previous_data = {}
    return previous_data


def create(list_name, items):
    my_db_path = 'my_db/'
    previous_data = read_notes_if_exist()
    list_check = previous_data.get(list_name, None)
    if list_check is None:
        previous_data[list_name] = items
    else:
        previous_data[list_name] = list(set((list_check + items)))
    with open(f'{my_db_path}notes.json', 'w') as notes_json:
        json.dump(previous_data, notes_json)
    return True


def delete_todo(input_text, question_answering_model):
    input_text = input_text.lower()
    list_name = question_answering_model(question="what is the type of list?", context=input_text)
    list_name = [list_name['answer']]
    list_name = list_name[0].replace(" ", "").replace("list", "")
    previous_data = read_notes_if_exist()
    check_list = previous_data.get(list_name, None)
    if check_list is None:
        return True, f"{list_name} list does not exist"
    else:
        previous_data.pop(list_name)
    my_db_path = 'my_db/'
    with open(f'{my_db_path}notes.json', 'w') as notes_json:
        json.dump(previous_data, notes_json)
    return True, f"{list_name} Deleted"


def make_todo(input_text, question_answering_model):
    """
    parameter:
        input_text (str): user_input_text
        question_answering_model (object): qna transformers model's object
    return:
        list_name (str)
        items (list)
    """
    input_text = input_text.lower()
    list_name = question_answering_model(question="what is the type of list?", context=input_text)
    list_name = [list_name['answer']]
    list_name = list_name[0].replace(" ", "").replace("list", "")

    items = question_answering_model(question="what is the item in my list?", context=input_text)
    items = [items['answer']]
    items = items[0].replace("add", "").split(" ")
    status = create(list_name, items)
    return status

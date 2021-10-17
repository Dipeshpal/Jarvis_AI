
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
    list_name = list_name[0].replace(" ","").replace("list", "")

    items = question_answering_model(question="what is the item in my list?", context=input_text)
    items = [items['answer']]
    print("...................", items, "\n", type(items))
    items = items[0].replace("add", "").split(" ")
    return list_name, items

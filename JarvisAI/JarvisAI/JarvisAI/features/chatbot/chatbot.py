import sys
from transformers import pipeline, Conversation
import wikipedia
import re
from string import punctuation
from googlesearch import search
import warnings

warnings.filterwarnings('ignore')

try:
    import en_core_web_sm
    nlp = en_core_web_sm.load()
except Exception as e:
    print(e, "Downloading...")
    import os
    os.system('python -m spacy download en')
    import en_core_web_sm
    nlp = en_core_web_sm.load()


def get_keyword(text):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN']  # 1
    doc = nlp(text.lower())  # 2
    for token in doc:
        if (token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if (token.pos_ in pos_tag):
            result.append(token.text)
    return result


class SearchAnything:
    def __init__(self, high_accuracy=False):
        if high_accuracy:
            self.question_answering = pipeline("question-answering")
        else:
            self.question_answering = pipeline("question-answering", model="mrm8488/bert-small-finetuned-squadv2")


    # def get_answer_from_context(self, question, context):
    #     result = self.question_answering(question=question, context=context)
    #     return [result['answer']]


    def get_context_from_question(self, question):
        output = get_keyword(question)
        output = ' '.join(output)

        try:
            try:
                context = wikipedia.summary(output)
            except Exception as e:
                ny = wikipedia.page(output)
                res = str(ny.content[:500].encode('utf-8'))
                context = re.sub('[^a-zA-Z.\d\s]', '', res)[1:]

            result = self.question_answering(question=question, context=context)
            return [result['answer']]

        except Exception as e:
            context = []
            search_results = search(output)
            for result in search_results:
                context.append(result)

            context = [x for x in context if x.startswith("https")]
            return context


class IntentRecognition(SearchAnything):
    def __init__(self, high_accuracy=False):
        super().__init__(high_accuracy)
        if high_accuracy:
            self.classifier = pipeline("zero-shot-classification", model="joeddav/bart-large-mnli-yahoo-answers")
        else:
            self.classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")

    def intent_recognition(self, question):
        intent = self.classifier(
            question,
            candidate_labels=["conversation", "greetings", "out of scope", "explore"],
        )
        return intent['labels'][0]


class ChatBot:
    def __init__(self, high_accuracy=False):
        self.conversational_pipeline = pipeline("conversational")
        # if high_accuracy:
        #     self.conversational_pipeline = pipeline("conversational", model="microsoft/DialoGPT-large")
        # else:
        #     self.conversational_pipeline = pipeline("conversational", model="microsoft/DialoGPT-small")
        self.conv1 = None
        self.conv2 = None
        self.count = 0
        self.last = None

    def chat(self, text):
        if self.count == 0:
            self.conv1 = Conversation("Hi")
            self.conv2 = Conversation(text)
            self.count += 1
        else:
            self.conv1.add_user_input(self.last)
            self.conv2.add_user_input(text)
            self.count += 1
        self.last = text
        ans = self.conversational_pipeline([self.conv1, self.conv2])
        ans = ans[-1]
        ans = str(ans).split("bot")[-1].replace("bot >>", "").strip().replace(">>", "")
        return ans


def load_chatbot_models(high_accuracy=False, chatbot_large=False):
    if chatbot_large:
        intent_obj = IntentRecognition(high_accuracy)
        conv_obj = ChatBot(high_accuracy)
    else:
        intent_obj = None
        conv_obj = ChatBot(high_accuracy)
    return {"intent_model": intent_obj, "conversational_model": conv_obj}


def start_chatbot_large(input_text, model_dict=None):
    """
    If chat bot can't answer then it will do wikipedia/google search
    """
    if model_dict['intent_model'] is None:
        print("You can't use chatbot_large if chatbot_large is set to False")
        print("Set 'JarvisAI.JarvisAssistant(chatbot_large=True)' then use chatbot_large")
        print("Exiting now, try again...")
        print(sys.exit())
    question = input_text
    question = re.sub("[^A-Za-z]", " ", question)
    question = question.strip()
    intent = model_dict['intent_model'].intent_recognition(question)
    if intent in ["out of scope", "explore"]:
        ans = model_dict['intent_model'].get_context_from_question(question)
        # print(ans)
    else:
        ans = model_dict['conversational_model'].chat(question)
        # print(ans)
    return ans


def start_chatbot_small(input_text, model_dict=None):
    """
    Conversational Chatbot without using wikipedia/google search
    """
    if model_dict is None:
        print()

    question = input_text
    question = re.sub("[^A-Za-z]", " ", question)
    question = question.strip()
    ans = model_dict['conversational_model'].chat(question)
    # print(ans)
    return ans


if __name__ == '__main__':
    # pass
    start_chatbot_small()
    # start_chatbot(high_accuracy=True)
    # start_chatbot_with_internet_search(high_accuracy=False)

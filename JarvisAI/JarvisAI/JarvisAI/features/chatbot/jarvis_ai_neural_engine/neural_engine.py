from transformers import pipeline, Conversation
import requests
import best_answer_finder
from youtubesearchpython import VideosSearch
import googlesearch
import wikipedia
import shutup
shutup.please()


def search_on_wikipedia(query):
    """
    This function will return the top Wikipedia search results for the query
    :param query: string
    :return: string
    """
    # python code to search on wikipedia
    try:
        summary = wikipedia.summary(query)
        return summary
    except Exception as e:
        print(e)
        return None


def search_on_google(query):
    """
    This function will return the top Google search results for the query
    :param query: string
    :return: list of strings
    """
    # python code to search on Google
    google_results = []
    for j in googlesearch.search(query):
        google_results.append(j)
    google_results = [x for x in google_results if x.startswith('https://')]
    return google_results


def search_on_youtube(query):
    """
    This function will return the top 10 YouTube videos for the query
    :param query: string
    :return: list of strings
    """
    # python code to search on YouTube
    videosSearch = VideosSearch(query, limit=10)
    youtube_results = videosSearch.result()
    youtube_ = []
    for i in youtube_results['result']:
        youtube_.append((i['title'], i['link']))
    return youtube_


def general_knowledge(text):
    """
    :param text: string,
    :return: list of string
    """
    # https://huggingface.co/spaces/akhaliq/T0pp
    r = requests.post(url='https://hf.space/gradioiframe/akhaliq/T0pp/api/predict', json={"data": [text]})
    return r.json()['data']


def neural_search_engine(text):
    """
    :param text: string
    :return: list of strings
    """
    # https://huggingface.co/spaces/algomuffin/neural-search-engine
    r = requests.post(url='https://hf.space/gradioiframe/algomuffin/neural-search-engine/+/api/predict',
                      json={"data": [text]})
    return r.json()['data']


class ChatBot:
    def __init__(self, conversational_pipeline):
        self.conversational_pipeline = conversational_pipeline
        self.conv1 = None
        self.conv2 = None
        self.count = 0
        self.last = None

    def chat(self, text):
        """
        This function takes in a text input and returns the response from the chatbot
        :param text: string
        :return: list of strings
        """
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
        return [ans]


class JarvisAINeuralEngine(ChatBot):
    def __init__(self):
        #   self.classifier = pipeline("zero-shot-classification")
        self.question_answering = pipeline("question-answering",
                                           model="bert-large-uncased-whole-word-masking-finetuned-squad")

        self.conversational_pipeline = pipeline("conversational", model="microsoft/DialoGPT-large")

        super().__init__(self.conversational_pipeline)

    def predict_outcome(self, text, enable_google=False, enable_youtube=False):
        suggest_best_answers = True
        # search answer in wikipedia
        wikipedia_context = search_on_wikipedia(text)
        wikipedia_result = []
        if wikipedia_context is not None:
            wikipedia_result = [self.question_answering(question=text, context=wikipedia_context)]
            # wikipedia_result_ = [i.get("answer") for i in wikipedia_result if i.get("answer") is not None]

        # search answer via chatbot
        conversation_result = self.chat(text)

        # search answer using general knowledge model
        gk_result = general_knowledge(text)
        gk_result = [self.question_answering(question=text, context=i) for i in gk_result]
        # gk_result_ = [i.get("answer") for i in gk_result if i.get("answer") is not None]

        # search answer using neural search engine
        nse_result = neural_search_engine(text)
        nse_result = [self.question_answering(question=text, context=i) for i in nse_result]
        # nse_result_ = [i.get("answer") for i in nse_result if i.get("answer") is not None]

        # all types of answers
        answers_dict = {
            "conversation": conversation_result,
            "general_knowledge": gk_result,
            "neural_search_engine": nse_result,
            "wikipedia_result": wikipedia_result,
        }
        response = {}
        response["suggested_answer"] = None
        response["weights_of_all_models"] = None
        if suggest_best_answers:
            weights_of_all_models, suggested_answer = best_answer_finder.find_best(text, answers_dict, self.question_answering)
            response["suggested_answer"] = suggested_answer
            response["weights_of_all_models"] = weights_of_all_models

        response["google_results_links"] = search_on_google(text) if enable_youtube else []
        response["youtube_results_title_and_links"] = search_on_youtube(text) if enable_google else []

        return response


if __name__ == "__main__":
    jarvis = JarvisAINeuralEngine()
    print(jarvis.predict_outcome("what is the meaning of life"))

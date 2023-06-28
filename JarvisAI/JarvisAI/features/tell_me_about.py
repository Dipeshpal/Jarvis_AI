import wikipedia
import re


def tell_me_about(*args, **kwargs):
    # topic = kwargs.get("query")
    entities = kwargs.get("entities")
    if len(entities) == 0:
        return "Entity not found"
    li = ['EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY', 'NORP', 'ORDINAL', 'ORG',
          'PERCENT', 'PERSON', 'PRODUCT', 'TIME', 'WORK_OF_ART']
    topic = [entity[0] for entity in entities if entity[1] in li][0]
    try:
        ny = wikipedia.page(topic)
        res = str(ny.content[:500].encode('utf-8'))
        res = re.sub('[^a-zA-Z.\d\s]', '', res)[1:]
        return res
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    import spacy
    import os

    try:
        nlp = spacy.load("en_core_web_trf")
    except:
        print("Downloading spaCy NLP model...")
        print("This may take a few minutes and it's one time process...")
        os.system(
            "pip install https://huggingface.co/spacy/en_core_web_trf/resolve/main/en_core_web_trf-any-py3-none-any.whl")
        nlp = spacy.load("en_core_web_trf")


    def perform_ner(*args, **kwargs):
        query = kwargs['query']
        # Process the input text with spaCy NLP model
        doc = nlp(query)

        # Extract named entities and categorize them
        entities = [(entity.text, entity.label_) for entity in doc.ents]

        return entities


    query = "tell me about Narendra Modi"
    # Perform NER on input text
    entities = perform_ner(query=query)

    print(tell_me_about(query=query, entities=entities))

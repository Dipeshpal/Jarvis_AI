import spacy
import os

try:
    nlp = spacy.load("en_core_web_trf")
except:
    print("Downloading spaCy NLP model...")
    print("This may take a few minutes and it's one time process...")
    os.system("pip install https://huggingface.co/spacy/en_core_web_trf/resolve/main/en_core_web_trf-any-py3-none-any.whl")
    nlp = spacy.load("en_core_web_trf")


def perform_ner(*args, **kwargs):
    query = kwargs['query']
    # Process the input text with spaCy NLP model
    doc = nlp(query)

    # Extract named entities and categorize them
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    return entities


if __name__ == "__main__":
    # Example input text
    input_text = "I want to buy a new iPhone 12 Pro Max from Apple."

    # Perform NER on input text
    entities = perform_ner(query=input_text)

    # Print the extracted entities
    print(entities)

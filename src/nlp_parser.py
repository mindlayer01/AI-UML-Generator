import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(text)

    nouns = []
    verbs = []

    for token in doc:

        if token.pos_ == "NOUN":
            nouns.append(token.text)

        if token.pos_ == "VERB":
            verbs.append(token.text)

    return nouns, verbs
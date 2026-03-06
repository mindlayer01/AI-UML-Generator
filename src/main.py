from preprocess import load_srs, clean_text
from nlp_parser import extract_entities
from uml_generator import generate_uml

text = load_srs("../data/sample_srs.txt")

cleaned = clean_text(text)

nouns, verbs = extract_entities(cleaned)

uml_code = generate_uml(nouns, verbs)

with open("../output/diagram.puml", "w") as f:
    f.write(uml_code)

print("UML Diagram Generated Successfully")
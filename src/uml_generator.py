def generate_uml(nouns, verbs):

    classes = list(set(nouns))

    uml = "@startuml\n"

    for c in classes:
        uml += f"class {c}\n"

    for i in range(min(len(classes)-1, len(verbs))):
        uml += f"{classes[i]} --> {classes[i+1]} : {verbs[i]}\n"

    uml += "@enduml"

    return uml
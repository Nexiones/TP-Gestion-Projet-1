import json

def ajouter_contact(contact, fichier="contacts.json"):
    try:
        with open(fichier, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []
    contacts.append(contact)
    with open(fichier, "w") as f:
        json.dump(contacts, f, indent=4)


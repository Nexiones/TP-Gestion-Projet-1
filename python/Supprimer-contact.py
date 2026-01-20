import json

def supprimer_contact(index, fichier="contacts.json"):
    try:
        with open(fichier, "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'existe pas.")
        return  # Rien à supprimer si le fichier n'existe pas
    
    if index < 0 or index >= len(contacts):
        print(f"Index {index} invalide. La liste contient {len(contacts)} contacts.")
        return
    
    contact_supprime = contacts.pop(index)
    with open(fichier, "w") as f:
        json.dump(contacts, f, indent=4)
    print(f"Contact supprimé : {contact_supprime}")

# TP-Gestion-Projet-1

# TP – Gestion de projet avec GitHub Projects

**Développement Python avec GitHub Projects (Kanban & Roadmap)**

## Objectifs

* Structurer un **projet informatique collaboratif**
* Utiliser **GitHub Projects** pour planifier et suivre un projet
* Mettre en œuvre un **workflow Kanban** et une **Roadmap (Gantt)**
* Gérer des **issues**, des **milestones (sprints)** et des **labels**
* Relier **développement**, **tests** et **documentation**
* Produire un **livrable professionnel** (code + suivi de projet)

## Pré-requis

* Compte GitHub actif
* Notions de base sur :

  * repositories
  * issues
* Poste avec navigateur web
* Bases de Python

## Outils utilisés

* GitHub
* GitHub Projects (Kanban + Roadmap)
* Python
  *(IDLE, VS Code, Thonny ou Jupyter Notebook)*

## Mini-projet support

### Application Python : **Gestionnaire de contacts**

L’application permet de gérer une liste de contacts stockée dans un fichier (JSON ou CSV).

### Fonctionnalités attendues

| Issue                     | Description                         | Responsable | Sprint   | Début | Fin   |
| ------------------------- | ----------------------------------- | ----------- | -------- | ----- | ----- |
| Création fichier contacts | Stockage des contacts (JSON ou CSV) | Élève 1     | Sprint 1 | 19/01 | 20/01 |
| Ajouter un contact        | Ajout d’un contact                  | Élève 2     | Sprint 1 | 19/01 | 21/01 |
| Supprimer un contact      | Suppression d’un contact            | Élève 2     | Sprint 1 | 20/01 | 22/01 |
| Lister les contacts       | Affichage des contacts              | Élève 3     | Sprint 1 | 20/01 | 22/01 |
| Tests unitaires           | Vérification des fonctionnalités    | Élève 4     | Sprint 2 | 22/01 | 23/01 |
| Documentation utilisateur | Procédure d’utilisation             | Élève 3     | Sprint 2 | 22/01 | 23/01 |

## Répartition des rôles

### 1. Chef de projet / Scrum Master

* Création et gestion du **GitHub Project**
* Suivi du Kanban et de la Roadmap
* Reporting d’avancement

### 2. Développeur Python principal

* Développement des fonctionnalités cœur
* Mise à jour des issues associées

### 3. Développeur Python secondaire / Testeur

* Fonctions complémentaires
* Tests unitaires simples

### 4. Documentaliste / Testeur

* Fiches de test
* Fiche de recette
* Mini-manuel utilisateur

> Pour le groupe de **3 étudiants**, certains rôles peuvent être cumulés.

## Étape 1 – Création du repository et du projet

1. Créer un repository GitHub nommé :

   ```
   TP-Gestion-Projet-GroupeX
   ```
2. Aller dans **Projects → New Project**
3. Choisir le template **Kanban (Basic)**
4. Créer les colonnes :

   * `To do`
   * `In progress`
   * `Done`
5. Ajouter une **description du projet** et ses objectifs

> *Le projet sera lié aux issues et utilisé pour la Roadmap.*

## Étape 2 – Création des issues

> **Une issue = une tâche**

Pour chaque issue :

* Assigner un responsable
* Ajouter un **label** :

  * `feature`
  * `test`
  * `documentation`
  * `bug`
* Associer une **milestone (Sprint 1 ou 2)**
* Renseigner une **date d’échéance (Due date)**

> Ces dates permettront la génération automatique du **diagramme de Gantt (Roadmap)**.

### Exemple d’issue

```
Title: Ajouter un contact
Label: feature
Milestone: Sprint 1
Assignee: Élève B
Due date: 21/01/2026
```

## Étape 3 – Organisation du Kanban

1. Placer toutes les issues dans **To do**
2. Passer une issue en **In progress** au démarrage du travail
3. Déplacer en **Done** une fois terminée

Workflow :

```
To do → In progress → Done
```

> *Un commentaire d’avancement est fortement recommandé.*

## Étape 4 – Gestion des milestones (Sprints)

1. Créer deux milestones :

   * **Sprint 1** : développement
   * **Sprint 2** : tests & documentation
2. Associer chaque issue à un sprint
3. Observer le **taux d’avancement** par sprint

> *Permet de suivre la charge et le respect du planning.*

## Étape 5 – Roadmap (Diagramme de Gantt)

1. Ouvrir **Projects → Roadmap**
2. Vérifier :

   * dates de début / fin
   * chevauchements
   * tâches en retard
3. Ajouter des commentaires si nécessaire

> *La Roadmap est le Gantt du projet, directement lié aux issues.*

## Étape 6 – Développement Python

Créer le fichier `contacts.py`.

### Fonctions (exemple)

```python
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

def lister_contacts(fichier="contacts.json"):
    try:
        with open(fichier, "r") as f:
            contacts = json.load(f)
        for c in contacts:
            print(c)
    except FileNotFoundError:
        print("Aucun contact trouvé.")
```

- Chaque étudiant développe **uniquement ses fonctionnalités assignées**
- Les tests sont réalisés par le testeur

## Étape 7 – Suivi et reporting

1. Filtrer les issues par :

   * label
   * milestone
   * responsable
2. Rédiger un **reporting dans le README ou le Wiki**

### Exemple

```
Sprint 1 : 4/4 tâches terminées (100%)
Sprint 2 : 2/2 tâches terminées (100%)

Observations :
- Fonctionnalités Python opérationnelles
- Tests validés
- Documentation finalisée
```

## Étape 8 – Analyse et synthèse

Répondre collectivement :

* Quelles difficultés rencontrées ?
* Quelles tâches ont pris plus de temps que prévu ?
* Pourquoi ?
* Quelles améliorations pour un projet réel ?

Lien avec :

* fiche de test
* fiche de recette
* fiche de configuration

## Remarques

* L’évaluation porte principalement sur :

  * le **suivi de projet**
  * la cohérence du Kanban et de la Roadmap
  * l’utilisation correcte des issues, labels et milestones
* Le code doit être **fonctionnel**, mais la **méthodologie est prioritaire**

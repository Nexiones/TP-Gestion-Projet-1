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
| Création fichier contacts | Stockage des contacts (JSON ou CSV) | Noa         | Sprint 1 | 15/01 | 17/01 |
| Ajouter un contact        | Ajout d’un contact                  | Charles     | Sprint 1 | 15/01 | 18/01 |
| Supprimer un contact      | Suppression d’un contact            | Charles     | Sprint 1 | 20/01 | 22/01 |
| Lister les contacts       | Affichage des contacts              | Luc         | Sprint 1 | 20/01 | 22/01 |
| Tests unitaires           | Vérification des fonctionnalités    | Enzo        | Sprint 2 | 25/01 | 27/01 |
| Documentation utilisateur | Procédure d’utilisation             | Luc         | Sprint 2 | 25/01 | 28/01 |

## Répartition des rôles

### 1. Chef de projet / Scrum Master - Doumbia Noa

* Création et gestion du **GitHub Project**
* Suivi du Kanban et de la Roadmap
* Reporting d’avancement

### 2. Développeur Python principal - Feuntun Charles

* Développement des fonctionnalités cœur
* Mise à jour des issues associées

### 3. Développeur Python secondaire / Testeur - Tournier Luc

* Fonctions complémentaires
* Tests unitaires simples

### 4. Documentaliste / Testeur - Dufour Enzo

* Fiches de test
* Fiche de recette
* Mini-manuel utilisateur

# 🚀 Projet Test : Pilotage par Roadmap & Issues

## 📝 Description du projet
Ce projet est un environnement de test dédié à l'expérimentation des outils de gestion de projet de GitHub. L'idée centrale est de valider un flux de travail où la **gouvernance technique** (via les Issues) alimente directement la **vision stratégique** (via la Roadmap).

L'objectif est de démontrer comment une équipe peut maintenir une synchronisation parfaite entre le développement quotidien et les objectifs à long terme sans quitter l'écosystème GitHub.

---

## 🎯 Objectifs du test

* **Traçabilité complète :** Lier chaque modification du code à une `Issue` spécifique pour comprendre le "pourquoi" derrière chaque "quoi".
* **Pilotage par la Roadmap :** Utiliser les vues chronologiques de *GitHub Projects* pour visualiser l'avancement des grands chantiers.
* **Standardisation :** Tester des modèles d'Issues (Issue Templates) pour garantir la qualité des informations remontées.
* **Automatisation du Workflow :** Configurer les triggers pour que le statut de la Roadmap se mette à jour automatiquement selon l'activité des branches.

---

## 🛠️ Structure du test

| Élément | Utilisation prévue |
| :--- | :--- |
| **Issues** | Unités de travail atomiques (Bugs, Features, Tests). |
| **Labels** | Catégorisation par priorité (`prio:high`) et par type (`type:test`). |
| **Milestones** | Regroupement des issues par versions ou sprints. |
| **Project (V2)** | Vue Kanban pour le quotidien et vue Roadmap pour la planification. |

---

> [!IMPORTANT]
> Ce dépôt est un environnement de test. Les données et les issues créées ici servent uniquement à valider la configuration de la Roadmap.

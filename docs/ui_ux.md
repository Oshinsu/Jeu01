# Guide UI/UX — Re:2003

## 1. Principes directeurs
- **Retro-futurisme** : interface évoquant les débuts des années 2000 tout en restant moderne et accessible.
- **Lisibilité** : hiérarchie claire, typographie lisible, code couleur cohérent pour différencier vie scolaire, finances et relations.
- **Modularité** : panneaux dockables (calendrier, finances, relations, inventaire) pour adapter l'interface aux préférences du joueur.
- **Temps réel maîtrisé** : indicateurs visuels et auditifs pour signaler le passage du temps et les événements urgents.

## 2. Layout global
```
┌──────────────────────────────────────────────────────┐
│ Barre supérieure : date, météo, indicateurs clés      │
├───────────────┬───────────────────────────────────────┤
│ Navigation    │  Zone principale contextuelle          │
│ (icônes)      │  - Planning jour/semaine                │
│               │  - Tableau de bord finances             │
│               │  - Vue relations (diagramme social)     │
│               │  - Écrans narratifs (dialogues GPT)     │
├───────────────┴───────────────────────────────────────┤
│ Barre inférieure : actions rapides, journal, agent GPT │
└──────────────────────────────────────────────────────┘
```

## 3. Composants clés
### 3.1 Tableau de bord calendrier
- Vue jour/semaine/mois.
- Drag & drop d'activités (cours, rendez-vous, tâches de développement).
- Indicateurs de focus (études, business, social) pour visualiser l'équilibre.
- Timeline d'événements mondiaux alimentée par GPT.

### 3.2 Module finances
- Graphiques interactifs : portefeuille d'actions, cashflow, valeur nette.
- Tableaux détaillés : performances, dividendes, échéances fiscales.
- Bouton "Conseil GPT" pour analyser des opportunités ou risques.

### 3.3 Relations & PNJ
- Graphe social interactif (nodes = PNJ, edges = relations).
- Fiches PNJ : stats, affinités, historique des interactions, quêtes en cours.
- Système de messagerie rétro (SMS, emails, forums) avec réponse GPT.

### 3.4 Inventaire & Lifestyle
- Catégorisation par type (technologie, immobilier, luxe, projets).
- Visualisation 3D/2D des biens de prestige (galerie, showroom virtuel).
- Bouton "Profiter" déclenchant des scènes (fêtes, voyages, sorties culturelles).

### 3.5 Espace coding & entreprise
- IDE simplifié pour mini-jeux de programmation (syntax highlighting, auto-complétion).
- Tableaux Kanban pour gérer projets et équipes.
- Graphiques de croissance (utilisateurs, revenus, satisfaction).

## 4. Agent GPT dans l'UI
- Widget persistent en bas à droite : avatar personnalisable, bulles contextuelles.
- Modes d'interaction : conversation libre, suggestions proactives, requêtes rapides.
- Historique consultable pour revoir les conseils, quêtes et décisions passées.
- Mode "Focus" : GPT guide le joueur pas à pas lors d'activités complexes (examens, négociations, développement produit).

## 5. Accessibilité
- Mode daltonien, contraste élevé, prise en charge clavier/souris/manette.
- Options de vitesse du temps (pause, ralenti, accéléré) pour gérer la charge cognitive.
- Assistants contextuels pour expliquer mécaniques économiques ou sociales.

## 6. Inspirations visuelles
- Dashboards modernes (Notion, Linear) + touches rétro (Windows XP, PalmOS).
- Couleurs : palette bleus/gris pour l'école, verts/or pour la finance, violets pour le lifestyle.
- Typographie : Titres en "Poppins" ou "Montserrat", texte en "Inter" pour lisibilité.

## 7. Prochaines étapes UI/UX
1. Wireframes basse fidélité pour chaque écran principal.
2. Prototype interactif (Figma) avec transitions et animations.
3. Tests utilisateurs ciblés (fans de jeux de gestion, RPG narratifs).
4. Implémentation front-end modulaire (React + Tailwind + d3.js pour graphes).

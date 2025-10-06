# Architecture Technique — Re:2003

## 1. Stack proposée
- **Front-end** : React + TypeScript, Vite, Zustand (ou Redux Toolkit) pour l'état, Tailwind CSS pour le styling, d3.js / Recharts pour les visualisations.
- **Back-end** : NestJS (Node.js) ou FastAPI (Python) pour les API et la logique métier.
- **Base de données** : PostgreSQL (données structurées), Redis (cache, file d'événements temps réel), Pinecone/Weaviate (mémoire vectorielle GPT).
- **Infra** : Docker + Kubernetes, CI/CD GitHub Actions, hébergement sur Azure/AWS/GCP.

## 2. Modules principaux
1. **Simulation de temps**
   - Service orchestrant le calendrier, la progression jour/heure et la génération d'événements.
   - WebSocket pour pousser les mises à jour au front.
2. **Gestion scolaire & sociale**
   - Microservice dédié aux cours, notes, relations PNJ.
   - Stockage des PNJ, états relationnels, historique des interactions.
3. **Économie & finance**
   - Module boursier avec données historiques préchargées.
   - Service d'entrepreneuriat (projets, entreprises, finances, employés).
4. **Narration & GPT**
   - Orchestrateur de prompts avec context builder (journal, état du monde, intent).
   - Moteur de quêtes : définit arcs, conditions, récompenses, délègue la génération de contenu à GPT.
   - Filtre/modérateur (policy checker, safety).
5. **Inventaire & lifestyle**
   - Gestion des assets physiques et numériques.
   - Système d'événements lifestyle (voyages, achats de luxe) avec effets sur stats.

## 3. Intégration de l'agent GPT
- **Pipeline de requêtes** :
  1. Collecte de contexte (état joueur, PNJ, calendrier, objectifs).
  2. Construction du prompt (gabarits + mémoire vectorielle).
  3. Appel API GPT-5 (ou modèle open source finetuné si disponible).
  4. Post-traitement (vérification cohérence, génération d'objets, mise à jour du monde).
  5. Stockage des réponses dans un journal structuré.
- **Mode offline** : fallback vers scénarios préécrits si l'API est indisponible.
- **Observabilité** : logs, traces et métriques (latence, coût tokens, satisfaction joueur).

## 4. Données & Sauvegarde
- Snapshot quotidien de l'état du monde + journal incrémental pour replays.
- Sauvegardes multiples (timelines alternatives) avec possibilité de "rewind".
- Export JSON/CSV pour analytics, IA training et équilibrage.

## 5. Sécurité & conformité
- Gestion d'identité (OAuth 2.0) pour le joueur, + rôles pour l'équipe dev.
- Protection des mineurs (contenu approprié, modération).
- Limitation des abus de l'IA (profanités, conseils financiers irresponsables) via règles et RLHF.

## 6. Outils & Workflow
- **CI/CD** : lint, tests unitaires, tests d'intégration, QA automatisée.
- **Monitoring** : Grafana + Prometheus, Sentry pour erreurs front/back.
- **Feature flags** : LaunchDarkly ou module maison pour déployer progressivement les systèmes (économie, quêtes, lifestyle).

## 7. Roadmap technique
1. Prototype vertical slice (front React, back API simple, intégration GPT minimale).
2. Ajout simulateur calendrier + état joueur persistant.
3. Implémentation modules finance et relations avec tests.
4. Optimisation performance, scalabilité et outils live-ops (événements saisonniers).

# Project "Re:2003"

"Re:2003" est un concept de jeu narratif-gestion dans lequel le joueur est propulsé en 2003 avec l'intégralité de ses connaissances de 2025. Cette première itération du dépôt décrit la vision, les mécaniques clés et l'architecture technique proposées pour construire une expérience riche, dynamique et alimentée par un agent GPT intégré.

## Table des matières
- [Pitch rapide](#pitch-rapide)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Écosystème GPT](#écosystème-gpt)
- [Documents de conception](#documents-de-conception)
- [Prochaines étapes](#prochaines-étapes)

## Pitch rapide
- **Cadre temporel** : du 1er septembre 2003 jusqu'à la fin de l'année scolaire, avec possibilité d'extensions sur plusieurs années.
- **Protagoniste** : un lycéen fraîchement réincarné, doté de connaissances futuristes (technologie, tendances culturelles, événements géopolitiques et sportifs, etc.).
- **Objectif** : maîtriser la vie scolaire, sociale et entrepreneuriale tout en capitalisant sur l'avance informationnelle pour bâtir un empire financier et personnel.

## Fonctionnalités principales
- **Calendrier vivant** : emploi du temps scolaire, événements clés du monde réel (sorties de consoles/jeux, compétitions sportives, élections, sorties cinéma…), rendez-vous sociaux et deadlines.
- **Économie systémique** : investissements boursiers, lancements de start-ups, création d'applications (blog, réseaux sociaux naissants), paris sportifs, collection d'art, immobilier (maisons, villas, yachts, voitures de luxe).
- **Vie scolaire et sociale** : gestion des cours, des révisions, des notes et des interactions avec professeurs et camarades. Possibilité de créer des clubs, de participer à des compétitions et de gérer des relations complexes.
- **Gameplay hybride** : boucle quotidienne mêlant simulation de calendrier, mini-jeux (échecs, jeux vidéo rétro, coding challenges) et prise de décisions à choix multiples.
- **Évolution dynamique** : le monde réagit aux actions du joueur, les opportunités se renouvellent et l'histoire se ramifie.

## Écosystème GPT
- **Agent narratif** : GPT-5 orchestre les dialogues, les quêtes et la génération d'événements, en respectant une bible narrative et des garde-fous définis.
- **Assistant stratégique** : l'agent fournit des conseils contextuels (analyse de marché, tutoriels de code, recommandations scolaires) basés sur l'état actuel du joueur.
- **Génération procédurale** : création en temps réel de personnages, de missions, d'objets et de story beats cohérents avec l'époque 2003.
- **Sécurité et cohérence** : système de modération et de validation pour filtrer les réponses, maintenir la timeline historique et éviter les incohérences majeures.

## Documents de conception
- [docs/game_design.md](docs/game_design.md) — vision détaillée, mécaniques et progression.
- [docs/ui_ux.md](docs/ui_ux.md) — principes d'interface et expériences utilisateur attendues.
- [docs/technical_architecture.md](docs/technical_architecture.md) — architecture logicielle et intégration de l'agent GPT.

## Prochaines étapes
1. Définir un prototype jouable (paper prototype + maquette interactive Figma).
2. Développer un noyau gameplay en React + TypeScript avec état persisté (ex. Zustand) et simulateur de calendrier.
3. Intégrer une API GPT (OpenAI ou Azure) avec un middleware de modération et de mémoire longue.
4. Itérer sur l'équilibrage économique et la progression narrative.
5. Concevoir un système de sauvegarde multi-chronologies (timelines alternatives).

Cette base documentaire servira de fondation pour organiser le développement collaboratif du jeu.

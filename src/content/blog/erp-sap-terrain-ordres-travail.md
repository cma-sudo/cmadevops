---
title: "SAP en mode terrain : ce que j'ai appris en pilotant des milliers d'ordres de travail"
description: "Retour d'expérience sur l'usage de SAP comme Power User dans le déploiement FTTH chez Cablex — entre la logique de l'ERP et la réalité du chantier."
pubDate: 'May 05 2026'
---

Chez Cablex, filiale infrastructure du groupe Swisscom, j'ai piloté pendant plusieurs années des centaines d'ordres de travail par mois dans SAP. Pas depuis un bureau isolé, mais en interface directe avec les équipes terrain, les sous-traitants et les coordinateurs de projet. Ce rôle de Power User certifié m'a appris une chose essentielle : un ERP ne ment pas, mais il simplifie — et cette simplification peut coûter cher quand on déploie du FTTH à l'échelle d'un canton.

## L'ERP voit des lignes, le terrain voit des caves

Dans SAP, un ordre de travail c'est une entrée propre : un identifiant, une adresse, un statut, une date. Sur le terrain, c'est autre chose. Une cave inaccessible parce que le propriétaire n'a pas transmis le code, une gaine bouchée non référencée, un sous-traitant bloqué faute d'habilitation spécifique au canton du Jura. Ces réalités n'ont pas de champ dédié dans la transaction standard.

Ma première réflexion, après quelques mois dans ce rôle, a été de ne pas chercher à tout faire rentrer dans le moule ERP — mais d'identifier précisément ce que l'ERP doit porter (la traçabilité réglementaire, la facturation, le suivi global) et ce qu'il ne verra jamais (la friction humaine, les blocages terrain, les délais officieux).

## Construire un pont sans tout réinventer

J'ai mis en place une couche intermédiaire légère : des extractions SAP quotidiennes croisées avec les remontées terrain via un tableur structuré, puis visualisées sur un tableau de bord Grafana interne. Pas de développement lourd. Le but n'était pas de créer un shadow system, mais de donner aux coordinateurs une vue à 48h qui complète ce que SAP ne montre qu'à J+3 ou J+7 selon les cycles de clôture.

Ce qui a changé concrètement : la détection des ordres bloqués est passée de "on le voit à la facturation" à "on intervient le lendemain". Sur un déploiement FTTH en milieu urbain dense — Delémont, zone industrielle, immeubles collectifs — ce delta de quelques jours fait toute la différence sur les engagements contractuels.

## Ce que la certification SAP m'a vraiment apporté

Être Power User certifié ne signifie pas connaître chaque transaction par cœur. Ça signifie comprendre la logique de données sous-jacente : comment un ordre de travail s'articule avec un projet, comment les statuts système et utilisateur interagissent, pourquoi une clôture comptable peut bloquer une réouverture terrain.

Cette compréhension m'a permis de former les coordinateurs avec des mots concrets : "Si tu fermes cet ordre avant la réception contradictoire, voilà ce que tu déclenches en aval." Pas de la formation SAP abstraite — de la conséquence opérationnelle directe.

## Ce que j'emporte de cette expérience

Avec du recul, la coordination ERP/terrain ne s'improvise pas. Elle demande quelqu'un capable de parler les deux langues : celle des systèmes (statuts, flux de données, cycles de traitement) et celle des chantiers (aléas, priorités changeantes, contraintes locales propres à chaque canton).

Ce rôle d'interface — que j'ai occupé entre les équipes Wireline Rollout et les fonctions support chez Cablex — est souvent sous-estimé dans les projets d'infrastructure. On investit dans l'ERP, dans la formation, dans les processus. Mais le maillon qui traduit entre la donnée et la réalité, c'est humain. Et ça s'entraîne.

Si vous déployez un projet d'infrastructure complexe et que votre ERP et votre terrain ne se parlent plus, n'hésitez pas à m'écrire : christophe-matt.e3ypb@simplelogin.com

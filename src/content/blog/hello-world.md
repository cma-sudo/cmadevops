---
title: 'Bienvenue'
description: "Pourquoi je lance ce site et à quoi s'attendre"
pubDate: 'Apr 05 2026'
---

J'auto-héberge ma maison depuis des années — Home Assistant, agents Python maison,
LLM on-prem, tout le bazar. Chaque semaine je me prends un mur, je le résous, et
j'oublie immédiatement comment je l'ai résolu. Les notes de session s'empilent dans
des fichiers markdown éparpillés sur iCloud.

Ce site, c'est l'index de ces notes.

## À quoi s'attendre

Des articles courts et argumentés sur ce qui se passe vraiment dans mon homelab :

- Fixer un regex qui matchait `"souvent"` à cause du pattern `"vent"`
- Pourquoi le speedtest UDM bat tous les exporters Docker
- Construire un context manager central pour tuer les alertes CO2 à 1h du matin dans les chambres
- Ce qui se passe quand votre `rest_command` YAML casse à cause de l'échappement Markdown

Pas de tutos, pas de « 10 choses à savoir sur Kubernetes ». Juste : ce qui a cassé,
ce qui l'a réparé, et ce que je ferais différemment la prochaine fois.

## La stack derrière ce site

Ce site tourne sur [Astro](https://astro.build) en build statique, déployé sur
Cloudflare Pages, avec le DNS chez Infomaniak. Le repo est public, le contenu est
en Markdown, et l'ensemble se rebuild à chaque git push.

Parce que si le homelab tombe, le blog doit rester debout.

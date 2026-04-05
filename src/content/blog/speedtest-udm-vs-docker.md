---
title: "Pourquoi mon UDM bat tous les exporters Docker sur le speedtest"
description: "Trois mois à essayer de monitorer mon débit WAN depuis un conteneur. Résultat : le chiffre le plus fiable venait déjà de la box."
pubDate: 'Apr 06 2026'
---

J'ai passé trois mois à brancher des exporters speedtest dans Prometheus. Image
officielle Ookla, fork communautaire, wrapper Python maison qui tapait sur
`librespeed`, j'ai tout essayé. Le dashboard Grafana avait fière allure : courbe
download, courbe upload, latence, jitter, le tout scrapé toutes les 15 minutes
depuis un conteneur sur mon NUC.

Sauf que les chiffres étaient faux.

## Le symptôme

4 Gb/s annoncés par l'opérateur. Mon exporter me sortait entre 800 Mb/s et
1.2 Gb/s, jamais au-delà. J'ai d'abord accusé le câble, puis le switch, puis
Docker, puis la NIC du NUC. J'ai fini par sortir un laptop, le brancher en
direct sur le port LAN de l'UDM, et là : 3.8 Gb/s. Propre.

Le problème n'était pas le réseau. C'était le point de mesure.

## Ce que fait vraiment un exporter dans un conteneur

Un conteneur Docker sur un hôte Linux passe par le bridge `docker0`, qui passe
par le kernel de l'hôte, qui passe par la NIC de l'hôte, qui passe par le
switch, qui passe par l'UDM. À chaque saut vous perdez soit en débit soit en
overhead CPU. Sur un lien 1 Gb/s ça se voit à peine. Sur un lien 4 Gb/s
symétrique, vous plafonnez bien avant le WAN.

Et surtout : le test Ookla lancé depuis un conteneur choisit son serveur
miroir en fonction de l'IP source vue côté serveur. Avec une NIC grand public
et un MTU mal réglé, vous tapez sur un miroir à 600 km qui bride.

## Ce que fait l'UDM

L'UDM embarque son propre client speedtest (`ubnt-tools speedtest`) qui tourne
directement sur le CPU du routeur, bypasse le bridge Docker de votre host, et
surtout choisit un serveur Ookla très proche — typiquement le miroir régional
du FAI lui-même. Résultat : le chiffre collé au débit WAN réel.

La commande qui m'a fait gagner trois mois :

```bash
ssh root@udm "ubnt-tools speedtest" | jq
```

Sortie JSON propre, exploitable directement. J'ai branché ça dans un script
bash côté host, qui écrit dans un fichier `.prom` lu par le `node_exporter`
en mode `textfile collector`. Trois lignes de code, une valeur fiable toutes
les 30 minutes.

## Ce que ça m'a appris

Quand vous monitorez du réseau, mesurez depuis l'équipement qui fait le
réseau. Pas depuis un conteneur qui traverse trois couches d'abstraction pour
atteindre la fibre.

Les exporters Docker sont géniaux pour tout ce qui est applicatif. Dès que
vous touchez à du bas-niveau — débit WAN, latence inter-VLAN, perte de
paquets — remontez d'un cran. L'outil intégré au routeur ou au switch bat
quasi systématiquement le conteneur.

Le dashboard Grafana n'a pas changé. Juste la source de vérité derrière.

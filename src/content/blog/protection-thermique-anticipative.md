---
title: 'Ma maison apprend à anticiper (la chaleur, la conso, le surplus)'
description: 'Petite mécanique d''une sandbox : volets, talon de consommation, surplus solaire. Apprendre à piloter la courbe chez soi avant de projeter ailleurs.'
pubDate: 'May 29 2026'
---

<figure class="blog-illustration">
  <img src="/blog/illustrations/protection-thermique-anticipative.svg" alt="Illustration : quatre échelles emboîtées — maison, borne EV, PAC voisinage, parc de bâtiments — qui partagent la même grammaire : lire, anticiper, piloter la demande par l'offre." />
</figure>

---

Le marché de l'énergie est en train de basculer. La valeur se déplace : moins dans les watts produits, plus dans les watts pilotés. Qui consomme à quelle heure, qui efface, qui shift, qui valorise le creux. C'est dans cette zone — l'arbitrage et la coordination — que se logent les nouvelles marges, les nouveaux acteurs et les nouveaux métiers. Tout ce qui suit, je le teste à la maison. Une sandbox, à petite échelle, pour comprendre les briques avant qu'elles ne grossissent.

Première version de ma protection solaire à la maison : salon dépasse 24°C → fermer à 70%. Salon dépasse 26°C, ou cadre de baie dépasse 38°C → fermer à 100%. Lisible, propre, ça marchait.

Ce matin, vers 9h, je ferme tout à la main : volet est, volets sud, velux salon. Il fait 25°C dehors, le soleil n'a pas encore tapé sur la baie sud-sud-ouest, le salon est à 24,9°C. Selon mes propres seuils, **tout devrait rester ouvert**. Sauf qu'à l'œil nu, c'est évident : ça va taper. Mes seuils sont en retard d'une guerre.

J'ai sorti la tendance. Extérieur passé de 15°C à 25°C depuis 7h, +1,3°C par heure, encore en hausse. Ciel à 10 % de couverture, UV à 7. La maison n'a pas refroidi la nuit. L'extérieur est sur le point de dépasser l'intérieur. Et le soleil va basculer plein SSO à midi. *Une logique de seuils ne voit rien de tout ça.*

J'ai refait la couche d'actionnement. Anticiper la journée chaude (ciel clair, UV ≥ 4, extérieur ≥ 22°C qui monte). Détecter le faisceau direct sur la façade — pas un seuil de lux absolu (mon capteur Hue sature à 14 444, bug rigolo dans la v1). Réouverture avec hystérésis : intérieur redescendu **et** soleil parti. Reset matinal à 7h pour éviter qu'une machine d'état RTS se fige.

Et puis j'ai réalisé que c'est exactement la même histoire côté **énergie**.

Mon installation tient en deux chiffres : **1 600 W de PV** en micro-onduleurs, répartis 800 maison + 800 cabane, en autoconsommation, sans batterie. Aujourd'hui ça aura produit **6,7 kWh** et couvert **32 % de ma conso**. À l'échelle d'un labo perso, c'est modeste — la valeur n'est pas dans les watts produits, elle est dans le pilotage. Sans batterie, le seul moyen de valoriser le surplus midi, c'est de **consommer quand l'énergie est gratuite**. Le déshumidificateur de la chambre sous-sol s'allume quand l'Ecojoko mesure 0 W de soutirage réseau pendant 15 minutes — entre 10h et 17h, fenêtre où le surplus est probable. Charge utile, pas charge subie.

Même grammaire un cran plus loin, dans le garage : la prise de la trottinette et celle du chargeur d'outils s'allument quand le solaire couvre la conso (production > 300 W, soutirage < 100 W, stabilisé sur 10 min) et se coupent dès qu'un autre poste tire dessus (> 500 W net pendant 15 min) ou à 17h pile. Piloté par un agent Python dédié, avec hystérésis sur les seuils et mémoire d'état pour ne pas yo-yo — pas une auto isolée.

<figure class="blog-illustration">
  <img src="/blog/illustrations/boucle-anticipative.svg" alt="Schéma de principe : capteurs (lux, températures, UV, couverture nuageuse, conso, production solaire) alimentent une décision anticipative qui pilote des actions (fermer/ouvrir un volet, brancher/couper une prise), avec une boucle de feedback hystérésis + mémoire d'état, et des filets de sécurité (reset matinal 7h, fin de plage 17h, seuils critiques)." />
</figure>

Et puis il y a le **talon de consommation** — ce que la maison consomme en continu, juste pour exister. Vu en percentile 5 sur 4h glissantes, sur 7 jours, avec son coût annuel à côté. C'est la chose la plus banale et la plus invisible : une box qui chauffe, une recharge oubliée, un onduleur passé en mode lui-même. Pas spectaculaire. Mais c'est lui qui paie ton abonnement quand tu n'es pas là.

Tout ça, c'est ma sandbox. Une vraie maison, des capteurs qui font du bruit, des moteurs RTS qui résistent, des humains qui ouvrent une fenêtre au mauvais moment. **Le vrai luxe d'une sandbox, c'est de pouvoir se planter.** J'ai laissé un seuil de lux à 30 000 sur un capteur qui sature à 14 444 pendant des semaines. Personne ne m'a facturé l'erreur ; je l'ai regardée tomber d'elle-même quand j'ai sorti la courbe.

Mais c'est précisément là que ça commence à devenir un **marché**. Une fois la mécanique rodée à la maison, elle se projette à peu près partout — et à l'échelle où ça compte. **Une borne de recharge (IRVE) qui choisit son heure** au lieu d'attendre qu'on la branche : pricing, retour client, partenariat distributeur. **Des dispositifs de pilotage** — compteurs connectés, thermostats, supervision de conso — qui font de l'**autoconsommation collective** et de l'**effacement** à l'échelle d'un voisinage. **Un déploiement smart grid local** — compteurs intelligents, réseaux basse tension, branchements — qui industrialise la coordination entre quartiers producteurs et quartiers soutireurs. **Du photovoltaïque** où la valeur n'est plus dans le module installé mais dans son intégration au pilotage. Les briques sont les mêmes : lire en pente, anticiper l'offre, piloter la demande.

À la maison, l'enjeu c'est trois degrés au salon et 1 600 W de PV qui décident où aller. À l'échelle d'un réseau, c'est le pricing de l'heure suivante, l'arbitrage entre un quartier qui produit et un quartier qui soutire, des marges que l'énergie n'a pas encore comprimées. Entre les deux, c'est la même grammaire — et, ce qu'on saisit moins à première vue, **les mêmes logiques industrielles que les télécoms** : déployer, exploiter, maintenir, superviser. La différence avec la fibre, c'est qu'ici les marges ne sont pas encore comprimées. Il manque juste l'échelle — et un labo isolé ne répond pas à ça : c'est un marché qui se construit.

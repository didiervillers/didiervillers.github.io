Créer un site statique avec Pelican
###################################

:date: 2018-08-02 21:30
:category: TIC
:tags: pelican
:slug: 2018-08-02-creer-un-site-statique-avec-pelican

Au début du web, les sites personnels étaient directement écrits en html. Les "blogs" sont rapidement apparus à la fin du siècle dernier, et ensuite, des logiciels spécialisés ont été créés pour faciliter l'écriture des articles et leur hébergement sur un serveur. À l'heure actuelle, un blog est le plus souvent un site web dynamique géré entièrement par l'utilisateur, ou simplement hébergé sur une plateforme de blog (Blogger/Blogspot, WordPress.com, Skyblog, Overblog...). La première solution exige l'utilisation d'un serveur mutualisé ou hébergé, avec une base de données. Un coût y est associé et il faut s'assurer régulièrement des mises à jour et de la sécurité. Dans le second cas, le service est proposé par une société, qui se rémunère par de la publicité et/ou l'exploitation de données personnelles de l'auteur ou des lecteurs.

Les sites web dynamiques permettent des fonctionnalités sophistiquées, et lorsqu'une page est demandée, le contenu correpondant est extrait de la base de données afin de générer une page html corespondante. Dans le cas d'un blog "classique", ces logiciels (comme Wordpress qui est le plus utilisé) sont largement surdimensionnés par rapport aux besoins habituels d'un blogueur.

Un générateur de site statique va au contraire préparer exhaustivement toutes les pages html sur base de fichiers sources n'étant pas nécessairement sur le serveur : fichiers de configuration, et fichiers de description des pages dans des formats simplifiés. Les fichiers de sortie sont transférés sur le serveur web, et actualisés à l'occasion de l'écriture de nouveaux éléments. Ce mode de fonctionnement est beaucoup plus simple et sûr par rapport à un serveur dynamique. L'absence de mise à jour ne constitue par exemple pas un risque en matière de sécurité. Le serveur est fort peu exigeant en ressources matérielles, la sauvegarde et la migration sont très simples.

Plusieurs générateurs statiques existent, comme `Hugo <https://gohugo.io/>`_, `Jekyll <https://jekyllrb.com/>`_ et `Pelican <https://blog.getpelican.com/>`_. J'ai choisi ce dernier, écrit en Python, et permettant l'écriture en `markdown <https://daringfireball.net/projects/markdown/>`_ ou `reStructuredText <https://fr.wikipedia.org/wiki/ReStructuredText>`_.

.. contents:: Table des matières

Prérequis
=========
- gestionnaire de version Git
- outils Python et Anaconda
- espace GitHub (ou solution analogue)

`Git <https://fr.wikipedia.org/wiki/Git>`_ est un logiciel de gestion de versions décentralisé, permettant de stocker un ensemble de fichiers en conservant l'historique de toutes les modifications effectuées. Il est particulièrement indiqué pour des données textuelles telles que les fichiers sources décrivant des pages web. Il n'est pas adapté pour la gestion de fichiers binaires : documents de suites bureautiques, sorties PDF, media (images, sons, vidéos notamment), etc. Un dépot local peut être synchronisé sur un serveur distant, qui permettra pour notre usage d'assurer à la fois la sauvegarde et le partage des sources du site web, mais également sa publication. L'usage de Git pourra se limiter aux commandes principales comme init, add, commit, push dont la description est faite dans de nombreux tutoriels.

Pelican est écrit en Python, et utilise quelques librairies spécifiques. Il est recommandé d'utiliser une distribution, la plus répandue étant `Anaconda <https://www.anaconda.com/>`_, qui fonctionne aussi bien sous Windows, Mac OS X et GNU/Linux. Anaconda permet la gestion d'environnements virtuels qui assurent l'homogénéité et la compatibilité des paquets logiciels utilisés.

Différentes solutions existent pour l'hébergement du site, la plus simple étant d'utiliser la plateforme `GitHub <https://github.com/>`_, gratuite pour des dépôts publics. La création d'un compte est immédiate.


Installation
============
- Installer pelican
- créer ses premières pages
- prévisualisation du site
- publication via GitHub


Thème
=====
Galeries, exemple de pelican-bootstrap3


Configuration
=============
- pelicanconf.py et publishconf.py
- réseaux sociaux
- licence
- ...

Plugins
=======
Math, Jupyter,...

Hébergement sur GitHub
======================
Détails...

Références
==========

#. `Making a Static Blog with Pelican <http://nafiulis.me/making-a-static-blog-with-pelican.html>`_;
#. `reStructuredText quickref <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_;
#. `Pelican Documentation <https://media.readthedocs.org/pdf/pelican/stable/pelican.pdf>` ;
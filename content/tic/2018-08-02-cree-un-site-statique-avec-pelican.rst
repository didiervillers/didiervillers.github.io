Créer un site statique avec Pelican
###################################

:date: 2018-08-02 21:30
:category: TIC
:tags: pelican
:slug: 2018-08-02-cree-un-site-statique-avec-pelican

Au début du web, zut, les sites personnels étaient directement écrits en html. Les "blogs" sont apparus à la fin du siècle dernier, et très rapidement, des logiciels spécialisés ont été créés pour faciliter l'écriture des articles et leur hébergement sur un serveur. À l'heure actuelle, un blog est le plus souvent un site web dynamique géré entièrement par l'utilisateur, ou simplement hébergé sur une plateforme de blog (Blogger/Blogspot, WordPress.com, Skyblog, Overblog...). La première solution exige l'utilisation d'un serveur mutualisé ou hébergé, avec une base de données. Il y a un coût et il faut s'assurer régulièrement des mises à jour et de la sécurité. Dans le second cas, le service est proposé par une société, qui se rémunère par de la publicité et/ou l'exploitation de données personnelles de l'auteur ou des lecteurs.

Les sites web dynamiques permettent des fonctionnalités sophistiquées, et lorsqu'une page est demandée, le contenu correpondant est extrit de la base de donnée afin de générer une page html corespondante. Dans le cas d'un blog "classique", ces logiciels (comme Wordpress qui est le plus utilisé) sont largement surdimensionnés.

Un générateur de site statique va au contraire préparer exhaustivement toutes les pages html sur base de fichiers sources n'étant pas nécessairement sur le serveur : fichiers de configuration, et fichiers de description des pages dans des formats de description simplifiés. Les fichiers de sortie sont alors transférés sur le serveur web. Celui-ci est beaucoup plus simple et sûr par rapport à un serveur dynamique. L'absence de mise à jour ne constitue par exemple pas un risque en matière de sécurité. Le serveur est fort peu exigeant en ressources matérielles, la sauvegarde et la migration sont très simples.

Plusieurs générateurs existent, comme Hugo, Jekyll et `pelican <https://blog.getpelican.com/>`_. J'ai choisi ce dernier, écrit en Python, et permettant l'écriture en markdown ou `reStructuredText <https://fr.wikipedia.org/wiki/ReStructuredText>`_.

.. contents:: Table des matières

Prérequis
=========
- gestionnaire de version Git
- outils Python et Anaconda
- espace GitHub (ou solution analogue)

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

Références :
============

#. `Making a Static Blog with Pelican <http://nafiulis.me/making-a-static-blog-with-pelican.html>`_;
#. `reStructuredText quickref <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_;
#. `Pelican Documentation <https://media.readthedocs.org/pdf/pelican/stable/pelican.pdf>` ;
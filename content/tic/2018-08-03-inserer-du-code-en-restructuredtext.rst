Insérer du code en reStructuredText
###################################

:date: 2018-08-03 10:30
:category: TIC
:tags: pelican, code
:slug: 2018-08-03-inserer-du-code-en-restructuredtext

Voici le code source en reStructuredText (RST) permettant de générer la présentation d'un code python :

.. code-block:: RST

    .. code-block:: py⁣thon

        #! /usr/bin/env python
        # -*- coding: utf-8 -*-
        """
        Calcul de la factorielle d'un nombre
        Référence : http://fr.wikipedia.org/wiki/Factorielle
        """
        def factorielle(arg_n):
            """
            structure de répétition pour appliquer la définition de la factorielle
            """
            reponse = 1               # la réponse sera dans la variable reponse
            i = 1                     # on va commencer par 1
            while i <= arg_n:         # répétition "while" avec une condition à préciser
                reponse = reponse * i #actualisation de reponse
                i = i + 1             #incrémenter i
            return reponse
         
        # on demande le nombre :
        print("Calcul de la factorielle de n")
        chainelue=input("Que vaut n ? ")
        n = int(chainelue)
        print(n)
         
        # on affiche la réponse
        print("La factorielle vaut ",factorielle(n))

Le code Python apparaît alors comme ceci :

.. code-block:: python

    #! /usr/bin/env python
    # -*- coding: utf-8 -*-
    """
    Calcul de la factorielle d'un nombre
    Référence : http://fr.wikipedia.org/wiki/Factorielle
    """
    def factorielle(arg_n):
        """
        structure de répétition pour appliquer la définition de la factorielle
        """
        reponse = 1               # la réponse sera dans la variable reponse
        i = 1                     # on va commencer par 1
        while i <= arg_n:         # répétition "while" avec une condition à préciser
            reponse = reponse * i #actualisation de reponse
            i = i + 1             #incrémenter i
        return reponse
     
    # on demande le nombre :
    print("Calcul de la factorielle de n")
    chainelue=input("Que vaut n ? ")
    n = int(chainelue)
    print(n)
     
    # on affiche la réponse
    print("La factorielle vaut ",factorielle(n))

La coloration syntaxique est effectuée par `Pygments <http://pygments.org/>`_, et peut s'adapter à différents langages : Ruby, Python, Java, C, C++, CSS, HTML,...

N.B. : pour l'affichage du code sans coloration dans la présentation du code RST, j'ai introduit un `Unicode Character 'INVISIBLE SEPARATOR' (U+2063) <https://www.fileformat.info/info/unicode/char/2063/index.htm>`_ entre "py" et "thon" !!



Références
==========

#. `Restructured Text (reST) and Sphinx CheatSheet <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_;
#. `reStructuredText Primer <http://www.sphinx-doc.org/en/stable/rest.html>`_;
#. `quickref <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_;
#. `cheat sheet <https://github.com/ralsina/rst-cheatsheet>`_;
#. `Pygments <http://pygments.org/>`_.




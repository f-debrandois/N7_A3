# Calcul différentiel et EDO

Cours de calcul différentiel et équations différentielles ordinaires pour la formation ModIA.

**Remarque préliminaire.** Voir la [documentation générale](https://gitlab.irit.fr/toc/etu-n7/documentation) pour récupérer le cours (clonage d'un projet Git), etc.

## Cours

Le cours se trouve sur un unique [Polycopié](https://gitlab.irit.fr/toc/etu-n7/calcul-differentiel-edo/-/raw/main/cours-cd-edo.pdf?ref_type=heads).

## TP

Nous allons utiliser le langage [Julia](https://julialang.org) pour les TPs. Nous allons créer un environnement spécifique à ce cours, pour cela suivez les étapes suivantes :

1. Installer Julia : télécharger la version courante sur la page [downloads](https://julialang.org/downloads/) de Julia et l'installer classiquement. Si vous êtes sous `linux`, décompressez l'archive, placez-la où vous voulez et ajouter dans le `PATH` le répertoire `bin` du dossier Julia où se trouve l'exécutable `julia`.

```
N'installez pas Julia via conda !
```

2. Exécutez les cellules du notebook [`tp/install.ipynb`](tp/install.ipynb) sous `VSCode`. Il vous faudra peut-être choisir le noyau Julia à l'ouverture du notebook pour pouvoir l'exécuter. Il y a trois cellules qui permettent :

    - d'activer le projet dans le répertoire courant ;
    - d'installer les packages dans le projet courant (cela créer deux fichiers `.toml`) -- environ 13 min ;
    - de charger les packages pour vérifier que cela fonctionne.



![Test](image.png)
# Fabrication de potions

Cette brillante idée n'était pas si lumineuse qu'il n'y paraît : contre toute attente, les fantômes sont passés au travers du drap ! 😱 Et vous êtes maintenant repérés. S'ensuit alors une traque effrénée dans les couloirs obscurs du manoir à la suite de laquelle vous parvenez à vous barricader dans un laboratoire d'alchimie poussiéreux. Après une inspection méticuleuse des lieux, vous trouvez un vieux livre de recettes dont certaines pourraient bien vous sauver la vie dans ce manoir.

Chaque recette permet de faire une potion à partir de deux autres potions. Il y a dans le laboratoire une quantité illimitée de fioles de certaines potions. Combien de ces fioles allez-vous devoir utiliser pour faire la potion recherchée ?

## Données

### Entrée

**Ligne 1** : Le nom de la potion objectif, une chaîne de caractères sans espaces, de taille comprise entre 1 et 20.

**Ligne 2** : Le nombre `N` de potions disponibles en quantités illimitées.

**Ligne 3** : Les noms des `N` potions disponibles, séparées par des espaces, dans le même format que la potion objectif, `0 < N <= 100`.

**Ligne 4** : Le nombre `M` de recettes, `0 < M <= 1000`.

**Les `M` lignes suivantes** : Une recette par ligne, au format `A B C` où `A` est la potion fabriquée, et `B` et `C` les potions nécessaires à sa fabrication (qui sont donc utilisées une fois chacune pour faire une potion de `A`).

On précise qu'il n'y a pas de cycles dans les recettes, c'est-à-dire qu'une potion n'aura jamais besoin d'elle-même pour être fabriquée. Par exemple, si on a `C` à disposition, le livre ne peut pas contenir les recettes `A B C` et `B A C` car alors `A` a besoin de `B` et `B` a besoin de `A`.

### Sortie

Le nombre minimum de fioles de potions disponibles utilisées au total (celles dans la ligne 3), ou `impossible` si la potion objectif ne peut pas être fabriquée à partir des potions disponibles.

## Exemples

### Exemple 1

#### Entrée

```plaintext
A
2
C D
2
B C D
A B C
```

Il faut utiliser les potions `C` et `D` pour faire la `B` qui permet de faire la `A` en combinaison avec la `C`. On a donc utilisé 2 fois `C` et une fois `D`, d'où la réponse :

```plaintext
3
```

### Exemple 2

#### Entrée

```plaintext
I
6
L M N O P Q
4
I J K
J L M
K N O
O P Q
```

#### Sortie

```plaintext
4
```

A noter ici : la potion `O` peut être faite à partir des potions `P` et `Q`, mais elle fait également partie des potions disponibles. Il n'est donc pas nécessaire de la créer, et le nombre attendu est 4.

### Exemple 3

#### Entrée

```plaintext
levitation
1
elixir_bleu
1
levitation elixir_bleu huile_de_licorne
```

#### Sortie

```plaintext
impossible
```

L'`huile_de_licorne` est nécessaire à la potion de `levitation`, mais n'est pas disponible, c'est donc impossible.
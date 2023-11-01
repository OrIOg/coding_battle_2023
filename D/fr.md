![Test](image.png)
# Jeu de mots

Fort de vos nouveaux pouvoirs acquis avec les potions, vous poursuivez votre exploration de cette sinistre bâtisse. L'exploration est beaucoup plus simple quand on peut voir dans le noir !

Au détour d'une salle, la porte se referme derrière vous. Vous vous retrouvez nez à nez avec une voyante au sourire machiavélique, qui ne vous laissera partir en vie que si vous gagnez contre elle à un jeu.

C'est un jeu à deux joueurs : chacun son tour, les joueurs doivent ajouter une lettre à la fin d'un début de mot. Le premier qui ne peut plus ajouter de lettre a perdu. On ne peut rajouter une lettre que si la chaîne de caractère formée est le début d'un mot autorisé. Les mots autorisés sont donnés au début.

Vous et la voyante jouez à ce jeu **de manière optimale**, c'est-à-dire que chacun son tour, vous choisissez toujours de jouer les lettres qui vous permettront de gagner à coup sûr, s'il existe de telles lettres. C'est à vous de commencer, quelles lettres vous assurent la victoire ?

## Données

### Entrée

**Ligne 1** : un nombre `N`, le nombre de mots, avec `0 < N <= 10^5`.

**Les `N` lignes suivantes** : un mot par ligne, les mots autorisés, de taille comprise entre 1 et 25 caractères.

## Sortie

La liste des premières lettres qui vous permet de gagner à coup sûr, une lettre par ligne, dans l'ordre alphabétique. Si vous ne pouvez pas gagner, affichez `impossible`.

## Exemples

### Exemple 1

#### Entrée

```plaintext
4
ce
tri
bar
banc
```

Si vous commencez par `c`, la voyante ajoute `e` et vous ne pouvez rien ajouter, vous avez donc perdu. En commençant avec `t`, c'est vous qui gagnerez en prononçant la dernière lettre. Si vous commencez par `b`, elle ne peut ajouter que `a`, puis vous pouvez ajouter `r` et le bloquer. Pour gagner, il faut donc commencer par `b` ou `t`, d'où la réponse (par ordre alphabétique) :

#### Sortie

```plaintext
b
t
```

### Exemple 2

#### Entrée

```plaintext
2
je
tu
```

#### Sortie

```plaintext
impossible
```
![Test](image.png)
# Play on words

Strong of the new powers you've acquired with your potions, you continue your exploration of this sinister building. Exploring is much easier when you can see in the dark!

At the end of a room, the door closes behind you. You find yourself face to face with a clairvoyant with a mischievous smile. She will only let you leave alive if you win a game against her.

It's a two-player game: players take turns adding a letter to the end of a word. The first player who can no longer add a letter loses. A letter can only be added if the string formed is the beginning of an authorized word. Authorized words are given at the beginning.

You and the clairvoyant play the game **optimally**, i.e. you only play the letters that guarantee the victory, if they exist. You start the game, which letters guarantee you the victory?

## Data

### Input

**Line 1**: a number `N`, the number of words, with `0 < N <= 10^5`.

**The `N` following lines**: one word per line, the words allowed, between 1 and 25 characters long.

## Output

The list of the first letters that will let you win for sure, one letter per line, in alphabetical order. If you can't win, display `impossible`.

## Examples

### Example 1

#### Input

```plaintext
4
ce
tri
bar
banc
```

If you start with `c`, the clairvoyant adds `e` and you can't add anything, so you've lost. If you start with `t`, you will win by pronouncing the last letter. If you start with `b`, she can only add `a`, then you can add `r` and block it. So to win, you have to start with `b` or `t`, hence the answer (in alphabetical order):

#### Output

```plaintext
b
t
```

### Example 2

#### Input

```plaintext
2
je
tu
```

#### Output

```plaintext
impossible
```
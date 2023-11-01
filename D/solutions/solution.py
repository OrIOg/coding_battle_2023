#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import string

LOG = True

log = lambda x: sys.stderr.write(f"{x}\n") if LOG else None

# ------------------- Parsing ------------------- #

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

allowed_words = lines[1:]

# ------------------- Solving ------------------- #

# Building tree
tree = {} 

for word in allowed_words:
    node = tree
    for letter in word:
        if letter not in node:
            node[letter] = {}
        node = node[letter]

def minimax(states, player_1=False, depth=1):
    if not states:
        return depth % 2 != 0

    if player_1:
        return max([
            minimax(new_state, player_1=False, depth=depth+1)
            for new_state in states.values()
        ])
    else:
        return min([
            minimax(new_state, player_1=True, depth=depth+1)
            for new_state in states.values()
        ])

winning_letters = []
for start_letter, states in tree.items():
    result = minimax(states)
    if result:
        winning_letters.append(start_letter)

# ------------------- Submission ------------------- #

answers = sorted(winning_letters)

if len(answers) == 0:
    print("impossible")
else:
    for answer in answers:
        print(answer)
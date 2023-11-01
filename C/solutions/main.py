#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

LOG = False

log = lambda x: sys.stderr.write(f"{x}\n") if LOG else None

# ------------------- Parsing ------------------- #

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

potion_objectif = lines[0]

_nb_unlimited_potions = int(lines[1])
unlimited_potions = {potion for potion in lines[2].split()}

nb_recipes = int(lines[3])

recipes = {}

for recipe_line in lines[4:4+nb_recipes]:
  crafted, *ingredients = recipe_line.split()
  recipes[crafted] = ingredients

log(f"{potion_objectif=}")
log(f"{unlimited_potions=}")
log(f"{recipes=}")

# ------------------- Solving ------------------- #

memory = {potion: 1 for potion in unlimited_potions}
cost = 0
stack = [potion_objectif]

while stack:
  potion_needed = stack.pop()

  if potion_needed in memory:
    cost += memory[potion_needed]
  elif potion_needed in recipes.keys():
    stack.extend(recipes[potion_needed])
  else:
    cost = "impossible"
    break

answer = cost

print(answer)
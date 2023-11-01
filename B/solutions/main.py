#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

min_x, min_y = 1000, 1000
max_x, max_y = 0, 0

for ghost in lines[1:]:
  x, y = [int(pos) for pos in ghost.split()]

  if x > max_x:
    max_x = x
  if x < min_x:
    min_x = x

  if y > max_y:
    max_y = y
  if y < min_y:
    min_y = y

max_side = max(max_x-min_x, max_y-min_y) + 1
answer = max_side * max_side

print(answer)
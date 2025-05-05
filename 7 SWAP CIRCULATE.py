a, b = 1, 2
a, b = b, a
print("Swapped:", a, b)
a, b, c = 1, 2, 3
a, b, c = c, a, b
print("Circulated:", a, b, c)
import math
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", distance)

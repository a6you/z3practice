from z3 import *

# Declare int variables within the puzzle
a, b, c = Ints('a b c') 

# Declare z3 solver
s = Solver()

# Specify horizontal equations
s.add((10 * a + a) * (10 * a + a) == (100 * a + 10 * b + a)) # aa * aa = aba
s.add((10 * a + b) - a == (10 * a + a)) # ab - a = aa
s.add((100 * a + 10 * c + b) / (10 * a + b) == (10 * a + a)) # acb / ab = aa

# Specify vertical equations
s.add((10 * a + a) * (10 * a + b) == (100 * a + 10 * c + b)) # aa * ab = acb
s.add((10 * a + a) + a == (10 * a + b)) # aa + a = ab
s.add((100 * a + 10 * b + a) / (10 * a + a) == (10 * a + a)) # aba / aa = aa

# Generate a solution
if s.check() == sat:
    m = s.model()
    for d in m.decls():
        print("%s = %s" % (d.name(), m[d]))

# In this case, a solution is
# a = 1, b = 2, c = 3
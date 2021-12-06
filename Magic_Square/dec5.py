from z3 import *

# Declare int variables representing blank squares in the
# initial state of the magic square
# a b c: Top row
# d e f: Middle row
# g: Bottom row
a, b, c, d, e, f, g = Ints('a b c d e f g')

# Declare int variable for the value for the Magic Sum
x = Int('x')

# Declare z3 solver
s = Solver()


# Add row equations as constraints
s.add(a + b + c == x)
s.add(d + e + f == x)
s.add(g + (-264) + 51 == x)

# Add column equations as constraints
s.add(a + d + g == x)
s.add(b + e + (-264) == x)
s.add(c + f + 51 == x)

# Add diagonal equations as constraints
s.add(a + e + 51 == x)
s.add(c + e + g == x)

# Generate a solution
if s.check() == sat:
    m = s.model()
    for d in m.decls():
        print("%s = $s", (d.name(), m[d]))

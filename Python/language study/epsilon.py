import math, sys

x = 0.1 + 0.2
print(math.fabs(x - 0.3) <= sys.float_info.epsilon)
print(math.isclose(0.1 + 0.2, 0.3))

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.2'))

from fractions import Fraction

print(Fraction('10/3'))
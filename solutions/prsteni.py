N = int(input())
rings = [int(ea) for ea in input().split(' ')]

from fractions import Fraction

for r in rings[1:]:
    f = Fraction(rings[0], r)
    print(f'{f.numerator}/{f.denominator}')
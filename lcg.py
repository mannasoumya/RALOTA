import time
import traceback
import sys
#  Linear congruential generators
# f(X) = aX + c mod m


def usage():
    print(
        f'Usage: python {sys.argv[0]} <lower-limit> <upper-limit>')
    sys.exit(1)


if len(sys.argv) == 1:
    usage()
try:
    m1 = int(sys.argv[1])
    m2 = int(sys.argv[2])
    # n = int(sys.argv[3])
    if m2 < m1:
        raise Exception("LimitsMismatch")
except ValueError:
    usage()
except Exception as e:
    print(e)
    print(traceback.format_exc())
    usage()


def lcg_gx(a, x, c, m=(2**31-1), gx=False):
    val = ((a*x+c) % m)
    if gx:
        return val/m
    return val


A = 16807
c = 0
t = time.time()
x = int(str(t-int(t)).replace(".", ""))
# m = m2-m1+1
m = 2147483647
# if m == 1:
#     print(m1)
# else:
#     print(lcg_gx(A, x, c, m))
ran = lcg_gx(A, x, c, m, True)
if m2-m1 == 0:
    print(m1)
else:
    print(int(m1 + (m2 - m1 + 1) * ran))

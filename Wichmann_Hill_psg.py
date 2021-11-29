# [r, s1, s2, s3] = function(s1, s2, s3) is
#    // s1, s2, s3 should be random from 1 to 30,000. Use clock if available.
#    s1 := mod(171 × s1, 30269)
#    s2 := mod(172 × s2, 30307)
#    s3 := mod(170 × s3, 30323)
#
#    r := mod(s1/30269.0 + s2/30307.0 + s3/30323.0, 1)
# period : 7^12

import time
import sys
import traceback
m1 = None
m2 = None
n = None


def usage():
    print(
        f'Usage: python {sys.argv[0]} <lower-limit> <upper-limit> <how-many>')
    sys.exit(1)


def validate_args():
    if len(sys.argv) < 4:
        usage()
    global m1, m2, n
    try:
        m1 = int(sys.argv[1])
        m2 = int(sys.argv[2])
        n = int(sys.argv[3])
        if m2 < m1:
            raise Exception("LimitsMismatch")
    except ValueError:
        usage()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        usage()


def generate_wh_rng(s1, s2, s3):
    s_1 = (171 * s1) % 30269
    s_2 = (172 * s2) % 30307
    s_3 = (170 * s3) % 30323
    r = (s1/30269.0 + s2/30307.0 + s3/30323.0) % 1
    return s_1, s_2, s_3, r


def squeeze_range(m1, m2, r, float_mode=False):
    assert (m1 <= m2)
    assert (r >= 0 and r <= 1)
    val = m1 + (m2-m1+1)*r
    if float_mode:
        return val
    return int(val)


if __name__ == "__main__":
    validate_args()
    t = time.perf_counter()
    s1_0 = int(str(t-int(t)).replace(".", ""))
    t = time.perf_counter()
    s2_0 = int(str(t-int(t)).replace(".", ""))
    t = time.perf_counter()
    s3_0 = int(str(t-int(t)).replace(".", ""))
    s1_1, s2_1, s3_1, r = generate_wh_rng(s1_0, s2_0, s3_0)
    print(squeeze_range(m1, m2, r))
    for i in range(1, n):
        s1_1, s2_1, s3_1, r = generate_wh_rng(s1_1, s2_1, s3_1)
        print(squeeze_range(m1, m2, r))

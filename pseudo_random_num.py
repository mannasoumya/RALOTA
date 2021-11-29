import time
import os
import sys
import traceback
from Wichmann_Hill_psg import generate_wh_rng

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
        if m2-m1+1 < n:
            raise Exception("LimitsMismatch")
    except ValueError:
        usage()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        usage()


def squeeze_range(m1, m2, r, float_mode=False):
    assert (m1 <= m2)
    assert (r >= 0 and r <= 1)
    val = m1 + (m2-m1+1)*r
    if float_mode:
        return val
    return int(val)


def check_or_set_initial_seed():
    s1_0 = None
    s2_0 = None
    s3_0 = None
    if os.path.exists("seed.val"):
        with open("seed.val", "r") as f:
            content = f.read()
        s1_0, s2_0, s3_0 = (int(x) for x in content.split(","))
    else:
        t = time.perf_counter()
        s1_0 = int(str(t-int(t)).replace(".", ""))
        t = time.perf_counter()
        s2_0 = int(str(t-int(t)).replace(".", ""))
        t = time.perf_counter()
        s3_0 = int(str(t-int(t)).replace(".", ""))
        write_new_seed(f"{s1_0},{s2_0},{s3_0}")

    return s1_0, s2_0, s3_0


def write_new_seed(s1, s2, s3, file_path="seed.val"):
    with open(file_path, "w") as f:
        f.write(f"{s1},{s2},{s3}")


def generate_pseudo_random(m1, m2, n):
    dct = {}
    count = 0
    while count < n:
        s1_0, s2_0, s3_0 = check_or_set_initial_seed()
        s1, s2, s3, r = generate_wh_rng(s1_0, s2_0, s3_0)
        write_new_seed(s1, s2, s3)
        num = squeeze_range(m1, m2, r)
        if num not in dct:
            dct[num] = None
            count = count + 1
    return [x for x in dct.keys()]


if __name__ == "__main__":
    validate_args()
    for k in generate_pseudo_random(m1,m2,n):
        print(k)

import std/os
from strutils import parseInt

var n            : uint64
var program_name : string = getAppFilename()
var r_seed       : uint64 = 12345678
const m          : uint64 = 2147483647
const a          : uint64 = 48271
const q          : uint64 = 44488
const r          : uint64 = 3399
 
proc usage(): void =
    echo "\nUsage: '", program_name, "' <how-many>\n"

proc generate(): float64 =
    var hi,lo,t,maxpossible :uint64
    hi = r_seed div q
    lo = r_seed - q * hi
    t  = a * lo - r * hi
    if t > 0:
        r_seed = t
    else:
        r_seed = t + m
    
    maxpossible = high(uint64)
    result      = float64(r_seed) / float64(maxpossible)

proc validate_args(): void =
    try:
        assert (paramCount() == 1)
    except:
        usage()
        quit(1)
    try:
        n  = uint64(parseInt(paramStr(1)))
    except:
        var err = getCurrentException()
        echo "ERROR: ", err.msg
        quit(1)

proc main(): void =
    validate_args()
    var i: uint64 = 0
    while i <= n:
        var r = generate()
        echo r
        inc i

main()
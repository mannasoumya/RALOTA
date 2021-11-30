# xn = a11xn_1 + a12xn_2 + a13xn_3 (mod m1) 
# Yn = a21Yn-i + a22Yn-2 + a23 (mod m2) 
# zn = xn - Yn (mod m1) 
# un = zn/m1 
# Period : 2^191

import Dates

a11 = 0 
a12 = 1403580 
a13 = -810728 
m1  = 2^32 - 209 
a21 = 527612
a22 = 0
a23 = -1370589
m2  = 2^32 - 22853 

function usage()
    println("Usage: julia " * PROGRAM_FILE * " <lower-limit> <upper-limit> <how-many>")
    exit(1)
end

macro assert(ex, msgs...)
    msg_body = isempty(msgs) ? ex : msgs[1]
    msg      = string(msg_body)
    return :($ex ? nothing : throw(AssertionError($msg)))
end

function validate_args()
    ll = nothing
    ul = nothing
    n  = nothing
    try
        ll = parse(Int64,ARGS[1])
        ul = parse(Int64,ARGS[2])
        n  = parse(Int64,ARGS[3])
        if n > ul-ll+1
            error("LimitsMismatch")
        end
        if ll > ul 
            error("LimitsMismatch")
        end
    catch e
        println(e)
        exit(1)
    end
    return (ll,ul,n)
end

ticks() = (return convert(UInt64,Dates.datetime2unix(Dates.unix2datetime(time()))*1000);)


function generate_initial_xs()
    x1 = 2096367628361 + Int(ticks())
    x2 = 1638267496885 + Int(ticks())
    x3 = 6377396958484 + Int(ticks())
    y1 = 9542607296802 + Int(ticks())
    y2 = 7716177293560 + Int(ticks())
    return (x1,x2,x3,y1,y2)
end

function generate_next(xn_1,xn_2,xn_3,Yn_1,Yn_2,m1,m2)
    xn = mod(a11 * xn_1 + a12 * xn_2 + a13 * xn_3, m1) 
    Yn = mod(a21 * Yn_1 + a22 * Yn_2 + a23, m2) 
    zn = mod(xn - Yn, m1) 
    un = zn/m1
    return (xn,Yn,un)
end

function squeeze_range(ll,ul,r,float_mode)
    val = ll + (ul - ll + 1) * r
    if float_mode
        return val
    end
    return trunc(Int,val)
end

function main()
    try
        @assert(length(ARGS) == 3 , "")
    catch 
        usage()
    end
    ll, ul, n          = validate_args()
    x0, x1, x2, y1, y2 = generate_initial_xs()
    i = 0
    d = Dict()
    while i<n
        xn,Yn,r = generate_next(x0,x1,x2,y1,y2,m1,m2)
        ran_num = squeeze_range(ll,ul,r,false)
        x0 = x1
        x1 = x2
        x2 = xn
        y1 = y2
        y2 = Yn
        if !(string(ran_num) in keys(d))
            println(ran_num)
            d[string(ran_num)] = nothing
            i=i+1
        end
    end
end 

main()
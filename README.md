# RALOTA : Repository about Random Number Generator Algorithms
###### this name has nothing to do with the algorithms (actually it is also randomly generated through a code)

## Quick Start
```console
$ python pseudo_random_num.py  # This is using WichMann_Hill
Usage: python .\pseudo_random_num.py <lower-limit> <upper-limit> <how-many>
$ python pseudo_random_num.py 10 100 5
19
31
40
18
12
```
```console
$ julia .\MRG32k3a.jl
Usage: julia .\MRG32k3a.jl <lower-limit> <upper-limit> <how-many>
$ julia .\MRG32k3a.jl 10 100 5
50
34
40
78
14
```
## References
- https://www.math.arizona.edu/~tgk/mc/book_chap3.pdf
- https://en.wikipedia.org/wiki/Random_number_generation
- https://en.wikipedia.org/wiki/Wichmann%E2%80%93Hill
- https://en.wikipedia.org/wiki/Linear_congruential_generator
- https://spec.oneapi.io/versions/latest/elements/oneMKL/source/domains/rng/mkl-rng-mrg32k3a.html

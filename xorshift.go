package main

import (
	"fmt"
	"os"
	"strconv"
)

var initial_seed = 88172645463325252
var xorshift64_state_var = xorshift64_state{a: uint64(initial_seed)}

const XORSHIFT128_STATE_CAPACITY = 4

type xorshift32_state struct {
	a uint32
}

type xorshift64_state struct {
	a uint64
}

type xorshift128_state struct {
	x [XORSHIFT128_STATE_CAPACITY]uint32
}

//The state word must be initialized to non-zero
func xorshift32(state *xorshift32_state) uint32 {
	// Algorithm "xor" from p. 4 of Marsaglia, "Xorshift RNGs"
	x := state.a
	x ^= (x << 13)
	x ^= (x >> 17)
	x ^= (x << 5)
	state.a = x
	return x
}
func xorshift64(state *xorshift64_state) uint64 {
	x := state.a
	x ^= (x << 13)
	x ^= (x >> 7)
	x ^= (x << 17)
	state.a = x
	return x
}

// The state array must be initialized to not be all zero
func xorshift128(state *xorshift128_state) uint32 {
	t := state.x[3]
	s := state.x[0] //Perform a contrived 32-bit shift.
	state.x[3] = state.x[2]
	state.x[2] = state.x[1]
	state.x[1] = s

	t ^= t << 11
	t ^= t >> 8
	tss := t ^ s ^ (s >> 19)
	state.x[0] = tss
	return tss
}

func squeeze_range_float(ll uint64, ul uint64, r float64) float64 {
	val := float64(ll) + float64((ul-ll+1))*r
	return val
}
func squeeze_range_int(ll int64, ul int64, r float64) int64 {
	val := float64(ll) + float64((ul-ll+1))*r
	return int64(val)
}

func generate_random_number() float64 {
	xorshift64(&xorshift64_state_var)
	ran := float64(xorshift64_state_var.a) / float64(1<<63)
	if ran > 1 {
		ran = ran - float64(int64(ran))
	}
	return ran
}

func generate(ll int64, ul int64, how_many int64) []int64 {
	i := 0
	var x = make([]int64, how_many)
	for i < int(how_many) {
		x[i] = squeeze_range_int(ll, ul, generate_random_number())
		i++
	}
	return x
}

func usage() {
	fmt.Printf("Usage: go run xorshift.go <lower-limit> <upper-limit> <how-many>\n")
}

func validate_args() (int64, int64, int64) {
	var temp = make([]int64, 3)
	for i := 1; i < len(os.Args); i++ {
		el, err := strconv.Atoi(string(os.Args[i]))
		if err != nil {
			fmt.Println(err)
			os.Exit(2)
		}
		temp[i-1] = int64(el)
	}

	if temp[2] > temp[1]-temp[0]+1 {
		usage()
		panic("LimitsMismatch")
	}
	if temp[0] > temp[1] {
		usage()
		panic("LimitsMismatch")
	}

	return temp[0], temp[1], temp[2]
}

func main() {
	if len(os.Args) < 4 {
		usage()
		os.Exit(1)
	}
	m1, m2, n := validate_args()
	res := generate(m1, m2, n)
	for i := 0; i < len(res); i++ {
		fmt.Println(res[i])
	}
}

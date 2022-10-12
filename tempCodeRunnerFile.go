package main

/*
Write a program that takes 2 complex numbers and the operation to be performed on
them as command line arguments, and prints the result as a complex number.
Commandline arguments to the program are in the following format
complexnum1 binaryop complexnum2
If one of the arguments is in complex form and the other is either in integer or float
form, assume its imaginary part is zero (0).
Note: Assume there is no embedded space in complex number argument.
*/

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"math/cmplx"
)

func main() {

	res_2 := cmplx.Conj(-1 + 12i)
	fmt.Printf("\nResult 2:  %f", res_2)
}
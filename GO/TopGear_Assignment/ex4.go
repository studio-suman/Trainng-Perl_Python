package main

/*
Implement the function num2hex() which takes an unsigned integer and returns its
hexa equivalent as a string. Function should take an extra argument which specifies
whether the hexa digits should be in lower case (default) or upper case.
Using the function num2hex() implement main which takes an integer value and prints
its hexa equivalent. If the number precedes with –u option, then the hexa value should
be printed in uppercase. Any other option other than –u should be considered invalid.
*/

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	var x string
	//print("Enter the Number: ")
	x = os.Args[1]
	switch {
	case strings.Contains(x, "-u"):
		y := os.Args[2]
		z := num2hex(y)
		if z == 0 {
			fmt.Printf("Invalid Number")
		} else {
			fmt.Printf("The Entered Number to Hex: %X", z)
		}
		break
	case strings.Contains(x, "-"):
		print("Invalid Option")
		break
	default:
		z := num2hex(x)
		if z == 0 {
			fmt.Printf("Invalid Number")
		} else {
			fmt.Printf("The Entered Number to Hex: %x", z)
		}
		break
	}

}

func num2hex(x string) int {

	y, e := strconv.Atoi(x)
	if e != nil {
		return 0
	}
	return y
}

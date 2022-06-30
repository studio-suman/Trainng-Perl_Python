package main

/*
Write a program that takes 2 complex numbers and the operation to be performed on
them as command line arguments, and prints the result as a complex number.
Commandline arguments to the program are in the following format
complexnum1 binaryop complexnum2
If one of the arguments is in complex form and the other is either in integer or float
form, assume its imaginary part is zero (0).
Note: Assume there is no embedded space in complex number argument.

Command Output expected
go run ex5.go 3-4i + 7+2i 10-2i
go run ex5.go -15i - 3-4i -3-11i
go run ex5.go 3-5i * 12 36-60i

*/

import (
	"fmt"
	"regexp"
	"strconv"
)

func main() {

	var z, x, l string
	print("Enter the complex nos serially :")
	print("\nEnter the 1st number: ")
	fmt.Scanln(&x)
	k := verify(x)
	res_1 := complex(str2float(k[0]), str2float(k[1]))
	print("Please enter the (+/-/*): ")
	fmt.Scanln(&z)
	print("Enter the 2nd number: ")
	fmt.Scanln(&l)
	g := verify(l)
	res_2 := complex(str2float(g[0]), str2float(g[1]))
	switch z {
	case "+":
		fmt.Printf("\nResult is:  %v", res_1+res_2)
		break
	case "-":
		fmt.Printf("\nResult is:  %v", res_1-res_2)
		break
	case "*":
		fmt.Printf("\nResult is:  %v", res_1*res_2)
		break
	}

}

func verify(x string) []string {

	var reg_final []string
	// Matches complex number with BOTH real AND imaginary parts.
	// Ex: -3-2.0i
	reg3 := regexp.MustCompile(`([-]?[0-9]+[0-9]?)+([-|+]+[0-9]?\.?[0-9])[i$]`)
	// Matches ONLY real number.
	// Ex: 3.145 or 3
	reg := regexp.MustCompile(`[-|+]?[0-9]?\.?[0-9]`)
	// Matches ONLY Imaginary number.
	// Ex: 3.145i or 3i
	reg2 := regexp.MustCompile(`([-|+]+[0-9]?\.?[0-9])`)

	found := reg3.MatchString(x)
	found2 := reg.MatchString(x)
	if found {
		reg_final := reg.FindAllString(x, len(x))
		return reg_final
	} else if found2 {
		reg_final = reg.FindAllString(x, len(x))
		reg_final = append(reg_final[:1], "0")
		return reg_final
	} else {
		reg_final = reg2.FindAllString(x, len(x))
		reg_final = append(reg_final[:1], "0")
		copy(reg_final[1:], reg_final[0:])
		reg_final[0] = "0"
		return reg_final
	}
}

func str2float(x string) float64 {

	i, err := strconv.Atoi(x)
	if err == nil {
		return float64(i)
	}
	return 0

}

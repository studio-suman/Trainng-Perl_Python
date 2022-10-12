package main

/*
Implement the function maxPower() that takes two parameters M and N and returns
the smallest integer K such that M <= N**k
maxPower (80000, 5) should return 8
maxPower (30000, 9) should return 5
*/

import (
	"fmt"
	"math"
)

func main() {
	fmt.Print("Enter the Number (x,y): ")
	var x, y float64
	fmt.Scanln(&x, &y)
	println("\nThe Lowest possible integer for power: ", maxPower(x, y))
}

func maxPower(M float64, N float64) int {

	var K int
	K = 0
	for M >= math.Pow(N, float64(K)) {
		//for M >= N**K {
		//fmt.Printf("\nValue / increrement: %v %v", math.Pow(N, float64(K)), K)
		K++
	}

	return K
}

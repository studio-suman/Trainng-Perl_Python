package main

/*
Implement the function num2words() which takes a number and returns the number in
words as a string.
For example, num2words(123) should return the string “one two three”.
*/

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	print("Enter the Number: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	x := scanner.Text()
	fmt.Printf("\nEntered number in words: (%v) ", x)
	num2words(x)
	//fmt.Printf("\nEntered number in words: (%v) ", y)
	//num2words(y)

}

func num2words(n string) string {

	conv := map[string]string{
		"1": "One",
		"2": "Two",
		"3": "Three",
		"4": "Four",
		"5": "Five",
		"6": "Six",
		"7": "Seven",
		"8": "Eight",
		"9": "Nine"}
	var z string
	z = "0"

	test := strings.Fields(n)
	for i := range test {
		str := strings.SplitAfter(test[i], "")
		for t := range str {
			z = conv[str[t]]
			print(z + " ")
		}
	}
	return z
}

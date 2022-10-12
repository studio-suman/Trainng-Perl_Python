package main

/*
Implement the function words2num() which takes a string and returns the number
represented by the string.
For example, words2num(“one two three”) should return 123.
Function argument can be in lowercase/uppercase/mixedcase.
Test correctness of the function in main(), which takes a string as commandline
arguments, calls words2num() & prints the returned value.
If any of the word does not represent a digit, program should print an error messages
indicating invalid input.
*/

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	print("Enter the Number in words: ")
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	x := scanner.Text()
	fmt.Printf("Entered number in words: %s", words2num(x))

}

func words2num(n string) []string {

	conv := map[string]string{
		"one":   "1",
		"two":   "2",
		"three": "3",
		"four":  "4",
		"five":  "5",
		"six":   "6",
		"seven": "7",
		"eight": "8",
		"nine":  "9",
		"zero":  "0"}

	var z []string
	null := ""
	test := strings.Fields(n)
	for i := range test {
		if conv[strings.ToLower(test[i])] != null {
			str := strings.SplitAfter(test[i], " ")
			for k := range str {
				z = append(z, conv[strings.ToLower(str[k])])
			}
		} else {
			z[0] = "Invalid Input"
			break
		}
	}
	return z
}

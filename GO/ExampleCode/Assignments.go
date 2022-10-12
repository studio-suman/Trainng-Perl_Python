package main

import (
	"fmt"
	"strconv"
)

// Define comment
/*
\nnn = Octal
\xnn = Hexadecimal

%T = Type of Variable
%v = Default value of Variable
%t = True or False
%b = Base(2)
%o = Base(8)
%d = Base(10)
%x = Base(16)
%c = Character
*/
func main() {
	/*
		var x int
		var y uint16 = 100
		var z = 423322343
		a:= 1
		b:= 2
		//fmt.Printf("%T %T %T %T %v %v %v %v", x, y,z,a, x, y,z,a)
		//fmt.Printf("The Value of b %c %v", b, b)
	*/
	x:="123"
    y, e := strconv.Atoi(x)
    if e == nil {
        fmt.Printf("%T \n %x", y, y)
}
}
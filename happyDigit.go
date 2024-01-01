package main

import (
	"fmt"
)

func main() {
	var n int
	_, _ = fmt.Scan(&n)
	sumDigits := 0
	originalN := n
	for n > 0 {
		sumDigits += n % 10
		n /= 10
	}
	if originalN%sumDigits == 0 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}

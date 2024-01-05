package main

import (
	"fmt"
)

func main() {
	var n int
	_, _ = fmt.Scan(&n)
	digitalRoot := calculateDigitalRoot(n)
	fmt.Println(digitalRoot)
}

func calculateDigitalRoot(n int) int {
	digitalRoot := 0
	for n > 0 {
		digitalRoot += n % 10
		n /= 10
	}
	if digitalRoot > 9 {
		digitalRoot = calculateDigitalRoot(digitalRoot)
	}
	return digitalRoot
}

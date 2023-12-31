package main

import (
	"fmt"
)

func main() {
	var n int
	_, _ = fmt.Scan(&n)
	power := 1
	for power <= n {
		fmt.Println(power)
		power *= 2
	}
}

package main

import (
	"fmt"
)

func main() {
	var num, number, count int

	for {
		_, _ = fmt.Scan(&num)
		if num == 0 {
			break
		}
		if number != 0 && number < num {
			count++
		}
		number = num
	}
	fmt.Println(count)
}

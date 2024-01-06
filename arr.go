package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	_, _ = fmt.Scan(&n)

	arr := make([]int, n)
	for i := 0; i < n; i++ {
		_, _ = fmt.Scan(&arr[i])
	}

	for i := 0; i < n-1; i += 2 {
		arr[i], arr[i+1] = arr[i+1], arr[i]
	}
	fmt.Println(strings.Trim(fmt.Sprint(arr), "[]"))
}

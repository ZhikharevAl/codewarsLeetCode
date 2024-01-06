package main

import (
	"fmt"
)

func main() {
	var n int
	_, _ = fmt.Scan(&n)
	arr := make([]int, n)
	for i := range arr {
		_, _ = fmt.Scan(&arr[i])
	}
	minIndex := 0
	maxIndex := 0
	for i := 1; i < n; i++ {
		if arr[i] < arr[minIndex] {
			minIndex = i
		}
		if arr[i] > arr[maxIndex] {
			maxIndex = i
		}
	}
	fmt.Println(maxIndex - minIndex)
}

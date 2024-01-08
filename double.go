package main

import "fmt"

func main() {
	var s string
	_, _ = fmt.Scan(&s)
	slice := make([]string, 0)
	for i := 0; i < len(s); i++ {
		slice = append(slice, string(s[i]))
		for j := 0; j < len(slice); j++ {
			if s[i] == s[j] && i != j {
				fmt.Print(string(s[i]))
				break
			}
		}
	}
}

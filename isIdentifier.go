package main

import (
	"fmt"
	"unicode"
)

func isIdentifier(str string) bool {
	firstRune := rune(str[0])
	if !(unicode.IsLetter(firstRune) && unicode.Is(unicode.Latin, firstRune) || 
		firstRune == '_') {
		return false
	}

	for _, r := range str[1:] {
		if !(unicode.IsLetter(r) && unicode.Is(unicode.Latin, r) ||
			unicode.IsDigit(r) || r == '_') {
			return false
		}
	}

	return true
}

func main() {
	var input string
	_, _ = fmt.Scan(&input)
	if isIdentifier(input) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}

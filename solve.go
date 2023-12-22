func solve(str string) string {
	upperCaseCount := 0
	for _, char := range str {
		if unicode.IsUpper(char) {
			upperCaseCount++
		}
	}

	if upperCaseCount > len(str)/2 {
		return strings.ToUpper(str)
	} else {
		return strings.ToLower(str)
	}
}

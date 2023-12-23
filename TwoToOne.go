func TwoToOne(s1 string, s2 string) string {
	word := ""
	s := s1 + s2
	for _, v := range s {
		if !strings.Contains(word, string(v)) {
			word += string(v)
		}
	}

	r := []rune(word)

	sort.Slice(r, func(i, j int) bool {
		return r[i] < r[j]
	})

	return string(r)
}

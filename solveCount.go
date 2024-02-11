

func Solve(s string) int {
	n, max := 0, 0
	for _, r := range s {
		switch r {
		case 'a', 'e', 'i', 'o', 'u':
			if n++; n > max {
				max = n
			}
		default:
			n = 0
		}
	}
	return max
}

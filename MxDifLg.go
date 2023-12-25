func MxDifLg(a1 []string, a2 []string) int {
	if len(a1) == 0 || len(a2) == 0 {
		return -1
	}

	maxDiff := -1

	for _, x := range a1 {
		for _, y := range a2 {
			diff := math.Abs(float64(len(x) - len(y)))
			if int(diff) > maxDiff {
				maxDiff = int(diff)
			}
		}
	}

	return maxDiff
}

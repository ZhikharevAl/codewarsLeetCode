func NbYear(p0 int, percent float64, aug int, p int) int {
	years := 0
	for i := 0; p0 < p; i++ {
		p0 += int(float64(p0)*percent/100) + aug
		years++
	}
	return years

}

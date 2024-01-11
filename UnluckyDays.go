func UnluckyDays(year int) int {
	counter := 0
	for month := 1; month <= 12; month++ {
		date := time.Date(year, time.Month(month), 13, 0, 0, 0, 0, time.UTC)
		if date.Weekday() == time.Friday {
			counter++
		}
	}
	return counter
}

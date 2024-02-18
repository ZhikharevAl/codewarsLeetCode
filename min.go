func main() {
	var data = [3][3]int{
		{5, 2, 3},
		{4, 5, 6},
		{7, -1, 9},
	}
	min := data[0][0]
	for _, row := range data {
		for _, value := range row {
			if value < min {
				min = value
			}
		}
	}
	fmt.Println(min)
}

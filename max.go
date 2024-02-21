func main() {
    data := ReadInput()
    max := data[0][0]
	for _, row := range data {
		for _, value := range row {
			if value > max {
				max = value
			}
		}
	}
    fmt.Println(max)
}

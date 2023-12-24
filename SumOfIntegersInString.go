func SumOfIntegersInString(strng string) int {

	re := regexp.MustCompile("[0-9]+")
	res := re.FindAllString(strng, -1)
	sum := 0
	for _, val := range res {
		num, _ := strconv.Atoi(val)
		sum += num
	}
	return sum
}

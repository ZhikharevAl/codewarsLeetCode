func Divisors(n int)int{
	count:=0
	for i:=1; i <= n; i++{
		if n%i == 0{
			count +=1
		}
	}
	return count
}

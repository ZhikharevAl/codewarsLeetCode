func removeDuplicates(tags []string) []string {
	list:=make([]string, 0, len(tags))
	for i := 0; i < len(tags); i++ {
		if i == 0 || tags[i] != tags[i-1] {
			list = append(list, tags[i])
		}
	}
	return list
}

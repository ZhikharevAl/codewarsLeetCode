fun high(str: String) : String {
    var result = ""
    for (i in str) {
        if (i.isUpperCase()) {
            result += i
        }
    }
    return result
}

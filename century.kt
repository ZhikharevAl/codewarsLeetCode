fun century(number: Int): Int {
    return if (number%100 > 0) number/100 + 1 else number/100
}

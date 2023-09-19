fun findMissingLetter(chars: CharArray): Char {
    for (i in 0 until chars.size - 1) {
        if (chars[i+1].code - chars[i].code != 1) {
            return (chars[i].code + 1).toChar()
        }
    }
    return ' '
}

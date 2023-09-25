fun high(s: String): String {
    val words = s.split(" ")
    var maxScore = 0
    var maxScoreWord = ""

    for (word in words) {
        val score = word.sumBy { it - 'a' + 1 }
        if (score > maxScore) {
            maxScore = score
            maxScoreWord = word
        }
    }

    return maxScoreWord
}

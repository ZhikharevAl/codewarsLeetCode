fun getCount(str : String) : Int{
    var count = 0
    val vowei = listOf("a", "e", "i", "o", "u")
    for (i in str) {
        if (i.toString() in vowei) {
            count ++
        }
    }
    return count
}
